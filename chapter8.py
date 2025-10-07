# contours and shapes detection

import cv2
import numpy as np


def getcontours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(cnt)
        # now draw these areas
        cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
        # calculate corners of shapes
        perimeter = cv2.arcLength(cnt, True)
        # print(perimeter)
        # approx the corner points
        approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
        print(len(approx))
        objCor = len(approx)
        # create a bounding box around obj
        x, y, w, h = cv2.boundingRect(approx)

        # categorize objects
        if objCor == 3:
            objectType = "Tri"
        elif objCor == 4:
            aspectRatio = w/float(h)
            if aspectRatio > 0.95 and aspectRatio < 1.05:
                objectType = "Square"
            else:
                objectType = "Rectangle"
        elif objCor > 4:
            objectType = "Circle"
        else:
            objectType = "None"

        cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(imgContour, objectType, (x+(w//2)-10, y+(h//2)), cv2.FONT_HERSHEY_PLAIN, 0.7, (0, 0, 0), 1)


path = 'resources/test_shape.png'
img = cv2.imread(path)
img = cv2.resize(img, (700, 500))

imgContour = img.copy()

# first convert it into gray scale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# add a little bit blur
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# Find the edges
imgCanny = cv2.Canny(imgBlur, 150, 400)
# call function to get contours
getcontours(imgCanny)

cv2.imshow("Original", img)
cv2.imshow("gray", imgGray)
cv2.imshow("blur", imgBlur)
cv2.imshow("canny", imgCanny)
cv2.imshow("contour", imgContour)
cv2.waitKey(0)
