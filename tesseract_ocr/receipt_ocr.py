import os
from PIL import Image
import sys
import matplotlib.pyplot as plt

import pyocr
import pyocr.builders

os.environ['TESSDATA_PREFIX'] = r"C:\Program Files\Tesseract-OCR\tessdata"

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = 'eng'
print("Will use lang '%s'" % (lang))

folder = r"C:\Users\amrul\Documents\programming\tesseract_dataset"
img_file = "fibonacci_01.jpg"

img = Image.open(os.path.join(folder, img_file))

txt = tool.image_to_string(img, lang=lang, builder=pyocr.builders.TextBuilder(tesseract_layout=6))

print(f"Processed text :\n {txt}")
plt.imshow(img)
