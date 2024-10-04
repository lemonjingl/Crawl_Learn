window=global;
const JSEncrypt=require('jsencrypt')
const fs=require('fs')

window.JSEncrypt=JSEncrypt

var public_key=fs.readFileSync('publick_key.pem','utf8')
var private_key=fs.readFileSync('private_key.pem','utf8')

// HOOK
const org_setPrivateKey=JSEncrypt.prototype.setPrivateKey
JSEncrypt.prototype.setPrivateKey=function(key){
    console.log('Hook RSA 设置私钥 -->',key)
    org_setPrivateKey.call(this,key)
}

const org_encrypt=JSEncrypt.prototype.encrypt
JSEncrypt.prototype.encrypt=function (plain_text){
    console.log('Hook RSA 加密前的明文 -->',plain_text)
    cipher_text=org_encrypt.call(this,plain_text)
    return cipher_text
}

const org_decrypt=JSEncrypt.prototype.decrypt
JSEncrypt.prototype.decrypt=function (cipher_text){
    console.log('Hook RSA 解密前的明文 -->',cipher_text)
    decode_text=org_encrypt.call(this,cipher_text)
    return decode_text
}

//加密
plain_text='这是明文'
cipher=new JSEncrypt()
cipher.setPublicKey(public_key)
cipher_text=cipher.encrypt(plain_text)

//解密
cipher.setPrivateKey(private_key)
decode_text=cipher.decrypt(cipher_text)

console.log('加密后的数据',cipher_text)
console.log('解密后的数据',decode_text)