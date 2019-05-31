# HSV変換
import cv2
from MyPackages.RGB_to_HSV import RGB_to_HSV

img = cv2.imread("source/imori.jpg")

answer = RGB_to_HSV(img)

answer[:, :, 0] += 180

cv2.imwrite("answer/answer_Q5.jpg", answer)
