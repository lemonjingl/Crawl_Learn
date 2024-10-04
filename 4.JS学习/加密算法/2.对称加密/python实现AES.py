# pycryptodome
# AES/DES/3DES..

# pad和unpad分别是填充函数和逆填充函数。因为AES加密对加密文本有长度要求，必须是密钥字节数的倍数。
# 这里的encryptKey在经过base64解码后的长度是16个字节。
# 2、实际上AES加密有AES-128、AES-192、AES-256三种，分别对应三种密钥长度128bits（16字节）、
# 192bits（24字节）、256bits（32字节）。当然，密钥越长，安全性越高，加解密花费时间也越长。
# 默认的是AES-128，其安全性完全够用。


from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad,unpad
import base64

# CBC,iv 偏移向量
# ECB

def aes_encrypt(key,iv,plain_text):
    # 创建 AES 密码器对象
    cipher = AES.new(key=key, mode=AES.MODE_CBC, iv=iv)
    # 将明文填充为 AES 分组大小的整数倍
    plain_text_pad = pad(plain_text, AES.block_size)
    # 使用了 AES 密码器对象的 encrypt 方法来加密填充后的明文
    cipher_text = cipher.encrypt(plain_text_pad)
    # 加密后的二进制数据进行 Base64 编码
    cipher_text_b64 = base64.b64encode(cipher_text).decode()
    return cipher_text_b64

def aes_decrypt(key,iv,cipher_text_b64):
    cipher_text=base64.b64encode(cipher_text_b64)
    cipher=AES.new(key=key,nooe=AES.MODE_CBC,iv=iv)
    plain_text_unpad=cipher.decrypt(cipher_text)
    plain_text=unpad(plain_text_unpad,AES.block_size)
    return plain_text.decode()

if __name__ == '__main__':
    key=b'0123456789abcdef' # byte
    iv=b'0123456789abcdef'
    plain_text='这是原始数据'.encode()
    cipher_text_b64=aes_encrypt(key,iv,plain_text)
    decrpt_text=aes_decrypt(key,iv,cipher_text_b64)
    print(decrpt_text)