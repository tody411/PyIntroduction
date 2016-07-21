# -*- coding: utf-8 -*-
## @package simple_class
#
#  クラス作成の例.
#  @author      Tody
#  @date        2016/07/21

## パラメータクラスの作成
class Parameter:
    ## name, valでクラス変数データを初期化
    def __init__(self, name, val):
        self._name = name
        self._val = val

    def name(self):
        return self._name

    def value(self):
        return self._val

    def setValue(self, val):
        self._val = val

if __name__ == '__main__':
    # クラスインスタンスの作成
    param1 = Parameter("param1", 1.0)

    print("name:", param1.name(), ", value:", param1.value())

    # 値の変更が可能
    param1.setValue(2.0)
    print("name:", param1.name(), ", value:", param1.value())
