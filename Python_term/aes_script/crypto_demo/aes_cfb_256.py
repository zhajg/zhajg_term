import sys
from Crypto.Cipher import AES
import Crypto.Util.Counter
import math
import binascii

# 256 bit CFB
key=("\x60\x3d\xeb\x10\x15\xca\x71\xbe"
     "\x2b\x73\xae\xf0\x85\x7d\x77\x81"
     "\x1f\x35\x2c\x07\x3b\x61\x08\xd7"
     "\x2d\x98\x10\xa3\x09\x14\xdf\xf4")
iv=("\x00\x01\x02\x03\x04\x05\x06\x07"
    "\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f")
raw_buf=("\x6b\xc1\xbe\xe2\x2e\x40\x9f\x96"
         "\xe9\x3d\x7e\x11\x73\x93\x17\x2a"
         "\xae\x2d")

iv_length = len(iv)
key_length = len(key)
plain_length = len(raw_buf)
print 'The length of IV is:', iv_length
print 'The length of Key is:', key_length
print 'The length of Plain is:', plain_length
real_plain = binascii.b2a_hex(raw_buf)
print 'The result of plain is:', real_plain
# Encrypt part
aes_obj=AES.new(key, AES.MODE_CFB, iv)
encrypt_buf=aes_obj.encrypt(raw_buf)
real_encrypt = binascii.b2a_hex(encrypt_buf)
print 'The result of encrypt is:', real_encrypt
encrypt_text = real_encrypt.decode('hex')
# Decrypt part
aes_obj=AES.new(key, AES.MODE_CFB, iv)
decrypt_buf=aes_obj.decrypt(encrypt_text)
real_decrypt = binascii.b2a_hex(decrypt_buf)
print 'The result of decrypt is:', real_decrypt

if real_decrypt == real_plain:
    print 'Encrypt and Decrypt test success!'
elif real_decrypt != real_plain:
    print 'Encrypt and Decrypt test fail!'
