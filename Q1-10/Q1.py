# 画像を読み込み、RGBをBGRの順に入れ替える
import cv2

img = cv2.imread('source/imori.jpg')

R = img[:, :, 2].copy()
G = img[:, :, 1].copy()
B = img[:, :, 0].copy()

img[:, :, 2] = B
img[:, :, 1] = G
img[:, :, 0] = R

cv2.imwrite('answer/answer_Q1.jpg', img)
