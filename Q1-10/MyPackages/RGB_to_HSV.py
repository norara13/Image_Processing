# RGB値の画像をHSVに変換するプログラム
import numpy as np

def RGB_to_HSV(img):
    img = img.astype(np.float32) / 255
    out = np.zeros_like(img)

    R = img[:, :, 2].copy()
    G = img[:, :, 1].copy()
    B = img[:, :, 0].copy()

    # RGBのmax値とmin値を求める
    rgb_max = np.max(img, axis=2).copy()
    rgb_min = np.min(img, axis=2).copy()
    rgb_arg = np.argmax(img, axis=2)

    # Vを求める
    V = rgb_max.copy()

    # Sを求める
    S = rgb_max.copy() - rgb_min.copy()

    # Hを求める
    H = np.zeros_like(rgb_max)
    # これで通る理由わからん
    H[np.where(rgb_max == rgb_min)] = 0
    i = np.where(rgb_arg == 0)
    H[i] = 60 * (G[i] - R[i]) / (rgb_max - rgb_min) + 60
    i = np.where(rgb_arg == 1)
    H[i] = 60 * (R[i] - B[i]) / (rgb_max - rgb_min) + 300
    i = np.where(rgb_arg == 2)
    H[i] = 60 * (B[i] - G[i]) / (rgb_max - rgb_min) + 180

    return H, S, V
