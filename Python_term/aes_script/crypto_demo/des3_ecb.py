import sys
from Crypto.Cipher import DES3
import math
import binascii

# DES3 ECB
key=("\x01\x23\x45\x67\x89\xab\xcd\xef"
     "\x23\x45\x67\x89\xab\xcd\xef\x01"
     "\x45\x67\x89\xab\xcd\xef\x01\x23")
raw_buf=("\x4e\x6f\x77\x20\x69\x73\x20\x74"
         "\x43\xe9\x34\x00\x8c\x38\x9c\x0f"
         "\x68\x37\x88\x49\x9a\x7c\x05\xf6")

key_length = len(key)
plain_length = len(raw_buf)

print 'The length of Key is:', key_length
print 'The length of Plain is:', plain_length
real_plain = binascii.b2a_hex(raw_buf)
print 'The result of plain is:', real_plain
# Encrypt part
des3_obj=DES3.new(key, DES3.MODE_ECB, b'00000000')
encrypt_buf=des3_obj.encrypt(raw_buf)
real_encrypt = binascii.b2a_hex(encrypt_buf)
print 'The result of encrypt is:', real_encrypt
encrypt_text = real_encrypt.decode('hex')
# Decrypt part
des3_obj=DES3.new(key, DES3.MODE_ECB, b'00000000')
decrypt_buf=des3_obj.decrypt(encrypt_text)
real_decrypt = binascii.b2a_hex(decrypt_buf)
print 'The result of decrypt is:', real_decrypt

if real_decrypt == real_plain:
    print 'Encrypt and Decrypt test success!'
elif real_decrypt != real_plain:
    print 'Encrypt and Decrypt test fail!'