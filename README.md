# WP-XML-RPC-Brute-Tool


---

# 🛠️ WP XML-RPC Brute Tool

Brute forcer simples e poderoso para WordPress, utilizando a API `xmlrpc.php` para testar combinações de usuários e senhas.

Feito por **LulzSec BlackHat Grupo 🐍**  
Telegram: [https://t.me/lulzsec_blackhat_team](https://t.me/lulzsec_blackhat_team)

---

## ⚙️ Funcionalidades

✅ Verifica se `xmlrpc.php` está habilitado  
✅ Bruteforce com múltiplos usuários e senhas  
✅ Execução rápida com múltiplas threads  
✅ Salvamento automático de logins válidos  
✅ Suporte a wordlists por arquivo ou direto no terminal  
✅ Banner bonito no estilo underground 😎

---

## 📥 Instalação

Requisitos:

- Python 3.x
- `requests`
- `pyfiglet`

Instale as dependências:

```bash
pip install requests pyfiglet
````

---

## 🚀 Como usar

### Modo básico:

```bash
python3 wpbrute.py -u https://site.com/xmlrpc.php \
  --users users.txt \
  --passwords senhas.txt
```

### Modo rápido via linha:

```bash
python3 wpbrute.py -u https://site.com/xmlrpc.php \
  --users admin,joao,ana \
  --passwords 123456,admin123
```

### Com mais threads:

```bash
python3 wpbrute.py -u https://site.com/xmlrpc.php \
  --users lista.txt \
  --passwords lista.txt \
  -t 20
```

---

## 📁 Saída dos Resultados

Logins válidos são salvos automaticamente no arquivo:

```
output/result.txt
```

Com marcação de data e hora, exemplo:

```
[2025-07-19 14:36:08] SUCCESS: admin:admin123 -> https://site.com/xmlrpc.php
```

---

## 🧠 Sobre xmlrpc.php

Essa endpoint permite interações remotas com WordPress. Se habilitada, pode ser explorada para login via métodos como `wp.getUsersBlogs`. Muitos sites deixam essa porta aberta sem saber. A ferramenta identifica se está ativo antes de iniciar o ataque.

---

## ⚠️ Aviso Legal

> Esta ferramenta é para **uso educacional e testes autorizados** somente.
> O uso indevido contra alvos sem permissão **é ilegal** e de responsabilidade do usuário.

---

## 💀 Exemplo de banner na execução

```
 __      __.__            .__  .__  _____  _____  _______     
/  \    /  \__| ____    __|__| |__|/ ____\/ ____\/ ____\_ |__ 
\   \/\/   /  |/    \  / __ |  |  \   __\\   __\\   __\| __ \
 \        /|  |   |  \/ /_/ |  |  ||  |   |  |   |  |  | \_\ \
  \__/\  / |__|___|  /\____ |__|__||__|   |__|   |__|  |___  /
       \/          \/      \/                           \/\/
```

---

## 🤝 Contato

* Grupo: [t.me/lulzsec\_blackhat\_team](https://t.me/lulzsec_blackhat_team)
* Autor: Gnu23 🐍

```

---

### ✅ Dica

Se quiser deixar mais profissional no GitHub:

- Adiciona uma **licença** (ex: MIT)
- Cria uma **badge** de Python version com shields.io
- Coloca um **GIF do script rodando** (se quiser faço um .gif com demo)

Só mandar que te ajudo com isso também. Quer que eu te mande o `LICENSE` e `.gitignore` padrão Python já pronto também?
```
