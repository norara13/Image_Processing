# RGBを求めて返す関数

def RGB_Load(img):
    R = img[:, :, 2].copy()
    G = img[:, :, 1].copy()
    B = img[:, :, 0].copy()
    return R, G, B
