# Face detection

import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")

# # read images
# path = "resources/faces.jpg"
# img = cv2.imread(path)
# # convert img to gray scale
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
#
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#
# cv2.imshow("output", img)
# cv2.waitKey(0)

# read webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
# cap.set(10, 100)
# check if webcam is not opened successfully
if not cap.isOpened():
    print("Error: could not open webcam.")
    exit()

# Read frames from webcam
while True:
    success, frame = cap.read()
    if not success:
        print("Failed to rab frame.")
        break

    # convert frame to gray scale
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detect face in frame
    webcamFaces = faceCascade.detectMultiScale(frameGray, 1.1, 4)
    # draw rectangle
    for (x, y, w, h) in webcamFaces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # show result
    cv2.imshow("Wbcam", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()