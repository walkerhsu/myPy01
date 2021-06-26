import cv2
from matplotlib import pyplot as plt

img = cv2.imread('data/dog.jpeg') #BGR
img = img[:,:,::-1] #RGB

plt.imshow(img)
plt.show()