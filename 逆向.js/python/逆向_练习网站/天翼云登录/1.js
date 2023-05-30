var CryptoJS = require("crypto-js");

var key = CryptoJS.enc.Utf8.parse("G3JH98Y8MY9GWKWG")
var plaintText = "123456";

	// var key1 = CryptoJS.enc.Latin1.parse("G3JH98Y8MY9GWKWG");//key为密钥，16位的字符串
	// var iv1 = CryptoJS.enc.Latin1.parse("123456");//iv为偏移量，16位的字符串

	//CBC加密
	// var encryptedData = CryptoJS.AES.encrypt(plaintText, key, {
	//     iv:  CryptoJS.enc.Utf8.parse(key),
	//     mode: CryptoJS.mode.CBC,
	//     padding: CryptoJS.pad.Pkcs7
	// })

	//ECB模式
	var encryptedData = CryptoJS.AES.encrypt(plaintText, key, {
	    mode: CryptoJS.mode.ECB,
	    padding: CryptoJS.pad.Pkcs7
	})


	encryptedData = encryptedData.ciphertext.toString();
	console.log(encryptedData)
