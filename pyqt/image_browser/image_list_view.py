# -*- coding: utf-8 -*-
## @package image_browser.image_list_view
#
#  画像リストビュー．
#  @author      tody
#  @date        2016/07/02



import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class ImageIcon(QListWidgetItem):
    def __init__(self, file_path, parent=None):
        QLabel.__init__(self, parent=parent)
        file_path = file_path.replace("\\", "/")

        self._file_path = file_path

        self.setText(os.path.basename(file_path))
        self.setData(Qt.UserRole, file_path)
        self.setIcon(QIcon(file_path))

    def filepath(self):
        return self._file_path

class ImageListView(QListWidget):
    fileSelected = pyqtSignal(object)
    message_logging = pyqtSignal(object)

    # Constructor
    def __init__(self):
        super(ImageListView, self).__init__()
        self.setMouseTracking(True)
        self.setGridSize(QSize(256, 256))

        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setViewMode(QListWidget.IconMode)
        self.setIconSize(QSize(200, 200))
        self.selectionModel().selectionChanged.connect(self.selectFile)
        self.setResizeMode(QListWidget.Adjust)

    def setRootPath(self, dir_path):
        self.clear()

        image_files = []
        max_search_count = 2000
        search_count = 0
        for (root, dirs, files) in os.walk(dir_path):
            if search_count > max_search_count:
                break
            for file in files:
                if ".png" in file or ".jpg" in file:
                    image_files.append(os.path.join(root, file))
                search_count += 1

        image_files = [os.path.join(dir_path, image_file) for image_file in image_files]

        image_icons = []

        for image_file in image_files:
            if ".png" in image_file or ".jpg" in image_file:
                image_icon = ImageIcon(image_file)
                image_icons.append(image_icon)

        for image_icon in image_icons:
            self.addItem(image_icon)

        self._image_icons = image_icons


    def selectedFiles(self):
        selectionModel = self.selectionModel()
        selectionModel.selectedIndexes()

        files = []
        for selectionIndex in selectionModel.selectedIndexes():
            file_path = selectionIndex.data(Qt.UserRole)
            files.append(file_path)

        return files

    def selectFile(self):
        files = self.selectedFiles()

        if len(files) > 0:
            self.fileSelected.emit(files)
            self.message_logging.emit("Selected Images: %d images." % len(files))

    def mouseDoubleClickEvent(self, event):
        if len(self.selectedFiles()) > 0:
            os.system(self.selectedFiles()[0])

    def __repr__(self):
        return "ImageListView: %s images" % (len(self._image_icons))

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    view = ImageListView()
    view.setRootPath(os.path.abspath("../datasets/photo"))
    print(view)
    view.showMaximized()

    end = app.exec_()
