import cv2
import numpy as np

a = np.zeros((100, 100,3))
a[:,:,0] = 255

b = np.zeros((100, 100,3))
b[:,:,1] = 255

c = np.zeros((100, 200,3)) 
c[:,:,2] = 255

img = np.vstack((c, np.hstack((a, b))))

cv2.imshow('image', img)
cv2.waitKey(0)