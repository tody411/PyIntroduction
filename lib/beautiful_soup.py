# -*- coding: utf-8 -*-
## @package
#
#  Beautiful Soupのサンプル．
#  @author      tody
#  @date        2016/07/01

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

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print (soup.title)

print (soup.img['alt'])
print (soup.img['width'])

print (soup.find_all('td'))