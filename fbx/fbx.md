FBX, PyQtによる3Dプログラミング
====

3DCGで広く用いられているデータフォーマット FBXをPythonからも利用することができます．

## FBX SDK Pythonのインストール

[FBX SDK](http://usa.autodesk.com/adsk/servlet/pc/item?id=24314456&siteID=123112)のサイトから
FBX SDK 2016 Pythonをダウンロードします．

インストーラの構成はシンプルでクリックしていけば，数分でインストールが終わります．
インストールされたファイルは，
```C:\Program Files\Autodesk\FBX\FBX Python SDK\2016.1.1```のようになっていると思います．

libディレクトリに進むと，

* Python27_x64
* Python27_x86
* Python33_x64
* Python33_x86

のような形に分かれています．

現状，Python 3.3までがサポートされており，
AnacondaのPython 3.5に比べると若干サポートが遅れています．

これを動かすためには，Python2.7かPython3.3が必要になりますが，
本サイトでは，Python3系の2バージョンよりも，
Python2.7とPython3.5を使うケースの方が多いと考え，
Python2.7の物を採用します．

インストールは，64ビットマシンであれば，Python27_x64の中にあるファイルを
```[PythonPaty]/Lib/site-packages```内にコピーします．

Pythonインタプリタ上で，

``` Python
from fbx import *
```

と打って特にエラーが出なければインストール完了となります．

試しに，Python33_x64をPython3.5に入れてみましたが，
やはりエラーが出てしまってうまくいきませんでした．

``` Python
>>> from fbx import *
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: DLL load failed: 指定されたモジュールが見つかりません。
```

### 初期化と終了処理

FBXの機能を利用するためには，まずFbxManagerオブジェクトを生成するところから始めます．
FBXを扱う処理が終わったら，プログラムの最後でDestroy関数を呼び出して終了させる必要があります．

``` Python
manager = FbxManager.Create()
... FBXの処理 ...
manager.Destroy()
```

## チュートリアル

* [3Dファイルの読み込み](load_file.md)