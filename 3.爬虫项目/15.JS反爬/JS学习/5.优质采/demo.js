const CryptoJS = require('crypto-js')

// var a = 'ca8b71b2';
// var b = '913E1E2FC9EB10BA01918F58A15FBBFA210AE700B455062AD3FD11A0B17AE999B8787CEB1BAD0F47BBDA068269BA9BB159494721FAE0ECBB02100757C1BCA85D';

function main123(a, b) {
    var keyHex = CryptoJS['enc']['Utf8']['parse'](a),
        encrypted = CryptoJS['DES']['encrypt'](b, keyHex, {
            'mode': CryptoJS['mode']['ECB'],
            'padding': CryptoJS['pad']['Pkcs7']
        })
    encryptvrscode = encrypted['ciphertext']['toString']()
    b = escape(encryptvrscode)
    return b
}



