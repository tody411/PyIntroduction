
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


def mainHelloWorld():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400, 400)
    w.setWindowTitle('PyQt Hello World')
    w.show()
    sys.exit(app.exec_())


def mainButtons():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400, 400)
    w.setWindowTitle('PyQt Buttons')

    # ボタンの追加
    layout = QVBoxLayout()
    layout.addWidget(QPushButton("Button 1"))
    layout.addWidget(QPushButton("Button 2"))
    layout.addWidget(QPushButton("Button 3"))
    w.setLayout(layout)

    w.show()
    sys.exit(app.exec_())


def pushSlot(button_name):
    def func():
        print("%s is pushed." % button_name)
    return func

def mainPushButtons():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(400, 400)
    w.setWindowTitle('PyQt Buttons')

    # ボタンの追加
    layout = QVBoxLayout()
    button1 = QPushButton("Button 1")
    button1.clicked.connect(pushSlot("Button 1"))
    layout.addWidget(button1)
    layout.addWidget(QPushButton("Button 2"))
    layout.addWidget(QPushButton("Button 3"))
    w.setLayout(layout)

    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    mainPushButtons()
