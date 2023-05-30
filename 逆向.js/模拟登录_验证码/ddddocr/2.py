import ddddocr

# 识别图片验证码
ocr = ddddocr.DdddOcr()
with open('./img_2.png','rb') as f:
    img_bytes = f.read()
res = ocr.classification(img_bytes)
print(res)