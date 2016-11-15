
zipfile: Zipファイルの処理
====

zipfileはPythonにデフォルトで入っている強力なZipファイル処理ライブラリです．

使い方も下記のように非常にシンプルな処理でZipファイルを解凍することができます．

``` Python
import zipfile

# file_pathに指定されたZipファイルをdir_path以下に解凍．
def extractZipFile(file_path, dir_path):
    with zipfile.ZipFile(file_path, 'r') as zip_file:
        zip_file.extractall(path=dir_path)
```

extractall関数を使えば簡単ですね．
さて，こんな処理をするためにわざわざPythonを使わなくてもいいじゃないかと言う人もいるかもしれません．
確かにその通りです．世の中には，たくさんの優秀なZipファイル解凍ソフトが出回っています．

それでは，Pythonを使うと便利なケースというのはいったいどんな時でしょう？
自分の場合，解凍したZipファイルの中に**たくさんの子Zipファイル**が存在するという状況に最近出会いました．

* all.zip
    - subFile001.zip
    - subFile002.zip
    - subFile003.zip
    - ...
    - subFile300.zip

非常に嫌な感じです．手作業でZipファイルを1つ1つ開いていたら日が暮れてしまいます．
また，手作業の段階で間違ってしまうかもしれません．

そんな時にPythonの出番です．

``` Python
import zipfile

# file_pathに指定されたZipファイルを子Zipファイルも含めてdir_path以下に解凍．
def extractAllSubZipFiles(file_path, dir_path):
    with zipfile.ZipFile(file_path, 'r') as zip_file:
        zip_file.extractall(path=dir_path)

    sub_zip_files = os.listdir(dir_path)
    sub_zip_files = [sub_zip_file for sub_zip_file in sub_zip_files if ".zip" in sub_zip_file]
    sub_zip_files = [os.path.join(dir_path, sub_zip_file) for sub_zip_file in sub_zip_files]

    for sub_zip_file in sub_zip_files:
        sub_dir_path = sub_zip_file.replace(".zip", "")
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            zip_file.extractall(path=sub_dir_path)
```

Pythonを使えば，```os.listdir(dir_path)```を使ってディレクトリの中身を調べることができ，
各```sub_zip_file```に対して自動的に```zip_file.extractall```を呼んで解凍することが可能です．

これでボタン一発でZipファイルを全て解凍です．
このPythonプログラムのおかげで毎回30分くらいかかる作業が10秒に短縮されました．
やはりPythonは便利．