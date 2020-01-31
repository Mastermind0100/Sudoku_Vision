import cv2
import numpy as np
import operator

kernel = np.ones((1,1), np.uint8) 

img = cv2.imread('test.jpeg')
img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img2gray.copy(),(9,9),0)
th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)

cnts,_ = cv2.findContours(th3,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
c = max(cnts, key = cv2.contourArea)

bottom_right, _ = max(enumerate([pt[0][0] + pt[0][1] for pt in c]), key=operator.itemgetter(1))
top_left, _ = min(enumerate([pt[0][0] + pt[0][1] for pt in c]), key=operator.itemgetter(1))
bottom_left, _ = min(enumerate([pt[0][0] - pt[0][1] for pt in c]), key=operator.itemgetter(1))
top_right, _ = max(enumerate([pt[0][0] - pt[0][1] for pt in c]), key=operator.itemgetter(1))

bottom_left = c[bottom_left][0]
bottom_right = c[bottom_right][0]
top_left = c[top_left][0]
top_right = c[top_right][0]

d1 = ((top_left[0]-top_right[0])**2 + (top_left[1]-top_right[1])**2)**(0.5)
d2 = ((top_left[0]-bottom_left[0])**2 + (top_left[1]-bottom_left[1])**2)**(0.5)
d3 = ((bottom_left[0]-bottom_right[0])**2 + (bottom_left[1]-bottom_right[1])**2)**(0.5)
d4 = ((bottom_right[0]-top_right[0])**2 + (bottom_right[1]-top_right[1])**2)**(0.5)

side = max([d1,d2,d3,d4])
src = np.array([top_left, top_right, bottom_right, bottom_left], dtype='float32')
dst = np.array([[0, 0], [side - 1, 0], [side - 1, side - 1], [0, side - 1]], dtype='float32')
m = cv2.getPerspectiveTransform(src, dst)
finimg = cv2.warpPerspective(img, m, (int(side), int(side)))

newimg = cv2.drawContours(img.copy(),c,-1,(0,255,0),2)

cv2.imshow('contours', finimg)

cv2.waitKey()
cv2.destroyAllWindows()
