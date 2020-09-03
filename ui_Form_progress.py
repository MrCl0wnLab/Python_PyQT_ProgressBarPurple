# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_Form_progressUTbGBQ.ui'
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


class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(797, 551)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShowdan = QFrame(self.centralwidget)
        self.dropShowdan.setObjectName(u"dropShowdan")
        self.dropShowdan.setStyleSheet(u"QFrame {	\n"
"\n"
"	background-color: rgb(27, 19, 57);\n"
"\n"
"	color: rgb(220, 220, 220);\n"
"\n"
"	border-radius: 10px;\n"
"\n"
"}")
        self.dropShowdan.setFrameShape(QFrame.StyledPanel)
        self.dropShowdan.setFrameShadow(QFrame.Raised)
        self.progressBar = QProgressBar(self.dropShowdan)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(9, 300, 761, 41))
        self.progressBar.setStyleSheet(u"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"\n"
"QProgressBar {\n"
"	background-color: rgb(82, 64, 157);\n"
"	color: #fff;\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"	height: 50px;\n"
"}\n"
"\n"
"")
        self.progressBar.setValue(0)
        self.labelName = QLabel(self.dropShowdan)
        self.labelName.setObjectName(u"labelName")
        self.labelName.setGeometry(QRect(0, 120, 777, 66))
        font = QFont()
        font.setFamily(u"Montserrat")
        font.setPointSize(48)
        self.labelName.setFont(font)
        self.labelName.setStyleSheet(u"QLabel{\n"
" color: rgb(253, 89, 255)\n"
"}")
        self.labelName.setAlignment(Qt.AlignCenter)
        self.labelSubName = QLabel(self.dropShowdan)
        self.labelSubName.setObjectName(u"labelSubName")
        self.labelSubName.setGeometry(QRect(0, 200, 777, 21))
        font1 = QFont()
        font1.setFamily(u"Montserrat")
        font1.setPointSize(12)
        self.labelSubName.setFont(font1)
        self.labelSubName.setStyleSheet(u"QLabel{\n"
" color: rgb(82, 64, 157);\n"
"height: 5px;\n"
"}")
        self.labelSubName.setAlignment(Qt.AlignCenter)
        self.labelLoading = QLabel(self.dropShowdan)
        self.labelLoading.setObjectName(u"labelLoading")
        self.labelLoading.setGeometry(QRect(0, 370, 777, 21))
        self.labelLoading.setFont(font1)
        self.labelLoading.setStyleSheet(u"QLabel{\n"
" color: rgb(82, 64, 157);\n"
"height: 5px;\n"
"}")
        self.labelLoading.setAlignment(Qt.AlignCenter)
        self.labelCreated = QLabel(self.dropShowdan)
        self.labelCreated.setObjectName(u"labelCreated")
        self.labelCreated.setGeometry(QRect(3, 490, 761, 20))
        self.labelCreated.setStyleSheet(u"QLabel{\n"
" color: rgb(82, 64, 157);\n"
"height: 5px;\n"
"}")
        self.labelCreated.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.dropShowdan)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.labelName.setText(QCoreApplication.translate("SplashScreen", u"<strong>APP</strong> Mr. Cl0wnLab", None))
        self.labelSubName.setText(QCoreApplication.translate("SplashScreen", u"<strong>Qt Designer</strong> testing form ", None))
        self.labelLoading.setText(QCoreApplication.translate("SplashScreen", u"loading...", None))
        self.labelCreated.setText(QCoreApplication.translate("SplashScreen", u"<strong>Created:</strong> Cleiton Pinheiro", None))
    # retranslateUi

