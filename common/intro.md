Pythonの基本的な構文
====

簡単ではありますが，Pythonの基本的な構文をまとめます．

## 変数・データ型の基本

### 数値
みなさんが馴染みのある他の言語と特に変わらないかと思います．

``` Python
num1 = 10
num2 = 20
num3 = num1 + num2
print(num3)   # 30が出力されます．
```

### 文字列
文字列についても足し算で簡単に連結可能です．

``` Python
str1 = "Hello"
str2 = "Python"
str3 = str1 + str2
print(str3)   # HelloPythonが出力されます．
```

### リスト
リストも簡単に作れます．

``` Python
num_list = [1, 2, 3, 4]
num_list.append(5)
print(num_list)    # [1, 2, 3, 4, 5]になります．
```

### 辞書
他のプログラミング言語では，ハッシュやマップと呼ばれたりするデータ構造です．

``` Python
age_dict = {"yamada": 25, "suzuki": 30, "takahashi": 28}

print(age_dict) # 辞書の内容を出力
print(age_dict["suzuki"]) # 30が出力
age_dict["suzuki"] = 26
print(age_dict["suzuki"]) # 26が出力
```

出力は，

``` Python
{'takahashi': 28, 'yamada': 25, 'suzuki': 30}
30
26
```
のようになります．
ここで，出力内容を見てみると，```age_dict```に指定したデータの順番が入れ替わっていることに気づきます．
辞書には，キーと値のペアを作るのが重要でその順番は特に保存されないので注意が必要です．

## 関数

Pythonの関数宣言は，以下のようになります．

``` Python
def func1(param1, param2):
    print(param1 + param2)

func1(10, 20)   # 30が出力されます．
```

Pythonでは，他の言語でよく使われるブロック({}で囲まれた領域)の代わりに，
インデントで関数の中身かそうでないかを区別しています．

特に何も指定しなければ，PyDevはインデントをスペース4つ分とみなして，
関数宣言時や関数内部のエディット時に自動的にインデントを挿入します．

## クラス

Pythonでも，C++やJavaのようにクラスを定義することができます．

``` Python
# Sumクラスの実装
class Sum:
    # 初期化処理
    def __init__(self, num1, num2):
        self._num1 = num1
        self._num2 = num2

    def printSum(self):
        print(self._num1 + self._num2)


# インスタンスの作成
sum_instance = Sum(10, 20)

# printSum関数の実行
sum_instance.printSum()  # 30が出力されます．
```

実装したSumクラスは，初期化時に```num1, num2```の数値を受け取りメンバ変数に登録，
printSumメソッドでメンバ変数を足した内容を出力するという簡単な物です．

メンバ変数の定義の仕方やメソッド内でどのように呼び出すかを確認しておきましょう．

## forによる繰り返し文

Pythonでは，for文をかなり直感的に書くことができます．

``` Python
odd_list = [1, 3, 5, 7]

for num in odd_list:
    print(num)
```

```num```には，```odd_list```の要素が順に代入されてループが回ります．
出力結果も当然以下のような形になります．

``` Python
1
3
5
7
```

一般的に，ある範囲の```i```についてループを回したい場合，
range関数を使って以下のように書くことができます．

``` Python
for i in range(10):  # 0, 1, ..., 9の要素のループ
    print(i)
```

* range(a, b): [a, a + 1, ..., b-1]
* range(a, b, 2): [a, a + 2, ..., b-1]

のように，range関数を調整すると色々なループを回せますので，
少し調べておきましょう．

if文やwhile文は他のプログラミング言語ともよく似ているので本サイトでは割愛します．