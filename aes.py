import hashlib
import os
from Crypto.Cipher import AES

IV_SIZE = 16
KEY_SIZE = 32
SALT_SIZE = 16

cleartext = str(input("cleartext:"))
cleartext = bytes(cleartext, 'utf-8')

password = str(input("password:"))
password = bytes(password, 'utf-8')

salt = os.urandom(SALT_SIZE)
derived = hashlib.pbkdf2_hmac('sha256', password, salt, 100000, dklen=IV_SIZE + KEY_SIZE)
iv = derived[0:IV_SIZE]
key = derived[IV_SIZE:]

encrypted = salt + AES.new(key, AES.MODE_CFB, iv).encrypt(cleartext)
print(encrypted)

salt = encrypted[0:SALT_SIZE]
derived = hashlib.pbkdf2_hmac('sha256', password, salt, 100000, dklen=IV_SIZE + KEY_SIZE)
iv = derived[0:IV_SIZE]
key = derived[IV_SIZE:]
cleartext = AES.new(key, AES.MODE_CFB, iv).decrypt(encrypted[SALT_SIZE:])
print(cleartext)