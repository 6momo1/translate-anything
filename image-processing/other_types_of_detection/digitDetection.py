import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread('./assets/musk_tweet.png')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

hImg, wImg, imgDimension = img.shape


# Detect Digits Only

# config tesseract to filter for digits only
con = r'--oem 3 --psm 6 outputbase digits'

boxes = pytesseract.image_to_data(img, config=con)

for num, string in enumerate(boxes.splitlines()):

    # if we are not reading the first column from the boxes string, then:
    if num != 0:

        # box cordinate information
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
                (0, 0, 200), 1
            )

            # label the word
            cv2.putText(
                img,
                word,
                (x, y-5),
                cv2.FONT_HERSHEY_COMPLEX_SMALL,
                1,
                (0, 0, 200),
                1
            )

cv2.imshow('Result', img)

cv2.waitKey(0)
