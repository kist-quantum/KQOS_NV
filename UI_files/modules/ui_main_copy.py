# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainjWIBmf.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QScrollBar, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTextEdit, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.Shape.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Shadow.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Shadow.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 0, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.Shape.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Shadow.Plain)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setWeight(QFont.Weight(50))
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.Shape.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy1)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_counter = QPushButton(self.topMenu)
        self.btn_counter.setObjectName(u"btn_counter")
        sizePolicy1.setHeightForWidth(self.btn_counter.sizePolicy().hasHeightForWidth())
        self.btn_counter.setSizePolicy(sizePolicy1)
        self.btn_counter.setMinimumSize(QSize(0, 45))
        self.btn_counter.setFont(font)
        self.btn_counter.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_counter.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_counter.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-speedometer.png);")

        self.verticalLayout_8.addWidget(self.btn_counter)

        self.btn_confocal = QPushButton(self.topMenu)
        self.btn_confocal.setObjectName(u"btn_confocal")
        sizePolicy1.setHeightForWidth(self.btn_confocal.sizePolicy().hasHeightForWidth())
        self.btn_confocal.setSizePolicy(sizePolicy1)
        self.btn_confocal.setMinimumSize(QSize(0, 45))
        self.btn_confocal.setFont(font)
        self.btn_confocal.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_confocal.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_confocal.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-magnifying-glass.png);")

        self.verticalLayout_8.addWidget(self.btn_confocal)

        self.btn_magnet = QPushButton(self.topMenu)
        self.btn_magnet.setObjectName(u"btn_magnet")
        sizePolicy1.setHeightForWidth(self.btn_magnet.sizePolicy().hasHeightForWidth())
        self.btn_magnet.setSizePolicy(sizePolicy1)
        self.btn_magnet.setMinimumSize(QSize(0, 45))
        self.btn_magnet.setFont(font)
        self.btn_magnet.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_magnet.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_magnet.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-transfer.png);")

        self.verticalLayout_8.addWidget(self.btn_magnet)

        self.btn_control = QPushButton(self.topMenu)
        self.btn_control.setObjectName(u"btn_control")
        sizePolicy1.setHeightForWidth(self.btn_control.sizePolicy().hasHeightForWidth())
        self.btn_control.setSizePolicy(sizePolicy1)
        self.btn_control.setMinimumSize(QSize(0, 45))
        self.btn_control.setFont(font)
        self.btn_control.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_control.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_control.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-rss.png);")

        self.verticalLayout_8.addWidget(self.btn_control)

        self.btn_save = QPushButton(self.topMenu)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy1.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy1)
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setFont(font)
        self.btn_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_save.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-save.png)")

        self.verticalLayout_8.addWidget(self.btn_save)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy1.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy1)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-x.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy1.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy1)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setFrameShape(QFrame.Shape.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Shadow.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.Shape.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy1.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy1)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy1.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy1)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy1.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy1)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignmentFlag.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.Shape.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.Shape.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.Shape.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy2)
        self.leftBox.setFrameShape(QFrame.Shape.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy3)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.Shape.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.Shape.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.Shape.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.Shape.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.Shape.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.Shape.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy1.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy1)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy1.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy1)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy1.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy1)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)

        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.Shape.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(100)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy4)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.stackedWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.counter = QWidget()
        self.counter.setObjectName(u"counter")
        self.counter.setStyleSheet(u"")
        self.verticalLayoutWidget_2 = QWidget(self.counter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 10, 261, 41))
        self.verticalLayout_21 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Semibold"])
        font4.setPointSize(20)
        font4.setWeight(QFont.Weight(50))
        font4.setItalic(False)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.verticalLayout_21.addWidget(self.label)

        self.frame_2 = QFrame(self.counter)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 60, 1791, 661))
        self.frame_2.setFrameShape(QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QFrame.Shadow.Plain)
        self.counter_widget = QWidget(self.frame_2)
        self.counter_widget.setObjectName(u"counter_widget")
        self.counter_widget.setGeometry(QRect(0, 0, 1791, 661))
        self.verticalLayoutWidget = QWidget(self.counter_widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 1771, 641))
        self.counter_layout = QVBoxLayout(self.verticalLayoutWidget)
        self.counter_layout.setObjectName(u"counter_layout")
        self.counter_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.counter)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 730, 1791, 231))
        self.frame_3.setFrameShape(QFrame.Shape.Box)
        self.frame_3.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayoutWidget_2 = QWidget(self.frame_3)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(20, 100, 1751, 121))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.counter_counts = QLineEdit(self.gridLayoutWidget_2)
        self.counter_counts.setObjectName(u"counter_counts")
        self.counter_counts.setEnabled(False)
        self.counter_counts.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.counter_counts.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.counter_counts, 0, 2, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_25, 0, 3, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI Semibold"])
        font5.setPointSize(15)
        font5.setWeight(QFont.Weight(50))
        font5.setItalic(False)
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_4.addWidget(self.label_6, 0, 4, 1, 1)

        self.counter_standard_deviation = QLineEdit(self.gridLayoutWidget_2)
        self.counter_standard_deviation.setObjectName(u"counter_standard_deviation")
        self.counter_standard_deviation.setEnabled(False)
        self.counter_standard_deviation.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.counter_standard_deviation.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.counter_standard_deviation, 0, 8, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 1, 5, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_4.addWidget(self.label_7, 0, 7, 1, 1)

        self.counter_average_counts = QLineEdit(self.gridLayoutWidget_2)
        self.counter_average_counts.setObjectName(u"counter_average_counts")
        self.counter_average_counts.setEnabled(False)
        self.counter_average_counts.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.counter_average_counts.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.counter_average_counts, 0, 5, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 0, 6, 1, 1)

        self.counter_laser_power_2 = QLabel(self.gridLayoutWidget_2)
        self.counter_laser_power_2.setObjectName(u"counter_laser_power_2")
        self.counter_laser_power_2.setFont(font5)
        self.counter_laser_power_2.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.counter_laser_power_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.counter_laser_power_2.setWordWrap(True)
        self.counter_laser_power_2.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_4.addWidget(self.counter_laser_power_2, 2, 7, 1, 1)

        self.counter_laser_power = QLineEdit(self.gridLayoutWidget_2)
        self.counter_laser_power.setObjectName(u"counter_laser_power")
        self.counter_laser_power.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.counter_laser_power.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.counter_laser_power, 2, 8, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_4.addWidget(self.label_3, 2, 4, 1, 1)

        self.counter_trace_length = QLineEdit(self.gridLayoutWidget_2)
        self.counter_trace_length.setObjectName(u"counter_trace_length")
        self.counter_trace_length.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.counter_trace_length.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.counter_trace_length, 2, 5, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)

        self.counter_T_per_sec = QLineEdit(self.gridLayoutWidget_2)
        self.counter_T_per_sec.setObjectName(u"counter_T_per_sec")
        self.counter_T_per_sec.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.counter_T_per_sec.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.counter_T_per_sec, 2, 2, 1, 1)

        self.horizontalLayoutWidget_3 = QWidget(self.frame_3)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(1280, 20, 491, 51))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.counter_start = QPushButton(self.horizontalLayoutWidget_3)
        self.counter_start.setObjectName(u"counter_start")
        sizePolicy1.setHeightForWidth(self.counter_start.sizePolicy().hasHeightForWidth())
        self.counter_start.setSizePolicy(sizePolicy1)
        self.counter_start.setFont(font5)
        self.counter_start.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-media-play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.counter_start.setIcon(icon4)
        self.counter_start.setIconSize(QSize(40, 40))
        self.counter_start.setCheckable(False)

        self.horizontalLayout_8.addWidget(self.counter_start)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.counter_save = QPushButton(self.horizontalLayoutWidget_3)
        self.counter_save.setObjectName(u"counter_save")
        sizePolicy1.setHeightForWidth(self.counter_save.sizePolicy().hasHeightForWidth())
        self.counter_save.setSizePolicy(sizePolicy1)
        self.counter_save.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.counter_save.setIcon(icon5)
        self.counter_save.setIconSize(QSize(40, 40))

        self.horizontalLayout_8.addWidget(self.counter_save)

        self.horizontalLayoutWidget_7 = QWidget(self.frame_3)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(20, 20, 211, 51))
        self.horizontalLayout_15 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.counter_laser_on = QPushButton(self.horizontalLayoutWidget_7)
        self.counter_laser_on.setObjectName(u"counter_laser_on")
        sizePolicy1.setHeightForWidth(self.counter_laser_on.sizePolicy().hasHeightForWidth())
        self.counter_laser_on.setSizePolicy(sizePolicy1)
        self.counter_laser_on.setFont(font5)
        self.counter_laser_on.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        icon6 = QIcon()
        icon6.addFile(u":/icon/images/icons/cil-smile.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.counter_laser_on.setIcon(icon6)
        self.counter_laser_on.setIconSize(QSize(40, 40))
        self.counter_laser_on.setCheckable(False)

        self.horizontalLayout_15.addWidget(self.counter_laser_on)

        self.stackedWidget.addWidget(self.counter)
        self.confocal = QWidget()
        self.confocal.setObjectName(u"confocal")
        self.verticalLayout_20 = QVBoxLayout(self.confocal)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget = QWidget(self.confocal)
        self.widget.setObjectName(u"widget")
        self.horizontalLayoutWidget_2 = QWidget(self.widget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 0, 981, 41))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.horizontalLayoutWidget_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.horizontalLayout_7.addWidget(self.label_19)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)

        self.confocal_save = QPushButton(self.horizontalLayoutWidget_2)
        self.confocal_save.setObjectName(u"confocal_save")
        sizePolicy1.setHeightForWidth(self.confocal_save.sizePolicy().hasHeightForWidth())
        self.confocal_save.setSizePolicy(sizePolicy1)
        self.confocal_save.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.confocal_save.setIcon(icon5)

        self.horizontalLayout_7.addWidget(self.confocal_save)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.confocal_load = QPushButton(self.horizontalLayoutWidget_2)
        self.confocal_load.setObjectName(u"confocal_load")
        sizePolicy1.setHeightForWidth(self.confocal_load.sizePolicy().hasHeightForWidth())
        self.confocal_load.setSizePolicy(sizePolicy1)
        self.confocal_load.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.confocal_load.setIcon(icon7)

        self.horizontalLayout_7.addWidget(self.confocal_load)

        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 50, 981, 891))
        self.frame_4.setFrameShape(QFrame.Shape.Box)
        self.frame_4.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayoutWidget = QWidget(self.frame_4)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 590, 961, 61))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_11.setWordWrap(True)
        self.label_11.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.confocal_resolution = QLineEdit(self.horizontalLayoutWidget)
        self.confocal_resolution.setObjectName(u"confocal_resolution")
        self.confocal_resolution.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(20)
        sizePolicy5.setHeightForWidth(self.confocal_resolution.sizePolicy().hasHeightForWidth())
        self.confocal_resolution.setSizePolicy(sizePolicy5)
        self.confocal_resolution.setMaximumSize(QSize(100, 16777215))
        self.confocal_resolution.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.confocal_resolution.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.confocal_resolution)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)

        self.label_29 = QLabel(self.horizontalLayoutWidget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font5)
        self.label_29.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_29.setWordWrap(True)
        self.label_29.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.horizontalLayout_6.addWidget(self.label_29)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_19)

        self.confocal_T_per_point = QLineEdit(self.horizontalLayoutWidget)
        self.confocal_T_per_point.setObjectName(u"confocal_T_per_point")
        self.confocal_T_per_point.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(200)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.confocal_T_per_point.sizePolicy().hasHeightForWidth())
        self.confocal_T_per_point.setSizePolicy(sizePolicy6)
        self.confocal_T_per_point.setMaximumSize(QSize(100, 16777215))
        self.confocal_T_per_point.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.confocal_T_per_point.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.confocal_T_per_point)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_26)

        self.confocal_home = QPushButton(self.horizontalLayoutWidget)
        self.confocal_home.setObjectName(u"confocal_home")
        sizePolicy1.setHeightForWidth(self.confocal_home.sizePolicy().hasHeightForWidth())
        self.confocal_home.setSizePolicy(sizePolicy1)
        self.confocal_home.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.confocal_home.setIcon(icon8)

        self.horizontalLayout_6.addWidget(self.confocal_home)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.confocal_start = QPushButton(self.horizontalLayoutWidget)
        self.confocal_start.setObjectName(u"confocal_start")
        sizePolicy1.setHeightForWidth(self.confocal_start.sizePolicy().hasHeightForWidth())
        self.confocal_start.setSizePolicy(sizePolicy1)
        self.confocal_start.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.confocal_start.setIcon(icon4)

        self.horizontalLayout_6.addWidget(self.confocal_start)

        self.gridLayoutWidget_3 = QWidget(self.frame_4)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(10, 660, 961, 211))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 0, 3, 1, 1)

        self.x_fix = QCheckBox(self.gridLayoutWidget_3)
        self.x_fix.setObjectName(u"x_fix")
        self.x_fix.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")

        self.gridLayout_3.addWidget(self.x_fix, 1, 0, 1, 1)

        self.confocal_to_x = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_to_x.setObjectName(u"confocal_to_x")
        self.confocal_to_x.setEnabled(True)
        self.confocal_to_x.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.confocal_to_x.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.confocal_to_x, 1, 8, 1, 1)

        self.confocal_set_position_x = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_set_position_x.setObjectName(u"confocal_set_position_x")
        self.confocal_set_position_x.setEnabled(True)
        self.confocal_set_position_x.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.confocal_set_position_x.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.confocal_set_position_x, 1, 4, 1, 1)

        self.confocal_from_x = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_from_x.setObjectName(u"confocal_from_x")
        self.confocal_from_x.setEnabled(True)
        self.confocal_from_x.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.confocal_from_x.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.confocal_from_x, 1, 6, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.z_fix = QCheckBox(self.gridLayoutWidget_3)
        self.z_fix.setObjectName(u"z_fix")
        self.z_fix.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.z_fix.setChecked(True)

        self.gridLayout_3.addWidget(self.z_fix, 3, 0, 1, 1)

        self.confocal_position_x = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_position_x.setObjectName(u"confocal_position_x")
        self.confocal_position_x.setEnabled(False)
        self.confocal_position_x.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.confocal_position_x.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.confocal_position_x, 1, 2, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font5)
        self.label_12.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_3.addWidget(self.label_12, 0, 6, 1, 1)

        self.confocal_from_z = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_from_z.setObjectName(u"confocal_from_z")
        self.confocal_from_z.setEnabled(True)
        self.confocal_from_z.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.confocal_from_z.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.confocal_from_z, 3, 6, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 0, 7, 1, 1)

        self.confocal_position_z = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_position_z.setObjectName(u"confocal_position_z")
        self.confocal_position_z.setEnabled(False)
        self.confocal_position_z.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.confocal_position_z.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.confocal_position_z, 3, 2, 1, 1)

        self.confocal_set_position_z = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_set_position_z.setObjectName(u"confocal_set_position_z")
        self.confocal_set_position_z.setEnabled(True)
        self.confocal_set_position_z.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.confocal_set_position_z.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.confocal_set_position_z, 3, 4, 1, 1)

        self.y_fix = QCheckBox(self.gridLayoutWidget_3)
        self.y_fix.setObjectName(u"y_fix")
        self.y_fix.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")

        self.gridLayout_3.addWidget(self.y_fix, 2, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 0, 5, 1, 1)

        self.confocal_set_position_y = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_set_position_y.setObjectName(u"confocal_set_position_y")
        self.confocal_set_position_y.setEnabled(True)
        self.confocal_set_position_y.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.confocal_set_position_y.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.confocal_set_position_y, 2, 4, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_3.addWidget(self.label_9, 0, 2, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)

        self.confocal_to_z = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_to_z.setObjectName(u"confocal_to_z")
        self.confocal_to_z.setEnabled(True)
        self.confocal_to_z.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.confocal_to_z.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.confocal_to_z, 3, 8, 1, 1)

        self.confocal_position_y = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_position_y.setObjectName(u"confocal_position_y")
        self.confocal_position_y.setEnabled(False)
        self.confocal_position_y.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.confocal_position_y.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.confocal_position_y, 2, 2, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font5)
        self.label_13.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_3.addWidget(self.label_13, 0, 8, 1, 1)

        self.confocal_from_y = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_from_y.setObjectName(u"confocal_from_y")
        self.confocal_from_y.setEnabled(True)
        self.confocal_from_y.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.confocal_from_y.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.confocal_from_y, 2, 6, 1, 1)

        self.confocal_to_y = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_to_y.setObjectName(u"confocal_to_y")
        self.confocal_to_y.setEnabled(True)
        self.confocal_to_y.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.confocal_to_y.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.confocal_to_y, 2, 8, 1, 1)

        self.confocal_moveto = QPushButton(self.gridLayoutWidget_3)
        self.confocal_moveto.setObjectName(u"confocal_moveto")
        sizePolicy1.setHeightForWidth(self.confocal_moveto.sizePolicy().hasHeightForWidth())
        self.confocal_moveto.setSizePolicy(sizePolicy1)
        self.confocal_moveto.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.confocal_moveto.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-arrow-circle-right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.confocal_moveto.setIcon(icon9)

        self.gridLayout_3.addWidget(self.confocal_moveto, 0, 4, 1, 1)

        self.frame_13 = QFrame(self.frame_4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(10, 10, 961, 571))
        self.frame_13.setFrameShape(QFrame.Shape.Box)
        self.frame_13.setFrameShadow(QFrame.Shadow.Plain)
        self.widget_6 = QWidget(self.frame_13)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(10, 10, 771, 551))
        self.verticalLayoutWidget_9 = QWidget(self.widget_6)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(10, -40, 751, 591))
        self.confocal_layout = QVBoxLayout(self.verticalLayoutWidget_9)
        self.confocal_layout.setObjectName(u"confocal_layout")
        self.confocal_layout.setContentsMargins(0, 0, 0, 0)
        self.confocal_widget = QWidget(self.frame_13)
        self.confocal_widget.setObjectName(u"confocal_widget")
        self.confocal_widget.setGeometry(QRect(790, 10, 151, 451))
        self.horizontalLayoutWidget_10 = QWidget(self.confocal_widget)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(0, 10, 151, 431))
        self.horizontalLayout_18 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalSlider_2 = QSlider(self.horizontalLayoutWidget_10)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setStyleSheet(u"")
        self.verticalSlider_2.setOrientation(Qt.Orientation.Vertical)

        self.horizontalLayout_18.addWidget(self.verticalSlider_2)

        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(770, 460, 181, 101))
        self.frame_18.setFrameShape(QFrame.Shape.Box)
        self.frame_18.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayoutWidget_10 = QWidget(self.frame_18)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(10, 10, 160, 80))
        self.verticalLayout_23 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.verticalLayoutWidget_10)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font5)
        self.label_18.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_18.setWordWrap(True)
        self.label_18.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.verticalLayout_23.addWidget(self.label_18)

        self.confocal_counts = QLineEdit(self.verticalLayoutWidget_10)
        self.confocal_counts.setObjectName(u"confocal_counts")
        self.confocal_counts.setEnabled(False)
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(18)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.confocal_counts.sizePolicy().hasHeightForWidth())
        self.confocal_counts.setSizePolicy(sizePolicy7)
        self.confocal_counts.setMaximumSize(QSize(200, 16777215))
        self.confocal_counts.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.confocal_counts.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_23.addWidget(self.confocal_counts)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(990, 50, 801, 891))
        self.frame.setFrameShape(QFrame.Shape.Box)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayoutWidget_6 = QWidget(self.frame)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(10, 710, 781, 161))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.autofocus_size_z = QLineEdit(self.gridLayoutWidget_6)
        self.autofocus_size_z.setObjectName(u"autofocus_size_z")
        self.autofocus_size_z.setEnabled(True)
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.autofocus_size_z.sizePolicy().hasHeightForWidth())
        self.autofocus_size_z.setSizePolicy(sizePolicy8)
        self.autofocus_size_z.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.autofocus_size_z.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.autofocus_size_z, 3, 2, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_6)
        self.label_17.setObjectName(u"label_17")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy9)
        self.label_17.setFont(font5)
        self.label_17.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_17.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_17.setWordWrap(True)
        self.label_17.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_5.addWidget(self.label_17, 1, 2, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_21, 2, 5, 1, 1)

        self.confocal_step_z = QLineEdit(self.gridLayoutWidget_6)
        self.confocal_step_z.setObjectName(u"confocal_step_z")
        self.confocal_step_z.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.confocal_step_z.sizePolicy().hasHeightForWidth())
        self.confocal_step_z.setSizePolicy(sizePolicy8)
        self.confocal_step_z.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.confocal_step_z.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.confocal_step_z, 3, 4, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font5)
        self.label_14.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_14.setWordWrap(True)
        self.label_14.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_5.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font5)
        self.label_15.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_15.setWordWrap(True)
        self.label_15.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_5.addWidget(self.label_15, 3, 0, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font5)
        self.label_16.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_16.setWordWrap(True)
        self.label_16.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_5.addWidget(self.label_16, 1, 4, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_24, 3, 5, 1, 1)

        self.confocal_step_xy = QLineEdit(self.gridLayoutWidget_6)
        self.confocal_step_xy.setObjectName(u"confocal_step_xy")
        self.confocal_step_xy.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.confocal_step_xy.sizePolicy().hasHeightForWidth())
        self.confocal_step_xy.setSizePolicy(sizePolicy8)
        self.confocal_step_xy.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.confocal_step_xy.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.confocal_step_xy, 2, 4, 1, 1)

        self.autofocus_size_xy = QLineEdit(self.gridLayoutWidget_6)
        self.autofocus_size_xy.setObjectName(u"autofocus_size_xy")
        self.autofocus_size_xy.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.autofocus_size_xy.sizePolicy().hasHeightForWidth())
        self.autofocus_size_xy.setSizePolicy(sizePolicy8)
        self.autofocus_size_xy.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.autofocus_size_xy.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.autofocus_size_xy, 2, 2, 1, 1)

        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(10, 350, 781, 301))
        self.frame_14.setFrameShape(QFrame.Shape.Box)
        self.frame_14.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayoutWidget_5 = QWidget(self.frame_14)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(10, 10, 761, 281))
        self.autofocus_layout = QGridLayout(self.gridLayoutWidget_5)
        self.autofocus_layout.setObjectName(u"autofocus_layout")
        self.autofocus_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget_11 = QWidget(self.frame)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(10, 660, 781, 41))
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_27 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_27)

        self.autofocus_01 = QCheckBox(self.horizontalLayoutWidget_11)
        self.autofocus_01.setObjectName(u"autofocus_01")
        self.autofocus_01.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")

        self.horizontalLayout_19.addWidget(self.autofocus_01)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_31)

        self.autofocus_005 = QCheckBox(self.horizontalLayoutWidget_11)
        self.autofocus_005.setObjectName(u"autofocus_005")
        self.autofocus_005.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")

        self.horizontalLayout_19.addWidget(self.autofocus_005)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_32)

        self.autofocus_001 = QCheckBox(self.horizontalLayoutWidget_11)
        self.autofocus_001.setObjectName(u"autofocus_001")
        self.autofocus_001.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.autofocus_001.setChecked(True)

        self.horizontalLayout_19.addWidget(self.autofocus_001)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_35)

        self.autofocus_start = QPushButton(self.horizontalLayoutWidget_11)
        self.autofocus_start.setObjectName(u"autofocus_start")
        sizePolicy1.setHeightForWidth(self.autofocus_start.sizePolicy().hasHeightForWidth())
        self.autofocus_start.setSizePolicy(sizePolicy1)
        self.autofocus_start.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.autofocus_start.setIcon(icon4)

        self.horizontalLayout_19.addWidget(self.autofocus_start)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_34)

        self.autofocus_save = QPushButton(self.horizontalLayoutWidget_11)
        self.autofocus_save.setObjectName(u"autofocus_save")
        sizePolicy1.setHeightForWidth(self.autofocus_save.sizePolicy().hasHeightForWidth())
        self.autofocus_save.setSizePolicy(sizePolicy1)
        self.autofocus_save.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.autofocus_save.setIcon(icon5)

        self.horizontalLayout_19.addWidget(self.autofocus_save)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_33)


        self.verticalLayout_20.addWidget(self.widget)

        self.stackedWidget.addWidget(self.confocal)
        self.magnet = QWidget()
        self.magnet.setObjectName(u"magnet")
        self.horizontalLayoutWidget_5 = QWidget(self.magnet)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 0, 981, 41))
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.horizontalLayoutWidget_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font4)
        self.label_20.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.horizontalLayout_13.addWidget(self.label_20)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_16)

        self.magnet_save_2 = QPushButton(self.horizontalLayoutWidget_5)
        self.magnet_save_2.setObjectName(u"magnet_save_2")
        sizePolicy1.setHeightForWidth(self.magnet_save_2.sizePolicy().hasHeightForWidth())
        self.magnet_save_2.setSizePolicy(sizePolicy1)
        self.magnet_save_2.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.magnet_save_2.setIcon(icon5)

        self.horizontalLayout_13.addWidget(self.magnet_save_2)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_20)

        self.magnet_load = QPushButton(self.horizontalLayoutWidget_5)
        self.magnet_load.setObjectName(u"magnet_load")
        sizePolicy1.setHeightForWidth(self.magnet_load.sizePolicy().hasHeightForWidth())
        self.magnet_load.setSizePolicy(sizePolicy1)
        self.magnet_load.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.magnet_load.setIcon(icon7)

        self.horizontalLayout_13.addWidget(self.magnet_load)

        self.frame_5 = QFrame(self.magnet)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 60, 981, 891))
        self.frame_5.setFrameShape(QFrame.Shape.Box)
        self.frame_5.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayoutWidget_6 = QWidget(self.frame_5)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 700, 961, 61))
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_29 = QSpacerItem(10, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_29)

        self.label_21 = QLabel(self.horizontalLayoutWidget_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font5)
        self.label_21.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_21.setWordWrap(True)
        self.label_21.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.horizontalLayout_14.addWidget(self.label_21)

        self.magnet_counts = QLineEdit(self.horizontalLayoutWidget_6)
        self.magnet_counts.setObjectName(u"magnet_counts")
        self.magnet_counts.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.magnet_counts.sizePolicy().hasHeightForWidth())
        self.magnet_counts.setSizePolicy(sizePolicy8)
        self.magnet_counts.setMaximumSize(QSize(100, 16777215))
        self.magnet_counts.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.magnet_counts.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.magnet_counts)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_22)

        self.label_30 = QLabel(self.horizontalLayoutWidget_6)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font5)
        self.label_30.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_30.setWordWrap(True)
        self.label_30.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.horizontalLayout_14.addWidget(self.label_30)

        self.magnet_per_point = QLineEdit(self.horizontalLayoutWidget_6)
        self.magnet_per_point.setObjectName(u"magnet_per_point")
        self.magnet_per_point.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.magnet_per_point.sizePolicy().hasHeightForWidth())
        self.magnet_per_point.setSizePolicy(sizePolicy8)
        self.magnet_per_point.setMaximumSize(QSize(100, 16777215))
        self.magnet_per_point.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.magnet_per_point.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.magnet_per_point)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_37)

        self.magnet_start = QPushButton(self.horizontalLayoutWidget_6)
        self.magnet_start.setObjectName(u"magnet_start")
        sizePolicy1.setHeightForWidth(self.magnet_start.sizePolicy().hasHeightForWidth())
        self.magnet_start.setSizePolicy(sizePolicy1)
        self.magnet_start.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.magnet_start.setIcon(icon4)

        self.horizontalLayout_14.addWidget(self.magnet_start)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_23)

        self.horizontalSpacer_30 = QSpacerItem(10, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_30)

        self.gridLayoutWidget_8 = QWidget(self.frame_5)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(10, 780, 961, 91))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.gridLayoutWidget_8)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font5)
        self.label_25.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_25.setWordWrap(True)
        self.label_25.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_6.addWidget(self.label_25, 1, 4, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget_8)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setEnabled(True)
        self.label_22.setFont(font5)
        self.label_22.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_22.setWordWrap(True)
        self.label_22.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_6.addWidget(self.label_22, 2, 0, 1, 1)

        self.magnet_size = QLineEdit(self.gridLayoutWidget_8)
        self.magnet_size.setObjectName(u"magnet_size")
        self.magnet_size.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.magnet_size.sizePolicy().hasHeightForWidth())
        self.magnet_size.setSizePolicy(sizePolicy8)
        self.magnet_size.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.magnet_size.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.magnet_size, 2, 2, 1, 1)

        self.magnet_step = QLineEdit(self.gridLayoutWidget_8)
        self.magnet_step.setObjectName(u"magnet_step")
        self.magnet_step.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.magnet_step.sizePolicy().hasHeightForWidth())
        self.magnet_step.setSizePolicy(sizePolicy8)
        self.magnet_step.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.magnet_step.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.magnet_step, 2, 4, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget_8)
        self.label_24.setObjectName(u"label_24")
        sizePolicy9.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy9)
        self.label_24.setFont(font5)
        self.label_24.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_24.setWordWrap(True)
        self.label_24.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_6.addWidget(self.label_24, 1, 2, 1, 1)

        self.frame_19 = QFrame(self.frame_5)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(10, 10, 961, 681))
        self.frame_19.setFrameShape(QFrame.Shape.Box)
        self.frame_19.setFrameShadow(QFrame.Shadow.Plain)
        self.widget_7 = QWidget(self.frame_19)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setGeometry(QRect(10, 10, 941, 661))
        self.gridLayoutWidget_7 = QWidget(self.widget_7)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(-10, -20, 941, 681))
        self.magnet_layout = QGridLayout(self.gridLayoutWidget_7)
        self.magnet_layout.setObjectName(u"magnet_layout")
        self.magnet_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.magnet)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(1000, 60, 801, 251))
        self.frame_6.setFrameShape(QFrame.Shape.Box)
        self.frame_6.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayoutWidget_9 = QWidget(self.frame_6)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(10, 10, 781, 229))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.magnet_position_x = QLineEdit(self.gridLayoutWidget_9)
        self.magnet_position_x.setObjectName(u"magnet_position_x")
        self.magnet_position_x.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.magnet_position_x.sizePolicy().hasHeightForWidth())
        self.magnet_position_x.setSizePolicy(sizePolicy8)
        self.magnet_position_x.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.magnet_position_x.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.magnet_position_x, 4, 1, 1, 1)

        self.magnet_position_y = QLineEdit(self.gridLayoutWidget_9)
        self.magnet_position_y.setObjectName(u"magnet_position_y")
        self.magnet_position_y.setEnabled(False)
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.magnet_position_y.sizePolicy().hasHeightForWidth())
        self.magnet_position_y.setSizePolicy(sizePolicy10)
        self.magnet_position_y.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.magnet_position_y.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.magnet_position_y, 5, 1, 1, 1)

        self.magnet_position_z = QLineEdit(self.gridLayoutWidget_9)
        self.magnet_position_z.setObjectName(u"magnet_position_z")
        self.magnet_position_z.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.magnet_position_z.sizePolicy().hasHeightForWidth())
        self.magnet_position_z.setSizePolicy(sizePolicy8)
        self.magnet_position_z.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.magnet_position_z.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.magnet_position_z, 6, 1, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget_9)
        self.label_27.setObjectName(u"label_27")
        sizePolicy9.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy9)
        self.label_27.setFont(font5)
        self.label_27.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_27.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_27.setWordWrap(True)
        self.label_27.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_7.addWidget(self.label_27, 4, 0, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget_9)
        self.label_28.setObjectName(u"label_28")
        sizePolicy9.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy9)
        self.label_28.setFont(font5)
        self.label_28.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_28.setWordWrap(True)
        self.label_28.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_7.addWidget(self.label_28, 6, 0, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_9)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font5)
        self.label_26.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_26.setWordWrap(True)
        self.label_26.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_7.addWidget(self.label_26, 5, 0, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy9)
        self.label_23.setFont(font5)
        self.label_23.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_23.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_23.setWordWrap(True)
        self.label_23.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_7.addWidget(self.label_23, 3, 1, 1, 1)

        self.magnet_set_position_x = QLineEdit(self.gridLayoutWidget_9)
        self.magnet_set_position_x.setObjectName(u"magnet_set_position_x")
        self.magnet_set_position_x.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.magnet_set_position_x.sizePolicy().hasHeightForWidth())
        self.magnet_set_position_x.setSizePolicy(sizePolicy8)
        self.magnet_set_position_x.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.magnet_set_position_x.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.magnet_set_position_x, 4, 2, 1, 1)

        self.magnet_set_position_y = QLineEdit(self.gridLayoutWidget_9)
        self.magnet_set_position_y.setObjectName(u"magnet_set_position_y")
        self.magnet_set_position_y.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.magnet_set_position_y.sizePolicy().hasHeightForWidth())
        self.magnet_set_position_y.setSizePolicy(sizePolicy8)
        self.magnet_set_position_y.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.magnet_set_position_y.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.magnet_set_position_y, 5, 2, 1, 1)

        self.magnet_set_position_z = QLineEdit(self.gridLayoutWidget_9)
        self.magnet_set_position_z.setObjectName(u"magnet_set_position_z")
        self.magnet_set_position_z.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.magnet_set_position_z.sizePolicy().hasHeightForWidth())
        self.magnet_set_position_z.setSizePolicy(sizePolicy8)
        self.magnet_set_position_z.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.magnet_set_position_z.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_7.addWidget(self.magnet_set_position_z, 6, 2, 1, 1)

        self.magnet_moveto = QPushButton(self.gridLayoutWidget_9)
        self.magnet_moveto.setObjectName(u"magnet_moveto")
        sizePolicy8.setHeightForWidth(self.magnet_moveto.sizePolicy().hasHeightForWidth())
        self.magnet_moveto.setSizePolicy(sizePolicy8)
        self.magnet_moveto.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.magnet_moveto.setIcon(icon9)

        self.gridLayout_7.addWidget(self.magnet_moveto, 3, 2, 1, 1)

        self.frame_7 = QFrame(self.magnet)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(1000, 330, 801, 201))
        self.frame_7.setFrameShape(QFrame.Shape.Box)
        self.frame_7.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayoutWidget_10 = QWidget(self.frame_7)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(10, 80, 781, 111))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.magnet_jog_backward_z = QPushButton(self.gridLayoutWidget_10)
        self.magnet_jog_backward_z.setObjectName(u"magnet_jog_backward_z")
        sizePolicy8.setHeightForWidth(self.magnet_jog_backward_z.sizePolicy().hasHeightForWidth())
        self.magnet_jog_backward_z.setSizePolicy(sizePolicy8)
        self.magnet_jog_backward_z.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/cil-media-step-forward.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.magnet_jog_backward_z.setIcon(icon10)

        self.gridLayout_9.addWidget(self.magnet_jog_backward_z, 2, 2, 1, 1)

        self.magnet_jog_foward_y = QPushButton(self.gridLayoutWidget_10)
        self.magnet_jog_foward_y.setObjectName(u"magnet_jog_foward_y")
        sizePolicy8.setHeightForWidth(self.magnet_jog_foward_y.sizePolicy().hasHeightForWidth())
        self.magnet_jog_foward_y.setSizePolicy(sizePolicy8)
        self.magnet_jog_foward_y.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.magnet_jog_foward_y.setIcon(icon10)

        self.gridLayout_9.addWidget(self.magnet_jog_foward_y, 0, 1, 1, 1)

        self.magnet_jog_backward_x = QPushButton(self.gridLayoutWidget_10)
        self.magnet_jog_backward_x.setObjectName(u"magnet_jog_backward_x")
        sizePolicy8.setHeightForWidth(self.magnet_jog_backward_x.sizePolicy().hasHeightForWidth())
        self.magnet_jog_backward_x.setSizePolicy(sizePolicy8)
        self.magnet_jog_backward_x.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.magnet_jog_backward_x.setIcon(icon10)

        self.gridLayout_9.addWidget(self.magnet_jog_backward_x, 2, 0, 1, 1)

        self.magnet_jog_backward_y = QPushButton(self.gridLayoutWidget_10)
        self.magnet_jog_backward_y.setObjectName(u"magnet_jog_backward_y")
        sizePolicy8.setHeightForWidth(self.magnet_jog_backward_y.sizePolicy().hasHeightForWidth())
        self.magnet_jog_backward_y.setSizePolicy(sizePolicy8)
        self.magnet_jog_backward_y.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.magnet_jog_backward_y.setIcon(icon10)

        self.gridLayout_9.addWidget(self.magnet_jog_backward_y, 2, 1, 1, 1)

        self.magnet_jog_foward_z = QPushButton(self.gridLayoutWidget_10)
        self.magnet_jog_foward_z.setObjectName(u"magnet_jog_foward_z")
        sizePolicy8.setHeightForWidth(self.magnet_jog_foward_z.sizePolicy().hasHeightForWidth())
        self.magnet_jog_foward_z.setSizePolicy(sizePolicy8)
        self.magnet_jog_foward_z.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.magnet_jog_foward_z.setIcon(icon10)

        self.gridLayout_9.addWidget(self.magnet_jog_foward_z, 0, 2, 1, 1)

        self.magnet_jog_foward_x = QPushButton(self.gridLayoutWidget_10)
        self.magnet_jog_foward_x.setObjectName(u"magnet_jog_foward_x")
        sizePolicy8.setHeightForWidth(self.magnet_jog_foward_x.sizePolicy().hasHeightForWidth())
        self.magnet_jog_foward_x.setSizePolicy(sizePolicy8)
        self.magnet_jog_foward_x.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.magnet_jog_foward_x.setIcon(icon10)

        self.gridLayout_9.addWidget(self.magnet_jog_foward_x, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.horizontalLayoutWidget_8 = QWidget(self.frame_7)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 10, 781, 61))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.horizontalLayoutWidget_8)
        self.label_37.setObjectName(u"label_37")
        sizePolicy9.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy9)
        self.label_37.setFont(font5)
        self.label_37.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_37.setWordWrap(True)
        self.label_37.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.horizontalLayout_16.addWidget(self.label_37)

        self.magnet_step_jog = QLineEdit(self.horizontalLayoutWidget_8)
        self.magnet_step_jog.setObjectName(u"magnet_step_jog")
        self.magnet_step_jog.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.magnet_step_jog.sizePolicy().hasHeightForWidth())
        self.magnet_step_jog.setSizePolicy(sizePolicy8)
        self.magnet_step_jog.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.magnet_step_jog.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_16.addWidget(self.magnet_step_jog)

        self.stackedWidget.addWidget(self.magnet)
        self.control = QWidget()
        self.control.setObjectName(u"control")
        self.horizontalLayoutWidget_9 = QWidget(self.control)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 10, 781, 41))
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.horizontalLayoutWidget_9)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font4)
        self.label_38.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.horizontalLayout_17.addWidget(self.label_38)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_17)

        self.control_save = QPushButton(self.horizontalLayoutWidget_9)
        self.control_save.setObjectName(u"control_save")
        sizePolicy1.setHeightForWidth(self.control_save.sizePolicy().hasHeightForWidth())
        self.control_save.setSizePolicy(sizePolicy1)
        self.control_save.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.control_save.setIcon(icon5)

        self.horizontalLayout_17.addWidget(self.control_save)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_28)

        self.control_load = QPushButton(self.horizontalLayoutWidget_9)
        self.control_load.setObjectName(u"control_load")
        sizePolicy1.setHeightForWidth(self.control_load.sizePolicy().hasHeightForWidth())
        self.control_load.setSizePolicy(sizePolicy1)
        self.control_load.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.control_load.setIcon(icon7)

        self.horizontalLayout_17.addWidget(self.control_load)

        self.frame_8 = QFrame(self.control)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(1360, 0, 401, 61))
        self.frame_8.setFrameShape(QFrame.Shape.Box)
        self.frame_8.setFrameShadow(QFrame.Shadow.Plain)
        self.control_type = QComboBox(self.frame_8)
        self.control_type.addItem("")
        self.control_type.addItem("")
        self.control_type.addItem("")
        self.control_type.addItem("")
        self.control_type.addItem("")
        self.control_type.addItem("")
        self.control_type.addItem("")
        self.control_type.addItem("")
        self.control_type.setObjectName(u"control_type")
        self.control_type.setGeometry(QRect(10, 10, 186, 41))
        self.control_type.setMaximumSize(QSize(16777215, 16777211))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI Semibold"])
        font6.setPointSize(16)
        font6.setWeight(QFont.Weight(50))
        font6.setItalic(False)
        self.control_type.setFont(font6)
        self.control_type.setAutoFillBackground(False)
        self.control_type.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"font: 63 16pt \"Segoe UI Semibold\";\n"
