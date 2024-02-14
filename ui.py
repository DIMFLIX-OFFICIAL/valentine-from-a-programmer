# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(736, 736)
        MainWindow.setMinimumSize(QSize(736, 736))
        MainWindow.setMaximumSize(QSize(736, 736))
        MainWindow.setStyleSheet(u"border-radius: 30px;\n"
"background-image: url(:/bg/assets/main.png);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"\n"
"background-color: rgb(235, 215, 224);")
        self.accept_btn = QPushButton(self.centralwidget)
        self.accept_btn.setObjectName(u"accept_btn")
        self.accept_btn.setGeometry(QRect(240, 480, 221, 191))
        font = QFont()
        font.setFamily(u"Bahnschrift")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.accept_btn.setFont(font)
        self.accept_btn.setStyleSheet(u"background: transparent;\n"
"border-radius: 20px;\n"
"color: #FFFFFF;")
        self.refuse_btn = QPushButton(self.centralwidget)
        self.refuse_btn.setObjectName(u"refuse_btn")
        self.refuse_btn.setGeometry(QRect(20, 680, 181, 41))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift")
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.refuse_btn.setFont(font1)
        self.refuse_btn.setStyleSheet(u"border-radius: 10px;\n"
"color: #FFFFFF;\n"
"background:  rgb(201, 104, 135, 150);")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(0, 0, 721, 171))
        font2 = QFont()
        font2.setFamily(u"Bahnschrift SemiBold")
        font2.setPointSize(28)
        font2.setBold(True)
        font2.setWeight(75)
        self.title.setFont(font2)
        self.title.setStyleSheet(u"background: transparent;\n"
"color: rgb(201, 104, 135, 200);")
        self.title.setScaledContents(True)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setWordWrap(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.accept_btn.setText(QCoreApplication.translate("MainWindow", u"\u042f \u0441\u043e\u0433\u043b\u0430\u0441\u043d\u0430!", None))
        self.refuse_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0445\u043e\u0447\u0443, \u0443 \u043c\u0435\u043d\u044f \u043d\u0435 \u043f\u043e\u043b\u0443\u0447\u0438\u0442\u0441\u044f", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u041b\u044e\u0431\u0438\u043c\u0430\u044f, \u0434\u0430\u0432\u0430\u0439 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043c<br>\u044d\u0442\u043e\u0442 \u0432\u0435\u0447\u0435\u0440 \u0432\u043c\u0435\u0441\u0442\u0435?</p></body></html>", None))
    # retranslateUi

