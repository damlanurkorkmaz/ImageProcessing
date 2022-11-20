import cv2
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow


img = cv2.imread("/content/img.png")
cv2_imshow(img)

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2_imshow(gray_img)
img_gaussian = cv2.GaussianBlur(gray_img,(25,25),0)

sobelx = cv2.Sobel(img_gaussian,cv2.CV_8U,1,0,ksize=5)
sobely = cv2.Sobel(img_gaussian,cv2.CV_8U,0,1,ksize=5)
sobel_img = sobelx + sobely

cv2_imshow(sobelx)
cv2_imshow(sobely)
cv2_imshow(sobel_img)

kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])

img_prewittx = cv2.filter2D(img_gaussian, -1, kernelx)
img_prewitty = cv2.filter2D(img_gaussian, -1, kernely)
img_prewitt = img_prewitty + img_prewittx

cv2_imshow(img_prewittx)
cv2_imshow(img_prewitty)
cv2_imshow(img_prewitt)

img = cv2.imread("/imageHW/img.png",0).astype("float64")
img/=255.0

roberts_cross_v = np.array( [[1, 0 ],
                             [0,-1 ]] )
  
roberts_cross_h = np.array( [[ 0, 1 ],
                             [ -1, 0 ]] )

vertical = ndimage.convolve( img, roberts_cross_v )
horizontal = ndimage.convolve( img, roberts_cross_h )
  
edged_img = np.sqrt( np.square(horizontal) + np.square(vertical))
edged_img*=255

cv2_imshow(edged_img)

img2 = cv2.imread("/imageHW/img.png")

gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

blur = cv2.blur(gray,(3,3))
cv2_imshow(blur)

edges = cv2.Canny(blur,75,75)
cv2_imshow(edges)