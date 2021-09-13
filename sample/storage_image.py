import cv2
import numpy as np

img = cv2.imread('/home/hc/Desktop/workplace/dachanh/hadoop-python/sample/assets/images.jpg')
img = np.array(img,np.uint8)
shape = img.shape

np.savetxt('/home/hc/Desktop/workplace/dachanh/hadoop-python/sample/assets/file.txt',img.reshape(img.shape[0],-1))

