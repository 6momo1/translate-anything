"""

this module detects words on a image and displays a translation on top of it 

"""
import cv2
import pytesseract
from dominant_color_extractor import DominantColors


pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"


original = cv2.imread('./assets/amazon.png')
img = original.copy()

# get the dominant color of this image (background color)
clusters = 5
dc = DominantColors(original, clusters)
colors = dc.dominantColors()
colors = colors.tolist()

# convert bgr to rgb
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# get image dimensions
hImg, wImg, imgDimension = img.shape

# Detect words
boxes = pytesseract.image_to_data(img)

# iterate through words
for num, string in enumerate(boxes.splitlines()):

    # if we are not reading the first column from the boxes string, then...
    if num != 0:

        # split box cordinate information
        boxInfo = string.split()
        if len(boxInfo) == 12:

            # extract the word and position of each word
            word, x, y, w, h = boxInfo[11], int(boxInfo[6]), int(
                boxInfo[7]), int(boxInfo[8]), int(boxInfo[9])

            # draw the rectangle
            cv2.rectangle(
                original,
                (x, y),
                (w+x, y+h),
                colors[1],
                # (255, 255, 255),
                -1
            )

            # label the word
            cv2.putText(
                original,
                word,
                (x, y+h),
                cv2.FONT_HERSHEY_DUPLEX,
                1,
                (0, 0, 0),
                1
            )


cv2.imshow('Result', original)

cv2.waitKey(0)
