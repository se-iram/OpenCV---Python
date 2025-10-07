# Joining

import cv2
import numpy as np

test_img = cv2.imread('resources/test_img.jpg')
img = cv2.resize(test_img, (400, 400))

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])

    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range (0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, )

# hor = np.hstack((img, img))
# ver = np.vstack((img, img))
# cv2.imshow("Horizontal", hor)
# cv2.imshow("Vertical", ver)

cv2.waitKey(0)
