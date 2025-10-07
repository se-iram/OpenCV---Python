# Resizing and cropping
import cv2

img = cv2.imread('resources/test_img.jpg')
print(img.shape)

# resize img
imgResize = cv2.resize(img, (400, 400))     # (width, height)
print(imgResize.shape)

# cropped img
imgCropped = imgResize[100:300, 100:300]      # (height, width)

cv2.imshow("img", img)
cv2.imshow("img Resize", imgResize)
cv2.imshow("img cropped", imgCropped)
cv2.waitKey(0)
