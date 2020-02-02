import cv2
import numpy as np

img = cv2.imread('square.png',0)
rows,cols= img.shape

divr = rows//9
divc = cols//9
r = 0
c = 0
for i in range(0,9):
    for j in range(0,9):
        roi = img[r:r+divr,c:c+divc]
        c += divc
        cv2.imshow('wassup',roi)
        cv2.waitKey()
    r += divr
    c = 0



cv2.waitKey()
cv2.destroyAllWindows()