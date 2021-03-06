
CGソフトウェア開発のためのPython入門
====

プログラミング言語Python（パイソン）によるCGソフトウェア開発を具体的な事例から学習するためのサイト．
私自身，CG関連のプログラムを組むのにPythonを多く利用していますが，
初心者にも比較的わかりやすいプログラミング言語だと思います．

Pythonの強みは，ライブラリの豊富さです．
中でも数値計算ライブラリ**NumPy**, **Scipy**は非常に便利で
グラフ描画ライブラリ**matplotlib**と組み合わせるとMATLABのような数値計算・グラフ描画を行うことができます．

また，CG関連の技術で言うと，
3DCGや画像処理で用いられる**OpenGL**や**OpenCV**も比較的簡単に扱うことができます．
GUIもC++で広く利用されているQtのPython版PyQtを使うと高機能なソフトウェアも開発できます．

Blender, Mayaに代表される3DCGソフトウェアでは，Pythonによるスクリプト処理をサポートしています．
Pythonの基本構文やライブラリを学習しておくと，独自のスクリプトを開発する際にも役立ちます．

これを機にPythonを色々触ってみてもらえると嬉しいです．

## コンテンツ

筆者の開発環境からWindows10 64bit, Python3.5で検証を行っています．
基本的にはクロスプラットフォームなのでコードもそれなりに動くとは思いますが，
特に検証は行っておりませんのでご了承ください．

* [インストール](install/install.md)
* [Pythonの基本的な構文](common/intro.md)
* [Pythonでのクラス作成](common/class.md)
* [Pythonの標準ライブラリの利用](common/lib.md)
* [良く使うPythonライブラリ](lib/lib.md)
* [PythonからのOpenCV利用](opencv/opencv.md)
* [PyQtによるGUI開発](pyqt/pyqt.md)
* [MayaでのPython開発](maya/mayapy.md)
* [FBX, PyQtによる3Dプログラミング](fbx/fbx.md)

注: 不定期更新になると思いますが，なるべく早めに充実させたいと思います．

## License

The MIT License 2016 (c) tody