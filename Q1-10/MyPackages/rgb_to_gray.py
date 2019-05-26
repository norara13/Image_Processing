# RGB値で表されている画像をグレースケール化する関数
import numpy as np

def rgb_to_gray(img):
    b, g, r = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    return np.array(0.2126*r + 0.7152*g + 0.0722*b, dtype='uint8')