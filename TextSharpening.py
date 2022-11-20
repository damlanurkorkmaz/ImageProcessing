import cv2
import numpy as np

imagedata_original = cv2.imread('hw.jpg')

cv2.imshow('Original Image', imagedata_original)
cv2.waitKey(0)

sharpening_filter = np.array([[-1,-1,-1],
                              [-1,9,-1],
                              [-1,-1,-1]])

sharpened_image = cv2.filter2D(imagedata_original, -1, sharpening_filter)

cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()