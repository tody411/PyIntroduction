
Beautiful Soup: 簡単なHTML構文解析
====

Beautiful SoupはHTML構文を解析するのにかなり強力なライブラリです．

``` Python
html_doc = """
<html><head><title>HTMLの構文解析</title></head>
<body>
<p class="title"><b>Beautiful Soup - HTMLの構文解析</b></p>

<h1>概要</h1>
<p><a href="https://www.crummy.com/software/BeautifulSoup/bs4/doc/" >Beautiful Soup</a>はHTMLの構文解析可能なとても便利なPythonライブラリです．</p>
<img src="image/sample.png" alt="サンプル画像です" width=200 height=200></img>
<table>
    <tr>
        <td>長所: </td> <td> 簡単な構文でHTMLを解析できます． </td>
    </tr>
    <tr>
        <td>短所: </td> <td> 使用用途に関しては要検討というところでしょうか．．． </td>
    </tr>
</table>
"""
```

例えば，上記のようなHTML文を解析するとします．

``` Python
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
```

この2行でHTMLの基本構造を解析できます．
タイトルは下記の構文でアクセスできます．

``` Python
soup.title
# <title></title>

soup.string
# HTMLの構文解析
```

画像タグについている属性についてもアクセス可能です．

``` Python
soup.img['alt']
# サンプル画像です

soup.img['width']
# 200

soup.string
# HTMLの構文解析
```

また複数の要素を持つ場合も，検索可能です．

``` Python
soup.find_all('td')
# [<td>長所: </td>, <td> 簡単な構文でHTMLを解析できます． </td>,
#  <td>短所: </td>, <td> 使用用途に関しては要検討というとこ ろでしょうか．．． </td>]
```

上手く，絡めればHTMLから様々な情報を得ることができます．
使用用途は要検討ですが，
例えば自分のサイトやブログをどこかに移行する時，
データ変換を行う際に非常に便利です．