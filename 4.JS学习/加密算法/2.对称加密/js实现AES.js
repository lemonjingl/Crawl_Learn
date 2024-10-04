const CryptoJS=require('crypto-js')
// 使用CryptoJS库在CBC模式下进行AES加密和解密的示例代码
const key=CryptoJS.enc.Utf8.parse('my5ocretKey12345');//16字节密钥
const iv=CryptoJS.enc.Utf8.parse('myInitialization');//16字节初始化向量

// Hook AES加密
var _AES_backup=CryptoJS.AES.encrypt
CryptoJS.AES.encrypt=function (data,key,obj){
    debugger;
    console.log('HOOK AES ---> 加密前数据：',data)
    return _AES_backup(data,key,obj)
}

//加密函数
function encryptData(data){
    const encrypted=CryptoJS.AES.encrypt(data,key,{
        iv:iv,
        mode:CryptoJS.mode.CBC,
        padding:CryptoJS.pad.Pkcs7
    });
    return encrypted.toString()
}

//解密函数
function decryptData(data){
    const decrypted=CryptoJS.AES.decrypt(data,key,{
        iv:iv,
        mode:CryptoJS.mode.CBC,
        padding:CryptoJS.pad.Pkcs7
    });
    return decrypted.toString(CryptoJS.enc.Utf8)
}

// 调用加密和解密函数
const dataToEncrypt='Hello World';
const encryptedData=encryptData(dataToEncrypt)
console.log('加密后的数据:',encryptedData);

const decryptedData=decryptData(encryptedData)
console.log('解密后的数据：',decryptedData)