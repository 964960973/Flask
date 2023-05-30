function md5(e, t) {
                function n(e, t) {
                    return e << t | e >>> 32 - t
                }
                function i(e, t) {
                    var n, i, a, r, o;
                    return a = 2147483648 & e,
                    r = 2147483648 & t,
                    n = 1073741824 & e,
                    i = 1073741824 & t,
                    o = (1073741823 & e) + (1073741823 & t),
                    n & i ? 2147483648 ^ o ^ a ^ r : n | i ? 1073741824 & o ? 3221225472 ^ o ^ a ^ r : 1073741824 ^ o ^ a ^ r : o ^ a ^ r
                }
                function a(e, t, a, r, o, s, l) {
                    return e = i(e, i(i(function(e, t, n) {
                        return e & t | ~e & n
                    }(t, a, r), o), l)),
                    i(n(e, s), t)
                }
                function r(e, t, a, r, o, s, l) {
                    return e = i(e, i(i(function(e, t, n) {
                        return e & n | t & ~n
                    }(t, a, r), o), l)),
                    i(n(e, s), t)
                }
                function o(e, t, a, r, o, s, l) {
                    return e = i(e, i(i(function(e, t, n) {
                        return e ^ t ^ n
                    }(t, a, r), o), l)),
                    i(n(e, s), t)
                }
                function s(e, t, a, r, o, s, l) {
                    return e = i(e, i(i(function(e, t, n) {
                        return t ^ (e | ~n)
                    }(t, a, r), o), l)),
                    i(n(e, s), t)
                }
                function l(e) {
                    var t, n = "", i = "";
                    for (t = 0; t <= 3; t++)
                        n += (i = "0" + (e >>> 8 * t & 255).toString(16)).substr(i.length - 2, 2);
                    return n
                }
                var c, u, d, p, m, h, f, v, y, g = e, b = Array();
                for (b = function(e) {
                    for (var t, n = e.length, i = n + 8, a = 16 * ((i - i % 64) / 64 + 1), r = Array(a-1), o = 0, s = 0; s < n; )
                        o = s % 4 * 8,
                        r[t = (s - s % 4) / 4] = r[t] | e.charCodeAt(s) << o,
                        s++;
                    return t = (s - s % 4) / 4,
                    o = s % 4 * 8,
                    r[t] = r[t] | 128 << o,
                    r[a - 2] = n << 3,
                    r[a - 1] = n >>> 29,
                    r
                }(g),
                h = 1732584193,
                f = 4023233417,
                v = 2562383102,
                y = 271733878,
                c = 0; c < b.length; c += 16)
                    u = h,
                    d = f,
                    p = v,
                    m = y,
                    f = s(f = s(f = s(f = s(f = o(f = o(f = o(f = o(f = r(f = r(f = r(f = r(f = a(f = a(f = a(f = a(f, v = a(v, y = a(y, h = a(h, f, v, y, b[c + 0], 7, 3614090360), f, v, b[c + 1], 12, 3905402710), h, f, b[c + 2], 17, 606105819), y, h, b[c + 3], 22, 3250441966), v = a(v, y = a(y, h = a(h, f, v, y, b[c + 4], 7, 4118548399), f, v, b[c + 5], 12, 1200080426), h, f, b[c + 6], 17, 2821735955), y, h, b[c + 7], 22, 4249261313), v = a(v, y = a(y, h = a(h, f, v, y, b[c + 8], 7, 1770035416), f, v, b[c + 9], 12, 2336552879), h, f, b[c + 10], 17, 4294925233), y, h, b[c + 11], 22, 2304563134), v = a(v, y = a(y, h = a(h, f, v, y, b[c + 12], 7, 1804603682), f, v, b[c + 13], 12, 4254626195), h, f, b[c + 14], 17, 2792965006), y, h, b[c + 15], 22, 1236535329), v = r(v, y = r(y, h = r(h, f, v, y, b[c + 1], 5, 4129170786), f, v, b[c + 6], 9, 3225465664), h, f, b[c + 11], 14, 643717713), y, h, b[c + 0], 20, 3921069994), v = r(v, y = r(y, h = r(h, f, v, y, b[c + 5], 5, 3593408605), f, v, b[c + 10], 9, 38016083), h, f, b[c + 15], 14, 3634488961), y, h, b[c + 4], 20, 3889429448), v = r(v, y = r(y, h = r(h, f, v, y, b[c + 9], 5, 568446438), f, v, b[c + 14], 9, 3275163606), h, f, b[c + 3], 14, 4107603335), y, h, b[c + 8], 20, 1163531501), v = r(v, y = r(y, h = r(h, f, v, y, b[c + 13], 5, 2850285829), f, v, b[c + 2], 9, 4243563512), h, f, b[c + 7], 14, 1735328473), y, h, b[c + 12], 20, 2368359562), v = o(v, y = o(y, h = o(h, f, v, y, b[c + 5], 4, 4294588738), f, v, b[c + 8], 11, 2272392833), h, f, b[c + 11], 16, 1839030562), y, h, b[c + 14], 23, 4259657740), v = o(v, y = o(y, h = o(h, f, v, y, b[c + 1], 4, 2763975236), f, v, b[c + 4], 11, 1272893353), h, f, b[c + 7], 16, 4139469664), y, h, b[c + 10], 23, 3200236656), v = o(v, y = o(y, h = o(h, f, v, y, b[c + 13], 4, 681279174), f, v, b[c + 0], 11, 3936430074), h, f, b[c + 3], 16, 3572445317), y, h, b[c + 6], 23, 76029189), v = o(v, y = o(y, h = o(h, f, v, y, b[c + 9], 4, 3654602809), f, v, b[c + 12], 11, 3873151461), h, f, b[c + 15], 16, 530742520), y, h, b[c + 2], 23, 3299628645), v = s(v, y = s(y, h = s(h, f, v, y, b[c + 0], 6, 4096336452), f, v, b[c + 7], 10, 1126891415), h, f, b[c + 14], 15, 2878612391), y, h, b[c + 5], 21, 4237533241), v = s(v, y = s(y, h = s(h, f, v, y, b[c + 12], 6, 1700485571), f, v, b[c + 3], 10, 2399980690), h, f, b[c + 10], 15, 4293915773), y, h, b[c + 1], 21, 2240044497), v = s(v, y = s(y, h = s(h, f, v, y, b[c + 8], 6, 1873313359), f, v, b[c + 15], 10, 4264355552), h, f, b[c + 6], 15, 2734768916), y, h, b[c + 13], 21, 1309151649), v = s(v, y = s(y, h = s(h, f, v, y, b[c + 4], 6, 4149444226), f, v, b[c + 11], 10, 3174756917), h, f, b[c + 2], 15, 718787259), y, h, b[c + 9], 21, 3951481745),
                    h = i(h, u),
                    f = i(f, d),
                    v = i(v, p),
                    y = i(y, m);
                return 32 == t ? l(h) + l(f) + l(v) + l(y) : l(f) + l(v)
            }
function get_parme(e, t) {
            var n = String(e)
            return i(n, t >>> 0 || (o.test(n) ? 16 : 10))
        }
function aaa(e, t) {
            return e = String(aaa(e)),
            e
        }
// console.log(get_parme(1e7 * Math.random(), 10))
// var parme = 1660875616751;
// console.log(md5("16608780772275869105",32))
// 16608780772272172437
// 16608780772275869105
// 1660878153059