# Repository: vig-aes-encryption
# Description: A Python tool that combines Vigenère cipher and AES encryption
# for secure text encryption and decryption.

# ===============================================================
# Vigenère + AES Encryption Tool
# ===============================================================

# This Python project demonstrates a hybrid encryption approach using:
# 1. Vigenère cipher (classical text encryption)
# 2. AES encryption (modern symmetric encryption)
# The tool encrypts a message first with Vigenère, then AES, and decrypts in reverse.

# ---------------------------------------------------------------
# Features
# ---------------------------------------------------------------
# - Encrypt and decrypt text using Vigenère cipher with a custom key.
# - Encrypt and decrypt text using AES (random 256-bit key per message).
# - Hybrid encryption: Vigenère + AES for layered security.
# - Simple command-line interface.
# - Handles both lowercase letters and non-alphabetic characters.

# ---------------------------------------------------------------
# Requirements
# ---------------------------------------------------------------
# - Python 3.8+
# - pyAesCrypt library
# Install dependencies with:
# pip install pyAesCrypt

# ---------------------------------------------------------------
# Usage
# ---------------------------------------------------------------
# Run the script:
# python main.py
# Input your message, then follow the prompts.
# The message is first encrypted with Vigenère, then AES.
# To decrypt, AES is reversed first, then Vigenère.

# ---------------------------------------------------------------
# Example
# ---------------------------------------------------------------
# Input:
# Votre texte : hello world
# Output:
# Message original : hello world
# Après Vigenère : rcllo ysqld
# Clé AES : 1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p
# Ciphertext AES : b'\x00\x01\x02...' ...
# Après déchiffrement AES : rcllo ysqld
# Message final déchiffré : hello world

# ---------------------------------------------------------------
# Functions
# ---------------------------------------------------------------
# vig_encrypt(text, key) -> str
#   Encrypt a message with the Vigenère cipher.
# vig_decrypt(ciphertext, key) -> str
#   Decrypt a Vigenère-encrypted message.
# aes_encrypt(message) -> tuple(str, bytes)
#   Encrypt a message using AES; returns (key, ciphertext).
# aes_decrypt(ciphertext, key) -> str
#   Decrypt AES-encrypted message with the key.

# ---------------------------------------------------------------
# Notes
# ---------------------------------------------------------------
# - AES key is randomly generated for each encryption. Save it to decrypt later.
# - Vigenère key (cle_vig) is predefined as ["o", "u", "i"], but can be customized.
