PythonからのOpenCV利用
====

画像処理で一般的に使われているライブラリ OpenCVをPythonからも利用することができます．

## OpenCVのインストール

スタートメニュー->Anaconda3->Anaconda Promptを起動し，
以下のコマンドを実行します．

``` bash
conda install -c https://conda.binstar.org/menpo opencv3
```

condaはAnacondaのパッケージ管理用のコマンドで，
デフォルトで入っていないライブラリをインストールしたい時に使います．

途中で"Proceed?"と聞かれますが，yを入力してエンターキーを押せば問題なく進めます．
特に問題が起こらなければ，しばらくするとOpenCVのインストール処理が完了します．

### インストールされたOpenCVのバージョンのチェック

Pythonインタプリターを起動し，以下のコマンドを実行します．

``` Python
>>> import cv2
>>> cv2.__version__
'3.1.0'
>>> exit()
```

OpenCV 3.1.0がインストールされていることが分かります．（2016/6/25）

## OpenCVの開発に向けて

[公式チュートリアル(英語)](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)
は，英語で書かれていますが割と情報はまとまっています．

Python版の日本語チュートリアルはあまりまとまったものがなく，
C++版であれば[OpenCV.jp : OpenCV逆引きリファレンス](http://opencv.jp/cookbook/)が非常に参考になります．

Python版も，基本C++版と関数の機能自体は同じですが，
入力する引数の型が違っていたり，返り値を指定する場所も違っていたりします．

まずは，公式チュートリアルでPython版のOpenCVの基本に慣れ，
C++版のサンプルをPythonに移植してみるというのが理解への近道です．

とはいってもコードの変換にはそれなりの時間がかかるので，
本サイトではある程度Python単体でOpenCVを扱えるように解説を捕捉します．

## チュートリアル

[```pycv_tutorial```](pycv_tutorial)に各サンプルコードを配置．

* 入出力とGUI
    - [画像の表示](pycv_tutorial/display_image.md)
    - [Webカメラのキャプチャと表示](pycv_tutorial/video_capture.md)
    - [OpenCVの描画](pycv_tutorial/drawing.md)