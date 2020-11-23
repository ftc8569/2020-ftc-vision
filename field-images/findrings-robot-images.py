import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

# See https://www.youtube.com/watch?v=WQeoO7MI0Bs
# chapter 7 masking an image
# chapter 8 contours

imgBGR = cv2.imread('field-images/robot-images/ring-lab-one.png')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
imgHSV = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2HSV)

lower = np.array([5,100,0])
upper = np.array([25,255,255])
mask = cv2.inRange(imgHSV, lower, upper)
blurMask = cv2.medianBlur(mask,11)


# find the bounding rectangles
contours, hiearchy = cv2.findContours(blurMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
maxContourArea = 0
maxCountour = None
ringFound = False
for c in contours:
     poly = cv2.approxPolyDP(c,3,True)
     rect = cv2.boundingRect(poly)
     contourArea = cv2.contourArea(c)
     if (contourArea > maxContourArea):
          ringFound = True
          ringContourArea = contourArea
          maxContour = c
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


fig, (axImgRGB, axHSV, axMask, axBlur) = plt.subplots(1, 4, figsize=(8, 2.5))

axImgRGB.imshow(imgRGB)
axImgRGB.set_title('Original')
axImgRGB.axis('off')

axHSV.imshow(imgHSV)
axHSV.set_title('HSV')
axHSV.axis('off')

axMask.imshow(mask)
axMask.set_title('Mask')
axMask.axis('off')

axBlur.imshow(blurMask)
axBlur.set_title('Blur')
axBlur.axis('off')

plt.show()


