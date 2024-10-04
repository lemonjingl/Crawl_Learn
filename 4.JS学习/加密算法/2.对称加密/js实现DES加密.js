const CryptoJS=require('crypto-js')

//HOOK  DES解密
var _DES_backup=CryptoJS.DES.decrypt
CryptoJS.DES.decrypt=function (message,key,obj){
    console.log('HOOK DES 解密-->',message)
    return _DES_backup(message,key,obj)
}

function encryptDES(message,key){
    const keyHex=CryptoJS.enc.Utf8.parse(key);
    const encrypted=CryptoJS.DES.encrypt(message,keyHex,{
        mode:CryptoJS.mode.ECB,
        padding:CryptoJS.pad.Pkcs7,
    });
    return encrypted.toString();
}

function decryptDES(ciphertext,key){
    const keyHex=CryptoJS.enc.Utf8.parse(key);
    const decrypted=CryptoJS.DES.decrypt(ciphertext,keyHex,{
        mode:CryptoJS.mode.ECB,
        padding:CryptoJS.pad.Pkcs7,
    });
    return decrypted.toString(CryptoJS.enc.Utf8);
}

// 调用加密和解密函数
const dataToEncrypt='Hello World';
const encryptedData=encryptDES(dataToEncrypt)
console.log('加密后的数据:',encryptedData);

cipher_text=encryptDES('Hello World','Secret Passphrase')
console.log(decryptDES(cipher_text,'Secret Passphrase'))

