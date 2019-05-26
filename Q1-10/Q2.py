# グレースケール化
from MyPackages.rgb_to_gray import rgb_to_gray
import cv2

img = cv2.imread("source/imori.jpg")

gray = rgb_to_gray(img)

cv2.imwrite("answer/answer_Q2.jpg", gray)
