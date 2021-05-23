
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img = cv2.imread('./assets/musk_tweet.png')
# img = cv2.imread('./assets/twttr.png')

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img = cv2.resize(img, (0, 0), fx=2, fy=2)
# print(pytesseract.image_to_string(img))

hImg, wImg, imgDimension = img.shape


# Detect words
boxes = pytesseract.image_to_data(img)
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


# # detect individual characters
# boxes = pytesseract.image_to_boxes(img)
# for string in boxes.splitlines():

#     boxInfo = string.split(' ')

#     print(boxInfo)

#     char, xbox, ybox, wbox, hbox = boxInfo[0], int(boxInfo[1]), int(
#         boxInfo[2]), int(boxInfo[3]), int(boxInfo[4])

#     # draw the ractangles on the image
#     cv2.rectangle(
#         img,
#         (xbox, hImg-ybox),
#         (wbox, hImg - hbox),
#         (0, 0, 200), 1
#     )

#     cv2.putText(
#         img,
#         char,
#         (xbox, hImg-ybox+15),
#         cv2.FONT_HERSHEY_COMPLEX_SMALL,
#         1,
#         (0, 0, 200),
#         1
#     )

cv2.imshow('Result', img)

cv2.waitKey(0)
