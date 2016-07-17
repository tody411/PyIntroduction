# -*- coding: utf-8 -*-
## @package web_browser.web_browser
#
#  Webブラウザー制御のExampleコード.
#  @author      Tody
#  @date        2016/07/17

import sys


## PythonデフォルトライブラリでのWebブラウザー制御.
def mainPythonWebbrowserDefault(url):
    import webbrowser
    webbrowser.open(url)

## PythonデフォルトライブラリでのWebブラウザー制御(ブラウザー指定).
def mainPythonWebbrowserFromExe(url, browser_exe=""):
    import webbrowser
    browser_type = '"%s"' % browser_exe + ' \%s'
    browser = webbrowser.get(browser_type)
    browser.open(url)

## PythonデフォルトライブラリでのWebブラウザー制御.
def mainPythonWebbrowser():
    url = 'https://github.com/tody411/PyIntroduction'
    browser_exe = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'

    mainPythonWebbrowserDefault(url)
    mainPythonWebbrowserFromExe(url, browser_exe)

## PyQt4でのWebブラウザー作成.
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

## PyQt4でのWebブラウザー作成(Youtube用).
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
    QWebSettings.globalSettings().setAttribute(QWebSettings.DnsPrefetchEnabled, True)
    QWebSettings.globalSettings().setAttribute(QWebSettings.JavascriptEnabled, True)
    QWebSettings.globalSettings().setAttribute(QWebSettings.OfflineStorageDatabaseEnabled, True)
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


## PyQt5でのWebブラウザー作成.
def mainPyQt5():
    # 必要なモジュールのimport
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtCore import QUrl
    from PyQt5.QtWebEngineWidgets import QWebEngineView

    url = 'https://github.com/tody411/PyIntroduction'

    app = QApplication(sys.argv)

    # QWebEngineViewによるWebページ表示
    browser = QWebEngineView()
    browser.load(QUrl(url))
    browser.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    mainPyQt4Simple()