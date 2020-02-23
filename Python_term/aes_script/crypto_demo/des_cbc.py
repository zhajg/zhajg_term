import sys
from Crypto.Cipher import DES
import math
import binascii

# DES CBC
key="\x01\x23\x45\x67\x89\xab\xcd\xef"
iv="\x12\x34\x56\x78\x90\xab\xcd\xef"
raw_buf=("\x4e\x6f\x77\x20\x69\x73\x20\x74"
         "\x68\x65\x20\x74\x69\x6d\x65\x20"
         "\x66\x6f\x72\x20\x61\x6c\x6c\x20")

iv_length = len(iv)
key_length = len(key)
plain_length = len(raw_buf)
print 'The length of IV is:', iv_length
print 'The length of Key is:', key_length
print 'The length of Plain is:', plain_length
real_plain = binascii.b2a_hex(raw_buf)
print 'The result of plain is:', real_plain
# Encrypt part
des_obj=DES.new(key, DES.MODE_CBC, iv)
encrypt_buf=des_obj.encrypt(raw_buf)
real_encrypt = binascii.b2a_hex(encrypt_buf)
print 'The result of encrypt is:', real_encrypt
encrypt_text = real_encrypt.decode('hex')
# Decrypt part
des_obj=DES.new(key, DES.MODE_CBC, iv)
decrypt_buf=des_obj.decrypt(encrypt_text)
real_decrypt = binascii.b2a_hex(decrypt_buf)
print 'The result of decrypt is:', real_decrypt

if real_decrypt == real_plain:
    print 'Encrypt and Decrypt test success!'
elif real_decrypt != real_plain:
    print 'Encrypt and Decrypt test fail!'