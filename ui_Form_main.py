# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_Form_mainMfcajN.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1330, 980)
        MainWindow.setMinimumSize(QSize(1330, 980))
        MainWindow.setMaximumSize(QSize(1330, 980))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {	\n"
"\n"
"	background-color: rgb(27, 19, 57);\n"
"\n"
"	color: rgb(220, 220, 220);\n"
"\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.labelName = QLabel(self.frame)
        self.labelName.setObjectName(u"labelName")
        self.labelName.setGeometry(QRect(10, 320, 1311, 79))
        font = QFont()
        font.setFamily(u"Montserrat")
        font.setPointSize(48)
        self.labelName.setFont(font)
        self.labelName.setStyleSheet(u"QLabel{\n"
" color: rgb(253, 89, 255)\n"
"}")
        self.labelName.setAlignment(Qt.AlignCenter)
        self.labelSubName = QLabel(self.frame)
        self.labelSubName.setObjectName(u"labelSubName")
        self.labelSubName.setGeometry(QRect(560, 410, 209, 21))
        font1 = QFont()
        font1.setFamily(u"Montserrat")
        font1.setPointSize(12)
        self.labelSubName.setFont(font1)
        self.labelSubName.setStyleSheet(u"QLabel{\n"
" color: rgb(82, 64, 157);\n"
"height: 5px;\n"
"}")
        self.labelSubName.setAlignment(Qt.AlignCenter)
        self.labelSubName_2 = QLabel(self.frame)
        self.labelSubName_2.setObjectName(u"labelSubName_2")
        self.labelSubName_2.setGeometry(QRect(560, 900, 209, 21))
        self.labelSubName_2.setFont(font1)
        self.labelSubName_2.setStyleSheet(u"QLabel{\n"
" color:#fff;\n"
"height: 5px;\n"
"}")
        self.labelSubName_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1330, 22))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"APP Mr. Cl0wnLab", None))
        self.labelName.setText(QCoreApplication.translate("MainWindow", u"<strong>APP</strong> Mr. Cl0wnLab", None))
        self.labelSubName.setText(QCoreApplication.translate("MainWindow", u"<strong>Qt Designer</strong> testing form ", None))
        self.labelSubName_2.setText(QCoreApplication.translate("MainWindow", u"github.com/MrCl0wnLab", None))
    # retranslateUi

