#!/usr/bin/python
import sys
import Crypto.Util.Counter
from Crypto import Random
from Crypto.Cipher import AES

iv = b'\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'

def pad(s):
    result = len(s) % AES.block_size
    if result == 0:
        return s
    else:
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=256):
    message = pad(message)
    # iv = Random.new().read(AES.block_size)
    ctr = Crypto.Util.Counter.new(128, initial_value=long(iv.encode('hex'),16))
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
    return cipher.encrypt(message)

def decrypt(ciphertext, key):
    ctr = Crypto.Util.Counter.new(128, initial_value=long(iv.encode('hex'),16))
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
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

key = b'\x60\x3d\xeb\x10\x15\xca\x71\xbe\x2b\x73\xae\xf0\x85\x7d\x77\x81\x1f\x35\x2c\x07\x3b\x61\x08\xd7\x2d\x98\x10\xa3\x09\x14\xdf\xf4'

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