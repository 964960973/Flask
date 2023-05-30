# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 17:13:56 2019

@author: Lee
"""

import pytesseract
from PIL import Image

image = Image.open('./img.png')
info = pytesseract.image_to_string(image,lang="chi_sim")
images = Image.open('./img_1.png')
info1 = pytesseract.image_to_string(images,lang="chi_sim")
print(info)
print(info1)
