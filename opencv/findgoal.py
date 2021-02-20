import cv2
import numpy as np
import os

def empty(x):
     pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",600,300)
cv2.createTrackbar("Hue Min","TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max","TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min","TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat Max","TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min","TrackBars", 0, 255, empty)
cv2.createTrackbar("Val Max","TrackBars", 255, 255, empty)


img = cv2.imread('shooting-blue-1.png')
# img = cv2.imread('four-rings.jpg')
# img = cv2.imread('no-rings.jpg')
# img = cv2.imread('one-ring.jpg')

# imgResize = cv2.resize(img,(img.shape[1]//4, img.shape[0]//4), interpolation=cv2.INTER_LINEAR)
# cv2.imshow('Image', imgResize)

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image', imgHSV)


while True:
     h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
     h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
     s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
     s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
     v_min = cv2.getTrackbarPos("Val Min","TrackBars")
     v_max = cv2.getTrackbarPos("Val Max","TrackBars")
     print(h_min, h_max, s_min, s_max, v_min, v_max)

     lower = np.array([h_min, s_min, v_min])
     upper = np.array([h_max, s_max, v_max])
     mask = cv2.inRange(imgHSV, lower, upper)

     kernel = np.ones((3, 3), np.uint8)
     # Repeat the erosion and dilation by changing iterations.
     mask_erode = cv2.erode(mask, kernel, iterations=1)
     blurMask = cv2.dilate(mask_erode, kernel, iterations=1)

     # blurMask = cv2.medianBlur(mask,5)

     cv2.imshow('Mask', mask)
     cv2.imshow('Blur Mask', blurMask)

     if cv2.waitKey(1) == ord('q'):
          break



