#!/usr/bin/python
import sys
import Crypto.Util.Counter
from Crypto import Random
from Crypto.Cipher import DES3

iv = b'\x12\x34\x56\x78\x90\xab\xcd\xef'

def pad(s):
    result = len(s) % DES3.block_size
    if result == 0:
        return s
    else:
        return s + b"\0" * (DES3.block_size - len(s) % DES3.block_size)

def encrypt(message, key, key_size=128):
    message = pad(message)
    # iv = Random.new().read(DES3.block_size)
    cipher = DES3.new(key, DES3.MODE_CFB, iv)
    return cipher.encrypt(message)

def decrypt(ciphertext, key):
    cipher = DES3.new(key, DES3.MODE_CFB, iv)
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

key = b'\x01\x23\x45\x67\x89\xab\xcd\xef\x23\x45\x67\x89\xab\xcd\xef\x01\x45\x67\x89\xab\xcd\xef\x01\x23'

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