<p align="center">
  <img src="https://img.shields.io/badge/JWTXposer-v1.0-blueviolet?style=for-the-badge" />
  <img src="https://img.shields.io/github/stars/chaudharyarjun/JWTXposer?style=for-the-badge" />
  <img src="https://img.shields.io/github/license/chaudharyarjun/JWTXposer?style=for-the-badge" />
</p>

<h1 align="center"> JWTXposer </h1>
<h3 align="center">Automated JWT Discovery & Analysis Tool for Bug Bounty Hunters and Red Teamers</h3>

---

##  What Is JWTXposer?

**JWTXposer** automates the painful, time-consuming process of finding and analyzing JWTs (JSON Web Tokens) leaked in public sources — especially in Wayback Machine archives.

 It performs **automated passive recon**, **live endpoint analysis**, and **JWT decoding** to extract **juicy tokens** that may lead to:

- 🔓 Broken access control
- 🔐 Privilege escalation
- 🕵️‍♂️ Token replay attacks
- 🧬 Weak signing key discovery

---

##  Features

✅ Pulls **archived URLs** from Wayback Machine  
✅ Detects JWTs in **query params**, **path**, **encoded formats**  
✅ Decodes JWTs **without needing the secret key**  
✅ Extracts **juicy info** like roles, user IDs, scopes, etc.  
✅ Checks if JWT-carrying URLs are **still live**  
✅ Saves everything in **JSON** and renders output with `rich`  
✅ Supports **colored terminal output** for fast triage  
✅ Plug-and-play with any domain (`*.api.target.com`, etc.)

---

## 📸 Demo

>  *Watch JWTXposer in action:*

![demo](https://user-images.githubusercontent.com/youruser/demo.gif)

---

## 🛠️ Installation

###  Clone the repo
```bash
git clone https://github.com/yourusername/JWTXposer.git
cd JWTXposer
