function query2obj(e) {
        var o = {};
        return e.split("&").forEach(function(e) {
            var t = e.split("=")
              , n = t.shift();
            n && (o[decodeURIComponent(n)] = decodeURIComponent(t.join("=")))
        }),
        o
    }
    function obj2query(t) {
        var n = "";
        return Object.keys(t).forEach(function(e) {
            void 0 !== t[e] && (n += encodeURIComponent(e) + "=" + encodeURIComponent(t[e]) + "&")
        }),
        n.slice(0, -1)
    }
    function getCookie(e) {
        if ("undefined" == typeof document)
            return "";
        var t = document.cookie
          , n = "\\b" + e + "="
          , o = t.search(n);
        if (o < 0)
            return "";
        o += n.length - 2;
        var r = t.indexOf(";", o);
        return r < 0 && (r = t.length),
        t.substring(o, r)
    }
    function logReq(e) {
        (1 < arguments.length && void 0 !== arguments[1] ? arguments[1] : {}).data
    }
    var _extends$1 = Object.assign || function(e) {
        for (var t = 1; t < arguments.length; t++) {
            var n = arguments[t];
            for (var o in n)
                Object.prototype.hasOwnProperty.call(n, o) && (e[o] = n[o])
        }
        return e
    }
      , isWindow = "undefined" != typeof window
      , initFetch = function(e, t) {
        return {
            url: e,
            options: t
        }
    }
      , CT_TYPE = "Content-Type"
      , CT_FILE = "multipart/form-data"
      , FORM_TYPE = "application/x-www-form-urlencoded"
      , rMatchUrl = /(^|\.com)\/api/
      , KeyArr = ["query", "data"]
      , defaultOptions = {
        method: "post",
        credentials: "include",
        encrypt: isWindow,
        paramstr: !0,
        serializedParam: !1
    }
      , encryptFetch = function(e) {
        var t = 1 < arguments.length && void 0 !== arguments[1] ? arguments[1] : {}
          , n = 2 < arguments.length && void 0 !== arguments[2] ? arguments[2] : initFetch
          , o = e
          , r = {}
          , a = _extends$1({}, defaultOptions, t)
          , i = o.split("?");
        void 0 === a.headers && (a.headers = {});
        var s = a.headers
          , c = a.encrypt
          , l = a.paramstr
          , u = a.noEnc
          , d = a.serializedParam
          , f = a.whiteHost;
        delete a.encrypt,
        delete a.paramstr,
        delete a.noEnc,
        delete a.serializedParam;
        var p = c;
        void 0 === t.encrypt && void 0 !== u && (p = !u),
        l && (a.data = obj2str(a.data));
        var _ = s[CT_TYPE] !== CT_FILE
          , m = !1;
        if (f) {
            var h = [];
            "string" == typeof f ? h = [f] : isArray(f) && (h = h.concat(f)),
            m = h.some(function(e) {
                return -1 < o.indexOf(e)
            })
        }
        var y = m || rMatchUrl.test(o);
        if (p && _ && y) {
            logReq(o, a),
            s[CT_TYPE] = FORM_TYPE,
            2 === i.length && (r = query2obj(i[1])),
            o = i[0],
            KeyArr.forEach(function(e) {
                if (a[e]) {
                    var t = "string" == typeof a[e] ? query2obj(a[e]) : a[e];
                    r = _extends$1({}, r, t)
                }
            });
            var g = getCookie("__csrf");
            g && (r.csrf_token = g),
            o = o.replace(/\/api\//, "/weapi/") + (g ? "?" + obj2query({
                csrf_token: r.csrf_token
            }) : ""),
            a.method = "post",
            delete a.query,
            delete a.data;
            var v = encrypt.asrsea(JSON.stringify(r), enk.emj2code(["流泪", "强"]), enk.BASE_CODE, enk.emj2code(["爱心", "女孩", "惊恐", "大笑"]));
            return a.body = obj2query({
                params: v.encText,
                encSecKey: v.encSecKey
            }),
            n(o, a)
        }
        if (void 0 === s[CT_TYPE] && (a.headers[CT_TYPE] = FORM_TYPE),
        d) {
            var b = ""
              , S = a.data;
            isObject(S) ? b = obj2query(S) : "string" == typeof S && (b = S),
            delete a.data;
            var w = a.method;
            if ("string" == typeof w && (w = w.toLowerCase()),
            "post" === w)
                a.body = b;
            else if ("get" === w) {
                var E = -1 !== o.indexOf("?") ? "&" : "?";
                o += "" + E + b
            }
        }
        return n(o, a)
    }
      , createFetch = function(n) {
        return function(e, t) {
            return encryptFetch(e, t, n)
        }
    };