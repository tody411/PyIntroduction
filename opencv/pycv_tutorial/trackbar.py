# -*- coding: utf-8 -*-
## @package pycv_tutorial.trackbar
#
#  入出力とGUI: トラックバー
#  @author      tody
#  @date        2016/06/28


import cv2
import matplotlib.pyplot as plt


# 何もしないTrackbarのコールバック
def doNothing(x):
    pass

# OpenCVのTrackbar便利クラス
class CVTrackbar:
    def __init__(self, param_name, win_name, param_min, param_max, update_func=doNothing):
        self._update_func = update_func
        self._trackbar = cv2.createTrackbar(param_name, win_name, param_min, param_max, self._callback)
        self._param_name = param_name
        self._win_name = win_name

    # Trackbarの値を参照
    def value(self):
        return cv2.getTrackbarPos(self._param_name, self._win_name)

    # Trackbarの値を設定
    def setValue(self, value):
        cv2.setTrackbarPos(self._param_name, self._win_name, value)

    def _callback(self, x):
        self._update_func(x)

    # TrackbarのCallbackを設定
    def setCallBack(self, update_func):
        self._update_func = update_func


# OpenCVのTrackbarでCanny Edge抽出するデモ
def cvEdgeDetection(image_file):
    image_bgr = cv2.imread(image_file)
    image_Lab = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2LAB)
    L = image_Lab[:, :, 0]


    win_name = "CannyEdge"
    cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
    cv2.imshow(win_name, image_bgr)

    display_modes = ['Original', 'Gray', 'CannyEdge']
    display_mode = display_modes[2]

    low_threshold_trackbar = CVTrackbar("LowThr", win_name, 0, 200)
    low_threshold_trackbar.setValue(20)

    upper_threshold_trackbar = CVTrackbar("UpperThr", win_name, 0, 300)
    upper_threshold_trackbar.setValue(40)

    while True:
        key = cv2.waitKey(30) & 0xFF

        # 表示切り替えの実装
        if key == ord('1'):
            display_mode = display_modes[0]
            cv2.imshow(win_name, image_bgr)

        elif key == ord('2'):
            display_mode = display_modes[1]
            cv2.imshow(win_name, L)

        elif key == ord('3'):
            display_mode = display_modes[2]

        elif key == ord('q'):
            break

        # Canny Edgeのインタラクティブな描画更新
        if display_mode == display_modes[2]:
            edge = cv2.Canny(L, low_threshold_trackbar.value(), upper_threshold_trackbar.value())
            cv2.imshow(win_name, edge)

    cv2.destroyAllWindows()


# Matplot + OpenCVのTrackbarでCanny Edge抽出するデモ
def pltEdgeDetection(image_file):
    image_bgr = cv2.imread(image_file)
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    image_Lab = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2LAB)
    L = image_Lab[:, :, 0]

    win_name = "CannyEdge"

    cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

    low_threshold_trackbar = CVTrackbar("LowThr", win_name, 0, 200)
    low_threshold_trackbar.setValue(20)

    upper_threshold_trackbar = CVTrackbar("UpperThr", win_name, 0, 300)
    upper_threshold_trackbar.setValue(40)

    fig = plt.figure()
    fig.subplots_adjust(
        left=0.05, bottom=0.05, right=0.95, top=0.9, wspace=0.05, hspace=0.05)

    plt.subplot(1, 3, 1)
    plt.title('Original')
    plt.imshow(image_rgb)
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.title('Gray')
    plt.gray()
    plt.imshow(L)
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.title('CannyEdge')
    plt.gray()

    edge = cv2.Canny(L, low_threshold_trackbar.value(), upper_threshold_trackbar.value())
    edge_plt = plt.imshow(edge)
    plt.axis('off')

    # Canny Edgeのインタラクティブな描画更新
    def updateValue(x):
        edge = cv2.Canny(L, low_threshold_trackbar.value(), upper_threshold_trackbar.value())
        edge_plt.set_array(edge)
        fig.canvas.draw_idle()

    low_threshold_trackbar.setCallBack(updateValue)
    upper_threshold_trackbar.setCallBack(updateValue)

    plt.show()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    image_file = "images/peppers.png"
    cvEdgeDetection(image_file)
    pltEdgeDetection(image_file)
