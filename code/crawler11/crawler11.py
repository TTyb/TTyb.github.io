# !/usr/bin/python3.4
# -*- coding: utf-8 -*-

import pytesseract
from PIL import Image

image = Image.open('../jpg/code.png')
code = pytesseract.image_to_string(image)
print(code)