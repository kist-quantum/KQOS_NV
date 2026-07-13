# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from UI_files.modules import *
# from UI_files.widgets import *
import os
from PySide6.QtCore import QSize
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        description = "KQOS"
        # APPLY TEXTS
        # self.ui.setWindowTitle(title)
        self.ui.titleRightInfo.setText(description)
        self.ui.toggleButton.clicked.connect(lambda: self.toggleMenu(True))
        self.show()
        
        pixmap = QPixmap('UI_files/images/icons/cil-frown.png')
        smile_icon = QIcon()
        smile_icon.addPixmap(pixmap)
        
    def toggleMenu(self, enable):
        if enable:
            width = self.ui.leftMenuBg.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 60

            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
            
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F1:
            self.ui.stackedWidget.setCurrentIndex(0)
        elif e.key() == Qt.Key_F2:
            self.ui.stackedWidget.setCurrentIndex(1)
        elif e.key() == Qt.Key_F3:
            self.ui.stackedWidget.setCurrentIndex(2)
        elif e.key() == Qt.Key_F4:
            self.ui.stackedWidget.setCurrentIndex(3)
        elif e.key() == Qt.Key_F5:
            self.ui.stackedWidget.setCurrentIndex(4)
        elif e.key() == Qt.Key_F6:
            self.ui.stackedWidget.setCurrentIndex(5)
        elif e.key() == Qt.Key_F7:
            self.ui.stackedWidget.setCurrentIndex(6)
        elif e.key() == Qt.Key_F8:
            self.ui.stackedWidget.setCurrentIndex(7)