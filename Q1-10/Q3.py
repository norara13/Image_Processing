# グレースケール化してから二値化
from MyPackages.Binary import Binary
from MyPackages.rgb_to_gray import rgb_to_gray
import cv2

img = cv2.imread("source/imori.jpg")

gray = rgb_to_gray(img)

bi = Binary(gray)

cv2.imwrite("answer/answer_Q3.jpg", bi)
