# -*- coding: utf-8 -*-
## @package html_util
#
#  HTML出力クラスの作成.
#  @author      Tody
#  @date        2016/07/21


## HTML出力クラス
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