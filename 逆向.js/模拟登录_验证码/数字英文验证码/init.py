# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 17:13:56 2019

@author: Lee
"""

import pytesseract
import tesserocr
from PIL import Image

image = Image.open('000.jpg')
image2 = Image.open('img.png')
image3 = Image.open('img_1.png')
image4 = Image.open('img_4.png')
# info = pytesseract.image_to_string(image,lang="chi_sim")
# info = tesserocr.image_to_text(image,lang="eng")
info1 = tesserocr.image_to_text(image4,lang="eng")
info2 = tesserocr.image_to_text(image2)
info3 = tesserocr.image_to_text(image3)
info4 = tesserocr.image_to_text(image4)
# print(info,info1,info2,info3,info4)
print(info1)