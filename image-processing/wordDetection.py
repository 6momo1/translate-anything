
import cv2
import pytesseract
from dominant_color_extractor import DominantColors

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread('./assets/musk_tweet.png')

# get the dominant color of this image (background color)
clusters = 5
dc = DominantColors(img, clusters)
colors = dc.dominantColors()
colors = colors.tolist()

# convert bgr to rgb
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# get image dimensions
hImg, wImg, imgDimension = img.shape

# Detect words
boxes = pytesseract.image_to_data(img)
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
                img,
                (x, y),
                (w+x, y+h),
                colors[0],
                -1
            )

            # label the word
            cv2.putText(
                img,
                word,
                (x, y-5),
                cv2.FONT_HERSHEY_COMPLEX_SMALL,
                1,
                (0, 0, 0),
                1
            )


cv2.imshow('Result', img)

cv2.waitKey(0)
