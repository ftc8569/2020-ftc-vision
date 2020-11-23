import matplotlib.pyplot as plt

from skimage import data, io, color
from skimage.filters import threshold_otsu


imageRGB = io.imread('field-images/test-images/onering-flat.png')
imageHSV = color.rgb2hsv(imageRGB)


imageH = imageHSV[:,:,0]
threshH = 0.1  
binaryH = (imageH < threshH) & (imageH > 0.02)

imageS = imageHSV[:,:,1]
threshS = 0.5 
binaryS = (imageS > threshS) & (imageS < 0.95) 

imageV = imageHSV[:,:,2]
threshV = 0.5
binaryV = imageV > threshV


fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(8, 2.5))
ax = axes.ravel()
ax[0] = plt.subplot(4, 3, 1)
ax[1] = plt.subplot(4, 3, 2)
ax[2] = plt.subplot(4, 3, 3, sharex=ax[0], sharey=ax[0])

ax[0].imshow(imageH)
ax[0].set_title('Original')
ax[0].axis('off')

ax[1].hist(imageH.ravel(), bins=256)
ax[1].set_title('Histogram')
ax[1].axvline(threshH, color='r')

ax[2].imshow(binaryH)
ax[2].set_title('Thresholded')
ax[2].axis('off')

ax[3] = plt.subplot(4, 3, 4)
ax[4] = plt.subplot(4, 3, 5)
ax[5] = plt.subplot(4, 3, 6, sharex=ax[3], sharey=ax[3])

ax[3].imshow(imageS)
ax[3].set_title('Original')
ax[3].axis('off')

ax[4].hist(imageS.ravel(), bins=256)
ax[4].set_title('Histogram')
ax[4].axvline(threshS, color='r')

ax[5].imshow(binaryS)
ax[5].set_title('Thresholded')
ax[5].axis('off')

ax[6] = plt.subplot(4, 3, 7)
ax[7] = plt.subplot(4, 3, 8)
ax[8] = plt.subplot(4, 3, 9, sharex=ax[6], sharey=ax[6])

ax[6].imshow(imageV)
ax[6].set_title('Original')
ax[6].axis('off')

ax[7].hist(imageV.ravel(), bins=256)
ax[7].set_title('Histogram')
ax[7].axvline(threshV, color='r')

ax[8].imshow(binaryV)
ax[8].set_title('Thresholded')
ax[8].axis('off')

ax[9] = plt.subplot(4, 3, 10)
ax[10] = plt.subplot(4, 3, 11)
ax[11] = plt.subplot(4, 3, 12, sharex=ax[6], sharey=ax[6])

ax[9].imshow(imageRGB)
ax[9].set_title('Original')
ax[9].axis('off')

binary = binaryH & binaryS & binaryV
ax[11].imshow(binary)
ax[11].set_title('Thresholded')
ax[11].axis('off')


plt.show()