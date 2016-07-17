Webブラウザーの作成
====

## PythonデフォルトのWebブラウザーコントロール

PyQtでのWebブラウザーの作成をする前に，
PythonデフォルトのWebブラウザーライブラリの機能を見てみましょう．

``` Python
import webbrowser

url = 'https://github.com/tody411/PyIntroduction'
webbrowser.open(url)

```

実行すると，デフォルトのWebブラウザーが呼び出され，指定したURLのWebページが表示されたかと思います．
既にWebブラウザーが開かれている場合は，新しいタブにWebページが表示されるようになります．
webbrowserモジュールを呼び出すことで簡単にインストールされているWebブラウザーを使ってWebページを表示することができます．

次に，表示するWebブラウザーを変更する例を見てみます．

``` Python
import webbrowser

url = 'https://github.com/tody411/PyIntroduction'
browser_exe = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'

browser_type = '"%s"' % browser_exe + ' \%s'
browser = webbrowser.get(browser_type)
browser.open(url)

```

browser_exeは開きたいWebブラウザーのexeファイルのパスです．
ここでは，Chomeブラウザーのexeファイルを指定しています．
ブラウザーのタイプ```browser_type```には，```'"exeファイルのパス" %s'```という文字列を入れればうまく動作します．
exeファイルのパス```browser_exe```から```browser_type```を生成する処理を入れてあるので
コードをそのままコピペすれば問題なく動くと思います．

## PyQt4でのWebブラウザー作成

ここでは，QtWebKitのQWebViewを使ってPyQtのWidgetにWebページを表示する例を紹介します．
以下が簡単なひな形のおk－度になります．

``` Python
def mainPyQt4Simple():
    # 必要なモジュールのimport
    from PyQt4.QtCore import QUrl
    from PyQt4.QtGui import QApplication
    from PyQt4.QtWebKit import QWebView

    url = 'https://github.com/tody411/PyIntroduction'

    app = QApplication(sys.argv)

    # QWebViewによるWebページ表示
    browser = QWebView()
    browser.load(QUrl(url))
    browser.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    mainPyQt4Simple()
```

基本的には，QWebViewで作った```browser```に対して，```browser.load(QUrl(url))```の形でWebページを読み込むだけです．
実験していただくと分かりますが，このままだとYoutubeの動画を再生することはできません．

検索したWebサイトによると，以下のようなコードを入れるとYoutubeの動画を再生できるとありましたので
実験してみました．

``` Python
def mainPyQt4Youtube():
    # 必要なモジュールのimport
    from PyQt4.QtCore import QUrl
    from PyQt4.QtGui import QApplication
    from PyQt4.QtWebKit import QWebView, QWebSettings
    from PyQt4.QtNetwork import QNetworkProxyFactory

    url = 'https://www.youtube.com/?hl=ja&gl=JP'

    app = QApplication(sys.argv)

    # Youtube動画を読み込むための設定
    QNetworkProxyFactory.setUseSystemConfiguration(True)
    QWebSettings.globalSettings().setAttribute(QWebSettings.PluginsEnabled, True)
    QWebSettings.globalSettings().setAttribute(QWebSettings.AutoLoadImages, True)
    QWebSettings.globalSettings().setAttribute(QWebSettings.LocalStorageEnabled, True)
    QWebSettings.globalSettings().setAttribute(QWebSettings.PrivateBrowsingEnabled, True)
    QWebSettings.globalSettings().setAttribute(QWebSettings.DeveloperExtrasEnabled, True)

    # QWebViewによるWebページ表示
    browser = QWebView()
    browser.load(QUrl(url))
    browser.setEnabled(True)
    browser.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    mainPyQt4Youtube()
```

新しく追加したのは，Youtube動画を読み込むための設定部分です．
著作権の問題もあるのでYoutubeのトップページのURLを指定しました．
すると，トップページの動画は再生されましたが，肝心のYoutube動画は再生されませんでした．
どうやらYoutubeの仕様がflashによる再生からHtml5による再生に変わったらしく，
QWebViewがそれに対応しきれていない模様です．
少々残念な結果となってしまいました．

## PyQt5でのWebブラウザー作成

PyQt5からは，QtWebKitではなく，WebEngineViewによってWebページを表示するようになりました．
さっそく下記のひな形のコードを試してみました．

``` Python
def mainPyQt5():
    # 必要なモジュールのimport
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtCore import QUrl
    from PyQt5.QtWebEngineWidgets import QWebEngineView

    url = 'https://www.youtube.com/?hl=ja&gl=JP'

    app = QApplication(sys.argv)

    # QWebEngineViewによるWebページ表示
    browser = QWebEngineView()
    browser.load(QUrl(url))
    browser.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    mainPyQt5()
```

結論から行くと，QWebEngineViewでは真っ白なWindowが表示されるだけで，
Webページが正しく読み込まれませんでした(インストールの問題ですかね...)．

## まとめ

インストールした環境にもよるかと思いますが，
現状安定性だと，

Pythonのデフォルトライブラリ > PyQt4 > PyQt5

となりました．
PyQtで安定したWebブラウザを作成するのはもう少し先になりそうです．