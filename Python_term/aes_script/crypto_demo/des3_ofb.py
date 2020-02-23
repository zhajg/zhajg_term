import sys
from Crypto.Cipher import DES3
import math
import binascii

# DES3 ECB
# key="\x01\x23\x45\x67\x89\xab\xcd\xef\x23\x45\x67\x89\xab\xcd\xef\x01\x45\x67\x89\xab\xcd\xef\x01\x23"
# raw_buf="\x4e\x6f\x77\x20\x69\x73\x20\x74\x43\xe9\x34\x00\x8c\x38\x9c\x0f\x68\x37\x88\x49\x9a\x7c\x05\xf6"

# DES3 CBC
# key="\x01\x23\x45\x67\x89\xab\xcd\xef\x23\x45\x67\x89\xab\xcd\xef\x01\x45\x67\x89\xab\xcd\xef\x01\x23"
# iv="\x12\x34\x56\x78\x90\xab\xcd\xef"
# raw_buf="\x4e\x6f\x77\x20\x69\x73\x20\x74\x43\xe9\x34\x00\x8c\x38\x9c\x0f\x68\x37\x88\x49\x9a\x7c\x05\xf6"


# DES3 OFB
# key="\x01\x23\x45\x67\x89\xab\xcd\xef\x23\x45\x67\x89\xab\xcd\xef\x01\x45\x67\x89\xab\xcd\xef\x01\x23"
# iv="\x23\x45\x67\x89\x0a\xbc\xde\x0f"
# raw_buf="\xe6\xf7\x72\x06\x97\x32\x07\x04\x3e\x93\x40\x08\xc3\x89\xc0\x0f\x83\x78\x84\x99\xa7\xc0\x5f\x06"

# DES3 CFB
key="\x01\x23\x45\x67\x89\xab\xcd\xef\x23\x45\x67\x89\xab\xcd\xef\x01\x45\x67\x89\xab\xcd\xef\x01\x23"
iv="\x12\x34\x56\x78\x90\xab\xcd\xef"
raw_buf="\x4e\x6f\x77\x20\x69\x73\x20\x74\x43\xe9\x34\x00\x8c\x38\x9c\x0f\x68\x37\x88\x49\x9a\x7c\x05\xf6"

iv_length = len(iv)
key_length = len(key)
plain_length = len(raw_buf)
print 'The length of IV is:', iv_length
print 'The length of Key is:', key_length
print 'The length of Plain is:', plain_length
real_plain = binascii.b2a_hex(raw_buf)
print 'The result of plain is:', real_plain
# Encrypt part
# des3_obj=DES3.new(key, DES3.MODE_ECB, b'00000000')
# des3_obj=DES3.new(key, DES3.MODE_CBC, iv)
# des3_obj=DES3.new(key, DES3.MODE_OFB, iv)
des3_obj=DES3.new(key, DES3.MODE_CFB, iv)
encrypt_buf=des3_obj.encrypt(raw_buf)
real_encrypt = binascii.b2a_hex(encrypt_buf)
print 'The result of encrypt is:', real_encrypt
encrypt_text = real_encrypt.decode('hex')
# Decrypt part
# des3_obj=DES3.new(key, DES3.MODE_ECB, b'00000000')
# des3_obj=DES3.new(key, DES3.MODE_CBC, iv)
# des3_obj=DES3.new(key, DES3.MODE_OFB, iv)
des3_obj=DES3.new(key, DES3.MODE_CFB, iv)
decrypt_buf=des3_obj.decrypt(encrypt_text)
real_decrypt = binascii.b2a_hex(decrypt_buf)
print 'The result of decrypt is:', real_decrypt

if real_decrypt == real_plain:
    print 'Encrypt and Decrypt test success!'
elif real_decrypt != real_plain:
    print 'Encrypt and Decrypt test fail!'