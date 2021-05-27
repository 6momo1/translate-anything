"""

this module intends to extract sentences from an image

"""
import cv2
import pytesseract


class process_image:

    def __init__(self, image: str) -> None:

        self.pytesseract = pytesseract
        self.pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        self.image = image
        self.texts = ""

    def get_text(self):

        img = cv2.imread(self.image)

        # convert bgr to rgb
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # get string
        strings = self.pytesseract.image_to_string(img)
        self.texts = strings
        return strings


image = "./assets/musk_tweet.png"
texts = process_image(image).get_text()
print(texts)
