var s = function(e, t) {
            function n(e, t) {
                return e << t | e >>> 32 - t
            }
            function r(e, t) {
                var n, r, u, o, l;
                return u = 2147483648 & e,
                o = 2147483648 & t,
                l = (1073741823 & e) + (1073741823 & t),
                (n = 1073741824 & e) & (r = 1073741824 & t) ? 2147483648 ^ l ^ u ^ o : n | r ? 1073741824 & l ? 3221225472 ^ l ^ u ^ o : 1073741824 ^ l ^ u ^ o : l ^ u ^ o
            }
            function u(e, t, u, o, l, i, c) {
                return e = r(e, r(r(function(e, t, n) {
                    return e & t | ~e & n
                }(t, u, o), l), c)),
                r(n(e, i), t)
            }
            function o(e, t, u, o, l, i, c) {
                return e = r(e, r(r(function(e, t, n) {
                    return e & n | t & ~n
                }(t, u, o), l), c)),
                r(n(e, i), t)
            }
            function l(e, t, u, o, l, i, c) {
                return e = r(e, r(r(function(e, t, n) {
                    return e ^ t ^ n
                }(t, u, o), l), c)),
                r(n(e, i), t)
            }
            function i(e, t, u, o, l, i, c) {
                return e = r(e, r(r(function(e, t, n) {
                    return t ^ (e | ~n)
                }(t, u, o), l), c)),
                r(n(e, i), t)
            }
            function c(e) {
                var t, n = "", r = "";
                for (t = 0; t <= 3; t++)
                    n += (r = "0" + (e >>> 8 * t & 255).toString(16)).substr(r.length - 2, 2);
                return n
            }
            var d, a, s, p, h, f, m, v, g, y = e, b = Array();
            for (b = function(e) {
                for (var t, n = e.length, r = n + 8, u = 16 * ((r - r % 64) / 64 + 1), o = Array(u - 1), l = 0, i = 0; i < n; )
                    l = i % 4 * 8,
                    o[t = (i - i % 4) / 4] = o[t] | e.charCodeAt(i) << l,
                    i++;
                return l = i % 4 * 8,
                o[t = (i - i % 4) / 4] = o[t] | 128 << l,
                o[u - 2] = n << 3,
                o[u - 1] = n >>> 29,
                o
            }(y),
            f = 1732584193,
            m = 4023233417,
            v = 2562383102,
            g = 271733878,
            d = 0; d < b.length; d += 16)
                a = f,
                s = m,
                p = v,
                h = g,
                m = i(m = i(m = i(m = i(m = l(m = l(m = l(m = l(m = o(m = o(m = o(m = o(m = u(m = u(m = u(m = u(m, v = u(v, g = u(g, f = u(f, m, v, g, b[d + 0], 7, 3614090360), m, v, b[d + 1], 12, 3905402710), f, m, b[d + 2], 17, 606105819), g, f, b[d + 3], 22, 3250441966), v = u(v, g = u(g, f = u(f, m, v, g, b[d + 4], 7, 4118548399), m, v, b[d + 5], 12, 1200080426), f, m, b[d + 6], 17, 2821735955), g, f, b[d + 7], 22, 4249261313), v = u(v, g = u(g, f = u(f, m, v, g, b[d + 8], 7, 1770035416), m, v, b[d + 9], 12, 2336552879), f, m, b[d + 10], 17, 4294925233), g, f, b[d + 11], 22, 2304563134), v = u(v, g = u(g, f = u(f, m, v, g, b[d + 12], 7, 1804603682), m, v, b[d + 13], 12, 4254626195), f, m, b[d + 14], 17, 2792965006), g, f, b[d + 15], 22, 1236535329), v = o(v, g = o(g, f = o(f, m, v, g, b[d + 1], 5, 4129170786), m, v, b[d + 6], 9, 3225465664), f, m, b[d + 11], 14, 643717713), g, f, b[d + 0], 20, 3921069994), v = o(v, g = o(g, f = o(f, m, v, g, b[d + 5], 5, 3593408605), m, v, b[d + 10], 9, 38016083), f, m, b[d + 15], 14, 3634488961), g, f, b[d + 4], 20, 3889429448), v = o(v, g = o(g, f = o(f, m, v, g, b[d + 9], 5, 568446438), m, v, b[d + 14], 9, 3275163606), f, m, b[d + 3], 14, 4107603335), g, f, b[d + 8], 20, 1163531501), v = o(v, g = o(g, f = o(f, m, v, g, b[d + 13], 5, 2850285829), m, v, b[d + 2], 9, 4243563512), f, m, b[d + 7], 14, 1735328473), g, f, b[d + 12], 20, 2368359562), v = l(v, g = l(g, f = l(f, m, v, g, b[d + 5], 4, 4294588738), m, v, b[d + 8], 11, 2272392833), f, m, b[d + 11], 16, 1839030562), g, f, b[d + 14], 23, 4259657740), v = l(v, g = l(g, f = l(f, m, v, g, b[d + 1], 4, 2763975236), m, v, b[d + 4], 11, 1272893353), f, m, b[d + 7], 16, 4139469664), g, f, b[d + 10], 23, 3200236656), v = l(v, g = l(g, f = l(f, m, v, g, b[d + 13], 4, 681279174), m, v, b[d + 0], 11, 3936430074), f, m, b[d + 3], 16, 3572445317), g, f, b[d + 6], 23, 76029189), v = l(v, g = l(g, f = l(f, m, v, g, b[d + 9], 4, 3654602809), m, v, b[d + 12], 11, 3873151461), f, m, b[d + 15], 16, 530742520), g, f, b[d + 2], 23, 3299628645), v = i(v, g = i(g, f = i(f, m, v, g, b[d + 0], 6, 4096336452), m, v, b[d + 7], 10, 1126891415), f, m, b[d + 14], 15, 2878612391), g, f, b[d + 5], 21, 4237533241), v = i(v, g = i(g, f = i(f, m, v, g, b[d + 12], 6, 1700485571), m, v, b[d + 3], 10, 2399980690), f, m, b[d + 10], 15, 4293915773), g, f, b[d + 1], 21, 2240044497), v = i(v, g = i(g, f = i(f, m, v, g, b[d + 8], 6, 1873313359), m, v, b[d + 15], 10, 4264355552), f, m, b[d + 6], 15, 2734768916), g, f, b[d + 13], 21, 1309151649), v = i(v, g = i(g, f = i(f, m, v, g, b[d + 4], 6, 4149444226), m, v, b[d + 11], 10, 3174756917), f, m, b[d + 2], 15, 718787259), g, f, b[d + 9], 21, 3951481745),
                f = r(f, a),
                m = r(m, s),
                v = r(v, p),
                g = r(g, h);
            return 32 == t ? c(f) + c(m) + c(v) + c(g) : c(m) + c(v)
        }
console.log(s('',''))