"")
        self.control_type.setIconSize(QSize(16, 16))
        self.control_type.setFrame(True)
        self.control_params = QPushButton(self.frame_8)
        self.control_params.setObjectName(u"control_params")
        self.control_params.setGeometry(QRect(210, 10, 181, 41))
        sizePolicy1.setHeightForWidth(self.control_params.sizePolicy().hasHeightForWidth())
        self.control_params.setSizePolicy(sizePolicy1)
        self.control_params.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-settings.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.control_params.setIcon(icon11)
        self.frame_9 = QFrame(self.control)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(10, 70, 651, 211))
        self.frame_9.setFrameShape(QFrame.Shape.Box)
        self.frame_9.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayoutWidget_5 = QWidget(self.frame_9)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 10, 631, 191))
        self.control_autofocus = QVBoxLayout(self.verticalLayoutWidget_5)
        self.control_autofocus.setSpacing(0)
        self.control_autofocus.setObjectName(u"control_autofocus")
        self.control_autofocus.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.control)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(10, 290, 1791, 671))
        self.frame_11.setFrameShape(QFrame.Shape.Box)
        self.frame_11.setFrameShadow(QFrame.Shadow.Plain)
        self.control_average_widget = QWidget(self.frame_11)
        self.control_average_widget.setObjectName(u"control_average_widget")
        self.control_average_widget.setGeometry(QRect(10, -10, 1771, 671))
        self.verticalLayoutWidget_6 = QWidget(self.control_average_widget)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(-80, 20, 1961, 321))
        self.control_average_layout = QVBoxLayout(self.verticalLayoutWidget_6)
        self.control_average_layout.setSpacing(0)
        self.control_average_layout.setObjectName(u"control_average_layout")
        self.control_average_layout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_7 = QWidget(self.control_average_widget)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(-80, 350, 1961, 321))
        self.control_contrast_layout = QVBoxLayout(self.verticalLayoutWidget_7)
        self.control_contrast_layout.setSpacing(0)
        self.control_contrast_layout.setObjectName(u"control_contrast_layout")
        self.control_contrast_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.control)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(670, 70, 1131, 211))
        self.frame_10.setFrameShape(QFrame.Shape.Box)
        self.frame_10.setFrameShadow(QFrame.Shadow.Plain)
        self.gridLayoutWidget_13 = QWidget(self.frame_10)
        self.gridLayoutWidget_13.setObjectName(u"gridLayoutWidget_13")
        self.gridLayoutWidget_13.setGeometry(QRect(10, 10, 1111, 191))
        self.gridLayout_11 = QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_15, 1, 7, 1, 1)

        self.control_start = QPushButton(self.gridLayoutWidget_13)
        self.control_start.setObjectName(u"control_start")
        sizePolicy8.setHeightForWidth(self.control_start.sizePolicy().hasHeightForWidth())
        self.control_start.setSizePolicy(sizePolicy8)
        self.control_start.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.control_start.setIcon(icon4)

        self.gridLayout_11.addWidget(self.control_start, 0, 8, 1, 1)

        self.autofocus_in = QLineEdit(self.gridLayoutWidget_13)
        self.autofocus_in.setObjectName(u"autofocus_in")
        self.autofocus_in.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.autofocus_in.sizePolicy().hasHeightForWidth())
        self.autofocus_in.setSizePolicy(sizePolicy8)
        self.autofocus_in.setMaximumSize(QSize(150, 16777215))
        self.autofocus_in.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.autofocus_in.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.autofocus_in, 1, 6, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_10, 0, 9, 1, 1)

        self.horizontalSpacer_36 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_36, 0, 4, 1, 1)

        self.label_39 = QLabel(self.gridLayoutWidget_13)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy9)
        self.label_39.setFont(font5)
        self.label_39.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_39.setWordWrap(True)
        self.label_39.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_11.addWidget(self.label_39, 0, 5, 1, 1)

        self.label_40 = QLabel(self.gridLayoutWidget_13)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy9)
        self.label_40.setFont(font5)
        self.label_40.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_40.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_40.setWordWrap(True)
        self.label_40.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_11.addWidget(self.label_40, 1, 5, 1, 1)

        self.fit_from = QLineEdit(self.gridLayoutWidget_13)
        self.fit_from.setObjectName(u"fit_from")
        self.fit_from.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.fit_from.sizePolicy().hasHeightForWidth())
        self.fit_from.setSizePolicy(sizePolicy8)
        self.fit_from.setMaximumSize(QSize(150, 16777215))
        self.fit_from.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.fit_from.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.fit_from, 0, 1, 1, 1)

        self.label_42 = QLabel(self.gridLayoutWidget_13)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy9)
        self.label_42.setFont(font5)
        self.label_42.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_42.setWordWrap(True)
        self.label_42.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_11.addWidget(self.label_42, 0, 2, 1, 1)

        self.control_stop = QPushButton(self.gridLayoutWidget_13)
        self.control_stop.setObjectName(u"control_stop")
        sizePolicy1.setHeightForWidth(self.control_stop.sizePolicy().hasHeightForWidth())
        self.control_stop.setSizePolicy(sizePolicy1)
        self.control_stop.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-media-pause.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.control_stop.setIcon(icon12)

        self.gridLayout_11.addWidget(self.control_stop, 1, 8, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_14, 0, 7, 1, 1)

        self.reps = QLineEdit(self.gridLayoutWidget_13)
        self.reps.setObjectName(u"reps")
        self.reps.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.reps.sizePolicy().hasHeightForWidth())
        self.reps.setSizePolicy(sizePolicy1)
        self.reps.setMaximumSize(QSize(150, 16777215))
        self.reps.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.reps.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.reps, 0, 6, 1, 1)

        self.label_41 = QLabel(self.gridLayoutWidget_13)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy9)
        self.label_41.setFont(font5)
        self.label_41.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_41.setWordWrap(True)
        self.label_41.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_11.addWidget(self.label_41, 0, 0, 1, 1)

        self.fit_to = QLineEdit(self.gridLayoutWidget_13)
        self.fit_to.setObjectName(u"fit_to")
        self.fit_to.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.fit_to.sizePolicy().hasHeightForWidth())
        self.fit_to.setSizePolicy(sizePolicy8)
        self.fit_to.setMaximumSize(QSize(150, 16777215))
        self.fit_to.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.fit_to.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.fit_to, 0, 3, 1, 1)

        self.fit_result = QLineEdit(self.gridLayoutWidget_13)
        self.fit_result.setObjectName(u"fit_result")
        self.fit_result.setEnabled(False)
        sizePolicy8.setHeightForWidth(self.fit_result.sizePolicy().hasHeightForWidth())
        self.fit_result.setSizePolicy(sizePolicy8)
        self.fit_result.setMaximumSize(QSize(150, 16777215))
        self.fit_result.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.fit_result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_11.addWidget(self.fit_result, 1, 3, 1, 1)

        self.label_43 = QLabel(self.gridLayoutWidget_13)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy9)
        self.label_43.setFont(font5)
        self.label_43.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_43.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_43.setWordWrap(True)
        self.label_43.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_11.addWidget(self.label_43, 1, 2, 1, 1)

        self.control_fitting = QCheckBox(self.gridLayoutWidget_13)
        self.control_fitting.setObjectName(u"control_fitting")
        self.control_fitting.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")

        self.gridLayout_11.addWidget(self.control_fitting, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.control)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_44 = QLabel(self.page)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(10, 10, 149, 39))
        self.label_44.setFont(font4)
        self.label_44.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.frame_12 = QFrame(self.page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(10, 60, 751, 561))
        self.frame_12.setFrameShape(QFrame.Shape.Box)
        self.frame_12.setFrameShadow(QFrame.Shadow.Plain)
        self.widget_2 = QWidget(self.frame_12)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 10, 731, 541))
        self.verticalLayoutWidget_3 = QWidget(self.widget_2)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 731, 541))
        self.verticalLayout_22 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.pillars = QPlainTextEdit(self.verticalLayoutWidget_3)
        self.pillars.setObjectName(u"pillars")
        self.pillars.setMinimumSize(QSize(200, 200))
        self.pillars.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.verticalLayout_22.addWidget(self.pillars)

        self.frame_15 = QFrame(self.page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(10, 630, 751, 331))
        self.frame_15.setFrameShape(QFrame.Shape.Box)
        self.frame_15.setFrameShadow(QFrame.Shadow.Plain)
        self.widget_3 = QWidget(self.frame_15)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(10, 10, 731, 581))
        self.verticalLayoutWidget_4 = QWidget(self.widget_3)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 0, 731, 311))
        self.sensing_autofocus_layout = QVBoxLayout(self.verticalLayoutWidget_4)
        self.sensing_autofocus_layout.setObjectName(u"sensing_autofocus_layout")
        self.sensing_autofocus_layout.setContentsMargins(0, 0, 0, 0)
        self.label_58 = QLabel(self.frame_15)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(20, 0, 91, 39))
        self.label_58.setFont(font4)
        self.label_58.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.frame_16 = QFrame(self.page)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(770, 60, 1041, 561))
        self.frame_16.setFrameShape(QFrame.Shape.Box)
        self.frame_16.setFrameShadow(QFrame.Shadow.Plain)
        self.label_59 = QLabel(self.frame_16)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(10, 10, 149, 39))
        self.label_59.setFont(font4)
        self.label_59.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.widget_5 = QWidget(self.frame_16)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(10, 10, 1021, 541))
        self.verticalLayoutWidget_8 = QWidget(self.widget_5)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(-80, -110, 1141, 681))
        self.T1_contrast_layout = QVBoxLayout(self.verticalLayoutWidget_8)
        self.T1_contrast_layout.setObjectName(u"T1_contrast_layout")
        self.T1_contrast_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.page)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(770, 630, 1041, 331))
        self.frame_17.setFrameShape(QFrame.Shape.Box)
        self.frame_17.setFrameShadow(QFrame.Shadow.Plain)
        self.widget_4 = QWidget(self.frame_17)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(0, 20, 1031, 311))
        self.gridLayoutWidget_4 = QWidget(self.widget_4)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 30, 1021, 271))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_60 = QLabel(self.gridLayoutWidget_4)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy9)
        self.label_60.setFont(font5)
        self.label_60.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_60.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_60.setWordWrap(True)
        self.label_60.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_8.addWidget(self.label_60, 4, 6, 1, 1)

        self.label_53 = QLabel(self.gridLayoutWidget_4)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy9)
        self.label_53.setFont(font5)
        self.label_53.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_53.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_53.setWordWrap(True)
        self.label_53.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_8.addWidget(self.label_53, 5, 0, 1, 1)

        self.label_56 = QLabel(self.gridLayoutWidget_4)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy9)
        self.label_56.setFont(font5)
        self.label_56.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_56.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_56.setWordWrap(True)
        self.label_56.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_8.addWidget(self.label_56, 4, 5, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.left_down_x = QLineEdit(self.gridLayoutWidget_4)
        self.left_down_x.setObjectName(u"left_down_x")
        self.left_down_x.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.left_down_x.sizePolicy().hasHeightForWidth())
        self.left_down_x.setSizePolicy(sizePolicy1)
        self.left_down_x.setMaximumSize(QSize(150, 16777215))
        self.left_down_x.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.left_down_x.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.left_down_x, 1, 1, 1, 1)

        self.label_49 = QLabel(self.gridLayoutWidget_4)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy9)
        self.label_49.setFont(font5)
        self.label_49.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_49.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_49.setWordWrap(True)
        self.label_49.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_8.addWidget(self.label_49, 2, 0, 1, 1)

        self.label_47 = QLabel(self.gridLayoutWidget_4)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy9)
        self.label_47.setFont(font5)
        self.label_47.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_47.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_47.setWordWrap(True)
        self.label_47.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_8.addWidget(self.label_47, 0, 6, 1, 1)

        self.label_45 = QLabel(self.gridLayoutWidget_4)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy9)
        self.label_45.setFont(font5)
        self.label_45.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_45.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_45.setWordWrap(True)
        self.label_45.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_8.addWidget(self.label_45, 1, 0, 1, 1)

        self.sensing_pi = QLineEdit(self.gridLayoutWidget_4)
        self.sensing_pi.setObjectName(u"sensing_pi")
        self.sensing_pi.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.sensing_pi.sizePolicy().hasHeightForWidth())
        self.sensing_pi.setSizePolicy(sizePolicy1)
        self.sensing_pi.setMaximumSize(QSize(150, 16777215))
        self.sensing_pi.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.sensing_pi.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.sensing_pi, 5, 2, 1, 1)

        self.label_55 = QLabel(self.gridLayoutWidget_4)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy9)
        self.label_55.setFont(font5)
        self.label_55.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_55.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_55.setWordWrap(True)
        self.label_55.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_8.addWidget(self.label_55, 4, 2, 1, 1)

        self.label_54 = QLabel(self.gridLayoutWidget_4)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy9)
        self.label_54.setFont(font5)
        self.label_54.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_54.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_54.setWordWrap(True)
        self.label_54.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_8.addWidget(self.label_54, 1, 5, 1, 1)

        self.right_down_y = QLineEdit(self.gridLayoutWidget_4)
        self.right_down_y.setObjectName(u"right_down_y")
        self.right_down_y.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.right_down_y.sizePolicy().hasHeightForWidth())
        self.right_down_y.setSizePolicy(sizePolicy1)
        self.right_down_y.setMaximumSize(QSize(150, 16777215))
        self.right_down_y.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.right_down_y.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.right_down_y, 2, 2, 1, 1)

        self.bins_x = QLineEdit(self.gridLayoutWidget_4)
        self.bins_x.setObjectName(u"bins_x")
        self.bins_x.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.bins_x.sizePolicy().hasHeightForWidth())
        self.bins_x.setSizePolicy(sizePolicy1)
        self.bins_x.setMaximumSize(QSize(150, 16777215))
        self.bins_x.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.bins_x.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.bins_x, 1, 6, 1, 1)

        self.start_x = QLineEdit(self.gridLayoutWidget_4)
        self.start_x.setObjectName(u"start_x")
        self.start_x.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.start_x.sizePolicy().hasHeightForWidth())
        self.start_x.setSizePolicy(sizePolicy1)
        self.start_x.setMaximumSize(QSize(150, 16777215))
        self.start_x.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.start_x.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.start_x, 2, 6, 1, 1)

        self.bins_y = QLineEdit(self.gridLayoutWidget_4)
        self.bins_y.setObjectName(u"bins_y")
        self.bins_y.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.bins_y.sizePolicy().hasHeightForWidth())
        self.bins_y.setSizePolicy(sizePolicy1)
        self.bins_y.setMaximumSize(QSize(150, 16777215))
        self.bins_y.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.bins_y.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.bins_y, 1, 7, 1, 1)

        self.label_52 = QLabel(self.gridLayoutWidget_4)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy9)
        self.label_52.setFont(font5)
        self.label_52.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_52.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_52.setWordWrap(True)
        self.label_52.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_8.addWidget(self.label_52, 4, 1, 1, 1)

        self.sensing_tau = QLineEdit(self.gridLayoutWidget_4)
        self.sensing_tau.setObjectName(u"sensing_tau")
        self.sensing_tau.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.sensing_tau.sizePolicy().hasHeightForWidth())
        self.sensing_tau.setSizePolicy(sizePolicy1)
        self.sensing_tau.setMaximumSize(QSize(150, 16777215))
        self.sensing_tau.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.sensing_tau.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.sensing_tau, 5, 5, 1, 1)

        self.sensing_rf = QLineEdit(self.gridLayoutWidget_4)
        self.sensing_rf.setObjectName(u"sensing_rf")
        self.sensing_rf.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.sensing_rf.sizePolicy().hasHeightForWidth())
        self.sensing_rf.setSizePolicy(sizePolicy1)
        self.sensing_rf.setMaximumSize(QSize(150, 16777215))
        self.sensing_rf.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.sensing_rf.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.sensing_rf, 5, 1, 1, 1)

        self.left_down_y = QLineEdit(self.gridLayoutWidget_4)
        self.left_down_y.setObjectName(u"left_down_y")
        self.left_down_y.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.left_down_y.sizePolicy().hasHeightForWidth())
        self.left_down_y.setSizePolicy(sizePolicy1)
        self.left_down_y.setMaximumSize(QSize(150, 16777215))
        self.left_down_y.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.left_down_y.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.left_down_y, 1, 2, 1, 1)

        self.label_46 = QLabel(self.gridLayoutWidget_4)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_46.sizePolicy().hasHeightForWidth())
        self.label_46.setSizePolicy(sizePolicy9)
        self.label_46.setFont(font5)
        self.label_46.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_46.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_46.setWordWrap(True)
        self.label_46.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_8.addWidget(self.label_46, 0, 1, 1, 1)

        self.start_y = QLineEdit(self.gridLayoutWidget_4)
        self.start_y.setObjectName(u"start_y")
        self.start_y.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.start_y.sizePolicy().hasHeightForWidth())
        self.start_y.setSizePolicy(sizePolicy1)
        self.start_y.setMaximumSize(QSize(150, 16777215))
        self.start_y.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.start_y.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.start_y, 2, 7, 1, 1)

        self.right_down_x = QLineEdit(self.gridLayoutWidget_4)
        self.right_down_x.setObjectName(u"right_down_x")
        self.right_down_x.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.right_down_x.sizePolicy().hasHeightForWidth())
        self.right_down_x.setSizePolicy(sizePolicy1)
        self.right_down_x.setMaximumSize(QSize(150, 16777215))
        self.right_down_x.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.right_down_x.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.right_down_x, 2, 1, 1, 1)

        self.label_50 = QLabel(self.gridLayoutWidget_4)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy9)
        self.label_50.setFont(font5)
        self.label_50.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_50.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_50.setWordWrap(True)
        self.label_50.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_8.addWidget(self.label_50, 0, 7, 1, 1)

        self.label_48 = QLabel(self.gridLayoutWidget_4)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy9)
        self.label_48.setFont(font5)
        self.label_48.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_48.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_48.setWordWrap(True)
        self.label_48.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_8.addWidget(self.label_48, 0, 2, 1, 1)

        self.label_57 = QLabel(self.gridLayoutWidget_4)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy9)
        self.label_57.setFont(font5)
        self.label_57.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_57.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_57.setWordWrap(True)
        self.label_57.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_8.addWidget(self.label_57, 2, 5, 1, 1)

        self.sensing_iteration = QLineEdit(self.gridLayoutWidget_4)
        self.sensing_iteration.setObjectName(u"sensing_iteration")
        self.sensing_iteration.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.sensing_iteration.sizePolicy().hasHeightForWidth())
        self.sensing_iteration.setSizePolicy(sizePolicy1)
        self.sensing_iteration.setMaximumSize(QSize(150, 16777215))
        self.sensing_iteration.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.sensing_iteration.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.sensing_iteration, 5, 6, 1, 1)

        self.label_61 = QLabel(self.gridLayoutWidget_4)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy9)
        self.label_61.setFont(font5)
        self.label_61.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_61.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_61.setWordWrap(True)
        self.label_61.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.gridLayout_8.addWidget(self.label_61, 4, 7, 1, 1)

        self.sensing_reps_2 = QLineEdit(self.gridLayoutWidget_4)
        self.sensing_reps_2.setObjectName(u"sensing_reps_2")
        self.sensing_reps_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.sensing_reps_2.sizePolicy().hasHeightForWidth())
        self.sensing_reps_2.setSizePolicy(sizePolicy1)
        self.sensing_reps_2.setMaximumSize(QSize(150, 16777215))
        self.sensing_reps_2.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.sensing_reps_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_8.addWidget(self.sensing_reps_2, 5, 7, 1, 1)

        self.label_51 = QLabel(self.widget_4)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(20, -10, 149, 39))
        self.label_51.setFont(font4)
        self.label_51.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.horizontalLayoutWidget_12 = QWidget(self.frame_17)
        self.horizontalLayoutWidget_12.setObjectName(u"horizontalLayoutWidget_12")
        self.horizontalLayoutWidget_12.setGeometry(QRect(610, 10, 411, 41))
        self.horizontalLayout_20 = QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.sensing_start = QPushButton(self.horizontalLayoutWidget_12)
        self.sensing_start.setObjectName(u"sensing_start")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.sensing_start.sizePolicy().hasHeightForWidth())
        self.sensing_start.setSizePolicy(sizePolicy11)
        self.sensing_start.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.sensing_start.setIcon(icon4)

        self.horizontalLayout_20.addWidget(self.sensing_start)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_2)

        self.sensing_pause = QPushButton(self.horizontalLayoutWidget_12)
        self.sensing_pause.setObjectName(u"sensing_pause")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.sensing_pause.sizePolicy().hasHeightForWidth())
        self.sensing_pause.setSizePolicy(sizePolicy12)
        self.sensing_pause.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.sensing_pause.setIcon(icon12)

        self.horizontalLayout_20.addWidget(self.sensing_pause)

        self.stackedWidget.addWidget(self.page)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton.setIcon(icon7)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy1.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy1)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon13 = QIcon()
        icon13.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.commandLinkButton.setIcon(icon13)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font7);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy13)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.Shape.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setBold(False)
        font8.setItalic(False)
        self.creditsLabel.setFont(font8)
        self.creditsLabel.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_counter.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.btn_confocal.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_magnet.setText(QCoreApplication.translate("MainWindow", u"Widgets", None))
        self.btn_control.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
        self.extraLabel.setText(QCoreApplication.translate("MainWindow", u"Left Box", None))
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close left box", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_adjustments.setText(QCoreApplication.translate("MainWindow", u"Adjustments", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">An interface created using Python and PySide (support for PyQt), and with colors based on the Dracula theme created by Zen"
                        "o Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-in"
                        "dent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
        self.titleRightInfo.setText("")
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Counter", None))
        self.counter_counts.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Average counts (kcps)", None))
        self.counter_standard_deviation.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Current counts (kcps)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Standrad deviation", None))
        self.counter_average_counts.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.counter_laser_power_2.setText(QCoreApplication.translate("MainWindow", u"Laser power (a.u.)", None))
        self.counter_laser_power.setText(QCoreApplication.translate("MainWindow", u"35000", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Trace length (sec)", None))
        self.counter_trace_length.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Per second (sec)", None))
        self.counter_T_per_sec.setText(QCoreApplication.translate("MainWindow", u"0.05", None))
        self.counter_start.setText(QCoreApplication.translate("MainWindow", u" Start", None))
        self.counter_save.setText(QCoreApplication.translate("MainWindow", u" Save", None))
        self.counter_laser_on.setText(QCoreApplication.translate("MainWindow", u" Laser off", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Confocal", None))
        self.confocal_save.setText(QCoreApplication.translate("MainWindow", u" Save image", None))
        self.confocal_load.setText(QCoreApplication.translate("MainWindow", u" Load image", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.confocal_resolution.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Per point (sec)", None))
        self.confocal_T_per_point.setText(QCoreApplication.translate("MainWindow", u"0.01", None))
        self.confocal_home.setText(QCoreApplication.translate("MainWindow", u" Home", None))
        self.confocal_start.setText(QCoreApplication.translate("MainWindow", u" Start", None))
        self.x_fix.setText(QCoreApplication.translate("MainWindow", u"x axis", None))
        self.confocal_to_x.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.confocal_set_position_x.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.confocal_from_x.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.z_fix.setText(QCoreApplication.translate("MainWindow", u"z axis", None))
        self.confocal_position_x.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>From (\u03bcm)</p></body></html>", None))
        self.confocal_from_z.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.confocal_position_z.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.confocal_set_position_z.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.y_fix.setText(QCoreApplication.translate("MainWindow", u"y axis", None))
        self.confocal_set_position_y.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Axis fix", None))
        self.confocal_to_z.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.confocal_position_y.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"To (\u03bcm)", None))
        self.confocal_from_y.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.confocal_to_y.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.confocal_moveto.setText(QCoreApplication.translate("MainWindow", u" Move to ", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Counts (kcps)", None))
        self.confocal_counts.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.autofocus_size_z.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Size (\u03bcm)", None))
        self.confocal_step_z.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"x axis", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"z axis", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Step (\u03bcm)", None))
        self.confocal_step_xy.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.autofocus_size_xy.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.autofocus_01.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.autofocus_005.setText(QCoreApplication.translate("MainWindow", u"0.05", None))
        self.autofocus_001.setText(QCoreApplication.translate("MainWindow", u"0.01", None))
        self.autofocus_start.setText(QCoreApplication.translate("MainWindow", u" Start", None))
        self.autofocus_save.setText(QCoreApplication.translate("MainWindow", u" Save", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Magnetic field alignment", None))
        self.magnet_save_2.setText(QCoreApplication.translate("MainWindow", u" Save image", None))
        self.magnet_load.setText(QCoreApplication.translate("MainWindow", u" Load image", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Counts (kcps)", None))
        self.magnet_counts.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Per point (sec)", None))
        self.magnet_per_point.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.magnet_start.setText(QCoreApplication.translate("MainWindow", u" Start", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Step (mm)", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"xy axis", None))
        self.magnet_size.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.magnet_step.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Size (mm)", None))
        self.magnet_position_x.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.magnet_position_y.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.magnet_position_z.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"x (mm)", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"z (mm)", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"y (mm)", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Current position", None))
        self.magnet_set_position_x.setText("")
        self.magnet_set_position_y.setText("")
        self.magnet_set_position_z.setText("")
        self.magnet_moveto.setText(QCoreApplication.translate("MainWindow", u" Move to", None))
        self.magnet_jog_backward_z.setText(QCoreApplication.translate("MainWindow", u" Jog backward z", None))
        self.magnet_jog_foward_y.setText(QCoreApplication.translate("MainWindow", u" Jog foward y", None))
        self.magnet_jog_backward_x.setText(QCoreApplication.translate("MainWindow", u" Jog backward x", None))
        self.magnet_jog_backward_y.setText(QCoreApplication.translate("MainWindow", u" Jog backward y", None))
        self.magnet_jog_foward_z.setText(QCoreApplication.translate("MainWindow", u" Jog foward z", None))
        self.magnet_jog_foward_x.setText(QCoreApplication.translate("MainWindow", u" Jog foward x", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Step (mm)", None))
        self.magnet_step_jog.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Spin control", None))
        self.control_save.setText(QCoreApplication.translate("MainWindow", u" Save results", None))
        self.control_load.setText(QCoreApplication.translate("MainWindow", u" Load results", None))
        self.control_type.setItemText(0, QCoreApplication.translate("MainWindow", u"ODMR", None))
        self.control_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Rabi", None))
        self.control_type.setItemText(2, QCoreApplication.translate("MainWindow", u"PODMR", None))
        self.control_type.setItemText(3, QCoreApplication.translate("MainWindow", u"Ramsey", None))
        self.control_type.setItemText(4, QCoreApplication.translate("MainWindow", u"XY16", None))
        self.control_type.setItemText(5, QCoreApplication.translate("MainWindow", u"T1", None))
        self.control_type.setItemText(6, QCoreApplication.translate("MainWindow", u"C13_Rabi", None))
        self.control_type.setItemText(7, "")

        self.control_params.setText(QCoreApplication.translate("MainWindow", u" Parameters", None))
        self.control_start.setText(QCoreApplication.translate("MainWindow", u" Start", None))
        self.autofocus_in.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Current reps", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Autofocus in", None))
        self.fit_from.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.control_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.reps.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.fit_to.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.fit_result.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Resonance frequency", None))
        self.control_fitting.setText(QCoreApplication.translate("MainWindow", u"Fitting", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"T1 Sensing", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Autofocus</span></p></body></html>", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">T1 contrast</span></p></body></html>", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"iterations", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"MW settings", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"tau (us)", None))
        self.left_down_x.setText(QCoreApplication.translate("MainWindow", u"141.9", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Right down pillar", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Left down pillar", None))
        self.sensing_pi.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Pi pulse (ns)", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Bins", None))
        self.right_down_y.setText(QCoreApplication.translate("MainWindow", u"69.8", None))
        self.bins_x.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.start_x.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bins_y.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"frequency (MHz)", None))
        self.sensing_tau.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.sensing_rf.setText(QCoreApplication.translate("MainWindow", u"2870", None))
        self.left_down_y.setText(QCoreApplication.translate("MainWindow", u"69.8", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"x pos", None))
        self.start_y.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.right_down_x.setText(QCoreApplication.translate("MainWindow", u"146", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"y pos", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.sensing_iteration.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Soc internal reps", None))
        self.sensing_reps_2.setText(QCoreApplication.translate("MainWindow", u"25000", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Settings</span></p></body></html>", None))
        self.sensing_start.setText(QCoreApplication.translate("MainWindow", u" Start", None))
        self.sensing_pause.setText(QCoreApplication.translate("MainWindow", u" Pause", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: \ud06c\uc655\ubb34\uc12d\uc9d5", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v 1.0", None))
    # retranslateUi

