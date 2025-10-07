# color detection
import cv2
import numpy as np

path = 'resources/test_img.jpg'


# this function will call when any change happen in trackbars
def empty(a):
    pass


# introduce track bars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", (400, 250))
# trackbars
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 142, 179, empty)
cv2.createTrackbar("Saturation Min", "TrackBars", 107, 255, empty)
cv2.createTrackbar("Saturation Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Value Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Value Max", "TrackBars", 255, 255, empty)

curr_img = cv2.imread(path)
img = cv2.resize(curr_img, (400, 400))

while True:
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # get values from trackbars
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Saturation Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Saturation Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Value Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Value Max", "TrackBars")
    # print(h_min, h_max, s_min, s_max, v_min, v_max)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("output", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("img result", imgResult)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == 27:
        break

cv2.destroyAllWindows()
