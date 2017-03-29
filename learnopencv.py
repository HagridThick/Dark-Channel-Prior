import cv2
import numpy as np


img = cv2.imread('test.jpg')
px = img[100, 100]
print(px)
