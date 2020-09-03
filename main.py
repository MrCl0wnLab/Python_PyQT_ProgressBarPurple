import sys
import platform
from PySide2 import QtCore, QtGui,  QtWidgets
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


from ui_Form_progress import Ui_SplashScreen
from ui_Form_main import Ui_MainWindow

## GLOBAL
counter = 0

## FORM CENTRAL / POS SPLASH
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

## FORM SPLASH
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ## CREATE DROP SHADOWN EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,60))
        ## SET DROP SHADOWN EFFECT IN FRAME
        self.ui.dropShowdan.setGraphicsEffect(self.shadow)
        
        # QTIMER START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(100)


        # CHANGE DESCRIPTION / labelSubName
        QtCore.QTimer.singleShot(1000, lambda: self.ui.labelSubName.setText("<strong>LOADING</strong><font style=\"color:white\"> EXPLOITS</font>"))
        QtCore.QTimer.singleShot(1500, lambda: self.ui.labelSubName.setText("<strong>LOADING</strong><font style=\"color:white\"> DATABASE</font>"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.labelSubName.setText("<strong>LOADING</strong><font style=\"color:white\"> USER INTERFACE</font>"))

        ## SHOW MAIN WINDOWS
        self.show()
    def progress(self):
        global counter

        #SET VALUE TO PROGRESS
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREEM AND OPEN THING
        if counter > 100:
            self.timer.stop()
            ## CREATE FORM CENTRAL
            self.main = MainWindow()
            ## SET DROP SHADOWN EFFECT IN FRAME
            self.main.ui.frame.setGraphicsEffect(self.shadow)
            ## SHOW MAIN WINDOWS / FORM CENTRAL
            self.main.show()
            self.close()
        counter+=1



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())