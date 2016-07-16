メディアプレーヤーの作成
====

今回は，PyQt5のQMediaPlayerを使ってメディアプレーヤーを作成してみます．
QMediaPlayerはPyQtの中でも新しい機能なのでPyQt5にしか入っていません．
まず，手持ちの環境にPyQt5を入れるところから始めましょう．

公式には，Anacondaプロンプト上から以下のコマンドを打てばインストールできます．

``` bash
conda install -c dsdale24 pyqt5
```

pipでもPyQt5は64bit版が提供されていますので，
もし上のコマンドで入らない場合は，以下のコマンドでインストールします．

``` bash
pip install pyqt5
```

基本的にな構文は，PyQt4とPyQt5でそんなには変わっていません．
ただし，PyQt5では今回紹介するQMediaPlayerやQtQuick等，
新しく便利な機能が追加されています．

それでは，早速QMediaPlayerを使って簡単なビデオプレーヤーを作ってみましょう．
以下がひな形のコードになります．

``` Python
import sys

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# QVideoWidgetを拡張したビデオ再生用Widget
class VideoPlayer(QVideoWidget):
    def __init__(self):
        super(VideoPlayer, self).__init__()

        self._player = QMediaPlayer()
        self._playlist = QMediaPlaylist()
        self._stopped = True

    # プレイリストに動画を追加
    def addMedia(self, media_file):
        media_content = QMediaContent(QUrl.fromLocalFile(media_file))
        self._playlist.addMedia(media_content)

    # クリックでポーズ・再生の切り替え
    def mousePressEvent(self, event):
        if self._stopped:
            self.play()
        else:
            self._player.pause()
            self._stopped = True

    # ダブルクリックで動画を読み込み，再生
    def mouseDoubleClickEvent(self, event):
        self._player.setVideoOutput(self)
        self._player.setPlaylist(self._playlist)
        self.play()

    def play(self):
        self._player.play()
        self._stopped = False


def main():
    app = QApplication(sys.argv)

    video_player = VideoPlayer()
    video_player.show()

    video_player.addMedia("movie1.wmv")

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```

まず，VideoPlayerの実行部分ですが，

``` Python
    video_player = VideoPlayer()
    video_player.show()

    video_player.addMedia("movie1.wmv")
```

addMedia関数でローカルファイル内の動画を作成できるようになっています．
URLとして，Web中の動画を再生することもできますが，".wmv"や".flv"のように
動画ファイルを指定しなければいけないみたいです．
そのままYoutubeの動画を作成することはできません．

それでは，次にVideoPlayerを構成する部分について見ていきましょう．
まず，コンストラクタ部分ですが，QVideoWidgetクラスを拡張したVideoPlayerを作り，
内部変数としてQMediaPlayer，QMediaPlaylistのデータを持っています．

``` Python
# QVideoWidgetを拡張したビデオ再生用Widget
class VideoPlayer(QVideoWidget):
    def __init__(self):
        super(VideoPlayer, self).__init__()

        self._player = QMediaPlayer()
        self._playlist = QMediaPlaylist()
        self._stopped = True
```

QMediaPlayerは動画の再生を管理するクラス，
QMediaPlaylistは動画リストを管理するクラスになります．

次に，プレイリストに動画を追加する部分を見てみましょう．

``` Python
    # プレイリストに動画を追加
    def addMedia(self, media_file):
        media_content = QMediaContent(QUrl.fromLocalFile(media_file))
        self._playlist.addMedia(media_content)
```

動画の追加は，QMediaContentをQMediaPlaylistに登録することでできます．
ここでは，```QMediaContent(QUrl.fromLocalFile(media_file))```で
ローカルファイルを登録できるようにしています．

``` Python
    # ダブルクリックで動画を読み込み，再生
    def mouseDoubleClickEvent(self, event):
        self._player.setVideoOutput(self)
        self._player.setPlaylist(self._playlist)
        self.play()
```

ダブルクリック時にQMediaPlayerをQVideoWidgetに登録することで
動画を表示するための準備をしています．
ここで，実装上の注意点ですが，このsetVideoOutputは関数はWidget作成時に呼ぶと落ちます．

ダブルクリック時に呼ぶようにすることで動画の再生が安定します．
ただし，Python版のQVideoWidget表示はC++版に比べると処理が重く，
同じ動画を再生してもフリッカーが少し起こってしまいました．
PyQtインストール時の問題かもしれませんが，
今後のバージョンで改善されることを期待したいところです．