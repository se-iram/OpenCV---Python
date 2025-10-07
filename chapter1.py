# Reading Image, Video and Webcam

import cv2

# reading image
# img = cv2.imread('resources/img4.jpg')
# cv2.imshow('output', img)
# cv2.waitKey(3000)


# reading video
# cap = cv2.VideoCapture('resources/test_video.mp4')
# need a loop to go through each frame one by one
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video output", img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break


# reading webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)     # width
cap.set(4, 480)     # height
cap.set(10, 100)    # brightness
while True:
    success, img = cap.read()
    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
