# 画像を読み込み、RGBをBGRの順に入れ替える
from MyPackages.RGB_Load import RGB_Load
import cv2

img = cv2.imread("source/imori.jpg")
R, G, B = RGB_Load(img)

img[:, :, 2] = B
img[:, :, 1] = G
img[:, :, 0] = R

cv2.imwrite("answer/answer_Q1.jpg", img)

