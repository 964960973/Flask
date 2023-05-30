import ddddocr

det = ddddocr.DdddOcr(det=False, ocr=False)

with open('a.png', 'rb') as f:
    target_bytes = f.read()

with open('img1.png', 'rb') as f:
    background_bytes = f.read()

res = det.slide_match(target_bytes, background_bytes, simple_target=True)
print(res)

