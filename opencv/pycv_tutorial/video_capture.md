入出力とGUI: Webカメラのキャプチャと表示
====

OpenCVを使えば，Webカメラのキャプチャも容易にできます．
以下は，OpenCVとmatplotlibによるWebカメラのキャプチャ表示のサンプルコードです．

``` Python
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
```

もし，自分のPC環境にWebカメラがつながっている場合，
上記のプログラムでWebカメラの映像がリアルタイムに表示されると思います．

まず，Webカメラキャプチャの初期化処理ですが，

``` Python
    capture = cv2.VideoCapture(0)

    if capture.isOpened() is False:
        raise("IO Error")
```

で行います．

```cv2.VideoCapture(device_id)```のように指定すると，
PCにつながっているWebカメラからキャプチャできます．
複数台カメラがつながっている場合，```device_id```の値を変えることで切り替えられます．

また，```cv2.VideoCapture(video_file)```のように指定すると，
動画ファイルを読み込むこともできます．

フレームを読み込む処理は，

``` Python
    ret, image = capture.read()
```

になります．```ret=False```の場合，
フレームの読み込みに失敗していますので，
例外処理を行う必要があります．

最後に，```capture.release()```を呼び，
Webカメラのキャプチャオブジェクトの開放を行う必要があります．

動画表示になると，matplotlibは少しフレームレートが落ちてしまうので，
OpenCV単体で処理した方がよさそうです．