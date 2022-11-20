import random
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os.path

def add_noise(image):
	row , col = image.shape
	number_of_pixels = random.randint(300, 10000)
	for i in range(number_of_pixels):

		y_coord=random.randint(0, row - 1)

		x_coord=random.randint(0, col - 1)
		
		image[y_coord][x_coord] = 255
		
	number_of_pixels = random.randint(300 , 10000)
	for i in range(number_of_pixels):
	
		y_coord=random.randint(0, row - 1)
		
		x_coord=random.randint(0, col - 1)
		
		image[y_coord][x_coord] = 0
		
	return image
image = cv2.imread('C:\Users\dmlnr\imageHw\foto.png',
				cv2.IMREAD_GRAYSCALE)
cv2.imwrite('C:\Users\dmlnr\imageHw\foto.png',
			add_noise(image))

print(image)
print(image.ravel())
hist = cv2.calcHist([image],[0],None,[256],[0,256])
plt.hist(image.ravel(),256,[0,256])
plt.title('Histogram of salt and and picture')
plt.show()
