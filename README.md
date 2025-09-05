# Vigenère + AES Encryption Tool

A Python tool that combines **Vigenère cipher** and **AES encryption** for secure text encryption and decryption.

## Description

This project demonstrates a hybrid encryption approach using:  
1. Classical **Vigenère cipher**  
2. Modern **AES encryption**  

The tool encrypts a message first with Vigenère, then with AES, and decrypts in reverse order.

---

## Features

- Encrypt and decrypt text with **Vigenère cipher** using a custom key.  
- Encrypt and decrypt text with **AES** (random 256-bit key generated per message).  
- Hybrid encryption: **Vigenère + AES** for layered security.  
- Handles lowercase letters and non-alphabetic characters.  
- Simple command-line interface.

---

## Requirements

- Python 3.8+  
- [pyAesCrypt](https://pypi.org/project/pyAesCrypt/)  

Install dependencies with:

```bash
pip install pyAesCrypt
