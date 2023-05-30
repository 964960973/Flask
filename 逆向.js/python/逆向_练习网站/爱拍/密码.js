var md5 =  function(l) {
    var e = "0123456789abcdef"
        , d = function (o) {
        var p = "";
        for (j = 0; j <= 3; j++) {
            p += e.charAt((o >> (j * 8 + 4)) & 15) + e.charAt((o >> (j * 8)) & 15)
        }
        return p
    }
        , f = function (o) {
        nblk = ((o.length + 8) >> 6) + 1;
        blks = new Array(nblk * 16);
        for (i = 0; i < nblk * 16; i++) {
            blks[i] = 0
        }
        for (i = 0; i < o.length; i++) {
            blks[i >> 2] |= o.charCodeAt(i) << ((i % 4) * 8)
        }
        blks[i >> 2] |= 128 << ((i % 4) * 8);
        blks[nblk * 16 - 2] = o.length * 8;
        return blks
    }
        , n = function (o, r) {
        var q = (o & 65535) + (r & 65535);
        var p = (o >> 16) + (r >> 16) + (q >> 16);
        return (p << 16) | (q & 65535)
    }
        , c = function (o, p) {
        return (o << p) | (o >>> (32 - p))
    }
        , k = function (w, r, p, o, v, u) {
        return n(c(n(n(r, w), n(o, u)), v), p)
    }
        , a = function (q, p, w, v, o, u, r) {
        return k((p & w) | ((~p) & v), q, p, o, u, r)
    }
        , g = function (q, p, w, v, o, u, r) {
        return k((p & v) | (w & (~v)), q, p, o, u, r)
    }
        , b = function (q, p, w, v, o, u, r) {
        return k(p ^ w ^ v, q, p, o, u, r)
    }
        , m = function (q, p, w, v, o, u, r) {
        return k(w ^ (p | (~v)), q, p, o, u, r)
    }
        , h = function (u) {
        x = f(u);
        var w = 1732584193;
        var v = -271733879;
        var t = -1732584194;
        var s = 271733878;
        for (i = 0; i < x.length; i += 16) {
            var r = w;
            var q = v;
            var p = t;
            var o = s;
            w = a(w, v, t, s, x[i + 0], 7, -680876936);
            s = a(s, w, v, t, x[i + 1], 12, -389564586);
            t = a(t, s, w, v, x[i + 2], 17, 606105819);
            v = a(v, t, s, w, x[i + 3], 22, -1044525330);
            w = a(w, v, t, s, x[i + 4], 7, -176418897);
            s = a(s, w, v, t, x[i + 5], 12, 1200080426);
            t = a(t, s, w, v, x[i + 6], 17, -1473231341);
            v = a(v, t, s, w, x[i + 7], 22, -45705983);
            w = a(w, v, t, s, x[i + 8], 7, 1770035416);
            s = a(s, w, v, t, x[i + 9], 12, -1958414417);
            t = a(t, s, w, v, x[i + 10], 17, -42063);
            v = a(v, t, s, w, x[i + 11], 22, -1990404162);
            w = a(w, v, t, s, x[i + 12], 7, 1804603682);
            s = a(s, w, v, t, x[i + 13], 12, -40341101);
            t = a(t, s, w, v, x[i + 14], 17, -1502002290);
            v = a(v, t, s, w, x[i + 15], 22, 1236535329);
            w = g(w, v, t, s, x[i + 1], 5, -165796510);
            s = g(s, w, v, t, x[i + 6], 9, -1069501632);
            t = g(t, s, w, v, x[i + 11], 14, 643717713);
            v = g(v, t, s, w, x[i + 0], 20, -373897302);
            w = g(w, v, t, s, x[i + 5], 5, -701558691);
            s = g(s, w, v, t, x[i + 10], 9, 38016083);
            t = g(t, s, w, v, x[i + 15], 14, -660478335);
            v = g(v, t, s, w, x[i + 4], 20, -405537848);
            w = g(w, v, t, s, x[i + 9], 5, 568446438);
            s = g(s, w, v, t, x[i + 14], 9, -1019803690);
            t = g(t, s, w, v, x[i + 3], 14, -187363961);
            v = g(v, t, s, w, x[i + 8], 20, 1163531501);
            w = g(w, v, t, s, x[i + 13], 5, -1444681467);
            s = g(s, w, v, t, x[i + 2], 9, -51403784);
            t = g(t, s, w, v, x[i + 7], 14, 1735328473);
            v = g(v, t, s, w, x[i + 12], 20, -1926607734);
            w = b(w, v, t, s, x[i + 5], 4, -378558);
            s = b(s, w, v, t, x[i + 8], 11, -2022574463);
            t = b(t, s, w, v, x[i + 11], 16, 1839030562);
            v = b(v, t, s, w, x[i + 14], 23, -35309556);
            w = b(w, v, t, s, x[i + 1], 4, -1530992060);
            s = b(s, w, v, t, x[i + 4], 11, 1272893353);
            t = b(t, s, w, v, x[i + 7], 16, -155497632);
            v = b(v, t, s, w, x[i + 10], 23, -1094730640);
            w = b(w, v, t, s, x[i + 13], 4, 681279174);
            s = b(s, w, v, t, x[i + 0], 11, -358537222);
            t = b(t, s, w, v, x[i + 3], 16, -722521979);
            v = b(v, t, s, w, x[i + 6], 23, 76029189);
            w = b(w, v, t, s, x[i + 9], 4, -640364487);
            s = b(s, w, v, t, x[i + 12], 11, -421815835);
            t = b(t, s, w, v, x[i + 15], 16, 530742520);
            v = b(v, t, s, w, x[i + 2], 23, -995338651);
            w = m(w, v, t, s, x[i + 0], 6, -198630844);
            s = m(s, w, v, t, x[i + 7], 10, 1126891415);
            t = m(t, s, w, v, x[i + 14], 15, -1416354905);
            v = m(v, t, s, w, x[i + 5], 21, -57434055);
            w = m(w, v, t, s, x[i + 12], 6, 1700485571);
            s = m(s, w, v, t, x[i + 3], 10, -1894986606);
            t = m(t, s, w, v, x[i + 10], 15, -1051523);
            v = m(v, t, s, w, x[i + 1], 21, -2054922799);
            w = m(w, v, t, s, x[i + 8], 6, 1873313359);
            s = m(s, w, v, t, x[i + 15], 10, -30611744);
            t = m(t, s, w, v, x[i + 6], 15, -1560198380);
            v = m(v, t, s, w, x[i + 13], 21, 1309151649);
            w = m(w, v, t, s, x[i + 4], 6, -145523070);
            s = m(s, w, v, t, x[i + 11], 10, -1120210379);
            t = m(t, s, w, v, x[i + 2], 15, 718787259);
            v = m(v, t, s, w, x[i + 9], 21, -343485551);
            w = n(w, r);
            v = n(v, q);
            t = n(t, p);
            s = n(s, o)
        }
        return d(w) + d(v) + d(t) + d(s)
    };
    return h(l)
}
console.log(md5('123456'))