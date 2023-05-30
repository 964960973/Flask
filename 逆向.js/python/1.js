var pdd;
!function (e){
    var n = {}
    function f(t){
        if (n[t])
            return n[t].exports;
        console.log("----->",t);// 这个可以看见没有的模块
        var r = n[t] = {
            i:t,
            l:!1,
            exports:{}
        };
        return e[t].call(r.exports,r,r.exports,f),
        r.l = !0,
        r.exports
    }
    pdd = f;
    // 导出对象
}({
92471: function(t, e) {
        var n;
        t.exports = (n = n || function(t, e) {
            var n = Object.create || function() {
                function t() {}
                return function(e) {
                    var n;
                    return t.prototype = e,
                    n = new t,
                    t.prototype = null,
                    n
                }
            }()
              , r = {}
              , o = r.lib = {}
              , i = o.Base = {
                extend: function(t) {
                    var e = n(this);
                    return t && e.mixIn(t),
                    e.hasOwnProperty("init") && this.init !== e.init || (e.init = function() {
                        e.$super.init.apply(this, arguments)
                    }
                    ),
                    e.init.prototype = e,
                    e.$super = this,
                    e
                },
                create: function() {
                    var t = this.extend();
                    return t.init.apply(t, arguments),
                    t
                },
                init: function() {},
                mixIn: function(t) {
                    for (var e in t)
                        t.hasOwnProperty(e) && (this[e] = t[e]);
                    t.hasOwnProperty("toString") && (this.toString = t.toString)
                },
                clone: function() {
                    return this.init.prototype.extend(this)
                }
            }
              , a = o.WordArray = i.extend({
                init: function(t, e) {
                    t = this.words = t || [],
                    this.sigBytes = null != e ? e : 4 * t.length
                },
                toString: function(t) {
                    return (t || u).stringify(this)
                },
                concat: function(t) {
                    var e = this.words
                      , n = t.words
                      , r = this.sigBytes
                      , o = t.sigBytes;
                    if (this.clamp(),
                    r % 4)
                        for (var i = 0; i < o; i++) {
                            var a = n[i >>> 2] >>> 24 - i % 4 * 8 & 255;
                            e[r + i >>> 2] |= a << 24 - (r + i) % 4 * 8
                        }
                    else
                        for (i = 0; i < o; i += 4)
                            e[r + i >>> 2] = n[i >>> 2];
                    return this.sigBytes += o,
                    this
                },
                clamp: function() {
                    var e = this.words
                      , n = this.sigBytes;
                    e[n >>> 2] &= 4294967295 << 32 - n % 4 * 8,
                    e.length = t.ceil(n / 4)
                },
                clone: function() {
                    var t = i.clone.call(this);
                    return t.words = this.words.slice(0),
                    t
                },
                random: function(e) {
                    for (var n, r = [], o = function(e) {
                        var n = 987654321
                          , r = 4294967295;
                        return function() {
                            var o = ((n = 36969 * (65535 & n) + (n >> 16) & r) << 16) + (e = 18e3 * (65535 & e) + (e >> 16) & r) & r;
                            return o /= 4294967296,
                            (o += .5) * (t.random() > .5 ? 1 : -1)
                        }
                    }, i = 0; i < e; i += 4) {
                        var s = o(4294967296 * (n || t.random()));
                        n = 987654071 * s(),
                        r.push(4294967296 * s() | 0)
                    }
                    return new a.init(r,e)
                }
            })
              , s = r.enc = {}
              , u = s.Hex = {
                stringify: function(t) {
                    for (var e = t.words, n = t.sigBytes, r = [], o = 0; o < n; o++) {
                        var i = e[o >>> 2] >>> 24 - o % 4 * 8 & 255;
                        r.push((i >>> 4).toString(16)),
                        r.push((15 & i).toString(16))
                    }
                    return r.join("")
                },
                parse: function(t) {
                    for (var e = t.length, n = [], r = 0; r < e; r += 2)
                        n[r >>> 3] |= parseInt(t.substr(r, 2), 16) << 24 - r % 8 * 4;
                    return new a.init(n,e / 2)
                }
            }
              , c = s.Latin1 = {
                stringify: function(t) {
                    for (var e = t.words, n = t.sigBytes, r = [], o = 0; o < n; o++) {
                        var i = e[o >>> 2] >>> 24 - o % 4 * 8 & 255;
                        r.push(String.fromCharCode(i))
                    }
                    return r.join("")
                },
                parse: function(t) {
                    for (var e = t.length, n = [], r = 0; r < e; r++)
                        n[r >>> 2] |= (255 & t.charCodeAt(r)) << 24 - r % 4 * 8;
                    return new a.init(n,e)
                }
            }
              , l = s.Utf8 = {
                stringify: function(t) {
                    try {
                        return decodeURIComponent(escape(c.stringify(t)))
                    } catch (e) {
                        throw new Error("Malformed UTF-8 data")
                    }
                },
                parse: function(t) {
                    return c.parse(unescape(encodeURIComponent(t)))
                }
            }
              , f = o.BufferedBlockAlgorithm = i.extend({
                reset: function() {
                    this._data = new a.init,
                    this._nDataBytes = 0
                },
                _append: function(t) {
                    "string" == typeof t && (t = l.parse(t)),
                    this._data.concat(t),
                    this._nDataBytes += t.sigBytes
                },
                _process: function(e) {
                    var n = this._data
                      , r = n.words
                      , o = n.sigBytes
                      , i = this.blockSize
                      , s = o / (4 * i)
                      , u = (s = e ? t.ceil(s) : t.max((0 | s) - this._minBufferSize, 0)) * i
                      , c = t.min(4 * u, o);
                    if (u) {
                        for (var l = 0; l < u; l += i)
                            this._doProcessBlock(r, l);
                        var f = r.splice(0, u);
                        n.sigBytes -= c
                    }
                    return new a.init(f,c)
                },
                clone: function() {
                    var t = i.clone.call(this);
                    return t._data = this._data.clone(),
                    t
                },
                _minBufferSize: 0
            })
              , d = (o.Hasher = f.extend({
                cfg: i.extend(),
                init: function(t) {
                    this.cfg = this.cfg.extend(t),
                    this.reset()
                },
                reset: function() {
                    f.reset.call(this),
                    this._doReset()
                },
                update: function(t) {
                    return this._append(t),
                    this._process(),
                    this
                },
                finalize: function(t) {
                    return t && this._append(t),
                    this._doFinalize()
                },
                blockSize: 16,
                _createHelper: function(t) {
                    return function(e, n) {
                        return new t.init(n).finalize(e)
                    }
                },
                _createHmacHelper: function(t) {
                    return function(e, n) {
                        return new d.HMAC.init(t,n).finalize(e)
                    }
                }
            }),
            r.algo = {});
            return r
        }(Math),
        n)
    },
                83455: function(t, e, n) {
        var r;
        t.exports = (r = n(92471),
        function(t) {
            var e = r
              , n = e.lib
              , o = n.WordArray
              , i = n.Hasher
              , a = e.algo
              , s = [];
            !function() {
                for (var e = 0; e < 64; e++)
                    s[e] = 4294967296 * t.abs(t.sin(e + 1)) | 0
            }();
            var u = a.MD5 = i.extend({
                _doReset: function() {
                    this._hash = new o.init([1732584193, 4023233417, 2562383102, 271733878])
                },
                _doProcessBlock: function(t, e) {
                    for (var n = 0; n < 16; n++) {
                        var r = e + n
                          , o = t[r];
                        t[r] = 16711935 & (o << 8 | o >>> 24) | 4278255360 & (o << 24 | o >>> 8)
                    }
                    var i = this._hash.words
                      , a = t[e + 0]
                      , u = t[e + 1]
                      , p = t[e + 2]
                      , h = t[e + 3]
                      , m = t[e + 4]
                      , v = t[e + 5]
                      , g = t[e + 6]
                      , y = t[e + 7]
                      , _ = t[e + 8]
                      , b = t[e + 9]
                      , w = t[e + 10]
                      , E = t[e + 11]
                      , D = t[e + 12]
                      , S = t[e + 13]
                      , k = t[e + 14]
                      , O = t[e + 15]
                      , C = i[0]
                      , x = i[1]
                      , T = i[2]
                      , A = i[3];
                    C = c(C, x, T, A, a, 7, s[0]),
                    A = c(A, C, x, T, u, 12, s[1]),
                    T = c(T, A, C, x, p, 17, s[2]),
                    x = c(x, T, A, C, h, 22, s[3]),
                    C = c(C, x, T, A, m, 7, s[4]),
                    A = c(A, C, x, T, v, 12, s[5]),
                    T = c(T, A, C, x, g, 17, s[6]),
                    x = c(x, T, A, C, y, 22, s[7]),
                    C = c(C, x, T, A, _, 7, s[8]),
                    A = c(A, C, x, T, b, 12, s[9]),
                    T = c(T, A, C, x, w, 17, s[10]),
                    x = c(x, T, A, C, E, 22, s[11]),
                    C = c(C, x, T, A, D, 7, s[12]),
                    A = c(A, C, x, T, S, 12, s[13]),
                    T = c(T, A, C, x, k, 17, s[14]),
                    C = l(C, x = c(x, T, A, C, O, 22, s[15]), T, A, u, 5, s[16]),
                    A = l(A, C, x, T, g, 9, s[17]),
                    T = l(T, A, C, x, E, 14, s[18]),
                    x = l(x, T, A, C, a, 20, s[19]),
                    C = l(C, x, T, A, v, 5, s[20]),
                    A = l(A, C, x, T, w, 9, s[21]),
                    T = l(T, A, C, x, O, 14, s[22]),
                    x = l(x, T, A, C, m, 20, s[23]),
                    C = l(C, x, T, A, b, 5, s[24]),
                    A = l(A, C, x, T, k, 9, s[25]),
                    T = l(T, A, C, x, h, 14, s[26]),
                    x = l(x, T, A, C, _, 20, s[27]),
                    C = l(C, x, T, A, S, 5, s[28]),
                    A = l(A, C, x, T, p, 9, s[29]),
                    T = l(T, A, C, x, y, 14, s[30]),
                    C = f(C, x = l(x, T, A, C, D, 20, s[31]), T, A, v, 4, s[32]),
                    A = f(A, C, x, T, _, 11, s[33]),
                    T = f(T, A, C, x, E, 16, s[34]),
                    x = f(x, T, A, C, k, 23, s[35]),
                    C = f(C, x, T, A, u, 4, s[36]),
                    A = f(A, C, x, T, m, 11, s[37]),
                    T = f(T, A, C, x, y, 16, s[38]),
                    x = f(x, T, A, C, w, 23, s[39]),
                    C = f(C, x, T, A, S, 4, s[40]),
                    A = f(A, C, x, T, a, 11, s[41]),
                    T = f(T, A, C, x, h, 16, s[42]),
                    x = f(x, T, A, C, g, 23, s[43]),
                    C = f(C, x, T, A, b, 4, s[44]),
                    A = f(A, C, x, T, D, 11, s[45]),
                    T = f(T, A, C, x, O, 16, s[46]),
                    C = d(C, x = f(x, T, A, C, p, 23, s[47]), T, A, a, 6, s[48]),
                    A = d(A, C, x, T, y, 10, s[49]),
                    T = d(T, A, C, x, k, 15, s[50]),
                    x = d(x, T, A, C, v, 21, s[51]),
                    C = d(C, x, T, A, D, 6, s[52]),
                    A = d(A, C, x, T, h, 10, s[53]),
                    T = d(T, A, C, x, w, 15, s[54]),
                    x = d(x, T, A, C, u, 21, s[55]),
                    C = d(C, x, T, A, _, 6, s[56]),
                    A = d(A, C, x, T, O, 10, s[57]),
                    T = d(T, A, C, x, g, 15, s[58]),
                    x = d(x, T, A, C, S, 21, s[59]),
                    C = d(C, x, T, A, m, 6, s[60]),
                    A = d(A, C, x, T, E, 10, s[61]),
                    T = d(T, A, C, x, p, 15, s[62]),
                    x = d(x, T, A, C, b, 21, s[63]),
                    i[0] = i[0] + C | 0,
                    i[1] = i[1] + x | 0,
                    i[2] = i[2] + T | 0,
                    i[3] = i[3] + A | 0
                },
                _doFinalize: function() {
                    var e = this._data
                      , n = e.words
                      , r = 8 * this._nDataBytes
                      , o = 8 * e.sigBytes;
                    n[o >>> 5] |= 128 << 24 - o % 32;
                    var i = t.floor(r / 4294967296)
                      , a = r;
                    n[15 + (o + 64 >>> 9 << 4)] = 16711935 & (i << 8 | i >>> 24) | 4278255360 & (i << 24 | i >>> 8),
                    n[14 + (o + 64 >>> 9 << 4)] = 16711935 & (a << 8 | a >>> 24) | 4278255360 & (a << 24 | a >>> 8),
                    e.sigBytes = 4 * (n.length + 1),
                    this._process();
                    for (var s = this._hash, u = s.words, c = 0; c < 4; c++) {
                        var l = u[c];
                        u[c] = 16711935 & (l << 8 | l >>> 24) | 4278255360 & (l << 24 | l >>> 8)
                    }
                    return s
                },
                clone: function() {
                    var t = i.clone.call(this);
                    return t._hash = this._hash.clone(),
                    t
                }
            });
            function c(t, e, n, r, o, i, a) {
                var s = t + (e & n | ~e & r) + o + a;
                return (s << i | s >>> 32 - i) + e
            }
            function l(t, e, n, r, o, i, a) {
                var s = t + (e & r | n & ~r) + o + a;
                return (s << i | s >>> 32 - i) + e
            }
            function f(t, e, n, r, o, i, a) {
                var s = t + (e ^ n ^ r) + o + a;
                return (s << i | s >>> 32 - i) + e
            }
            function d(t, e, n, r, o, i, a) {
                var s = t + (n ^ (e | ~r)) + o + a;
                return (s << i | s >>> 32 - i) + e
            }
            e.MD5 = i._createHelper(u),
            e.HmacMD5 = i._createHmacHelper(u)
        }(Math),
        r.MD5)
    },
})


function aa(url){
    // return pdd(83455)("55b03"+pdd(83455)("bundle=category_landing_page&cat_level=1&catid=11012819&limit=60&offset=120",undefined).toString()+"55b03").toString()
    return "55b03-" + pdd(83455)("55b03"+pdd(83455)(url,undefined).toString()+"55b03").toString()

}
console.log(aa('bundle=category_landing_page&cat_level=1&catid=11012819&limit=60&offset=60'))