
# -*- coding: utf-8 -*-
## @package pycv_tutorial.color_space
#
#  画像処理: 色空間の変換
#  @author      tody
#  @date        2016/06/27

import cv2
import matplotlib.pyplot as plt

# RGB画像の表示
def showImageRGB(image_file):
    image_bgr = cv2.imread(image_file)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    plt.title('RGB')
    plt.imshow(image_rgb)
    plt.axis('off')
    plt.show()


# グレースケール画像の表示
def showImageGray(image_file):
    image_gray = cv2.imread(image_file, 0)
    plt.title('Gray')
    plt.gray()
    plt.imshow(image_gray)
    plt.axis('off')
    plt.show()


# HSVチャンネルの表示
def showImageHSV(image_file):
    image_bgr = cv2.imread(image_file)
    image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)

    H = image_hsv[:, :, 0]
    S = image_hsv[:, :, 1]
    V = image_hsv[:, :, 2]

    plt.subplot(1, 3, 1)
    plt.title('Hue')
    plt.gray()
    plt.imshow(H)
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title('Saturation')
    plt.gray()
    plt.imshow(S)
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title('Value')
    plt.gray()
    plt.imshow(V)
    plt.axis('off')

    plt.show()


# Labチャンネルの表示
def showImageLab(image_file):
    image_bgr = cv2.imread(image_file)
    image_Lab = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2LAB)

    L = image_Lab[:, :, 0]
    a = image_Lab[:, :, 1]
    b = image_Lab[:, :, 2]

    plt.subplot(1, 3, 1)
    plt.title('L')
    plt.gray()
    plt.imshow(L)
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title('a')
    plt.gray()
    plt.imshow(a)
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title('b')
    plt.gray()
    plt.imshow(b)
    plt.axis('off')

    plt.show()


if __name__ == '__main__':
    image_file = "images/peppers.png"
    showImageRGB(image_file)
    showImageGray(image_file)
    showImageHSV(image_file)
    showImageLab(image_file)