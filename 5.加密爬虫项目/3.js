// API_KEY = "a2c903cc-b31e-4547-9299-b6d07b7631ab";
API_KEY='a2c903cc-b31e-4547-9299-b6d07b7631ab';
l = 1111111111111;

function encryptApiKey(API_KEY) {
    var e = API_KEY
            , t = e.split("")
            , r = t.splice(0, 8);
    return t.concat(r).join("");
}

function encryptTime(e, l) {
    var t = (1 * e + l).toString().split("")
      , r = parseInt(10 * Math.random(), 10)
      , n = parseInt(10 * Math.random(), 10)
      , i = parseInt(10 * Math.random(), 10);
    return t.concat([r, n, i]).join("")
}

function comb(e, t) {
    var r = "".concat(e, "|").concat(t);
    return btoa(r);
}

function getApiKey(API_KEY, l) {
    var e = (new Date).getTime()
            , t = encryptApiKey(API_KEY);
    e = encryptTime(e, l);
    return comb(t, e);
}


a=getApiKey(API_KEY,l)
console.log(a)
