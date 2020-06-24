import hashlib
from zlib import crc32
from Crypto.Hash import MD2, MD4
import time

def mesaure(x):
    start = time.time()
    x
    end = time.time()
    return str(end - start)

print('md2: ' + mesaure(MD2.new(b'password')))
print('md4: ' + mesaure(MD4.new(b'password')))
print('md5: ' + mesaure(hashlib.md5(b'password')))
print('sha1: ' + mesaure(hashlib.sha1(b'password')))
print('sha224: ' + mesaure(hashlib.sha224(b'password')))
print('sha256: ' + mesaure(hashlib.sha256(b'password')))
print('sha384: ' + mesaure(hashlib.sha384(b'password')))
print('sha512: ' + mesaure(hashlib.sha512(b'password')))
print('crc32: ' + mesaure(crc32(b'password')))