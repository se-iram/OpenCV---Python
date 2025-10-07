# Shapes and Texts
import cv2
import numpy as np

# create black image
img_black = np.zeros((512, 512, 3))

# create colored img
img_clr = np.zeros((512, 512, 3), np.uint8)
print(img_clr)
img_clr[200:300, 200:300] = 225,225,0

# create line
cv2.line(img_black, (0, 0), (200, 200), (0, 250, 0), 3)
cv2.line(img_clr, (0, 0 ), (img_clr.shape[1], img_clr.shape[0]), (0, 0, 255), 2)

# create a rectangle
cv2.rectangle(img_black, (200,300), (250, 100), (0, 0, 255), 2)     # cv2.FILLED
# create a circle
cv2.circle(img_black, (400, 50), 40, (255, 0, 0), 3)
# text on img
cv2.putText(img_black, "Hello World!", (100, 400), cv2.FONT_HERSHEY_PLAIN, 2, (0, 100, 150), 1)
cv2.imshow("img output", img_black)
cv2.imshow("clr img output", img_clr)

cv2.waitKey(0)