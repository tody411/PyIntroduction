開発で良く使うPythonライブラリ
====

かなり個人的な趣味も含まれていますが，開発で良く使うPythonライブラリをまとめます．
ある程度カテゴリも分けてまとめますので参考にしてみて下さい．

### 画像処理関連の開発をする際に良く使うライブラリ．

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

#### その他の数値計算・画像処理ライブラリ

* [scikit-learn](http://scikit-learn.org/stable/): 機械学習をお手軽に試せます．
* [scikit-image](http://scikit-image.org/): SuperPixels等，OpenCVにない関数があったりするのでこちらもたまに使います．
* [PyAMG](): 代数的マルチグリッド計算による最適化．

### Web周りの処理

あまり大したことはしていません．下記のBeautiful Soupを使うことがあるくらいです．

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): HTML構文を解析できるライブラリ．

Beautiful SoupはHTML構文を解析するのにかなり強力なライブラリです．

``` Python
html_doc = """
<html><head><title>HTMLの構文解析</title></head>
<body>
<p class="title"><b>Beautiful Soup - HTMLの構文解析</b></p>

<h1>概要</h1>
<p><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" >Beautiful Soup</a>はHTMLの構文解析可能なとても便利なPythonライブラリです．</p>
<img src="image/sample.png" alt="サンプル画像です" width=200 height=200></img>
<table>
    <tr>
        <td>長所: </td> <td> 簡単な構文でHTMLを解析できます． </td>
    </tr>
    <tr>
        <td>短所: </td> <td> 使用用途に関しては要検討というところでしょうか．．． </td>
    </tr>
</table>
"""
```

例えば，上記のようなHTML文を解析するとします．

``` Python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
```

この2行でHTMLの基本構造を解析できます．
タイトルは下記の構文でアクセスできます．

``` Python
soup.title
# <title></title>

soup.string
# HTMLの構文解析
```

画像タグについている属性についてもアクセス可能です．

``` Python
soup.img['alt']
# サンプル画像です

soup.img['width']
# 200

soup.string
# HTMLの構文解析
```

また複数の要素を持つ場合も，検索可能です．

``` Python
soup.find_all('td')
# [<td>長所: </td>, <td> 簡単な構文でHTMLを解析できます． </td>,
#  <td>短所: </td>, <td> 使用用途に関しては要検討というとこ ろでしょうか．．． </td>]
```

上手く，絡めればHTMLから様々な情報を得ることができます．
(使用用途は要件等ですが．．．)