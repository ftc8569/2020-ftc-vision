import cv2
import numpy as np
import os

# See https://www.youtube.com/watch?v=WQeoO7MI0Bs
# chapter 7 masking an image
# chapter 8 contours

img = cv2.imread('four-rings.jpg')
# img = cv2.imread('no-rings.jpg')
# img = cv2.imread('one-ring.jpg')
imgResize = cv2.resize(img,(640,480))
cv2.imshow('640x480 Image', imgResize)

imgHSV = cv2.cvtColor(imgResize, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image', imgHSV)

lower = np.array([6,155,70])
upper = np.array([67,255,255])
mask = cv2.inRange(imgHSV, lower, upper)
blurMask = cv2.medianBlur(mask,11)
cannyMask = cv2.Canny(blurMask,0,1)

cv2.imshow('Mask', mask)
cv2.imshow('Blur Mask', blurMask)
cv2.imshow('Canny Mask', cannyMask)

# find the bounding rectangles
contours, hiearchy = cv2.findContours(cannyMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
ringContourArea = 0;
ringFound = False
for c in contours:
     poly = cv2.approxPolyDP(c,3,True)
     rect = cv2.boundingRect(poly)
     contourArea = cv2.contourArea(c)
     if (contourArea > ringContourArea and contourArea > 1000):
          ringFound = True
          ringContourArea = contourArea
          ringContour = c
          ringBoundingRect = rect

if (ringFound):
     if(ringContourArea < 7500):
          print("Found One Ring")
     else:
          print("Found Four Rings")
     print(ringContourArea)
     print(ringBoundingRect)
else:
     print("Found No Rings")

cv2.waitKey(0)



# def empty(x):
#      pass

# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars",600,300)
# cv2.createTrackbar("Hue Min","TrackBars", 0, 179, empty)
# cv2.createTrackbar("Hue Max","TrackBars", 179, 179, empty)
# cv2.createTrackbar("Sat Min","TrackBars", 0, 255, empty)
# cv2.createTrackbar("Sat Max","TrackBars", 255, 255, empty)
# cv2.createTrackbar("Val Min","TrackBars", 0, 255, empty)
# cv2.createTrackbar("Val Max","TrackBars", 255, 255, empty)
# while True:
#     h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
#     h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
#     s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
#     s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
#     v_min = cv2.getTrackbarPos("Val Min","TrackBars")
#     v_max = cv2.getTrackbarPos("Val Max","TrackBars")
#     print(h_min, h_max, s_min, s_max, v_min, v_max)
