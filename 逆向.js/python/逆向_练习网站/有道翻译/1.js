var d = 'fanyideskweb'
var u = 'fanyideskweb'
var t ='fsdsogkndfokasodnaso'
var h = function h(e, t) {
    return v(`client=${d}&mysticTime=${e}&product=${u}&key=${t}`)
}
r =  function() {
            return e
        }
function v(e) {
    return r.a.createHash("md5").update(e.toString()).digest("hex")
}
t.exports = function(t) {
            return t = t.toLowerCase(),
            "md5" === t ? new i : "rmd160" === t || "ripemd160" === t ? new o : new u(s(t))
        }
console.log(h('fsdsogkndfokasodnaso',1683619857652))