# Basic Functions

import cv2
import numpy as np

# read image
curr_img = cv2.imread('resources/test_img.jpg')
# resize img
img = cv2.resize(curr_img, (400, 400))

# define a kernel
kernel = np.ones((5, 5), np.uint8)

# convert into gray scale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray output", imgGray)

# blur function
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
cv2.imshow("Blur img", imgBlur)

# edge detection
imgCanny = cv2.Canny(img, 100, 100)
cv2.imshow("edge output", imgCanny)

# dilation (thicker)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
cv2.imshow("img dilation", imgDilation)

# erosion (thinner)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)
cv2.imshow("img erosion", imgEroded)

cv2.waitKey(0)
