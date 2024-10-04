const CryptoJS = require('crypto-js')


_0x12f283 = {
    'PpsKp': function (_0x4f5765, _0x360a96) {
        return _0x4f5765 / _0x360a96;
    },
    'BDjWh':"tempenc",
    'WWRBt':"1234567887654321",
}
_0x1f950e = function (_0x4552c3, _0x5e979f) {
    _0x4552c3 = _0x4552c3 - (-0x238a + 0x87e + -0xe27 * -0x2);
    var _0x2a0b0b = _0x27f04e[_0x4552c3];
    return _0x2a0b0b;
}

var _0x5612dc = {
    'jKmqa': function (_0x5a99d3, _0x5c564a) {
        var _0x4aff89 = _0x1f950e;
        return _0x12f283['PpsKp'](_0x5a99d3, _0x5c564a);
    },
    'PSnpJ': _0x12f283['BDjWh'],
    'zxxfJ': _0x12f283['WWRBt']
}

function getResCode() {
    var _0xd02a36 = _0x1f950e
        ,
        _0x18a88e = CryptoJS['AES']['encrypt'](CryptoJS['enc']['Utf8']['parse'](Math['floor'](_0x5612dc['_0x5612dc'](new Date()['getTime'](), 0x668 * -0x1 + 0x21f + 0x831))), CryptoJS['enc']['Utf8']['parse'](localStorage['getItem'](_0x5612dc['PSnpJ']) || _0x5612dc['zxxfJ']), {
            'iv': CryptoJS['enc']['Utf8']['parse'](_0x5612dc['zxxfJ']),
            'mode': CryptoJS['mode']['CBC'],
            'padding': CryptoJS['pad']['Pkcs7']
        });
    return CryptoJS['enc']['Base64']['stringify'](_0x18a88e['ciphertext']);
}

console.log(getResCode())