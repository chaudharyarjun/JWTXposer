<p align="center">
  <img src="https://img.shields.io/badge/JWTXposer-v1.0-blueviolet?style=for-the-badge" />
  <img src="https://img.shields.io/github/stars/chaudharyarjun/JWTXposer?style=for-the-badge" />
  <img src="https://img.shields.io/github/license/chaudharyarjun/JWTXposer?style=for-the-badge" />
</p>

<h1 align="center"> JWTXposer </h1>
<h3 align="center">Automated JWT Discovery & Analysis Tool for Bug Bounty Hunters and Red Teamers</h3>




##  What Is JWTXposer?
![image](https://github.com/user-attachments/assets/9ef26fd8-6029-4049-98f7-f9ada770c4fe)

**JWTXposer** is an **automated reconnaissance tool** that scans public archives like the **Wayback Machine**, extracts leaked **JWT tokens**, and decodes them to identify potentially exploitable information.

 Built specifically for **bug bounty hunters**, **red teamers**, and **CTF players**, JWTXposer eliminates manual JWT hunting and highlights **juicy claims** like `userId`, `access_token`, `scope`, `authType`, etc.
 It performs **automated passive recon**, **live endpoint analysis**, and **JWT decoding** to extract **juicy tokens** that may lead to:

- 🔓 Broken access control
- 🔐 Privilege escalation
- 🕵️‍♂️ Token replay attacks
- 🧬 Weak signing key discovery



## 🔍 Why JWTXposer Exists

Many applications expose JWTs:
- In old, archived endpoints (e.g. via Wayback Machine)
- Inside query parameters or API paths
- Embedded in URLs, JS files, or redirects

These tokens may still:
- Be valid for replay
- Contain sensitive claims (like roles, user IDs, access tokens)
- Be improperly validated (`alg: none`, expired tokens accepted)



##  Features

- Scrapes Wayback Machine for archived endpoints  
- Extracts JWTs from URLs, query strings, and path parameters
- Automatically decodes** JWTs (no secret key required)
- Highlights sensitive JWT claims** (userId, scope, authType, etc.)
- Checks for live endpoints that are still accessible
- Uses `multi-threading` for speed (configurable!)
- Saves results in structured JSON output
- Outputs colorized summary table using `rich`
---

##  Demo

>  *Watch JWTXposer in action:*
![JWTXP](https://github.com/user-attachments/assets/09b7bd0e-7495-4e35-b8b7-50663bc04eb4)
![jwt2](https://github.com/user-attachments/assets/3fdd1115-201b-41ba-839b-c411c2b73bc8)




##  Installation

###  Clone the repo
```bash
git clone https://github.com/yourusername/JWTXposer.git
cd JWTXposer
```
### Install Requirements
```bash
pip install -r requirements.txt
```



## Output
Results are saved in:
```bash
jwt_results.json
```
![Jwtxposer_Output](https://github.com/user-attachments/assets/7b3070a6-7507-46c6-a6cf-08607da7e7ea)

## Upcoming Features
- Token replay testing (auto)
- Burp Suite plugin mode
- GitHub / Google dorking module
- JWT fuzzing (role, alg, scope)
- Anomaly detection on tokens (ML-based)


