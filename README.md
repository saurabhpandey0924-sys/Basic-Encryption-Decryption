# Basic-Encryption-Decryption
# 🔐 Caesar Cipher Encryption & Decryption Tool

A simple Python-based Caesar Cipher implementation developed as part of the DecodeLabs Cybersecurity Internship Project.

## 📌 Project Overview

The Caesar Cipher is one of the oldest and simplest encryption techniques. It works by shifting each letter in the plaintext by a fixed number of positions in the alphabet.

### Example

Input:
Hello World

Shift Key:
3

Output:
Encrypted: Khoor Zruog
Decrypted: Hello World

---

## 🚀 Features

- Encrypt text using Caesar Cipher
- Decrypt encrypted text back to original
- Supports uppercase and lowercase letters
- Preserves spaces, numbers, and special characters
- Automatic validation of encryption/decryption process
- Beginner-friendly project

---

## 📂 Project Structure

```
Project/
│
├── Main.py
├── README.md
```

---

## ⚙️ Encryption Formula

```
E(x) = (x + n) mod 26
```

Where:
- x = Position of character
- n = Shift key

## ⚙️ Decryption Formula

```
D(x) = (x - n) mod 26
```

---

## 🛠️ How to Run

### Clone Repository

```bash
git clone https://github.com/your-username/caesar-cipher.git
```

### Run Program

```bash
python Main.py
```

---

## 🖥️ Sample Output

```
==================================================
   DecodeLabs - Caesar Cipher Tool
==================================================

Enter the text to encrypt: Cyber Security
Enter shift key (1-25): 5

==================================================
Original Text  : Cyber Security
Shift Key      : 5
Encrypted Text : Hdgjw Xjhzwndy
Decrypted Text : Cyber Security
==================================================

✅ Validation Passed: Decryption matches original!
```

---

## 📚 Concepts Used

- Python Functions
- String Manipulation
- ASCII Values
- Modular Arithmetic
- Cryptography Basics

---

## 🔒 Security Note

Caesar Cipher is not secure for modern communication and is used for educational purposes only.

---

## 👨‍💻 Author

Saurabh Pandey

Cybersecurity & AI Enthusiast

GitHub: https://github.com/saurabh-p-pandey
LinkedIn: www.linkedin.com/in/saurabh-p-pandey-754923414

---

⭐ If you like this project, give it a Star!
