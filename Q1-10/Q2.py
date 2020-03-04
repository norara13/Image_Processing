# グレースケール化
import cv2
import numpy as np

img = cv2.imread("source/imori.jpg")

b = img[:, :, 0]
g = img[:, :, 1] 
r = img[:, :, 2]

gray = np.array(0.2126*r + 0.7152*g + 0.0722*b, dtype='uint8')

cv2.imwrite("answer/answer_Q2.jpg", gray)
