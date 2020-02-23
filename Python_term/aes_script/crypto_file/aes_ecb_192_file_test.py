#!/usr/bin/python
import sys
import Crypto.Util.Counter
from Crypto import Random
from Crypto.Cipher import AES

def pad(s):
    result = len(s) % AES.block_size
    if result == 0:
        return s
    else:
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=192):
    message = pad(message)
    cipher = AES.new(key, AES.MODE_ECB, b'0000000000000000')
    return cipher.encrypt(message)

def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB, b'0000000000000000')
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.rstrip(b"\0")

def encrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext, key)
    with open(file_name + ".txt", 'wb') as fo:
        fo.write(enc)

def decrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext, key)
    with open(file_name + ".txt", 'wb') as fo:
        fo.write(dec)

key = b'\x8e\x73\xb0\xf7\xda\x0e\x64\x52\xc8\x10\xf3\x2b\x80\x90\x79\xe5\x62\xf8\xea\xd2\x52\x2c\x6b\x7b'

encrypt_file('test1.txt', key)
decrypt_file('test1.txt.txt', key)

with open('test1.txt', 'rb') as fo:
        plain_text = fo.read()
with open('test1.txt.txt.txt', 'rb') as fo:
        decrypto_text = fo.read()

if plain_text == decrypto_text:
    print 'Encrypt and Decrypt file test successfully!'
else:
    print 'Encrypt and Decrypt file test fail!'