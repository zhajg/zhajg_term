import sys
from Crypto.Cipher import AES
import Crypto.Util.Counter
import math
import binascii

# 192 bit CFB
key=("\x8e\x73\xb0\xf7\xda\x0e\x64\x52"
    "\xc8\x10\xf3\x2b\x80\x90\x79\xe5"
    "\x62\xf8\xea\xd2\x52\x2c\x6b\x7b")
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