import base64
from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad,unpad

def des_encrypt(key,iv,plaintext):
    cipher=DES.new(key,DES.MODE_CBC,iv)
    ciphertext=cipher.encrypt(pad(plaintext.encode('utf-8'),DES.block_size))
    return base64.b64encode(ciphertext).decode('utf-8')

def des_decrypt(key,iv,ciphertext):
    cipher=DES.new(key,DES.MODE_CBC,iv)
    plaintext=unpad(cipher.decrypt(base64.b64decode(ciphertext)),DES.block_size)
    return plaintext.decode('utf-8')


def main():
    key = b'01234567'
    iv = b'abcdefgh'
    plaintext = '你好'

    ciphertext = des_encrypt(key, iv, plaintext)
    print(ciphertext)
    decrypted_plaintext = des_decrypt(key, iv, ciphertext)
    print(decrypted_plaintext)

main()