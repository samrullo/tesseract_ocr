import os
import sys
from PIL import Image
import pyocr.builders
import logging


class TesseractImageReader:
    """
    This class converts TEXT image to text.
    You need to specify the folder, image file and the tesseract language
    The class assumes that tesseract-ocr is installed on your system
    """

    def __init__(self, folder, img_file, tesseract_lang):
        self.folder = folder
        self.img_file = img_file
        os.environ['TESSDATA_PREFIX'] = r"C:\Program Files\Tesseract-OCR\tessdata"
        self.tesseract_lang = tesseract_lang
        self.tesseract_tool = self.get_tesseract_tool()

    def get_tesseract_tool(self):
        tools = pyocr.get_available_tools()
        if len(tools) == 0:
            print("No OCR tool found")
            sys.exit(1)
        # The tools are returned in the recommended order of usage
        tool = tools[0]
        print("Will use tool '%s'" % (tool.get_name()))
        return tool

    def get_text_from_image(self):
        im_orig = Image.open(os.path.join(self.folder, self.img_file))
        text = self.tesseract_tool.image_to_string(im_orig, lang=self.tesseract_lang, builder=pyocr.builders.TextBuilder(tesseract_layout=6))
        logging.info(f"Extracted text :\n{text}")
        return text
