# 与えられたグレースケール化された画像を二値画像に変換するプログラム

def Binary(gray) :
    # result = [0 if i < 128 else 1 for i in gray]
    # なんで通らないんだ？？
    t = 128
    pic = gray.copy()
    pic[gray < t] = 0
    pic[gray > t] = 255
    return pic