Pythonでのクラス作成
====

Pythonはオブジェクト指向型言語ですので，クラス作成することが可能です．

まずは，以下の簡単な例を見てみましょう．

``` Python

## パラメータクラスの作成
class Parameter:
    ## name, valでクラス変数データを初期化
    def __init__(self, name, val):
        self.name = name
        self.val = val

if __name__ == '__main__':
    # クラスインスタンスの作成
    param1 = Parameter("param1", 1.0)

    print("name:", param1.name, ", value:", param1.val)

    # 値の変更が可能
    param1.val = 2.0
    print("name:", param1.name, ", value:", param1.val)
```

まず，クラスの宣言方法ですが，```class [クラス名]:```となります．

次に，```def __init__(self, name, val):```ですが，
これはクラスを初期化する関数（コンストラクタ）です．
関数の中身を見ると，それぞれ```self.name = name```のようにselfがついた変数に代入されています．
これによって，コンストラクタの入力パラメータをクラス変数に設定しています．

main部分を見ると，```param1 = Parameter("param1", 1.0)```でクラスインスタンスが作成され，
それぞれの変数名で```param1.val```のように値にアクセスできることが分かります．

その後の例のように，値の変更も可能です．
最終的な出力は，以下のようになります．

``` bash
name: param1 , value: 1.0
name: param1 , value: 2.0
```

さて，ここでパラメータって値は変えるけど名前は変えないよなぁと思ったとします．
そこで，名前は初期化時に一度だけ設定し，値は外から変更するケースを考えてみます．

``` Python
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
```

先ほどのコードとほとんど同じですが，クラス変数にアンダースコアがついています．
これは，外からはこの変数にアクセスできないということを表します．

外からアクセスする方法として，このクラスではname, value, setValueの関数を使用しています．
setNameという関数がなくなりましたので，このクラスの```self._name```は，初期化時に一度だけ設定されるという具合になります．

このままだとあまり意味がないですが，valに関してもアンダースコアをつけて外からアクセスできないようにしています．
例えば，setValue関数で入力パラメータの値域をチェックするような機構を後から追加でき，安全にvalを変更することができます．

さて，それではもう少し具体的に，HTMLを出力するクラスを作成して遊んでみましょう．

``` Python
# HTML出力クラス
class HTML:
    def __init__(self):
        self._html = ""

    def html(self):
        return self._html

    def link(self, url, code, **kargs):
        kargs["href"] = url
        self.tag("a", code, **kargs)

    def tag(self, tag_name, code, **kargs):
        self._html += '<%s' % tag_name

        for attr_name, attr in kargs.items():
            self._html += ' %s="%s"' % (attr_name, attr)

        self._html += '> %s </%s>\n' % (code, tag_name)

if __name__ == '__main__':
    html = HTML()
    html.tag("h1", "HTML出力クラス")
    html.tag("p", "このクラスは，HTMLを出力するためのPythonクラスです．")
    html.tag("p", "**kargsは，HTMLタグのアトリビュートを設定するのに使えます．", align="center")
    link_code = HTML()
    link_code.link("https://github.com/tody411/PyIntroduction", "CGソフトウェア開発のためのPython入門")
    html.tag("p", link_code.html() + "のように，よく使うタグを関数化したり，部品のように組み合わせることができます．")
    print (html.html())
```

上のサンプルプログラムの出力は，以下のようになります．

``` html
<h1> HTML出力クラス </h1>
<p> このクラスは，HTMLを出力するためのPythonクラスです． </p>
<p align="center"> **kargsは，HTMLタグのアトリビュートを設定するのに使えます． </p>
<p> <a href="https://github.com/tody411/PyIntroduction"> CGソフトウェア開発のためのPython入門 </a>
のように，よく使うタグを関数化したり，部品のように組み合わせることができます． </p>
```

クラス構造が少し複雑になっていますが，基本は，```self._html```の内容をtag関数で更新しているだけです．
tag関数が自動で，```<tag_name>code</tag_name>```の出力を生成しています．

**kargsは，見慣れないかもしれませんが，```align="center"```のように，
本来tag関数の引数として設定されていない追加引数が入ります．
**kargsを参照しつつ，htmlタグと同じ方式でアトリビュート文字列を生成しているので，
htmlタグと同様の感覚でtag関数を使うことができます．

また，HTMLリンクのように，タグの方式が少し分かりづらいものは，関数化しておくと分かりやすくなります．
その際に，```kargs["href"] = url```の形で，追加引数を設定してtag関数に投げると，
aタグでhrefのアトリビュートをurlに設定したのと同じ意味合いになります．

このようなクラスを一つ作って関数を充実させておくと，
研究で解析した結果を自動的にまとめてWebページを作成するような場合に非常に便利です．