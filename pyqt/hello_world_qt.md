PyQtのHello World
====

## 空のWindow作成

まず，PyQtでGUI開発を行うにあたって一番簡単なひな形のコードを見てみましょう．

``` Python
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


def main():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400, 400)
    w.setWindowTitle('PyQt Hello World')
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```

まず，PyQtのimport文ですが，

``` Python
from PyQt4.QtCore import *
from PyQt4.QtGui import *
```

の2文を使ってPyQtの機能を呼び出しています．
今回の例では，QtGuiの機能しか必要ありませんが，
QtCoreの機能もよく使われるので一緒に載せています．

import文を細かく制御したい人は，
実行してどちらかを省けるか確認したり，

``` Python
from PyQt4.QtGui import QApplication, QWidget
```

のように明示的なimport文を書いてみましょう．
Eclipseを使っている人は，import文を消すと
QApplication, QWidgetに赤の下線がひかれるようになるので，
該当箇所にカーソルを持っていき，```Ctrl + Space```でコード補完機能を呼び出すと，
自動的にimport文が挿入されます．

冒頭の```app = QApplication(sys.argv)```では，コマンドラインの引数(```sys.argv```)を入力にして
Qtのアプリケーションを作成しています．
アプリケーションとして，```w = QWidget()```の空のWindowを作成し，
サイズを変えて，名前を付けて，表示しています．

```app.exec_()```の実行により，アプリケーションを実行し，
最後に```sys.exit(app.exec_())```とすることで，終了ステータスをシステムに伝えています．

## ボタンの配置

空のWindowだけだと味気ないので，
Widgetにボタンを追加してみます．

``` Python
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


def main():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400, 400)
    w.setWindowTitle('PyQt Hello World')

    # ボタンの追加
    layout = QVBoxLayout()
    layout.addWidget(QPushButton("Button 1"))
    layout.addWidget(QPushButton("Button 2"))
    layout.addWidget(QPushButton("Button 3"))
    w.setLayout(layout)

    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```

ここで，新たにQVBoxLayoutというのが出てきました．
これは，Windowの中でButtonをどのように配置するかを決める
レイアウトクラスです．
QVBoxLayoutの場合，作成されたボタンは上から順に並びます．

## ボタンを押した時の処理

ボタンを押した時の処理を実装してみましょう．

``` Python
...
def pushSlot(button_name):
    def func():
        print("%s is pushed." % button_name)
    return func

def mainPushButtons():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400, 400)
    w.setWindowTitle('PyQt Buttons')

    # ボタンの追加
    layout = QVBoxLayout()
    button1 = QPushButton("Button 1")
    button1.clicked.connect(pushSlot("Button 1"))
    layout.addWidget(button1)
    layout.addWidget(QPushButton("Button 2"))
    layout.addWidget(QPushButton("Button 3"))
    w.setLayout(layout)
    ...
```

ここでは，button1が押された時の処理を```button1.clicked.connect(pushSlot("Button 1"))```で指定しています．
この機構をシグナルとスロットと呼びます．

基本的な構文は，```signal.connect(slotFunc)```のように，
関数をシグナルに結びつけます．
ここでは，```pushSlot("Button 1")```で返される```func```関数をスロットとして使用しています．

他の言語に比べると，関数をオブジェクトとして扱えるような言語体系になっていますので，
このように，PyQtではボタンを押した時の処理を非常に簡単に記述することができます．