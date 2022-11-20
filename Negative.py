import cv2
import matplotlib.pyplot as plt
import numpy as np 
def fotograf_negatifi(foto):
    L=np.max(foto)
    negatif_foto=L-foto
    return negatif_foto

foto = cv2.imread("./imag processing/olives.jpg",0)
negatif_foto= fotograf_negatifi(foto)
yan_yana = np.hstack((foto, negatif_foto))
print("original foto:",foto.shape)
print("negatif foto:",negatif_foto.shape)
print("yan yana:", yan_yana.shape)

plt.imshow(yan_yana,cmap="gray")
plt.show()