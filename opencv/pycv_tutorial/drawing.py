# -*- coding: utf-8 -*-
## @package pycv_tutorial.drawing
#
#  入出力とGUI: OpenCVの描画
#  @author      tody
#  @date        2016/06/26

import cv2
import numpy as np


# 描画用の空画像の作成
def emptyImage():
    img = np.zeros((512, 512, 3), np.uint8)
    return img

# 直線の描画
def drawLine(img, pt1, pt2, color, width):
    print(dir(cv2))
    img = cv2.line(img, pt1, pt2, color, width, cv2.LINE_AA)

# 円の描画
def drawCircle(img, center, radius, color, width):
    img = cv2.circle(img, center, radius, color, width, cv2.LINE_AA)

# 楕円の描画
def drawElipse(img, center, axes, angle, startAngle, endAngle, color, width):
    img = cv2.ellipse(img, center, axes, angle, startAngle, endAngle, color, width, cv2.LINE_AA)

# 四角形の描画
def drawRectangle(img, pt1, pt2, color, width):
    img = cv2.rectangle(img, pt1, pt2, color, width, cv2.LINE_AA)

# ポリゴンの描画
def drawPolylines(img, pts, isClosed, color, width):
    img = cv2.polylines(img, pts, isClosed, color, width, cv2.LINE_AA)


font_types = [cv2.FONT_HERSHEY_SIMPLEX, cv2.FONT_HERSHEY_PLAIN, cv2.FONT_HERSHEY_COMPLEX,
              cv2.FONT_HERSHEY_COMPLEX_SMALL, cv2.FONT_HERSHEY_DUPLEX,
              cv2.FONT_HERSHEY_SCRIPT_COMPLEX, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
              cv2.FONT_HERSHEY_TRIPLEX, cv2.FONT_ITALIC]

# 文字の描画
def drawText(img, text, org, fontFace, fontScale, color, width):
    img = cv2.putText(img, text, org, fontFace, fontScale, color, width, cv2.LINE_AA)

def drawingDemo():
    img = emptyImage()

    # 太さ2の直線描画
    drawLine(img, (10, 10), (200, 200), (0, 0, 255), 2)

    # 太さに-1を指定すると，塗りつぶしになる
    drawCircle(img, (300, 100), 80, (0, 255, 0), -1)

    # 中と外を両方描画
    drawRectangle(img, (10, 210), (210, 350), (100, 100, 0), -1)
    drawRectangle(img, (10, 210), (210, 350), (255, 0, 0), 3)

    # 楕円の描画
    drawElipse(img, (450, 100), (30, 80), 0, 0, 360, (0, 100, 100), -1)

    # ポリゴンの描画
    pts = np.array([[(250, 240), (270, 280), (350, 320), (500, 300), (450, 230), (350, 210)]], dtype=np.int32)
    drawPolylines(img, pts, True, (255, 100, 100), 5)

    # テキストの描画
    drawText(img, 'OpenCV', (20, 450), font_types[0], 4, (200, 200, 200), 2)

    cv2.namedWindow('DrawingDemo', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('DrawingDemo', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    drawingDemo()
