from Crypto.Cipher import DES

def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text

des = DES.new(b'password', DES.MODE_ECB)
text = b'Word!'
padded_text = pad(text)

encrypted_text = des.encrypt(padded_text)
print(encrypted_text)