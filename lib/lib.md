良く使うPythonライブラリ
====

かなり個人的な趣味も含まれていますが，開発で良く使うPythonライブラリをまとめます．
ある程度カテゴリも分けてまとめますので参考にしてみて下さい．

### 画像処理関連の開発をする際に良く使うライブラリ．
開発で良く使うPythonライブラリ
* [NumPy](http://www.numpy.org/): 数値計算ライブラリ．MATLABのような密行列演算が可能．
* [SciPy](https://www.scipy.org/): 疎行列等，NumPyより少し高機能な数値計算ライブラリ．
* [matplotlib](http://matplotlib.org/): MATLABのようなグラフプロットを提供するライブラリ．
* [OpenCV](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html): 汎用的な画像処理ライブラリ．C++，Java等様々なプログラミング言語から利用可能．
* [PyQt](https://riverbankcomputing.com/software/pyqt/intro): 高機能なGUIライブラリ．C++でも広く使われており，Pythonでも人気が高い．

Pythonの場合，**NumPy**が多くのライブラリの基本データになっています．
例えば，**OpenCV**や**matplotlib**で画像を読み込んだり，出力する場合，**NumPy**行列データをやり取りするようにライブラリが設計されています．

MATLABのような数値計算，プロットをしたい人は，**NumPy**, **SciPy**, **matplotlib**のセットを選択し，
画像処理のプロトタイプを実験する場合は，**NumPy**, **OpenCV**, **matplotlib**を使う所からスタートします．

高機能なGUIが欲しくなった時は，**PyQt**を使うとクオリティの高いアプリケーションを手軽に開発できます．

本サイトでは，主に画像処理の観点から**OpenCV**の機能に焦点を当て,**NumPy**, **matplotlib**, **PyQt**の使い方についても解説を進めていきます．

* [PythonからのOpenCV利用](../opencv/opencv.md)

#### その他の数値計算・画像処理・CG系ライブラリ

* [scikit-learn](http://scikit-learn.org/stable/): 機械学習をお手軽に試せます．
* [scikit-image](http://scikit-image.org/): SuperPixels等，OpenCVにない関数があったりするのでこちらもたまに使います．
* [PyAMG](http://pyamg.org/): 代数的マルチグリッド計算による最適化．
* [FBX Python SDK](http://usa.autodesk.com/adsk/servlet/pc/item?id=24314456&siteID=123112): PythonからFBXを扱えるようにしたもの．
    - 現状Python 2.7とPython 3.3をサポート(2016/07/03)． Anaconda 3ではPython 3.5なので2系を入れるか3.3用の環境を作る必要がある．

### CGソフトでも使われるPython

Maya, Houdini, blender, のようなCGソフトウェアでは，
Pythonが拡張用の言語として用いられることが多いです．
これらのPython開発では，CGソフト固有のPythonライブラリを使って開発していきます．

本サイトでは，Mayaで使われるPythonを例に取り，Pythonを使って開発する際の一連の流れをまとめています．

* [PythonからのOpenCV利用](../maya/mayapy.md)

### PythonでのGUI開発

以下は，名前だけの紹介の物もありますが，Pythonで良く使われているGUIライブラリです．

* [PyQt](https://riverbankcomputing.com/software/pyqt/intro): 高機能なGUIライブラリ．C++でも広く使われており，Pythonでも人気が高い．
* [kivy](https://kivy.org/#home): スマートフォン上でも動作するゲーム開発向けのGUIライブラリ．
* [wxPython](https://www.wxpython.org/)
* [PyGTK](http://www.pygtk.org/)
* [TkInker](http://docs.python.jp/2/library/tkinter.html)

個人的には，**PyQt**しか使ったことが無いですが，スマフォ上でも動作する**kivy**はかなり気になっています．
本サイトでは，**PyQt**のGUIに関して個別に解説ページを作成する予定です．

### Web周りの処理

あまり大したことはしていません．下記のBeautiful Soupを使うことがあるくらいです．

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): HTML構文を解析できるライブラリ．

## チュートリアル

* [Beautiful Soup: 簡単なHTML構文解析](beautiful_soup.md)
* [PIL: 画像のExifデータの取得](pil_exif.md)
* [zipfile: Zipファイルの処理](zip_file.md)