# 大津の2値化を行うプログラム
import numpy as np

def otu(gray):
    # 未実装
    for i in range(255):
        v0 = gray[np.where(gray < i)]
        v1 = gray[np.where(gray >= i)]