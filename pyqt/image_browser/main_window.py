
# -*- coding: utf-8 -*-
## @package image_browser.main_window
#
#  イメージブラウザ.
#  @author      tody
#  @date        2016/07/01


import os

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from image_browser.dir_path_editor import DirPathEditor
from image_browser.directory_selector import DirectorySelector
from image_browser.image_list_view import ImageListView


## イメージブラウザ.
class ImageBrowser(QMainWindow):
    fileSelected = pyqtSignal(object)

    def __init__(self):
        super(ImageBrowser, self).__init__()
        self.setAcceptDrops(True)
        self.setWindowTitle("Image Browser")

        central_widget = QWidget()
        layout = QVBoxLayout()
        self._dir_path_selector = DirPathEditor()
        self._dir_path_selector.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        layout.addWidget(self._dir_path_selector)

        splitter = QSplitter()

        self._directory_selector = DirectorySelector()
        self._directory_selector.setFilter(QDir.NoDotAndDotDot | QDir.Dirs)
        ds_size_policy = self._directory_selector.sizePolicy()
        ds_size_policy.setHorizontalStretch(1)
        self._directory_selector.setSizePolicy(ds_size_policy)

        self._image_list_view = ImageListView()
        iml_size_policy = self._image_list_view.sizePolicy()
        iml_size_policy.setHorizontalStretch(4)
        self._image_list_view.setSizePolicy(iml_size_policy)

        splitter.addWidget(self._directory_selector)
        splitter.addWidget(self._image_list_view)

        self._dir_path_selector.dir_selected.connect(self._selectDir)
        self._directory_selector.fileSelected.connect(self._selectDirs)
        self._image_list_view.fileSelected.connect(self.fileSelected)

        layout.addWidget(splitter)
        central_widget.setLayout(layout)

        self._createMenus()
        self.setCentralWidget(central_widget)

        status_bar = QStatusBar(self)
        self._dir_path_selector.message_logging.connect(status_bar.showMessage)
        self._directory_selector.message_logging.connect(status_bar.showMessage)
        self._image_list_view.message_logging.connect(status_bar.showMessage)
        self.setStatusBar(status_bar)

    def selectedFiles(self):
        return self._image_list_view.selectedFiles()

    def setRootPath(self, dir_path):
        self._dir_path = os.path.abspath(dir_path)
        self._dir_path_selector.setDirPath(self._dir_path)
        self.update()

    def _selectDir(self, dir_path):
        self._directory_selector.setRootPath(dir_path)

    def _selectDirs(self, dir_path_list):
        if len(dir_path_list) > 0:
            self._image_list_view.setRootPath(dir_path_list[0])

    def _createMenus(self):
        pass

def printSelectedFiles(files):
    print(files)

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)

    win = ImageBrowser()
    win.setRootPath("../../")
    win.fileSelected.connect(printSelectedFiles)
    win.showMaximized()

    end = app.exec_()