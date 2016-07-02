# -*- coding: utf-8 -*-
## @package image_browser.directory_selector
#
#  ディレクトリ選択GUI
#  @author      tody
#  @date        2016/07/02


import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class DirectorySelector(QTreeView):
    fileSelected = pyqtSignal(object)
    message_logging = pyqtSignal(object)

    ## Constructor
    def __init__(self):
        super(DirectorySelector, self).__init__()
        self.setMouseTracking(True)

        self._model = QFileSystemModel()
        self.setModel(self._model)
        self._model.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)

        self.selectionModel().selectionChanged.connect(self.selectFile)

        self.setHeaderHidden(True)
        self.hideColumn(1)
        self.hideColumn(2)
        self.hideColumn(3)
        self.update()

    ## ダブルクリックでファイルを開く．
    def mouseDoubleClickEvent(self, event):
        files = self.selectedFiles
        if len(files) > 0:
            QDesktopServices.openUrl(QUrl(files[0]))
        super(DirectorySelector, self).mouseDoubleClickEvent(event)

    def setRootPath(self, dir_path):
        self._model.setRootPath(dir_path)
        self.setRootIndex(self._model.index(dir_path))
        self.update()

    def setFilter(self, filter):
        self._model.setFilter(filter)

    def setNameFilters(self, filters):
        self._model.setNameFilters(filters)

    @property
    def selectedFiles(self):
        selectionModel = self.selectionModel()
        selectionModel.selectedIndexes()

        files = []
        for selectionIndex in selectionModel.selectedIndexes():
            file_path = str(self._model.filePath(selectionIndex))
            files.append(file_path)
        return files

    def selectFile(self):
        files = self.selectedFiles

        if len(files) > 0:
            self.fileSelected.emit(files)
            self.message_logging.emit("Selected Directory: %s" % files[0])

    def __repr__(self):
        return "DirectorySelector: %s" % (self._model.rootPath())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    selector = DirectorySelector()
    selector.show()

    print (selector.setRootPath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

    end = app.exec_()
