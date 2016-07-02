
# -*- coding: utf-8 -*-
## @package image_browser.dir_path_editor
#
#  ディレクトリパスを指定するUI.
#  @author      tody
#  @date        2016/07/01

import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *


## Drag&Drop可能なQLineEdit
class DropLineEdit(QLineEdit):

    file_dropped = pyqtSignal(object)

    def __init__(self, parent):
        super(DropLineEdit, self).__init__(parent)
        self.setAcceptDrops(True)

    ## ファイルパスがある時にDropを受け入れる.
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    ## Line Editにファイルパスのテキストを設定．
    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            if len(event.mimeData().urls()) > 0:
                url = event.mimeData().urls()[0]
                self.setText(url.path()[1:])
                self.file_dropped.emit(str(self.text()))
            event.acceptProposedAction()
        else:
            event.ignore()

    ## ダブルクリックでファイルを開く．
    def mouseDoubleClickEvent(self, event):
        self.update()
        QDesktopServices.openUrl(QUrl(self.text()))
        super(DropLineEdit, self).mouseDoubleClickEvent(event)


## ディレクトリパスを指定するUI
class DirPathEditor(QWidget):
    dir_selected = pyqtSignal(object)
    message_logging = pyqtSignal(object)

    def __init__(self):
        QWidget.__init__(self)
        fileLabel = QLabel("&Dir path:")
        self._fileLineEdit = DropLineEdit(self)
        fileLabel.setBuddy(self._fileLineEdit)
        icon = QApplication.style().standardIcon(QStyle.SP_DirOpenIcon)

        file_open_button = QPushButton(icon, "")
        file_open_button.clicked.connect(self._openDialog)

        layout = QGridLayout()
        layout.addWidget(fileLabel, 0, 0)
        layout.addWidget(self._fileLineEdit, 0, 1)
        layout.addWidget(file_open_button, 0, 2)
        self.setLayout(layout)

        self._fileLineEdit.file_dropped.connect(self.setDirPath)
        self._fileLineEdit.editingFinished.connect(self._editingFinished)
        self.setWindowTitle("Dir Path Editor")

    def setDirPath(self, file_path):
        dir_path = file_path
        if os.path.isfile(file_path):
            dir_path = os.path.basename(file_path)
        self._fileLineEdit.setText(dir_path)
        self.dir_selected.emit(dir_path)
        self.message_logging.emit(self.__repr__())

    def dirPath(self):
        return self._fileLineEdit.text()

    def _editingFinished(self):
        self.setDirPath(self.dirPath())

    def _openDialog(self):
        dir_path = QFileDialog.getExistingDirectory(parent=self, caption='Open Directory', directory=self.dirPath(),
                                         options=QFileDialog.ShowDirsOnly)

        self.setDirPath(dir_path)

    def __repr__(self):
        return "DirPathEditor: %s" % self._fileLineEdit.text()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    dir_path_editor = DirPathEditor()
    dir_path_editor.show()
    sys.exit(app.exec_())
