入出力とGUI: 画像の表示
====

OpenCVでは，画像読み込み用の関数と画像表示用の関数を標準で利用することができます．
また，MATLABに似たグラフ描画機能を持っているmatplotlibを使うことで，
画像をタイトル付きで並べて配置する等，OpenCV単体だと少し難しい表示方法も可能になります．

以下のサンプルコードでは，
カラー画像，グレースケール画像を
OpenCV, matplotlibでそれぞれ表示する最小コードになります．

``` Python
from matplotlib import pyplot as plt
import cv2
import numpy as np

# OpenCVによるカラー画像表示
def cvShowImageColor(image_file):
    image_bgr = cv2.imread(image_file)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', image_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# OpenCVによるグレースケール画像の表示
def cvShowImageGray(image_file):
    image_gray = cv2.imread(image_file, 0)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', image_gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Matplotによるカラー画像表示
def pltShowImageColor(image_file):
    image_bgr = cv2.imread(image_file)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    plt.title('image')
    plt.imshow(image_rgb)
    plt.axis('off')
    plt.show()

# Matplotによるカラー画像表示
def pltShowImageGray(image_file):
    image_gray = cv2.imread(image_file, 0)

    plt.title('image')
    plt.gray()
    plt.imshow(image_gray)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    image_file = 'images/lena.jpg'
    cvShowImageColor(image_file)
    cvShowImageGray(image_file)

    pltShowImageColor(image_file)
    pltShowImageGray(image_file)
```