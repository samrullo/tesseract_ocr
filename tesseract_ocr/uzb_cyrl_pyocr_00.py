import os
from PIL import Image
import sys

import pyocr
import pyocr.builders

os.environ['TESSDATA_PREFIX'] = r"C:\Program Files\Tesseract-OCR\tessdata"
folder = r"C:\Users\amrul\Documents\various\izholi_lugat\downloads\a"

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
lang = langs[-1]
print("Will use lang '%s'" % (lang))
# Ex: Will use lang 'fra'
# Note that languages are NOT sorted in any way. Please refer
# to the system locale settings for the default language
# to use.

im_orig = Image.open(os.path.join(folder, "a_2.jpg"))
left_half = (0, 0, im_orig.width / 2, im_orig.height)
right_half = (im_orig.width / 2, 0, im_orig.width, im_orig.height)

left_half_img = im_orig.crop(left_half)
right_half_img = im_orig.crop(right_half)

txt_left = tool.image_to_string(left_half_img, lang="uzb_cyrl", builder=pyocr.builders.TextBuilder(tesseract_layout=6))
txt_right = tool.image_to_string(right_half_img, lang="uzb_cyrl", builder=pyocr.builders.TextBuilder(tesseract_layout=6))
print(txt_left)
# txt is a Python string

left_part_words = txt_left.split("\n\n")
right_part_words = txt_right.split("\n\n")

print("##################  LEFT PART WORDS #############################")
for no, word in enumerate(left_part_words):
    print("\n")
    print(f"{no} : {word}")
    print("\n")

print("##################  RIGHT PART WORDS #############################")
for no, word in enumerate(right_part_words):
    print("\n")
    print(f"{no} : {word}")
    print("\n")