from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5,PKCS1_OAEP
import base64

# 生成密钥对
def generate_key_pair():
    key=RSA.generate(2048)
    private_key=key.export_key()
    publick_key=key.public_key().export_key()
    with open('private_key.pem','wb')as f:
        f.write(private_key)
    with open('publick_key.pem','wb')as f:
        f.write(publick_key)
    return private_key,publick_key

def rsa_encrypt(publick_key,plain_text):
    key=RSA.import_key(publick_key)
    cipher=PKCS1_v1_5.new(key)
    cipher_text=cipher.encrypt(plain_text)
    return base64.b64encode(cipher_text)

def rsa_decrypt(private_key,cipher_text_b64):
    key=RSA.import_key(private_key)
    cipher=PKCS1_v1_5.new(key)
    cipher_text=base64.b64decode(cipher_text_b64)
    decode_text=cipher.decrypt(cipher_text,None)# None默认表示用PKCS1_v1-5进行填充
    return decode_text

if __name__=='__main__':
    plain_text='这是明文'.encode()
    private_key,publick_key=generate_key_pair()
    cipher_text_b64=rsa_encrypt(publick_key,plain_text)
    decode_text=rsa_decrypt(private_key,cipher_text_b64)
    print('加密后的数据：',cipher_text_b64)
    print('解密后的数据:',decode_text.decode())