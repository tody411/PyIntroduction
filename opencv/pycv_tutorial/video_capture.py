# -*- coding: utf-8 -*-
## @package pycv_tutorial.video_capture
#
#  入出力とGUI: Webカメラのキャプチャと表示
#  @author      tody
#  @date        2016/06/25

import cv2
import matplotlib.animation as animation
import matplotlib.pyplot as plt

# OpenCVによるWebカメラのキャプチャと表示
def cvCaptureVideo():
    capture = cv2.VideoCapture(0)

    if capture.isOpened() is False:
        raise("IO Error")

    cv2.namedWindow("Capture", cv2.WINDOW_NORMAL)

    while True:
        ret, image = capture.read()

        if ret == False:
            continue

        cv2.imshow("Capture", image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


# MatplotによるWebカメラのキャプチャと表示
def pltCaputreVideo():
    capture = cv2.VideoCapture(0)

    if capture.isOpened() is False:
        raise("IO Error")

    def updateFrame(num, capture, image_plt):
        ret, image_bgr = capture.read()
        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
        if ret == False:
            return image_plt,
        image_plt.set_array(image_rgb)
        return image_plt,

    ret, image_bgr = capture.read()
    if ret == False:
        capture.release()
        return

    fig = plt.figure()
    plt.title('Capture')
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    image_plt = plt.imshow(image_rgb, animated=True)
    plt.axis('off')
    ani = animation.FuncAnimation(fig, updateFrame, fargs=(capture, image_plt),
                                   interval=0, blit=True)
    plt.show()
    capture.release()

if __name__ == "__main__":
    cvCaptureVideo()
    pltCaputreVideo()
