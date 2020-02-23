#!/usr/bin/python
import sys
import Crypto.Util.Counter
from Crypto import Random
from Crypto.Cipher import DES

def pad(s):
    result = len(s) % DES.block_size
    if result == 0:
        return s
    else:
        return s + b"\0" * (DES.block_size - len(s) % DES.block_size)

def encrypt(message, key, key_size=64):
    message = pad(message)
    cipher = DES.new(key, DES.MODE_ECB, b'0000000000000000')
    return cipher.encrypt(message)

def decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB, b'0000000000000000')
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

key = b'\x01\x01\x01\x01\x01\x01\x01\x01'

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