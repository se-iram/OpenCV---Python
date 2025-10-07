# warp perspective
import cv2
import numpy as np

# pixel values: 269, 218 | 511, 218 | 269, 423 | 511, 423
width, height = 400, 400
test_img = cv2.imread('resources/card.jpg')
img = cv2.resize(test_img, (600, 500))

pts1 = np.float32([[269, 218], [511, 218], [269, 423], [511, 423]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
# transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("img", img)
cv2.imshow("output", imgOutput)
cv2.waitKey(0)
