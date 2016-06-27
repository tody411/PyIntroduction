
# -*- coding: utf-8 -*-
## @package pycv_tutorial.mouse_painting
#
#  pycv_tutorial.mouse_painting utility package.
#  @author      Hideki Todo
#  @date        2016/06/27

import cv2
import numpy as np


# OpenCVのイベントリストの出力
def printEvents():
    events = [i for i in dir(cv2) if 'EVENT' in i]
    print (events)

# OpenCVのマウスイベントを扱うためのクラス
class CVMouseEvent:
    def __init__(self, press_func=None, drag_func=None, release_func=None):
        self._press_func = press_func
        self._drag_func = drag_func
        self._release_func = release_func

        self._is_drag = False

    # Callback登録関数
    def setCallBack(self, win_name):
        cv2.setMouseCallback(win_name, self._callBack)

    def _doEvent(self, event_func, x, y):
        if event_func is not None:
            event_func(x, y)

    def _callBack(self, event, x, y, flags, param):
        # マウス左ボタンが押された時の処理
        if event == cv2.EVENT_LBUTTONDOWN:
            self._doEvent(self._press_func, x, y)
            self._is_drag = True

        # マウス左ドラッグ時の処理
        elif event == cv2.EVENT_MOUSEMOVE:
            if self._is_drag:
                self._doEvent(self._drag_func, x, y)

        # マウス左ボタンが離された時の処理
        elif event == cv2.EVENT_LBUTTONUP:
            self._doEvent(self._release_func, x, y)
            self._is_drag = False


# 描画用の空画像作成
def emptyImage():
    return np.zeros((512, 512, 3), np.uint8)


# シンプルなマウス描画のデモ
def simplePaint():
    img = emptyImage()

    colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]
    color = colors[0]

    # ドラッグ時に描画する関数の定義
    def brushPaint(x, y):
        cv2.circle(img, (x, y), 20, color, -1)

    win_name = 'PaintDemo'
    cv2.namedWindow(win_name)

    # CVMouseEventクラスによるドラッグ描画関数の登録
    mouse_event = CVMouseEvent(drag_func=brushPaint)
    mouse_event.setCallBack(win_name)

    while(1):
        cv2.imshow(win_name, img)

        key = cv2.waitKey(30) & 0xFF

        # 色切り替えの実装
        if key == ord('1'):
            color = colors[0]
        elif key == ord('2'):
            color = colors[1]
        elif key == ord('3'):
            color = colors[2]

        # 画像のリセット
        elif key == ord('r'):
            img = emptyImage()

        elif key == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    printEvents()
    simplePaint()