const CryptoJs=require('crypto-js')

//hook MD5
var md5_backup=CryptoJs.MD5
CryptoJs.MD5=function (s){
    console.log('MD5 HOOK --> 加密前的数据',s)
    return md5_backup(s)
}

s='lzzsll'

encrypt_s=CryptoJs.MD5(s).toString()
console.log(encrypt_s)