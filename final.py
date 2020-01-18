import cv2
import numpy as np

img = cv2.imread('testing123.png',0)
thresh = cv.adaptiveThreshold(img.copy(), 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

