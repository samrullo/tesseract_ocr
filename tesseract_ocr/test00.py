import os
from PIL import Image
import sys

import pyocr
import pyocr.builders


# os.environ['TESSDATA_PREFIX']=r"C:\Program Files\Tesseract-OCR\tessdata"

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
lang = langs[0]
print("Will use lang '%s'" % (lang))
# Ex: Will use lang 'fra'
# Note that languages are NOT sorted in any way. Please refer
# to the system locale settings for the default language
# to use.

txt = tool.image_to_string(
    Image.open(os.path.relpath('../iroha.jpg')),
    lang="jpn",
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)
print( txt )
# txt is a Python string