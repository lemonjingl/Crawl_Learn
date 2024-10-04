
//基础环境 没有定义的时候 直接补空字典
//某一个方法或者属性没有的时 就需要补充内部的内容
document={}
location={
    reload: function (){

    }

}

function main123() {
    var s = {},
        u, c, U, r, i, l = 0,
        a, e = eval,
        w = String.fromCharCode,
        sucuri_cloudproxy_js = '',
        S = 'YT0nWTInLnNsaWNlKDEsMikrImJzdSIuc2xpY2UoMCwxKSArICJjc3VjdXIiLmNoYXJBdCgwKSsiIiArImNzdWN1ciIuY2hhckF0KDApKyIyaiIuY2hhckF0KDApICsgIiIgK1N0cmluZy5mcm9tQ2hhckNvZGUoMHgzNikgKyAiYSIgKyAgJycgKyAKJzcnICsgICIiICsnYScgKyAgImEiICsgIjQiICsgICcnICsgCiI2c2VjIi5zdWJzdHIoMCwxKSArICAnJyArJycrIjhzZWMiLnN1YnN0cigwLDEpICsgIjNzdSIuc2xpY2UoMCwxKSArICAnJyArImVzdWN1ciIuY2hhckF0KDApKyAnJyArIjQiLnNsaWNlKDAsMSkgKyAiIiArJ0RmUWEnLnN1YnN0cigzLCAxKSArIjAiICsgJzgnICsgICIiICsiOXIiLmNoYXJBdCgwKSArICIiICsiMyIgKyAiOXNlYyIuc3Vic3RyKDAsMSkgKyAiIiArIjMiICsgU3RyaW5nLmZyb21DaGFyQ29kZSgweDYyKSArICAnJyArImYiICsgImMiICsgJ0ExJy5zbGljZSgxLDIpKydINCcuc2xpY2UoMSwyKSsgJycgKycnKyJmIiArICI2c3VjdXIiLmNoYXJBdCgwKSsiOXN1Ii5zbGljZSgwLDEpICsgIjkiICsgJyc7ZG9jdW1lbnQuY29va2llPSdzc3UnLmNoYXJBdCgwKSArJ3UnKydjJysnc3VjdXJpdScuY2hhckF0KDYpKydyc3UnLmNoYXJBdCgwKSArJ2lzdWMnLmNoYXJBdCgwKSsgJ3NfJy5jaGFyQXQoMSkrJ2MnKydsc3VjdScuY2hhckF0KDApICArJ29zdScuY2hhckF0KDApICsndScrJ3N1ZCcuY2hhckF0KDIpKydwc3VjdXJpJy5jaGFyQXQoMCkgKyAncicrJ29zJy5jaGFyQXQoMCkrJ3hzdWN1Jy5jaGFyQXQoMCkgICsneScrJ3NfJy5jaGFyQXQoMSkrJ3N1Y3VydScuY2hhckF0KDUpICsgJ3N1Y3V1Jy5jaGFyQXQoNCkrICdpJysnc3VkJy5jaGFyQXQoMikrJ19zdScuY2hhckF0KDApICsnZicrJzInKydjJysnJysnMScrJ2YnKydzdWN1OScuY2hhckF0KDQpKyAnNScrJzYnKydmc3VjdScuY2hhckF0KDApICArIj0iICsgYSArICc7cGF0aD0vO21heC1hZ2U9ODY0MDAnOyBsb2NhdGlvbi5yZWxvYWQoKTs=';
    L = S.length;
    U = 0;
    r = '';
    var A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
    for (u = 0; u < 64; u++) {
        s[A.charAt(u)] = u;
    }
    for (i = 0; i < L; i++) {
        c = s[S.charAt(i)];
        U = (U << 6) + c;
        l += 6;
        while (l >= 8) {
            ((a = (U >>> (l -= 8)) & 0xff) || (i < (L - 2))) && (r += w(a));
        }
    }
    e(r)
    return document.cookie
}
