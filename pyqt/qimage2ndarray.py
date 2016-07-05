# -*- coding: utf-8 -*-
## @package qimage2ndarray
#
#  QImage <-> NumPy行列
#  @author      tody
#  @date        2016/07/01


from PyQt4.QtCore import *
from PyQt4.QtGui import *

import numpy as np

# uint8 型への変換．
def to8U(img):
    if img.dtype == np.uint8:
        return img
    return np.clip(np.uint8(255.0 * img), 0, 255)

# float32 型への変換．
def to32F(img):
    if img.dtype == np.float32:
        return img
    return (1.0 / 255.0) * np.float32(img)

# Gray -> RGB.
def gray2rgb(gray):
    h, w = gray.shape[:2]
    img_rgb = np.zeros((h, w, 3))
    for ci in range(3):
        img_rgb[:, :, ci] = gray
    return img_rgb

# NumPy -> QImage.
def numpy2QImage(img):
    C_8U = to8U(img)

    if len(C_8U.shape) == 2:
        C_8U = gray2rgb(C_8U)

    if C_8U.shape[2] == 2:
        C_8U = rg2rgb(C_8U)

    if C_8U.shape[2] == 3:
        return rgb2Qrgb(C_8U)

    if C_8U.shape[2] == 4:
        return rgba2Qargb(C_8U)

    return QImage()

# NumPy -> QPixmap.
def numpy2QPixmap(img):
    qimg = numpy2QImage(img)
    return  QPixmap.fromImage(qimg)

# QImage -> NumPy.
def QImage2Numpy(qimage):
    qimage = qimage.rgbSwapped()
    buf = qimage.bits().asstring(qimage.numBytes())
    result = np.frombuffer(buf, np.uint8)

    w = qimage.width()
    h = qimage.height()
    ch = result.shape[0] / (w * h)

    result = result.reshape((h, w, ch))

    return result


def rg2rgb(C_8U):
    h, w, cs = C_8U.shape
    rgb_8U = np.zeros((h, w, 3))

    for ci in range(3):
        rgb_8U[:, :, ci] = C_8U[:, :, ci]
    return rgb_8U


def rgb2Qrgb(C_8U):
    return QImage(C_8U.data, C_8U.shape[1], C_8U.shape[0], QImage.Format_RGB888)


def rgba2Qargb(C_8U):
    return QImage(C_8U.data, C_8U.shape[1], C_8U.shape[0], QImage.Format_ARGB32).rgbSwapped()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    import matplotlib.pyplot as plt
    qimage = QImage("../opencv/pycv_tutorial/images/peppers.png")

    image = QImage2Numpy(qimage)

    plt.imshow(image)
    plt.show()
    sys.exit(app.exec_())
