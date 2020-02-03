import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image
from keras import models,layers
from keras.datasets import mnist
from keras.utils import to_categorical


arr_out = []
arr_result = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
model=load_model('fmodelwts.h5')

img = cv2.imread('testing123.png',0)
rows,cols= img.shape

divr = rows//9
divc = cols//9
r = 0
c = 0

for i in range(0,9):
    for j in range(0,9):
        roi = img[r:r+divr,c:c+divc]
        c += divc
        # cv2.imshow('wassup',roi)
        # cv2.waitKey()
        _,test_image = cv2.threshold(roi,100,255,cv2.THRESH_BINARY)
        test_image = cv2.medianBlur(test_image.copy(),3)
        test_image = cv2.resize(test_image.copy(),(64,64),interpolation = cv2.INTER_AREA)
        cv2.resize(test_image,(64,64))
        # cv2.imshow('ineed2seedis',test_image)
        # cv2.waitKey()
        test_image=(image.img_to_array(test_image))/255
        test_image=np.expand_dims(test_image, axis = 0)
        result=model.predict(test_image)  
        np.reshape(result, 36)
        high = np.amax(test_image)
        low = np.amin(test_image)
        if high != low:
            maxval = np.amax(result)
            index = np.where(result == maxval)
            arr_out.append(arr_result[index[1][0]])
    r += divr
    c = 0

for i in range(0,81):
    if arr_out[i]== 'T':
        arr_out[i] = '0'
print(arr_out)

cv2.waitKey()
cv2.destroyAllWindows()