# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 17:13:56 2019

@author: Lee
"""

import pytesseract
import tesserocr
from PIL import Image
# image = Image.open('image.png')
# print(tesserocr.image_to_text(image))
from PIL import Image

image = Image.open('img.png')
info = pytesseract.image_to_string(image,lang="chi_sim")
info1 = tesserocr.image_to_text(image,lang="chi_sim")
print(info1)
