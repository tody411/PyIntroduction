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