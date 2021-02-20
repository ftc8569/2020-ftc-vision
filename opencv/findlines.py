import cv2
import numpy as np
import os

from numpy.lib.function_base import piecewise


img = cv2.imread('shooting-blue-1.png')
cv2.imshow('Image', img)

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV Image', imgHSV)

# 75 179 25 196 25 255
lower = np.array([75,25,25])
upper = np.array([179,196,255])
mask = cv2.inRange(imgHSV, lower, upper)
blurMask = cv2.medianBlur(mask,11)
cannyMask = cv2.Canny(blurMask,0,1)

cv2.imshow('Mask', mask)
cv2.imshow('Blur Mask', blurMask)
cv2.imshow('Canny Mask', cannyMask)

lines = cv2.HoughLines(cannyMask, 1, np.pi/180 , 50)
horizontal_line_count = 0
horizontal_rho_total = 0
horizontal_theta_total = 0
vertical_line_count = 0
vertical_rho_total = 0
vertical_theta_total = 0

print(f"found {len(lines)} lines")

for line in lines:
    rho,theta = line[0]
    print(rho,180*theta/np.pi)

    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    # horizontal lines have a theta of 90 degrees (positive x is right, positive y is down, positive theta is counter clockwise from x toward y)
    # separate the horizontal from the vertical lines
    horizontal_line_theta = 90/180 * np.pi
    horizontal_line_threshold = 10/180 * np.pi # within 10 degrees of horizontal
    if abs(theta - horizontal_line_theta) < horizontal_line_threshold:
        horizontal_rho_total += rho
        horizontal_theta_total += theta
        horizontal_line_count += 1
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    else:
        vertical_rho_total += rho
        vertical_theta_total += theta
        vertical_line_count += 1
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow('lines', img)

horizontal_rho_average = horizontal_rho_total / horizontal_line_count
horizontal_theta_average = horizontal_theta_total / horizontal_line_count

vertical_rho_average = vertical_rho_total / vertical_line_count
vertical_theta_average = vertical_theta_total / vertical_line_count

print(f"horiztonal average rho={horizontal_rho_average}, theta={180*horizontal_theta_average/np.pi}")
print(f"vertical average rho={vertical_rho_average}, theta={180*vertical_theta_average/np.pi}")


cv2.waitKey(0)
