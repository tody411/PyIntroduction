MayaでのPython開発
====

3DCGソフトウェアのMayaでは，Pythonスクリプトによるコマンド実行処理・プラグイン開発をサポートしています．
Mayaが使っているPythonのバージョンは2.x系で古く，公式に配布されている物とも違っているので少し注意が必要です．

| Mayaのバージョン  | Pythonのバージョン     |
|:-----------|:----------------------|
| Maya2016 | Python2.7 |
| Maya2015 | Python2.7 |
| Maya2014 | Python2.7 |
| Maya2013 | Python2.6 |

開発に関しては，
エディタはEclipseを使いますが，コードの実行は基本Mayaのスクリプトウィンドウから行います．

## PythonコマンドMayaのPython開発環境

[公式ヘルプ](http://help.autodesk.com/view/MAYAUL/2016/JPN/)->テクニカルドキュメント->Pythonコマンドに情報がまとまっています．
各コマンドにはサンプルプログラムがついているので，それを実行してみるといいです．

例: polySphereコマンド．

``` Python
import maya.cmds as cmds

# X方向に40分割，Y方向に40分割，半径2の球を作成．
cmds.polySphere(sx=40, sy=40, r=2)

# X軸方向に2移動．
cmds.move(2.0, 0.0, 0.0)

```

半径20の球が生成され，X軸方向に2移動されます．

## PyMEL

MayaのPythonコマンドは，基本MELコマンドの構文を置換しただけなので，あまりPythonフレンドリーにできていません．
そこで登場したのがPyMELで，Pythonコマンドよりも直感的にオブジェクト指向でMayaのSceneデータにアクセスできます．

``` Python
import pymel.core as pm

# X方向に40分割，Y方向に40分割，半径2の球を作成．
sphere = pm.polySphere(n='pymelSphere', r=2)

# X軸方向に2移動．
sphere.setTranslation([2.0, 0.0, 0.0])
```

処理自体は，Pythonコマンドでも紹介した編集とほぼ同じですが，
オブジェクト指向を取り入れることで球に対し，直接移動量を設定することが可能です．

参考サイト:

* [PyMEL公式リファレンス(英語)](http://help.autodesk.com/cloudhelp/2016/ENU/Maya-Tech-Docs/PyMel/)
* [デジタル・フロンティア: 優しいpymel氏　– スクリプト入門者のあなたへ 2-](http://www.dfx.co.jp/dftalk/?p=3357)

## Python API

C++と同様に，Pythonスクリプトでプラグインを作成することができます．
Python, PyMELよりも高速に動作しますが，コードの記述は少し複雑になります．

参考サイト:

* [はじめてPythonで書くMayaデフォーマ](http://www.dfx.co.jp/dftalk/?p=10981)