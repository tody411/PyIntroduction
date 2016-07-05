シグナルとスロット
====

PyQtのGUI開発の入り口となるのが，Qtのシグナルとスロットです．
Qtで開発する場合，初心者の方がつまづくのはここが大体多いかと思います．
関数をあまりオブジェクトとして扱わないC++から入ると慣れが必要な機構ですが，
Pythonの場合は元々言語として関数をオブジェクトとして扱いますし，
概念さえ理解すれば使うこと自体は簡単です．

Parameterクラスを例にとってみましょう．

``` Python
class Parameter(QObject):
    valueChanged = pyqtSignal(object)

    def __init__(self):
        super(Parameter, self).__init__()

    def setValue(self, val):
        self._val = val
        self.valueChanged.emit(val)

def printParameter(val):
    print("Value Changed: %d" % val)

parameter = Parameter()
parameter.valueChanged.connect(printParameter)

parameter.setValue(10)
parameter.setValue(20)
```

まず，```valueChanged = pyqtSignal(object)```で定義されているのが
PyQtのシグナルです．```setValue```関数内で```self.valueChanged.emit(val)```を呼ぶことにより，
パラメータの値が```val```に変更されたということをクラス外部に通知しています．

実際にシグナルを利用する時は，```def printParameter(val):```のように，通知された値を受け取る関数を定義します．
この関数をスロットと呼び，シグナルの```connect```関数を使ってシグナルとスロットを結びつけることができます．

上の例では，まず，Parameterクラスのインスタンスを作り，```parameter.valueChanged.connect(printParameter)```を呼び出すことにより，
パラメータが変更された時に行う処理を```printParameter```として割り当てています．

このプログラムの出力結果は以下のようになります．

``` Python
Value Changed: 10
Value Changed: 20
```

もし，```parameter.valueChanged.connect(printParameter)```をコメントアウトすると，
出力はしなくなりますし，もっと他の関数を定義して例えばパラメータが変わった時に画像処理を行うといったことも可能です．