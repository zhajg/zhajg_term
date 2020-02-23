import sys
from Crypto.Cipher import DES
import math
import binascii

# DES ECB
key="\x01\x01\x01\x01\x01\x01\x01\x01"
raw_buf=("\x80\x00\x00\x00\x00\x00\x00\x00"
         "\x40\x00\x00\x00\x00\x00\x00\x00"
         "\x20\x00\x00\x00\x00\x00\x00\x00"
         "\x10\x00\x00\x00\x00\x00\x00\x00"
         "\x08\x00\x00\x00\x00\x00\x00\x00"
         "\x04\x00\x00\x00\x00\x00\x00\x00"
         "\x02\x00\x00\x00\x00\x00\x00\x00"
         "\x01\x00\x00\x00\x00\x00\x00\x00")

key_length = len(key)
plain_length = len(raw_buf)

print 'The length of Key is:', key_length
print 'The length of Plain is:', plain_length
real_plain = binascii.b2a_hex(raw_buf)
print 'The result of plain is:', real_plain
# Encrypt part
des_obj=DES.new(key, DES.MODE_ECB, b'00000000')

encrypt_buf=des_obj.encrypt(raw_buf)
real_encrypt = binascii.b2a_hex(encrypt_buf)
print 'The result of encrypt is:', real_encrypt
encrypt_text = real_encrypt.decode('hex')
# Decrypt part
des_obj=DES.new(key, DES.MODE_ECB, b'00000000')

decrypt_buf=des_obj.decrypt(encrypt_text)
real_decrypt = binascii.b2a_hex(decrypt_buf)
print 'The result of decrypt is:', real_decrypt

if real_decrypt == real_plain:
    print 'Encrypt and Decrypt test success!'
elif real_decrypt != real_plain:
    print 'Encrypt and Decrypt test fail!'