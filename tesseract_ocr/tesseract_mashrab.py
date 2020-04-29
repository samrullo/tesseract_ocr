import os
from tesseract_ocr.tesseract_image_reader import TesseractImageReader
import logging

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

folder = r"C:\Users\amrul\Documents\ziyo_istagan_qalblar_uchun"
img_file = "men_nola_qilay_shomu_sahar_dod_eshigingda.JPG"
tesseract_lang = "uzb_cyrl"

tesseract_reader = TesseractImageReader(folder, img_file, tesseract_lang)
txt = tesseract_reader.get_text_from_image()
