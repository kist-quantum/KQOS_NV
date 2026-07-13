# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'jp_edit_main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
        MainWindow.resize(2110, 1239)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
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
"	\n"
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
"	background-color: rgb(40, 44, 52);"
                        "\n"
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
"	background-color: rgb(189, 147, 249);\n"
"	color"
                        ": rgb(255, 255, 255);\n"
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
"	background-color: rgb(189, 147, 249);\n"
"}\n"
""
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
"	border-top: 3px solid rgb(40, 44"
                        ", 52);\n"
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
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: "
                        "4px; }\n"
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
"	color: rgb(255, 255, 255);\n"
"}\n"
""
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
"	background-color: rgb(33, 37, 43);\n"
"	"
                        "padding: 3px;\n"
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
"	selection-background-color: rgb(255, 121, 198);\n"
""
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
"QScrollBar::sub-line:horizon"
                        "tal {\n"
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
"     subcontrol-origin: margin;\n"
""
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
"	background-image: url(:/icons/ima"
                        "ges/icons/cil-check-alt.png);\n"
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
"	subcontrol-position: top right;\n"
""
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
"    height: 10px;\n"
"    width: 10p"
                        "x;\n"
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
"QCommandLinkButton {	\n"
"	color: rgb(255"
                        ", 121, 198);\n"
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
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 0, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
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

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy1)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.topMenu.sizePolicy().hasHeightForWidth())
        self.topMenu.setSizePolicy(sizePolicy2)
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_1_confocal = QPushButton(self.topMenu)
        self.btn_1_confocal.setObjectName(u"btn_1_confocal")
        sizePolicy1.setHeightForWidth(self.btn_1_confocal.sizePolicy().hasHeightForWidth())
        self.btn_1_confocal.setSizePolicy(sizePolicy1)
        self.btn_1_confocal.setMinimumSize(QSize(0, 43))
        self.btn_1_confocal.setMaximumSize(QSize(16777215, 16777215))
        self.btn_1_confocal.setFont(font)
        self.btn_1_confocal.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_1_confocal.setLayoutDirection(Qt.LeftToRight)
        self.btn_1_confocal.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-magnifying-glass.png);")

        self.verticalLayout_8.addWidget(self.btn_1_confocal)

        self.btn_2_magnet = QPushButton(self.topMenu)
        self.btn_2_magnet.setObjectName(u"btn_2_magnet")
        sizePolicy1.setHeightForWidth(self.btn_2_magnet.sizePolicy().hasHeightForWidth())
        self.btn_2_magnet.setSizePolicy(sizePolicy1)
        self.btn_2_magnet.setMinimumSize(QSize(0, 45))
        self.btn_2_magnet.setFont(font)
        self.btn_2_magnet.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_2_magnet.setLayoutDirection(Qt.LeftToRight)
        self.btn_2_magnet.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-transfer.png);")

        self.verticalLayout_8.addWidget(self.btn_2_magnet)

        self.btn_3_control = QPushButton(self.topMenu)
        self.btn_3_control.setObjectName(u"btn_3_control")
        sizePolicy1.setHeightForWidth(self.btn_3_control.sizePolicy().hasHeightForWidth())
        self.btn_3_control.setSizePolicy(sizePolicy1)
        self.btn_3_control.setMinimumSize(QSize(0, 45))
        self.btn_3_control.setFont(font)
        self.btn_3_control.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_3_control.setLayoutDirection(Qt.LeftToRight)
        self.btn_3_control.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-loop-circular.png);")

        self.verticalLayout_8.addWidget(self.btn_3_control)

        self.btn_4_PLE = QPushButton(self.topMenu)
        self.btn_4_PLE.setObjectName(u"btn_4_PLE")
        sizePolicy1.setHeightForWidth(self.btn_4_PLE.sizePolicy().hasHeightForWidth())
        self.btn_4_PLE.setSizePolicy(sizePolicy1)
        self.btn_4_PLE.setMinimumSize(QSize(0, 45))
        self.btn_4_PLE.setFont(font)
        self.btn_4_PLE.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_4_PLE.setLayoutDirection(Qt.LeftToRight)
        self.btn_4_PLE.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-signal-cellular-3.png);")

        self.verticalLayout_8.addWidget(self.btn_4_PLE)

        self.btn_5_entangle = QPushButton(self.topMenu)
        self.btn_5_entangle.setObjectName(u"btn_5_entangle")
        sizePolicy1.setHeightForWidth(self.btn_5_entangle.sizePolicy().hasHeightForWidth())
        self.btn_5_entangle.setSizePolicy(sizePolicy1)
        self.btn_5_entangle.setMinimumSize(QSize(0, 45))
        self.btn_5_entangle.setFont(font)
        self.btn_5_entangle.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_5_entangle.setLayoutDirection(Qt.LeftToRight)
        self.btn_5_entangle.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-infinity.png)")

        self.verticalLayout_8.addWidget(self.btn_5_entangle)

        self.btn_6_T1 = QPushButton(self.topMenu)
        self.btn_6_T1.setObjectName(u"btn_6_T1")
        sizePolicy1.setHeightForWidth(self.btn_6_T1.sizePolicy().hasHeightForWidth())
        self.btn_6_T1.setSizePolicy(sizePolicy1)
        self.btn_6_T1.setMinimumSize(QSize(0, 45))
        self.btn_6_T1.setFont(font)
        self.btn_6_T1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_6_T1.setLayoutDirection(Qt.LeftToRight)
        self.btn_6_T1.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-rss.png);")

        self.verticalLayout_8.addWidget(self.btn_6_T1)


        self.verticalMenuLayout.addWidget(self.topMenu)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
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
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
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
        self.extraIcon.setFrameShape(QFrame.NoFrame)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setMinimumSize(QSize(0, 0))
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setMinimumSize(QSize(0, 0))
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
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
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-share-boxed.png);")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_adjustments = QPushButton(self.extraTopMenu)
        self.btn_adjustments.setObjectName(u"btn_adjustments")
        sizePolicy1.setHeightForWidth(self.btn_adjustments.sizePolicy().hasHeightForWidth())
        self.btn_adjustments.setSizePolicy(sizePolicy1)
        self.btn_adjustments.setMinimumSize(QSize(0, 45))
        self.btn_adjustments.setFont(font)
        self.btn_adjustments.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adjustments.setLayoutDirection(Qt.LeftToRight)
        self.btn_adjustments.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_11.addWidget(self.btn_adjustments)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy1.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy1)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-layers.png);")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setMinimumSize(QSize(0, 0))
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.textEdit = QTextEdit(self.extraCenter)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(222, 0))
        self.textEdit.setStyleSheet(u"background: transparent;")
        self.textEdit.setFrameShape(QFrame.NoFrame)
        self.textEdit.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.textEdit)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy3)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy4)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon1)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
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
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setIcon(icon)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
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
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy1.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy1)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy1.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy1)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)

        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(100)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy5)
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.confocal = QWidget()
        self.confocal.setObjectName(u"confocal")
        self.verticalLayout_20 = QVBoxLayout(self.confocal)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget = QWidget(self.confocal)
        self.widget.setObjectName(u"widget")
        self.horizontalLayoutWidget_2 = QWidget(self.widget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 0, 981, 56))
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.horizontalLayoutWidget_2)
        self.label_19.setObjectName(u"label_19")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Semibold"])
        font4.setPointSize(20)
        font4.setBold(False)
        font4.setItalic(False)
        self.label_19.setFont(font4)
        self.label_19.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.horizontalLayout_7.addWidget(self.label_19)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.radioButto__CW_PSB = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButto__CW_PSB.setObjectName(u"radioButto__CW_PSB")
        self.radioButto__CW_PSB.setStyleSheet(u"")
        self.radioButto__CW_PSB.setChecked(True)

        self.horizontalLayout_7.addWidget(self.radioButto__CW_PSB)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_25)

        self.radioButton_CW_ZPL = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_CW_ZPL.setObjectName(u"radioButton_CW_ZPL")
        self.radioButton_CW_ZPL.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.radioButton_CW_ZPL)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_13)

        self.radioButton_PUL_PSB_GR = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_PUL_PSB_GR.setObjectName(u"radioButton_PUL_PSB_GR")
        self.radioButton_PUL_PSB_GR.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.radioButton_PUL_PSB_GR)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_28)

        self.radioButton_PUL_ZPL_GR = QRadioButton(self.horizontalLayoutWidget_2)
        self.radioButton_PUL_ZPL_GR.setObjectName(u"radioButton_PUL_ZPL_GR")
        self.radioButton_PUL_ZPL_GR.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.radioButton_PUL_ZPL_GR)

        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 70, 981, 921))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.horizontalLayoutWidget = QWidget(self.frame_4)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 620, 891, 62))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI Semibold"])
        font5.setPointSize(15)
        font5.setBold(False)
        font5.setItalic(False)
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_11.setWordWrap(True)
        self.label_11.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.confocal_resolution = QLineEdit(self.horizontalLayoutWidget)
        self.confocal_resolution.setObjectName(u"confocal_resolution")
        self.confocal_resolution.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(20)
        sizePolicy6.setHeightForWidth(self.confocal_resolution.sizePolicy().hasHeightForWidth())
        self.confocal_resolution.setSizePolicy(sizePolicy6)
        self.confocal_resolution.setMaximumSize(QSize(100, 16777215))
        self.confocal_resolution.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.horizontalLayout_6.addWidget(self.confocal_resolution)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_12)

        self.label_29 = QLabel(self.horizontalLayoutWidget)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font5)
        self.label_29.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_29.setWordWrap(True)
        self.label_29.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_6.addWidget(self.label_29)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_19)

        self.confocal_T_per_point = QLineEdit(self.horizontalLayoutWidget)
        self.confocal_T_per_point.setObjectName(u"confocal_T_per_point")
        self.confocal_T_per_point.setEnabled(True)
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(200)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.confocal_T_per_point.sizePolicy().hasHeightForWidth())
        self.confocal_T_per_point.setSizePolicy(sizePolicy7)
        self.confocal_T_per_point.setMaximumSize(QSize(100, 16777215))
        self.confocal_T_per_point.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.horizontalLayout_6.addWidget(self.confocal_T_per_point)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_26)

        self.confocal_home = QPushButton(self.horizontalLayoutWidget)
        self.confocal_home.setObjectName(u"confocal_home")
        sizePolicy1.setHeightForWidth(self.confocal_home.sizePolicy().hasHeightForWidth())
        self.confocal_home.setSizePolicy(sizePolicy1)
        self.confocal_home.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.confocal_home.setIcon(icon4)

        self.horizontalLayout_6.addWidget(self.confocal_home)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.confocal_start = QPushButton(self.horizontalLayoutWidget)
        self.confocal_start.setObjectName(u"confocal_start")
        sizePolicy1.setHeightForWidth(self.confocal_start.sizePolicy().hasHeightForWidth())
        self.confocal_start.setSizePolicy(sizePolicy1)
        self.confocal_start.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.confocal_start.setIcon(icon5)

        self.horizontalLayout_6.addWidget(self.confocal_start)

        self.gridLayoutWidget_3 = QWidget(self.frame_4)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 690, 861, 191))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 0, 3, 1, 1)

        self.x_fix = QCheckBox(self.gridLayoutWidget_3)
        self.x_fix.setObjectName(u"x_fix")
        self.x_fix.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")

        self.gridLayout_3.addWidget(self.x_fix, 1, 0, 1, 1)

        self.confocal_to_x = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_to_x.setObjectName(u"confocal_to_x")
        self.confocal_to_x.setEnabled(True)
        self.confocal_to_x.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_3.addWidget(self.confocal_to_x, 1, 8, 1, 1)

        self.confocal_set_position_x = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_set_position_x.setObjectName(u"confocal_set_position_x")
        self.confocal_set_position_x.setEnabled(True)
        self.confocal_set_position_x.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_3.addWidget(self.confocal_set_position_x, 1, 4, 1, 1)

        self.confocal_from_x = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_from_x.setObjectName(u"confocal_from_x")
        self.confocal_from_x.setEnabled(True)
        self.confocal_from_x.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_3.addWidget(self.confocal_from_x, 1, 6, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

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

        self.gridLayout_3.addWidget(self.confocal_position_x, 1, 2, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font5)
        self.label_12.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_12.setWordWrap(True)
        self.label_12.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_3.addWidget(self.label_12, 0, 6, 1, 1)

        self.confocal_from_z = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_from_z.setObjectName(u"confocal_from_z")
        self.confocal_from_z.setEnabled(True)
        self.confocal_from_z.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_3.addWidget(self.confocal_from_z, 3, 6, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 0, 7, 1, 1)

        self.confocal_position_z = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_position_z.setObjectName(u"confocal_position_z")
        self.confocal_position_z.setEnabled(False)
        self.confocal_position_z.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_3.addWidget(self.confocal_position_z, 3, 2, 1, 1)

        self.confocal_set_position_z = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_set_position_z.setObjectName(u"confocal_set_position_z")
        self.confocal_set_position_z.setEnabled(True)
        self.confocal_set_position_z.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_3.addWidget(self.confocal_set_position_z, 3, 4, 1, 1)

        self.y_fix = QCheckBox(self.gridLayoutWidget_3)
        self.y_fix.setObjectName(u"y_fix")
        self.y_fix.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")

        self.gridLayout_3.addWidget(self.y_fix, 2, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 0, 5, 1, 1)

        self.confocal_set_position_y = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_set_position_y.setObjectName(u"confocal_set_position_y")
        self.confocal_set_position_y.setEnabled(True)
        self.confocal_set_position_y.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_3.addWidget(self.confocal_set_position_y, 2, 4, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_9.setWordWrap(True)
        self.label_9.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_3.addWidget(self.label_9, 0, 2, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_8.setWordWrap(True)
        self.label_8.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)

        self.confocal_to_z = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_to_z.setObjectName(u"confocal_to_z")
        self.confocal_to_z.setEnabled(True)
        self.confocal_to_z.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_3.addWidget(self.confocal_to_z, 3, 8, 1, 1)

        self.confocal_position_y = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_position_y.setObjectName(u"confocal_position_y")
        self.confocal_position_y.setEnabled(False)
        self.confocal_position_y.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_3.addWidget(self.confocal_position_y, 2, 2, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font5)
        self.label_13.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_13.setWordWrap(True)
        self.label_13.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_3.addWidget(self.label_13, 0, 8, 1, 1)

        self.confocal_from_y = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_from_y.setObjectName(u"confocal_from_y")
        self.confocal_from_y.setEnabled(True)
        self.confocal_from_y.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_3.addWidget(self.confocal_from_y, 2, 6, 1, 1)

        self.confocal_to_y = QLineEdit(self.gridLayoutWidget_3)
        self.confocal_to_y.setObjectName(u"confocal_to_y")
        self.confocal_to_y.setEnabled(True)
        self.confocal_to_y.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_3.addWidget(self.confocal_to_y, 2, 8, 1, 1)

        self.confocal_moveto = QPushButton(self.gridLayoutWidget_3)
        self.confocal_moveto.setObjectName(u"confocal_moveto")
        sizePolicy1.setHeightForWidth(self.confocal_moveto.sizePolicy().hasHeightForWidth())
        self.confocal_moveto.setSizePolicy(sizePolicy1)
        self.confocal_moveto.setLayoutDirection(Qt.LeftToRight)
        self.confocal_moveto.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/icons/cil-arrow-circle-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.confocal_moveto.setIcon(icon6)

        self.gridLayout_3.addWidget(self.confocal_moveto, 0, 4, 1, 1)

        self.frame_13 = QFrame(self.frame_4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(0, 10, 961, 601))
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.widget_6 = QWidget(self.frame_13)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(10, -10, 681, 581))
        self.verticalLayoutWidget_9 = QWidget(self.widget_6)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(10, 10, 661, 561))
        self.confocal_layout = QVBoxLayout(self.verticalLayoutWidget_9)
        self.confocal_layout.setObjectName(u"confocal_layout")
        self.confocal_layout.setContentsMargins(0, 0, 0, 0)
        self.confocal_widget = QWidget(self.frame_13)
        self.confocal_widget.setObjectName(u"confocal_widget")
        self.confocal_widget.setGeometry(QRect(780, -10, 151, 451))
        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(690, 460, 171, 101))
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.verticalLayoutWidget_10 = QWidget(self.frame_18)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(10, 10, 151, 81))
        self.verticalLayout_23 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.verticalLayoutWidget_10)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font5)
        self.label_18.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_18.setWordWrap(True)
        self.label_18.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_23.addWidget(self.label_18)

        self.confocal_counts = QLineEdit(self.verticalLayoutWidget_10)
        self.confocal_counts.setObjectName(u"confocal_counts")
        self.confocal_counts.setEnabled(False)
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(18)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.confocal_counts.sizePolicy().hasHeightForWidth())
        self.confocal_counts.setSizePolicy(sizePolicy8)
        self.confocal_counts.setMaximumSize(QSize(200, 16777215))
        self.confocal_counts.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.verticalLayout_23.addWidget(self.confocal_counts)

        self.horizontalLayoutWidget_10 = QWidget(self.frame_13)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(700, 0, 151, 461))
        self.horizontalLayout_18 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalSlider_2 = QSlider(self.horizontalLayoutWidget_10)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setStyleSheet(u"")

        self.horizontalLayout_18.addWidget(self.verticalSlider_2)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(990, 0, 971, 1041))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.gridLayoutWidget_6 = QWidget(self.frame)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(80, 870, 781, 151))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.autofocus_size_z = QLineEdit(self.gridLayoutWidget_6)
        self.autofocus_size_z.setObjectName(u"autofocus_size_z")
        self.autofocus_size_z.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.autofocus_size_z.sizePolicy().hasHeightForWidth())
        self.autofocus_size_z.setSizePolicy(sizePolicy2)
        self.autofocus_size_z.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_5.addWidget(self.autofocus_size_z, 3, 2, 1, 1)

        self.label_17 = QLabel(self.gridLayoutWidget_6)
        self.label_17.setObjectName(u"label_17")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy9)
        self.label_17.setFont(font5)
        self.label_17.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_17.setWordWrap(True)
        self.label_17.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_5.addWidget(self.label_17, 1, 2, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.horizontalSpacer_21, 2, 5, 1, 1)

        self.confocal_step_z = QLineEdit(self.gridLayoutWidget_6)
        self.confocal_step_z.setObjectName(u"confocal_step_z")
        self.confocal_step_z.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.confocal_step_z.sizePolicy().hasHeightForWidth())
        self.confocal_step_z.setSizePolicy(sizePolicy2)
        self.confocal_step_z.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_5.addWidget(self.confocal_step_z, 3, 4, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font5)
        self.label_14.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_14.setWordWrap(True)
        self.label_14.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_5.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font5)
        self.label_15.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_15.setWordWrap(True)
        self.label_15.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_5.addWidget(self.label_15, 3, 0, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font5)
        self.label_16.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_16.setWordWrap(True)
        self.label_16.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_5.addWidget(self.label_16, 1, 4, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_5.addItem(self.horizontalSpacer_24, 3, 5, 1, 1)

        self.confocal_step_xy = QLineEdit(self.gridLayoutWidget_6)
        self.confocal_step_xy.setObjectName(u"confocal_step_xy")
        self.confocal_step_xy.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.confocal_step_xy.sizePolicy().hasHeightForWidth())
        self.confocal_step_xy.setSizePolicy(sizePolicy2)
        self.confocal_step_xy.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_5.addWidget(self.confocal_step_xy, 2, 4, 1, 1)

        self.autofocus_size_xy = QLineEdit(self.gridLayoutWidget_6)
        self.autofocus_size_xy.setObjectName(u"autofocus_size_xy")
        self.autofocus_size_xy.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.autofocus_size_xy.sizePolicy().hasHeightForWidth())
        self.autofocus_size_xy.setSizePolicy(sizePolicy2)
        self.autofocus_size_xy.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_5.addWidget(self.autofocus_size_xy, 2, 2, 1, 1)

        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(60, 560, 811, 251))
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.gridLayoutWidget_5 = QWidget(self.frame_14)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(20, 10, 781, 231))
        self.autofocus_layout = QGridLayout(self.gridLayoutWidget_5)
        self.autofocus_layout.setObjectName(u"autofocus_layout")
        self.autofocus_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget_11 = QWidget(self.frame)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(80, 820, 781, 47))
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_27 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_27)

        self.autofocus_01 = QCheckBox(self.horizontalLayoutWidget_11)
        self.autofocus_01.setObjectName(u"autofocus_01")
        self.autofocus_01.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")

        self.horizontalLayout_19.addWidget(self.autofocus_01)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_31)

        self.autofocus_005 = QCheckBox(self.horizontalLayoutWidget_11)
        self.autofocus_005.setObjectName(u"autofocus_005")
        self.autofocus_005.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")

        self.horizontalLayout_19.addWidget(self.autofocus_005)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_32)

        self.autofocus_001 = QCheckBox(self.horizontalLayoutWidget_11)
        self.autofocus_001.setObjectName(u"autofocus_001")
        self.autofocus_001.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.autofocus_001.setChecked(True)

        self.horizontalLayout_19.addWidget(self.autofocus_001)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_35)

        self.autofocus_start = QPushButton(self.horizontalLayoutWidget_11)
        self.autofocus_start.setObjectName(u"autofocus_start")
        sizePolicy1.setHeightForWidth(self.autofocus_start.sizePolicy().hasHeightForWidth())
        self.autofocus_start.setSizePolicy(sizePolicy1)
        self.autofocus_start.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.autofocus_start.setIcon(icon5)

        self.horizontalLayout_19.addWidget(self.autofocus_start)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_34)

        self.autofocus_save = QPushButton(self.horizontalLayoutWidget_11)
        self.autofocus_save.setObjectName(u"autofocus_save")
        sizePolicy1.setHeightForWidth(self.autofocus_save.sizePolicy().hasHeightForWidth())
        self.autofocus_save.setSizePolicy(sizePolicy1)
        self.autofocus_save.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        icon7 = QIcon()
        icon7.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.autofocus_save.setIcon(icon7)

        self.horizontalLayout_19.addWidget(self.autofocus_save)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_33)

        self.verticalLayoutWidget_18 = QWidget(self.frame)
        self.verticalLayoutWidget_18.setObjectName(u"verticalLayoutWidget_18")
        self.verticalLayoutWidget_18.setGeometry(QRect(0, 10, 971, 331))
        self.counter_layout = QVBoxLayout(self.verticalLayoutWidget_18)
        self.counter_layout.setObjectName(u"counter_layout")
        self.counter_layout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget_13 = QWidget(self.frame)
        self.horizontalLayoutWidget_13.setObjectName(u"horizontalLayoutWidget_13")
        self.horizontalLayoutWidget_13.setGeometry(QRect(0, 350, 971, 52))
        self.horizontalLayout_23 = QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.counter_laser_on = QPushButton(self.horizontalLayoutWidget_13)
        self.counter_laser_on.setObjectName(u"counter_laser_on")
        sizePolicy1.setHeightForWidth(self.counter_laser_on.sizePolicy().hasHeightForWidth())
        self.counter_laser_on.setSizePolicy(sizePolicy1)
        self.counter_laser_on.setFont(font5)
        self.counter_laser_on.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.counter_laser_on.setIconSize(QSize(40, 40))
        self.counter_laser_on.setCheckable(False)

        self.horizontalLayout_23.addWidget(self.counter_laser_on)

        self.counter_laser_on_2 = QPushButton(self.horizontalLayoutWidget_13)
        self.counter_laser_on_2.setObjectName(u"counter_laser_on_2")
        sizePolicy1.setHeightForWidth(self.counter_laser_on_2.sizePolicy().hasHeightForWidth())
        self.counter_laser_on_2.setSizePolicy(sizePolicy1)
        self.counter_laser_on_2.setFont(font5)
        self.counter_laser_on_2.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.counter_laser_on_2.setIconSize(QSize(40, 40))
        self.counter_laser_on_2.setCheckable(False)

        self.horizontalLayout_23.addWidget(self.counter_laser_on_2)

        self.counter_laser_on_3 = QPushButton(self.horizontalLayoutWidget_13)
        self.counter_laser_on_3.setObjectName(u"counter_laser_on_3")
        sizePolicy1.setHeightForWidth(self.counter_laser_on_3.sizePolicy().hasHeightForWidth())
        self.counter_laser_on_3.setSizePolicy(sizePolicy1)
        self.counter_laser_on_3.setFont(font5)
        self.counter_laser_on_3.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.counter_laser_on_3.setIconSize(QSize(40, 40))
        self.counter_laser_on_3.setCheckable(False)

        self.horizontalLayout_23.addWidget(self.counter_laser_on_3)

        self.counter_start = QPushButton(self.horizontalLayoutWidget_13)
        self.counter_start.setObjectName(u"counter_start")
        sizePolicy1.setHeightForWidth(self.counter_start.sizePolicy().hasHeightForWidth())
        self.counter_start.setSizePolicy(sizePolicy1)
        self.counter_start.setFont(font5)
        self.counter_start.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.counter_start.setIconSize(QSize(40, 40))
        self.counter_start.setCheckable(False)

        self.horizontalLayout_23.addWidget(self.counter_start)

        self.pushButton_AutoAlign_red = QPushButton(self.horizontalLayoutWidget_13)
        self.pushButton_AutoAlign_red.setObjectName(u"pushButton_AutoAlign_red")
        sizePolicy1.setHeightForWidth(self.pushButton_AutoAlign_red.sizePolicy().hasHeightForWidth())
        self.pushButton_AutoAlign_red.setSizePolicy(sizePolicy1)
        self.pushButton_AutoAlign_red.setMaximumSize(QSize(200, 16777215))
        self.pushButton_AutoAlign_red.setFont(font5)
        self.pushButton_AutoAlign_red.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.pushButton_AutoAlign_red.setIconSize(QSize(40, 40))
        self.pushButton_AutoAlign_red.setCheckable(False)

        self.horizontalLayout_23.addWidget(self.pushButton_AutoAlign_red)

        self.pushButton_AutoAlign_zpl = QPushButton(self.horizontalLayoutWidget_13)
        self.pushButton_AutoAlign_zpl.setObjectName(u"pushButton_AutoAlign_zpl")
        sizePolicy1.setHeightForWidth(self.pushButton_AutoAlign_zpl.sizePolicy().hasHeightForWidth())
        self.pushButton_AutoAlign_zpl.setSizePolicy(sizePolicy1)
        self.pushButton_AutoAlign_zpl.setMaximumSize(QSize(200, 16777215))
        self.pushButton_AutoAlign_zpl.setFont(font5)
        self.pushButton_AutoAlign_zpl.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.pushButton_AutoAlign_zpl.setIconSize(QSize(40, 40))
        self.pushButton_AutoAlign_zpl.setCheckable(False)

        self.horizontalLayout_23.addWidget(self.pushButton_AutoAlign_zpl)

        self.gridLayoutWidget_11 = QWidget(self.frame)
        self.gridLayoutWidget_11.setObjectName(u"gridLayoutWidget_11")
        self.gridLayoutWidget_11.setGeometry(QRect(0, 410, 971, 151))
        self.gridLayout_14 = QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.counter_average_counts = QLineEdit(self.gridLayoutWidget_11)
        self.counter_average_counts.setObjectName(u"counter_average_counts")
        self.counter_average_counts.setEnabled(False)
        self.counter_average_counts.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_14.addWidget(self.counter_average_counts, 0, 5, 1, 1)

        self.counter_laser_power = QLineEdit(self.gridLayoutWidget_11)
        self.counter_laser_power.setObjectName(u"counter_laser_power")
        self.counter_laser_power.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_14.addWidget(self.counter_laser_power, 1, 8, 1, 1)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.horizontalSpacer_41, 0, 3, 1, 1)

        self.label_71 = QLabel(self.gridLayoutWidget_11)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font5)
        self.label_71.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_71.setWordWrap(True)
        self.label_71.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_14.addWidget(self.label_71, 0, 7, 1, 1)

        self.label_72 = QLabel(self.gridLayoutWidget_11)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMinimumSize(QSize(150, 0))
        self.label_72.setFont(font5)
        self.label_72.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_72.setWordWrap(True)
        self.label_72.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_14.addWidget(self.label_72, 2, 0, 1, 1)

        self.counter_counts = QLineEdit(self.gridLayoutWidget_11)
        self.counter_counts.setObjectName(u"counter_counts")
        self.counter_counts.setEnabled(False)
        self.counter_counts.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_14.addWidget(self.counter_counts, 0, 2, 1, 1)

        self.label_73 = QLabel(self.gridLayoutWidget_11)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font5)
        self.label_73.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_73.setWordWrap(True)
        self.label_73.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_14.addWidget(self.label_73, 0, 0, 1, 1)

        self.label_74 = QLabel(self.gridLayoutWidget_11)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font5)
        self.label_74.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_74.setWordWrap(True)
        self.label_74.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_14.addWidget(self.label_74, 1, 0, 1, 1)

        self.counter_autoAlign_stepSize = QLineEdit(self.gridLayoutWidget_11)
        self.counter_autoAlign_stepSize.setObjectName(u"counter_autoAlign_stepSize")
        self.counter_autoAlign_stepSize.setMaximumSize(QSize(16777215, 16777215))
        self.counter_autoAlign_stepSize.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_14.addWidget(self.counter_autoAlign_stepSize, 2, 2, 1, 1)

        self.counter_laser_power_4 = QLabel(self.gridLayoutWidget_11)
        self.counter_laser_power_4.setObjectName(u"counter_laser_power_4")
        self.counter_laser_power_4.setFont(font5)
        self.counter_laser_power_4.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.counter_laser_power_4.setWordWrap(True)
        self.counter_laser_power_4.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_14.addWidget(self.counter_laser_power_4, 1, 7, 1, 1)

        self.counter_trace_length = QLineEdit(self.gridLayoutWidget_11)
        self.counter_trace_length.setObjectName(u"counter_trace_length")
        self.counter_trace_length.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_14.addWidget(self.counter_trace_length, 1, 5, 1, 1)

        self.label_75 = QLabel(self.gridLayoutWidget_11)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font5)
        self.label_75.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_75.setWordWrap(True)
        self.label_75.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_14.addWidget(self.label_75, 0, 4, 1, 1)

        self.counter_T_per_sec = QLineEdit(self.gridLayoutWidget_11)
        self.counter_T_per_sec.setObjectName(u"counter_T_per_sec")
        self.counter_T_per_sec.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_14.addWidget(self.counter_T_per_sec, 1, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.horizontalSpacer_9, 0, 1, 1, 1)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.horizontalSpacer_42, 0, 6, 1, 1)

        self.counter_standard_deviation = QLineEdit(self.gridLayoutWidget_11)
        self.counter_standard_deviation.setObjectName(u"counter_standard_deviation")
        self.counter_standard_deviation.setEnabled(False)
        self.counter_standard_deviation.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_14.addWidget(self.counter_standard_deviation, 0, 8, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_4, 2, 6, 1, 1)

        self.label_76 = QLabel(self.gridLayoutWidget_11)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font5)
        self.label_76.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_76.setWordWrap(True)
        self.label_76.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_14.addWidget(self.label_76, 1, 4, 1, 1)

        self.label_77 = QLabel(self.gridLayoutWidget_11)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font5)
        self.label_77.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_77.setWordWrap(True)
        self.label_77.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_14.addWidget(self.label_77, 2, 4, 1, 1)

        self.counter_AA_per_sec = QLineEdit(self.gridLayoutWidget_11)
        self.counter_AA_per_sec.setObjectName(u"counter_AA_per_sec")
        self.counter_AA_per_sec.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_14.addWidget(self.counter_AA_per_sec, 2, 5, 1, 1)

        self.pushButton_pulse_gen = QPushButton(self.gridLayoutWidget_11)
        self.pushButton_pulse_gen.setObjectName(u"pushButton_pulse_gen")
        sizePolicy1.setHeightForWidth(self.pushButton_pulse_gen.sizePolicy().hasHeightForWidth())
        self.pushButton_pulse_gen.setSizePolicy(sizePolicy1)
        self.pushButton_pulse_gen.setMaximumSize(QSize(200, 16777215))
        self.pushButton_pulse_gen.setFont(font5)
        self.pushButton_pulse_gen.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.pushButton_pulse_gen.setIconSize(QSize(40, 40))
        self.pushButton_pulse_gen.setCheckable(False)

        self.gridLayout_14.addWidget(self.pushButton_pulse_gen, 2, 8, 1, 1)


        self.verticalLayout_20.addWidget(self.widget)

        self.stackedWidget.addWidget(self.confocal)
        self.magnet = QWidget()
        self.magnet.setObjectName(u"magnet")
        self.horizontalLayoutWidget_5 = QWidget(self.magnet)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 0, 981, 56))
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.horizontalLayoutWidget_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font4)
        self.label_20.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.horizontalLayout_13.addWidget(self.label_20)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_16)

        self.magnet_save_2 = QPushButton(self.horizontalLayoutWidget_5)
        self.magnet_save_2.setObjectName(u"magnet_save_2")
        sizePolicy1.setHeightForWidth(self.magnet_save_2.sizePolicy().hasHeightForWidth())
        self.magnet_save_2.setSizePolicy(sizePolicy1)
        self.magnet_save_2.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.magnet_save_2.setIcon(icon7)

        self.horizontalLayout_13.addWidget(self.magnet_save_2)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_20)

        self.magnet_load = QPushButton(self.horizontalLayoutWidget_5)
        self.magnet_load.setObjectName(u"magnet_load")
        sizePolicy1.setHeightForWidth(self.magnet_load.sizePolicy().hasHeightForWidth())
        self.magnet_load.setSizePolicy(sizePolicy1)
        self.magnet_load.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        icon8 = QIcon()
        icon8.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.magnet_load.setIcon(icon8)

        self.horizontalLayout_13.addWidget(self.magnet_load)

        self.frame_5 = QFrame(self.magnet)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 60, 981, 891))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.horizontalLayoutWidget_6 = QWidget(self.frame_5)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(10, 700, 961, 62))
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_29 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_29)

        self.label_21 = QLabel(self.horizontalLayoutWidget_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font5)
        self.label_21.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_21.setWordWrap(True)
        self.label_21.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_14.addWidget(self.label_21)

        self.magnet_counts = QLineEdit(self.horizontalLayoutWidget_6)
        self.magnet_counts.setObjectName(u"magnet_counts")
        self.magnet_counts.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.magnet_counts.sizePolicy().hasHeightForWidth())
        self.magnet_counts.setSizePolicy(sizePolicy2)
        self.magnet_counts.setMaximumSize(QSize(100, 16777215))
        self.magnet_counts.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.horizontalLayout_14.addWidget(self.magnet_counts)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_22)

        self.label_30 = QLabel(self.horizontalLayoutWidget_6)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font5)
        self.label_30.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_30.setWordWrap(True)
        self.label_30.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_14.addWidget(self.label_30)

        self.magnet_per_point = QLineEdit(self.horizontalLayoutWidget_6)
        self.magnet_per_point.setObjectName(u"magnet_per_point")
        self.magnet_per_point.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.magnet_per_point.sizePolicy().hasHeightForWidth())
        self.magnet_per_point.setSizePolicy(sizePolicy2)
        self.magnet_per_point.setMaximumSize(QSize(100, 16777215))
        self.magnet_per_point.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.horizontalLayout_14.addWidget(self.magnet_per_point)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_37)

        self.magnet_start = QPushButton(self.horizontalLayoutWidget_6)
        self.magnet_start.setObjectName(u"magnet_start")
        sizePolicy1.setHeightForWidth(self.magnet_start.sizePolicy().hasHeightForWidth())
        self.magnet_start.setSizePolicy(sizePolicy1)
        self.magnet_start.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.magnet_start.setIcon(icon5)

        self.horizontalLayout_14.addWidget(self.magnet_start)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_23)

        self.horizontalSpacer_30 = QSpacerItem(10, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_30)

        self.gridLayoutWidget_8 = QWidget(self.frame_5)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(10, 780, 961, 112))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.gridLayoutWidget_8)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font5)
        self.label_25.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_25.setWordWrap(True)
        self.label_25.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_6.addWidget(self.label_25, 1, 4, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget_8)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setEnabled(True)
        self.label_22.setFont(font5)
        self.label_22.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_22.setWordWrap(True)
        self.label_22.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_6.addWidget(self.label_22, 2, 0, 1, 1)

        self.magnet_size = QLineEdit(self.gridLayoutWidget_8)
        self.magnet_size.setObjectName(u"magnet_size")
        self.magnet_size.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.magnet_size.sizePolicy().hasHeightForWidth())
        self.magnet_size.setSizePolicy(sizePolicy2)
        self.magnet_size.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_6.addWidget(self.magnet_size, 2, 2, 1, 1)

        self.magnet_step = QLineEdit(self.gridLayoutWidget_8)
        self.magnet_step.setObjectName(u"magnet_step")
        self.magnet_step.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.magnet_step.sizePolicy().hasHeightForWidth())
        self.magnet_step.setSizePolicy(sizePolicy2)
        self.magnet_step.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_6.addWidget(self.magnet_step, 2, 4, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget_8)
        self.label_24.setObjectName(u"label_24")
        sizePolicy9.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy9)
        self.label_24.setFont(font5)
        self.label_24.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_24.setWordWrap(True)
        self.label_24.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_6.addWidget(self.label_24, 1, 2, 1, 1)

        self.frame_19 = QFrame(self.frame_5)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(10, 10, 961, 681))
        self.frame_19.setFrameShape(QFrame.NoFrame)
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
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.gridLayoutWidget_9 = QWidget(self.frame_6)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(10, 10, 781, 254))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.magnet_position_x = QLineEdit(self.gridLayoutWidget_9)
        self.magnet_position_x.setObjectName(u"magnet_position_x")
        self.magnet_position_x.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.magnet_position_x.sizePolicy().hasHeightForWidth())
        self.magnet_position_x.setSizePolicy(sizePolicy2)
        self.magnet_position_x.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_7.addWidget(self.magnet_position_x, 4, 1, 1, 1)

        self.magnet_position_y = QLineEdit(self.gridLayoutWidget_9)
        self.magnet_position_y.setObjectName(u"magnet_position_y")
        self.magnet_position_y.setEnabled(False)
        sizePolicy10 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.magnet_position_y.sizePolicy().hasHeightForWidth())
        self.magnet_position_y.setSizePolicy(sizePolicy10)
        self.magnet_position_y.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_7.addWidget(self.magnet_position_y, 5, 1, 1, 1)

        self.magnet_position_z = QLineEdit(self.gridLayoutWidget_9)
        self.magnet_position_z.setObjectName(u"magnet_position_z")
        self.magnet_position_z.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.magnet_position_z.sizePolicy().hasHeightForWidth())
        self.magnet_position_z.setSizePolicy(sizePolicy2)
        self.magnet_position_z.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_7.addWidget(self.magnet_position_z, 6, 1, 1, 1)

        self.label_27 = QLabel(self.gridLayoutWidget_9)
        self.label_27.setObjectName(u"label_27")
        sizePolicy9.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy9)
        self.label_27.setFont(font5)
        self.label_27.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_27.setWordWrap(True)
        self.label_27.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_7.addWidget(self.label_27, 4, 0, 1, 1)

        self.label_28 = QLabel(self.gridLayoutWidget_9)
        self.label_28.setObjectName(u"label_28")
        sizePolicy9.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy9)
        self.label_28.setFont(font5)
        self.label_28.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_28.setWordWrap(True)
        self.label_28.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_7.addWidget(self.label_28, 6, 0, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_9)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font5)
        self.label_26.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_26.setWordWrap(True)
        self.label_26.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_7.addWidget(self.label_26, 5, 0, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy9)
        self.label_23.setFont(font5)
        self.label_23.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_23.setWordWrap(True)
        self.label_23.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_7.addWidget(self.label_23, 3, 1, 1, 1)

        self.magnet_set_position_x = QLineEdit(self.gridLayoutWidget_9)
        self.magnet_set_position_x.setObjectName(u"magnet_set_position_x")
        self.magnet_set_position_x.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.magnet_set_position_x.sizePolicy().hasHeightForWidth())
        self.magnet_set_position_x.setSizePolicy(sizePolicy2)
        self.magnet_set_position_x.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_7.addWidget(self.magnet_set_position_x, 4, 2, 1, 1)

        self.magnet_set_position_y = QLineEdit(self.gridLayoutWidget_9)
        self.magnet_set_position_y.setObjectName(u"magnet_set_position_y")
        self.magnet_set_position_y.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.magnet_set_position_y.sizePolicy().hasHeightForWidth())
        self.magnet_set_position_y.setSizePolicy(sizePolicy2)
        self.magnet_set_position_y.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_7.addWidget(self.magnet_set_position_y, 5, 2, 1, 1)

        self.magnet_set_position_z = QLineEdit(self.gridLayoutWidget_9)
        self.magnet_set_position_z.setObjectName(u"magnet_set_position_z")
        self.magnet_set_position_z.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.magnet_set_position_z.sizePolicy().hasHeightForWidth())
        self.magnet_set_position_z.setSizePolicy(sizePolicy2)
        self.magnet_set_position_z.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_7.addWidget(self.magnet_set_position_z, 6, 2, 1, 1)

        self.magnet_moveto = QPushButton(self.gridLayoutWidget_9)
        self.magnet_moveto.setObjectName(u"magnet_moveto")
        sizePolicy2.setHeightForWidth(self.magnet_moveto.sizePolicy().hasHeightForWidth())
        self.magnet_moveto.setSizePolicy(sizePolicy2)
        self.magnet_moveto.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.magnet_moveto.setIcon(icon6)

        self.gridLayout_7.addWidget(self.magnet_moveto, 3, 2, 1, 1)

        self.frame_7 = QFrame(self.magnet)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(1000, 330, 801, 201))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.gridLayoutWidget_10 = QWidget(self.frame_7)
        self.gridLayoutWidget_10.setObjectName(u"gridLayoutWidget_10")
        self.gridLayoutWidget_10.setGeometry(QRect(10, 80, 781, 115))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.magnet_jog_backward_z = QPushButton(self.gridLayoutWidget_10)
        self.magnet_jog_backward_z.setObjectName(u"magnet_jog_backward_z")
        sizePolicy2.setHeightForWidth(self.magnet_jog_backward_z.sizePolicy().hasHeightForWidth())
        self.magnet_jog_backward_z.setSizePolicy(sizePolicy2)
        self.magnet_jog_backward_z.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        icon9 = QIcon()
        icon9.addFile(u":/icons/images/icons/cil-media-step-forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.magnet_jog_backward_z.setIcon(icon9)

        self.gridLayout_9.addWidget(self.magnet_jog_backward_z, 2, 2, 1, 1)

        self.magnet_jog_foward_y = QPushButton(self.gridLayoutWidget_10)
        self.magnet_jog_foward_y.setObjectName(u"magnet_jog_foward_y")
        sizePolicy2.setHeightForWidth(self.magnet_jog_foward_y.sizePolicy().hasHeightForWidth())
        self.magnet_jog_foward_y.setSizePolicy(sizePolicy2)
        self.magnet_jog_foward_y.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.magnet_jog_foward_y.setIcon(icon9)

        self.gridLayout_9.addWidget(self.magnet_jog_foward_y, 0, 1, 1, 1)

        self.magnet_jog_backward_x = QPushButton(self.gridLayoutWidget_10)
        self.magnet_jog_backward_x.setObjectName(u"magnet_jog_backward_x")
        sizePolicy2.setHeightForWidth(self.magnet_jog_backward_x.sizePolicy().hasHeightForWidth())
        self.magnet_jog_backward_x.setSizePolicy(sizePolicy2)
        self.magnet_jog_backward_x.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.magnet_jog_backward_x.setIcon(icon9)

        self.gridLayout_9.addWidget(self.magnet_jog_backward_x, 2, 0, 1, 1)

        self.magnet_jog_backward_y = QPushButton(self.gridLayoutWidget_10)
        self.magnet_jog_backward_y.setObjectName(u"magnet_jog_backward_y")
        sizePolicy2.setHeightForWidth(self.magnet_jog_backward_y.sizePolicy().hasHeightForWidth())
        self.magnet_jog_backward_y.setSizePolicy(sizePolicy2)
        self.magnet_jog_backward_y.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.magnet_jog_backward_y.setIcon(icon9)

        self.gridLayout_9.addWidget(self.magnet_jog_backward_y, 2, 1, 1, 1)

        self.magnet_jog_foward_z = QPushButton(self.gridLayoutWidget_10)
        self.magnet_jog_foward_z.setObjectName(u"magnet_jog_foward_z")
        sizePolicy2.setHeightForWidth(self.magnet_jog_foward_z.sizePolicy().hasHeightForWidth())
        self.magnet_jog_foward_z.setSizePolicy(sizePolicy2)
        self.magnet_jog_foward_z.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.magnet_jog_foward_z.setIcon(icon9)

        self.gridLayout_9.addWidget(self.magnet_jog_foward_z, 0, 2, 1, 1)

        self.magnet_jog_foward_x = QPushButton(self.gridLayoutWidget_10)
        self.magnet_jog_foward_x.setObjectName(u"magnet_jog_foward_x")
        sizePolicy2.setHeightForWidth(self.magnet_jog_foward_x.sizePolicy().hasHeightForWidth())
        self.magnet_jog_foward_x.setSizePolicy(sizePolicy2)
        self.magnet_jog_foward_x.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.magnet_jog_foward_x.setIcon(icon9)

        self.gridLayout_9.addWidget(self.magnet_jog_foward_x, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_9.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.horizontalLayoutWidget_8 = QWidget(self.frame_7)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(10, 10, 781, 62))
        self.horizontalLayout_16 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.horizontalLayoutWidget_8)
        self.label_37.setObjectName(u"label_37")
        sizePolicy9.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy9)
        self.label_37.setFont(font5)
        self.label_37.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_37.setWordWrap(True)
        self.label_37.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_16.addWidget(self.label_37)

        self.magnet_step_jog = QLineEdit(self.horizontalLayoutWidget_8)
        self.magnet_step_jog.setObjectName(u"magnet_step_jog")
        self.magnet_step_jog.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.magnet_step_jog.sizePolicy().hasHeightForWidth())
        self.magnet_step_jog.setSizePolicy(sizePolicy2)
        self.magnet_step_jog.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.horizontalLayout_16.addWidget(self.magnet_step_jog)

        self.stackedWidget.addWidget(self.magnet)
        self.control = QWidget()
        self.control.setObjectName(u"control")
        self.horizontalLayoutWidget_9 = QWidget(self.control)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(10, 10, 781, 56))
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.horizontalLayoutWidget_9)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font4)
        self.label_38.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.horizontalLayout_17.addWidget(self.label_38)

        self.frame_8 = QFrame(self.control)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(1360, 0, 401, 61))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.control_type = QComboBox(self.frame_8)
        self.control_type.setObjectName(u"control_type")
        self.control_type.setGeometry(QRect(10, 10, 186, 41))
        self.control_type.setMaximumSize(QSize(16777215, 16777211))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI Semibold"])
        font6.setPointSize(16)
        font6.setBold(False)
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
        icon10 = QIcon()
        icon10.addFile(u":/icons/images/icons/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.control_params.setIcon(icon10)
        self.frame_9 = QFrame(self.control)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(10, 70, 651, 211))
        self.frame_9.setFrameShape(QFrame.NoFrame)
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
        self.frame_11.setFrameShape(QFrame.NoFrame)
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
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.gridLayoutWidget_13 = QWidget(self.frame_10)
        self.gridLayoutWidget_13.setObjectName(u"gridLayoutWidget_13")
        self.gridLayoutWidget_13.setGeometry(QRect(10, 10, 1111, 191))
        self.gridLayout_11 = QGridLayout(self.gridLayoutWidget_13)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.horizontalSpacer_15, 1, 7, 1, 1)

        self.control_start = QPushButton(self.gridLayoutWidget_13)
        self.control_start.setObjectName(u"control_start")
        sizePolicy2.setHeightForWidth(self.control_start.sizePolicy().hasHeightForWidth())
        self.control_start.setSizePolicy(sizePolicy2)
        self.control_start.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        self.control_start.setIcon(icon5)

        self.gridLayout_11.addWidget(self.control_start, 0, 8, 1, 1)

        self.autofocus_in = QLineEdit(self.gridLayoutWidget_13)
        self.autofocus_in.setObjectName(u"autofocus_in")
        self.autofocus_in.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.autofocus_in.sizePolicy().hasHeightForWidth())
        self.autofocus_in.setSizePolicy(sizePolicy2)
        self.autofocus_in.setMaximumSize(QSize(150, 16777215))
        self.autofocus_in.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_11.addWidget(self.autofocus_in, 1, 6, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.horizontalSpacer_10, 0, 9, 1, 1)

        self.horizontalSpacer_36 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.horizontalSpacer_36, 0, 4, 1, 1)

        self.label_39 = QLabel(self.gridLayoutWidget_13)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy9)
        self.label_39.setFont(font5)
        self.label_39.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_39.setWordWrap(True)
        self.label_39.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_11.addWidget(self.label_39, 0, 5, 1, 1)

        self.label_40 = QLabel(self.gridLayoutWidget_13)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy9)
        self.label_40.setFont(font5)
        self.label_40.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_40.setWordWrap(True)
        self.label_40.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_11.addWidget(self.label_40, 1, 5, 1, 1)

        self.fit_from = QLineEdit(self.gridLayoutWidget_13)
        self.fit_from.setObjectName(u"fit_from")
        self.fit_from.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.fit_from.sizePolicy().hasHeightForWidth())
        self.fit_from.setSizePolicy(sizePolicy2)
        self.fit_from.setMaximumSize(QSize(150, 16777215))
        self.fit_from.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_11.addWidget(self.fit_from, 0, 1, 1, 1)

        self.label_42 = QLabel(self.gridLayoutWidget_13)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy9)
        self.label_42.setFont(font5)
        self.label_42.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_42.setWordWrap(True)
        self.label_42.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_11.addWidget(self.label_42, 0, 2, 1, 1)

        self.control_stop = QPushButton(self.gridLayoutWidget_13)
        self.control_stop.setObjectName(u"control_stop")
        sizePolicy1.setHeightForWidth(self.control_stop.sizePolicy().hasHeightForWidth())
        self.control_stop.setSizePolicy(sizePolicy1)
        self.control_stop.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 15pt \"Segoe UI Semibold\";")
        icon11 = QIcon()
        icon11.addFile(u":/icons/images/icons/cil-media-pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.control_stop.setIcon(icon11)

        self.gridLayout_11.addWidget(self.control_stop, 1, 8, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_11.addItem(self.horizontalSpacer_14, 0, 7, 1, 1)

        self.reps = QLineEdit(self.gridLayoutWidget_13)
        self.reps.setObjectName(u"reps")
        self.reps.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.reps.sizePolicy().hasHeightForWidth())
        self.reps.setSizePolicy(sizePolicy1)
        self.reps.setMaximumSize(QSize(150, 16777215))
        self.reps.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_11.addWidget(self.reps, 0, 6, 1, 1)

        self.label_41 = QLabel(self.gridLayoutWidget_13)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy9)
        self.label_41.setFont(font5)
        self.label_41.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_41.setWordWrap(True)
        self.label_41.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_11.addWidget(self.label_41, 0, 0, 1, 1)

        self.fit_to = QLineEdit(self.gridLayoutWidget_13)
        self.fit_to.setObjectName(u"fit_to")
        self.fit_to.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.fit_to.sizePolicy().hasHeightForWidth())
        self.fit_to.setSizePolicy(sizePolicy2)
        self.fit_to.setMaximumSize(QSize(150, 16777215))
        self.fit_to.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_11.addWidget(self.fit_to, 0, 3, 1, 1)

        self.fit_result = QLineEdit(self.gridLayoutWidget_13)
        self.fit_result.setObjectName(u"fit_result")
        self.fit_result.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.fit_result.sizePolicy().hasHeightForWidth())
        self.fit_result.setSizePolicy(sizePolicy2)
        self.fit_result.setMaximumSize(QSize(150, 16777215))
        self.fit_result.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_11.addWidget(self.fit_result, 1, 3, 1, 1)

        self.label_43 = QLabel(self.gridLayoutWidget_13)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setEnabled(True)
        sizePolicy9.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy9)
        self.label_43.setFont(font5)
        self.label_43.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_43.setWordWrap(True)
        self.label_43.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_11.addWidget(self.label_43, 1, 2, 1, 1)

        self.control_fitting = QCheckBox(self.gridLayoutWidget_13)
        self.control_fitting.setObjectName(u"control_fitting")
        self.control_fitting.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")

        self.gridLayout_11.addWidget(self.control_fitting, 1, 1, 1, 1)

        self.stackedWidget.addWidget(self.control)
        self.Resonant = QWidget()
        self.Resonant.setObjectName(u"Resonant")
        self.label_62 = QLabel(self.Resonant)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(0, 0, 149, 39))
        self.label_62.setFont(font4)
        self.label_62.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.layoutWidget = QWidget(self.Resonant)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 50, 1571, 203))
        self.gridLayout_25 = QGridLayout(self.layoutWidget)
        self.gridLayout_25.setSpacing(10)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(10, 10, 10, 10)
        self.comboBox_WLM_ch1 = QComboBox(self.layoutWidget)
        self.comboBox_WLM_ch1.addItem("")
        self.comboBox_WLM_ch1.addItem("")
        self.comboBox_WLM_ch1.addItem("")
        self.comboBox_WLM_ch1.addItem("")
        self.comboBox_WLM_ch1.addItem("")
        self.comboBox_WLM_ch1.addItem("")
        self.comboBox_WLM_ch1.addItem("")
        self.comboBox_WLM_ch1.addItem("")
        self.comboBox_WLM_ch1.setObjectName(u"comboBox_WLM_ch1")
        self.comboBox_WLM_ch1.setFont(font)
        self.comboBox_WLM_ch1.setAutoFillBackground(False)
        self.comboBox_WLM_ch1.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_WLM_ch1.setIconSize(QSize(16, 16))
        self.comboBox_WLM_ch1.setFrame(True)

        self.gridLayout_25.addWidget(self.comboBox_WLM_ch1, 3, 3, 1, 1)

        self.label_CH2_curr_WL = QLabel(self.layoutWidget)
        self.label_CH2_curr_WL.setObjectName(u"label_CH2_curr_WL")
        self.label_CH2_curr_WL.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_25.addWidget(self.label_CH2_curr_WL, 4, 6, 1, 1)

        self.pushButton_CH2_connect = QPushButton(self.layoutWidget)
        self.pushButton_CH2_connect.setObjectName(u"pushButton_CH2_connect")
        self.pushButton_CH2_connect.setMinimumSize(QSize(100, 30))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI Semibold"])
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setItalic(False)
        self.pushButton_CH2_connect.setFont(font7)
        self.pushButton_CH2_connect.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_CH2_connect.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 10pt \"Segoe UI Semibold\";")

        self.gridLayout_25.addWidget(self.pushButton_CH2_connect, 4, 4, 1, 1)

        self.comboBox_laser_CH2 = QComboBox(self.layoutWidget)
        self.comboBox_laser_CH2.addItem("")
        self.comboBox_laser_CH2.addItem("")
        self.comboBox_laser_CH2.addItem("")
        self.comboBox_laser_CH2.setObjectName(u"comboBox_laser_CH2")
        self.comboBox_laser_CH2.setFont(font)
        self.comboBox_laser_CH2.setAutoFillBackground(False)
        self.comboBox_laser_CH2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_laser_CH2.setIconSize(QSize(16, 16))
        self.comboBox_laser_CH2.setFrame(True)

        self.gridLayout_25.addWidget(self.comboBox_laser_CH2, 4, 2, 1, 1)

        self.label_laser_ch2 = QLabel(self.layoutWidget)
        self.label_laser_ch2.setObjectName(u"label_laser_ch2")
        self.label_laser_ch2.setMaximumSize(QSize(200, 16777215))
        self.label_laser_ch2.setFont(font)
        self.label_laser_ch2.setStyleSheet(u"color:rgba(255, 255, 255, 210);")

        self.gridLayout_25.addWidget(self.label_laser_ch2, 4, 1, 1, 1)

        self.label_PLE_2 = QLabel(self.layoutWidget)
        self.label_PLE_2.setObjectName(u"label_PLE_2")
        self.label_PLE_2.setMaximumSize(QSize(16777215, 30))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI Semibold"])
        font8.setPointSize(14)
        font8.setBold(False)
        font8.setItalic(False)
        self.label_PLE_2.setFont(font8)
        self.label_PLE_2.setStyleSheet(u"font: 63 14pt \"Segoe UI Semibold\";")

        self.gridLayout_25.addWidget(self.label_PLE_2, 0, 1, 1, 1)

        self.lineEdit_changeWL_CH1 = QLineEdit(self.layoutWidget)
        self.lineEdit_changeWL_CH1.setObjectName(u"lineEdit_changeWL_CH1")
        self.lineEdit_changeWL_CH1.setMinimumSize(QSize(0, 30))
        self.lineEdit_changeWL_CH1.setMaximumSize(QSize(140, 16777215))
        self.lineEdit_changeWL_CH1.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_25.addWidget(self.lineEdit_changeWL_CH1, 3, 9, 1, 1)

        self.pushButton_laserlock_button_1 = QPushButton(self.layoutWidget)
        self.pushButton_laserlock_button_1.setObjectName(u"pushButton_laserlock_button_1")
        self.pushButton_laserlock_button_1.setEnabled(False)
        self.pushButton_laserlock_button_1.setMinimumSize(QSize(100, 30))
        self.pushButton_laserlock_button_1.setFont(font7)
        self.pushButton_laserlock_button_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_laserlock_button_1.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 10pt \"Segoe UI Semibold\";")

        self.gridLayout_25.addWidget(self.pushButton_laserlock_button_1, 3, 8, 1, 1)

        self.lineEdit_laserLock_CH1 = QLineEdit(self.layoutWidget)
        self.lineEdit_laserLock_CH1.setObjectName(u"lineEdit_laserLock_CH1")
        self.lineEdit_laserLock_CH1.setMinimumSize(QSize(0, 30))
        self.lineEdit_laserLock_CH1.setMaximumSize(QSize(140, 16777215))
        self.lineEdit_laserLock_CH1.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_25.addWidget(self.lineEdit_laserLock_CH1, 3, 7, 1, 1)

        self.pushButton_CH1_connect = QPushButton(self.layoutWidget)
        self.pushButton_CH1_connect.setObjectName(u"pushButton_CH1_connect")
        self.pushButton_CH1_connect.setMinimumSize(QSize(100, 30))
        self.pushButton_CH1_connect.setFont(font7)
        self.pushButton_CH1_connect.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_CH1_connect.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 10pt \"Segoe UI Semibold\";")

        self.gridLayout_25.addWidget(self.pushButton_CH1_connect, 3, 4, 1, 1)

        self.label_CH1_curr_WL = QLabel(self.layoutWidget)
        self.label_CH1_curr_WL.setObjectName(u"label_CH1_curr_WL")
        self.label_CH1_curr_WL.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_25.addWidget(self.label_CH1_curr_WL, 3, 6, 1, 1)

        self.label_PLE_4 = QLabel(self.layoutWidget)
        self.label_PLE_4.setObjectName(u"label_PLE_4")
        self.label_PLE_4.setMaximumSize(QSize(140, 30))
        self.label_PLE_4.setFont(font8)
        self.label_PLE_4.setStyleSheet(u"font: 63 14pt \"Segoe UI Semibold\";")

        self.gridLayout_25.addWidget(self.label_PLE_4, 0, 7, 1, 1)

        self.label_CH1_laserLock = QLabel(self.layoutWidget)
        self.label_CH1_laserLock.setObjectName(u"label_CH1_laserLock")
        self.label_CH1_laserLock.setMaximumSize(QSize(80, 16777215))
        self.label_CH1_laserLock.setFont(font)
        self.label_CH1_laserLock.setStyleSheet(u"color:rgba(255, 255, 255, 210);")
        self.label_CH1_laserLock.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_CH1_laserLock, 3, 5, 1, 1)

        self.label_CH1_laserLock_5 = QLabel(self.layoutWidget)
        self.label_CH1_laserLock_5.setObjectName(u"label_CH1_laserLock_5")
        self.label_CH1_laserLock_5.setMinimumSize(QSize(0, 0))
        self.label_CH1_laserLock_5.setMaximumSize(QSize(140, 16777215))
        self.label_CH1_laserLock_5.setFont(font)
        self.label_CH1_laserLock_5.setStyleSheet(u"color:rgba(255, 255, 255, 210);")
        self.label_CH1_laserLock_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_CH1_laserLock_5, 1, 7, 1, 1)

        self.comboBox_laser_CH1 = QComboBox(self.layoutWidget)
        self.comboBox_laser_CH1.addItem("")
        self.comboBox_laser_CH1.addItem("")
        self.comboBox_laser_CH1.addItem("")
        self.comboBox_laser_CH1.setObjectName(u"comboBox_laser_CH1")
        self.comboBox_laser_CH1.setFont(font)
        self.comboBox_laser_CH1.setAutoFillBackground(False)
        self.comboBox_laser_CH1.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_laser_CH1.setIconSize(QSize(16, 16))
        self.comboBox_laser_CH1.setFrame(True)

        self.gridLayout_25.addWidget(self.comboBox_laser_CH1, 3, 2, 1, 1)

        self.label_CH1_laserLock_4 = QLabel(self.layoutWidget)
        self.label_CH1_laserLock_4.setObjectName(u"label_CH1_laserLock_4")
        self.label_CH1_laserLock_4.setMinimumSize(QSize(0, 0))
        self.label_CH1_laserLock_4.setMaximumSize(QSize(140, 16777215))
        self.label_CH1_laserLock_4.setFont(font)
        self.label_CH1_laserLock_4.setStyleSheet(u"color:rgba(255, 255, 255, 210);")
        self.label_CH1_laserLock_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_CH1_laserLock_4, 1, 9, 1, 1)

        self.label_CH1_laserLock_2 = QLabel(self.layoutWidget)
        self.label_CH1_laserLock_2.setObjectName(u"label_CH1_laserLock_2")
        self.label_CH1_laserLock_2.setMaximumSize(QSize(80, 16777215))
        self.label_CH1_laserLock_2.setFont(font)
        self.label_CH1_laserLock_2.setStyleSheet(u"color:rgba(255, 255, 255, 210);")
        self.label_CH1_laserLock_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_CH1_laserLock_2.setMargin(0)

        self.gridLayout_25.addWidget(self.label_CH1_laserLock_2, 4, 5, 1, 1)

        self.lineEdit_laserLock_CH2 = QLineEdit(self.layoutWidget)
        self.lineEdit_laserLock_CH2.setObjectName(u"lineEdit_laserLock_CH2")
        self.lineEdit_laserLock_CH2.setMinimumSize(QSize(0, 30))
        self.lineEdit_laserLock_CH2.setMaximumSize(QSize(140, 16777215))
        self.lineEdit_laserLock_CH2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_25.addWidget(self.lineEdit_laserLock_CH2, 4, 7, 1, 1)

        self.label_laser_ch1 = QLabel(self.layoutWidget)
        self.label_laser_ch1.setObjectName(u"label_laser_ch1")
        self.label_laser_ch1.setMaximumSize(QSize(200, 16777215))
        self.label_laser_ch1.setFont(font)
        self.label_laser_ch1.setStyleSheet(u"color:rgba(255, 255, 255, 210);")

        self.gridLayout_25.addWidget(self.label_laser_ch1, 3, 1, 1, 1)

        self.pushButton_change_wavelength_2 = QPushButton(self.layoutWidget)
        self.pushButton_change_wavelength_2.setObjectName(u"pushButton_change_wavelength_2")
        self.pushButton_change_wavelength_2.setEnabled(False)
        self.pushButton_change_wavelength_2.setMinimumSize(QSize(150, 30))
        self.pushButton_change_wavelength_2.setFont(font7)
        self.pushButton_change_wavelength_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_change_wavelength_2.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 10pt \"Segoe UI Semibold\";")

        self.gridLayout_25.addWidget(self.pushButton_change_wavelength_2, 4, 10, 1, 1)

        self.lineEdit_changeWL_CH2 = QLineEdit(self.layoutWidget)
        self.lineEdit_changeWL_CH2.setObjectName(u"lineEdit_changeWL_CH2")
        self.lineEdit_changeWL_CH2.setMinimumSize(QSize(0, 30))
        self.lineEdit_changeWL_CH2.setMaximumSize(QSize(140, 16777215))
        self.lineEdit_changeWL_CH2.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout_25.addWidget(self.lineEdit_changeWL_CH2, 4, 9, 1, 1)

        self.label_start_WL_2 = QLabel(self.layoutWidget)
        self.label_start_WL_2.setObjectName(u"label_start_WL_2")
        self.label_start_WL_2.setMinimumSize(QSize(100, 0))
        self.label_start_WL_2.setMaximumSize(QSize(200, 30))
        self.label_start_WL_2.setFont(font)
        self.label_start_WL_2.setStyleSheet(u"color:rgba(255, 255, 255, 210);")

        self.gridLayout_25.addWidget(self.label_start_WL_2, 1, 2, 1, 1)

        self.label_CH1_laserLock_3 = QLabel(self.layoutWidget)
        self.label_CH1_laserLock_3.setObjectName(u"label_CH1_laserLock_3")
        self.label_CH1_laserLock_3.setMaximumSize(QSize(180, 16777215))
        self.label_CH1_laserLock_3.setFont(font)
        self.label_CH1_laserLock_3.setStyleSheet(u"color:rgba(255, 255, 255, 210);")
        self.label_CH1_laserLock_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_CH1_laserLock_3, 1, 6, 1, 1)

        self.comboBox_WLM_ch2 = QComboBox(self.layoutWidget)
        self.comboBox_WLM_ch2.addItem("")
        self.comboBox_WLM_ch2.addItem("")
        self.comboBox_WLM_ch2.addItem("")
        self.comboBox_WLM_ch2.addItem("")
        self.comboBox_WLM_ch2.addItem("")
        self.comboBox_WLM_ch2.addItem("")
        self.comboBox_WLM_ch2.addItem("")
        self.comboBox_WLM_ch2.addItem("")
        self.comboBox_WLM_ch2.setObjectName(u"comboBox_WLM_ch2")
        self.comboBox_WLM_ch2.setFont(font)
        self.comboBox_WLM_ch2.setAutoFillBackground(False)
        self.comboBox_WLM_ch2.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox_WLM_ch2.setIconSize(QSize(16, 16))
        self.comboBox_WLM_ch2.setFrame(True)

        self.gridLayout_25.addWidget(self.comboBox_WLM_ch2, 4, 3, 1, 1)

        self.label_start_WL_3 = QLabel(self.layoutWidget)
        self.label_start_WL_3.setObjectName(u"label_start_WL_3")
        self.label_start_WL_3.setMinimumSize(QSize(60, 0))
        self.label_start_WL_3.setMaximumSize(QSize(70, 16777215))
        self.label_start_WL_3.setFont(font)
        self.label_start_WL_3.setStyleSheet(u"color:rgba(255, 255, 255, 210);")

        self.gridLayout_25.addWidget(self.label_start_WL_3, 1, 3, 1, 1)

        self.pushButton_change_wavelength_1 = QPushButton(self.layoutWidget)
        self.pushButton_change_wavelength_1.setObjectName(u"pushButton_change_wavelength_1")
        self.pushButton_change_wavelength_1.setEnabled(False)
        self.pushButton_change_wavelength_1.setMinimumSize(QSize(150, 30))
        self.pushButton_change_wavelength_1.setFont(font7)
        self.pushButton_change_wavelength_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_change_wavelength_1.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 10pt \"Segoe UI Semibold\";")

        self.gridLayout_25.addWidget(self.pushButton_change_wavelength_1, 3, 10, 1, 1)

        self.pushButton_laserlock_button_2 = QPushButton(self.layoutWidget)
        self.pushButton_laserlock_button_2.setObjectName(u"pushButton_laserlock_button_2")
        self.pushButton_laserlock_button_2.setEnabled(False)
        self.pushButton_laserlock_button_2.setMinimumSize(QSize(100, 30))
        self.pushButton_laserlock_button_2.setFont(font7)
        self.pushButton_laserlock_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_laserlock_button_2.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 10pt \"Segoe UI Semibold\";")

        self.gridLayout_25.addWidget(self.pushButton_laserlock_button_2, 4, 8, 1, 1)

        self.verticalLayoutWidget_11 = QWidget(self.Resonant)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(10, 262, 1041, 826))
        self.verticalLayout_115 = QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_115.setObjectName(u"verticalLayout_115")
        self.verticalLayout_115.setContentsMargins(0, 0, 0, 0)
        self.label_PLE = QLabel(self.verticalLayoutWidget_11)
        self.label_PLE.setObjectName(u"label_PLE")
        self.label_PLE.setFont(font8)
        self.label_PLE.setStyleSheet(u"font: 63 14pt \"Segoe UI Semibold\";")

        self.verticalLayout_115.addWidget(self.label_PLE)

        self.verticalSpacer_79 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_115.addItem(self.verticalSpacer_79)

        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.widget_PLE_count = QWidget(self.verticalLayoutWidget_11)
        self.widget_PLE_count.setObjectName(u"widget_PLE_count")
        self.widget_PLE_count.setMinimumSize(QSize(800, 600))
        self.widget_PLE_count.setMaximumSize(QSize(800, 16777215))
        self.verticalLayout_76 = QVBoxLayout(self.widget_PLE_count)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.verticalLayout_76.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout_PLE_count = QVBoxLayout()
        self.verticalLayout_PLE_count.setSpacing(0)
        self.verticalLayout_PLE_count.setObjectName(u"verticalLayout_PLE_count")
        self.horizontalLayout_PLE_count = QHBoxLayout()
        self.horizontalLayout_PLE_count.setObjectName(u"horizontalLayout_PLE_count")
        self.widget_graph_PLE = QWidget(self.widget_PLE_count)
        self.widget_graph_PLE.setObjectName(u"widget_graph_PLE")
        self.widget_graph_PLE.setMinimumSize(QSize(0, 450))
        self.widget_graph_PLE.setMaximumSize(QSize(800, 500))

        self.horizontalLayout_PLE_count.addWidget(self.widget_graph_PLE)


        self.verticalLayout_PLE_count.addLayout(self.horizontalLayout_PLE_count)


        self.verticalLayout_76.addLayout(self.verticalLayout_PLE_count)


        self.horizontalLayout_78.addWidget(self.widget_PLE_count)


        self.verticalLayout_115.addLayout(self.horizontalLayout_78)

        self.gridLayout_NV_search_count_setting_5 = QGridLayout()
        self.gridLayout_NV_search_count_setting_5.setSpacing(10)
        self.gridLayout_NV_search_count_setting_5.setObjectName(u"gridLayout_NV_search_count_setting_5")
        self.label_10 = QLabel(self.verticalLayoutWidget_11)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_10.setWordWrap(True)
        self.label_10.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_NV_search_count_setting_5.addWidget(self.label_10, 0, 0, 1, 1)

        self.lineEdit_PLE_repeat = QLineEdit(self.verticalLayoutWidget_11)
        self.lineEdit_PLE_repeat.setObjectName(u"lineEdit_PLE_repeat")
        self.lineEdit_PLE_repeat.setEnabled(True)
        self.lineEdit_PLE_repeat.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_PLE_repeat.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_NV_search_count_setting_5.addWidget(self.lineEdit_PLE_repeat, 1, 5, 1, 1)

        self.lineEdit_PLE_step = QLineEdit(self.verticalLayoutWidget_11)
        self.lineEdit_PLE_step.setObjectName(u"lineEdit_PLE_step")
        self.lineEdit_PLE_step.setEnabled(True)
        self.lineEdit_PLE_step.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_PLE_step.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_NV_search_count_setting_5.addWidget(self.lineEdit_PLE_step, 0, 5, 1, 1)

        self.pushButton_PLE_repeat = QPushButton(self.verticalLayoutWidget_11)
        self.pushButton_PLE_repeat.setObjectName(u"pushButton_PLE_repeat")
        self.pushButton_PLE_repeat.setMinimumSize(QSize(150, 30))
        self.pushButton_PLE_repeat.setFont(font7)
        self.pushButton_PLE_repeat.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_PLE_repeat.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 10pt \"Segoe UI Semibold\";")

        self.gridLayout_NV_search_count_setting_5.addWidget(self.pushButton_PLE_repeat, 1, 6, 1, 1)

        self.lineEdit_PLE_end = QLineEdit(self.verticalLayoutWidget_11)
        self.lineEdit_PLE_end.setObjectName(u"lineEdit_PLE_end")
        self.lineEdit_PLE_end.setEnabled(True)
        self.lineEdit_PLE_end.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_PLE_end.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_NV_search_count_setting_5.addWidget(self.lineEdit_PLE_end, 0, 3, 1, 1)

        self.lineEdit_PLE_start = QLineEdit(self.verticalLayoutWidget_11)
        self.lineEdit_PLE_start.setObjectName(u"lineEdit_PLE_start")
        self.lineEdit_PLE_start.setEnabled(True)
        self.lineEdit_PLE_start.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_PLE_start.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")

        self.gridLayout_NV_search_count_setting_5.addWidget(self.lineEdit_PLE_start, 0, 1, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.radioButton_PLE_CH1 = QRadioButton(self.verticalLayoutWidget_11)
        self.radioButton_PLE_CH1.setObjectName(u"radioButton_PLE_CH1")
        self.radioButton_PLE_CH1.setStyleSheet(u"color:rgba(255, 255, 255, 210);")
        self.radioButton_PLE_CH1.setChecked(True)

        self.horizontalLayout_22.addWidget(self.radioButton_PLE_CH1)

        self.radioButton_PLE_CH2 = QRadioButton(self.verticalLayoutWidget_11)
        self.radioButton_PLE_CH2.setObjectName(u"radioButton_PLE_CH2")
        self.radioButton_PLE_CH2.setStyleSheet(u"color:rgba(255, 255, 255, 210);")
        self.radioButton_PLE_CH2.setChecked(False)

        self.horizontalLayout_22.addWidget(self.radioButton_PLE_CH2)


        self.gridLayout_NV_search_count_setting_5.addLayout(self.horizontalLayout_22, 0, 6, 1, 1)

        self.pushButton_PLE_start = QPushButton(self.verticalLayoutWidget_11)
        self.pushButton_PLE_start.setObjectName(u"pushButton_PLE_start")
        self.pushButton_PLE_start.setMinimumSize(QSize(150, 30))
        self.pushButton_PLE_start.setFont(font7)
        self.pushButton_PLE_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_PLE_start.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 10pt \"Segoe UI Semibold\";")

        self.gridLayout_NV_search_count_setting_5.addWidget(self.pushButton_PLE_start, 1, 2, 1, 1)

        self.label_31 = QLabel(self.verticalLayoutWidget_11)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font5)
        self.label_31.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_31.setWordWrap(True)
        self.label_31.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_NV_search_count_setting_5.addWidget(self.label_31, 0, 2, 1, 1)

        self.label_32 = QLabel(self.verticalLayoutWidget_11)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font5)
        self.label_32.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_32.setWordWrap(True)
        self.label_32.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_NV_search_count_setting_5.addWidget(self.label_32, 0, 4, 1, 1)

        self.label_33 = QLabel(self.verticalLayoutWidget_11)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font5)
        self.label_33.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_33.setWordWrap(True)
        self.label_33.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_NV_search_count_setting_5.addWidget(self.label_33, 1, 4, 1, 1)

        self.label_34 = QLabel(self.verticalLayoutWidget_11)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font5)
        self.label_34.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.label_34.setWordWrap(True)
        self.label_34.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout_NV_search_count_setting_5.addWidget(self.label_34, 1, 1, 1, 1)


        self.verticalLayout_115.addLayout(self.gridLayout_NV_search_count_setting_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")

        self.verticalLayout_115.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")

        self.verticalLayout_115.addLayout(self.horizontalLayout_79)

        self.verticalLayoutWidget_12 = QWidget(self.Resonant)
        self.verticalLayoutWidget_12.setObjectName(u"verticalLayoutWidget_12")
        self.verticalLayoutWidget_12.setGeometry(QRect(1060, 380, 561, 311))
        self.verticalLayout_116 = QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_116.setObjectName(u"verticalLayout_116")
        self.verticalLayout_116.setContentsMargins(0, 0, 0, 0)
        self.label_PLE_3 = QLabel(self.verticalLayoutWidget_12)
        self.label_PLE_3.setObjectName(u"label_PLE_3")
        self.label_PLE_3.setFont(font8)
        self.label_PLE_3.setStyleSheet(u"font: 63 14pt \"Segoe UI Semibold\";")

        self.verticalLayout_116.addWidget(self.label_PLE_3)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.widget_PLE_count_2 = QWidget(self.verticalLayoutWidget_12)
        self.widget_PLE_count_2.setObjectName(u"widget_PLE_count_2")
        self.widget_PLE_count_2.setMinimumSize(QSize(400, 200))
        self.widget_PLE_count_2.setMaximumSize(QSize(500, 16777215))
        self.verticalLayout_77 = QVBoxLayout(self.widget_PLE_count_2)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout_PLE_count_2 = QVBoxLayout()
        self.verticalLayout_PLE_count_2.setSpacing(0)
        self.verticalLayout_PLE_count_2.setObjectName(u"verticalLayout_PLE_count_2")
        self.horizontalLayout_wavelength = QHBoxLayout()
        self.horizontalLayout_wavelength.setObjectName(u"horizontalLayout_wavelength")

        self.verticalLayout_PLE_count_2.addLayout(self.horizontalLayout_wavelength)


        self.verticalLayout_77.addLayout(self.verticalLayout_PLE_count_2)


        self.horizontalLayout_80.addWidget(self.widget_PLE_count_2)

        self.verticalLayout_button_2 = QVBoxLayout()
        self.verticalLayout_button_2.setObjectName(u"verticalLayout_button_2")
        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.radioButton_WL_scan_CH1 = QRadioButton(self.verticalLayoutWidget_12)
        self.radioButton_WL_scan_CH1.setObjectName(u"radioButton_WL_scan_CH1")
        self.radioButton_WL_scan_CH1.setMaximumSize(QSize(70, 16777215))
        self.radioButton_WL_scan_CH1.setStyleSheet(u"color:rgba(255, 255, 255, 210);")
        self.radioButton_WL_scan_CH1.setChecked(True)

        self.horizontalLayout_56.addWidget(self.radioButton_WL_scan_CH1)

        self.radioButton_WL_scan_CH2 = QRadioButton(self.verticalLayoutWidget_12)
        self.radioButton_WL_scan_CH2.setObjectName(u"radioButton_WL_scan_CH2")
        self.radioButton_WL_scan_CH2.setMaximumSize(QSize(70, 70))
        self.radioButton_WL_scan_CH2.setStyleSheet(u"color:rgba(255, 255, 255, 210);")
        self.radioButton_WL_scan_CH2.setChecked(False)

        self.horizontalLayout_56.addWidget(self.radioButton_WL_scan_CH2)


        self.verticalLayout_button_2.addLayout(self.horizontalLayout_56)

        self.pushButton_wavelength_scan_start = QPushButton(self.verticalLayoutWidget_12)
        self.pushButton_wavelength_scan_start.setObjectName(u"pushButton_wavelength_scan_start")
        self.pushButton_wavelength_scan_start.setMinimumSize(QSize(80, 30))
        self.pushButton_wavelength_scan_start.setMaximumSize(QSize(500, 16777215))
        self.pushButton_wavelength_scan_start.setFont(font7)
        self.pushButton_wavelength_scan_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_wavelength_scan_start.setStyleSheet(u"background-color: rgb(52, 59, 72);\n"
"font: 63 10pt \"Segoe UI Semibold\";")

        self.verticalLayout_button_2.addWidget(self.pushButton_wavelength_scan_start)

        self.verticalSpacer_60 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_button_2.addItem(self.verticalSpacer_60)


        self.horizontalLayout_80.addLayout(self.verticalLayout_button_2)


        self.verticalLayout_116.addLayout(self.horizontalLayout_80)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_start_WL_4 = QLabel(self.verticalLayoutWidget_12)
        self.label_start_WL_4.setObjectName(u"label_start_WL_4")
        self.label_start_WL_4.setMaximumSize(QSize(200, 16777215))
        self.label_start_WL_4.setFont(font)
        self.label_start_WL_4.setStyleSheet(u"color:rgba(255, 255, 255, 210);")

        self.horizontalLayout_53.addWidget(self.label_start_WL_4)

        self.lineEdit_WL_start_voltage = QLineEdit(self.verticalLayoutWidget_12)
        self.lineEdit_WL_start_voltage.setObjectName(u"lineEdit_WL_start_voltage")
        self.lineEdit_WL_start_voltage.setMinimumSize(QSize(0, 30))
        self.lineEdit_WL_start_voltage.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_53.addWidget(self.lineEdit_WL_start_voltage)

        self.label_end_WL_2 = QLabel(self.verticalLayoutWidget_12)
        self.label_end_WL_2.setObjectName(u"label_end_WL_2")
        self.label_end_WL_2.setMaximumSize(QSize(180, 16777215))
        self.label_end_WL_2.setFont(font)
        self.label_end_WL_2.setStyleSheet(u"color:rgba(255, 255, 255, 210);")

        self.horizontalLayout_53.addWidget(self.label_end_WL_2)

        self.lineEdit_WL_end_voltage = QLineEdit(self.verticalLayoutWidget_12)
        self.lineEdit_WL_end_voltage.setObjectName(u"lineEdit_WL_end_voltage")
        self.lineEdit_WL_end_voltage.setMinimumSize(QSize(0, 30))
        self.lineEdit_WL_end_voltage.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_53.addWidget(self.lineEdit_WL_end_voltage)

        self.label_end_WL_3 = QLabel(self.verticalLayoutWidget_12)
        self.label_end_WL_3.setObjectName(u"label_end_WL_3")
        self.label_end_WL_3.setMaximumSize(QSize(180, 16777215))
        self.label_end_WL_3.setFont(font)
        self.label_end_WL_3.setStyleSheet(u"color:rgba(255, 255, 255, 210);")

        self.horizontalLayout_53.addWidget(self.label_end_WL_3)

        self.lineEdit_WL_step_size = QLineEdit(self.verticalLayoutWidget_12)
        self.lineEdit_WL_step_size.setObjectName(u"lineEdit_WL_step_size")
        self.lineEdit_WL_step_size.setMinimumSize(QSize(0, 30))
        self.lineEdit_WL_step_size.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_53.addWidget(self.lineEdit_WL_step_size)


        self.verticalLayout_116.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")

        self.verticalLayout_116.addLayout(self.horizontalLayout_81)

        self.verticalLayoutWidget_14 = QWidget(self.Resonant)
        self.verticalLayoutWidget_14.setObjectName(u"verticalLayoutWidget_14")
        self.verticalLayoutWidget_14.setGeometry(QRect(1060, 260, 561, 101))
        self.verticalLayout_117 = QVBoxLayout(self.verticalLayoutWidget_14)
        self.verticalLayout_117.setObjectName(u"verticalLayout_117")
        self.verticalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.Resonant)
        self.Entanglement = QWidget()
        self.Entanglement.setObjectName(u"Entanglement")
        self.horizontalLayoutWidget_4 = QWidget(self.Entanglement)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 120, 431, 211))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_21 = QWidget(self.horizontalLayoutWidget_4)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMinimumSize(QSize(300, 0))
        self.verticalLayoutWidget_13 = QWidget(self.widget_21)
        self.verticalLayoutWidget_13.setObjectName(u"verticalLayoutWidget_13")
        self.verticalLayoutWidget_13.setGeometry(QRect(0, 0, 301, 211))
        self.verticalLayout_spin_photon_count = QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_spin_photon_count.setObjectName(u"verticalLayout_spin_photon_count")
        self.verticalLayout_spin_photon_count.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_10.addWidget(self.widget_21)

        self.verticalLayout_75 = QVBoxLayout()
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.pushButton_spin_photon_start = QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_spin_photon_start.setObjectName(u"pushButton_spin_photon_start")
        self.pushButton_spin_photon_start.setMinimumSize(QSize(30, 30))
        self.pushButton_spin_photon_start.setFont(font)
        self.pushButton_spin_photon_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_spin_photon_start.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_spin_photon_start.setIcon(icon5)

        self.verticalLayout_75.addWidget(self.pushButton_spin_photon_start)


        self.horizontalLayout_10.addLayout(self.verticalLayout_75)

        self.label_63 = QLabel(self.Entanglement)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(10, 10, 181, 39))
        self.label_63.setFont(font4)
        self.label_63.setStyleSheet(u"font: 63 20pt \"Segoe UI Semibold\";")
        self.label_64 = QLabel(self.Entanglement)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(10, 70, 181, 39))
        self.label_64.setFont(font5)
        self.label_64.setStyleSheet(u"font: 63 15pt \"Segoe UI Semibold\";")
        self.stackedWidget.addWidget(self.Entanglement)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.NoFrame)
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
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
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
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton.setIcon(icon8)

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.NoFrame)
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

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
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

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon12 = QIcon()
        icon12.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon12)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.NoFrame)
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
        font9 = QFont()
        font9.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font9);
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
        sizePolicy11 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy11)
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
        brush3 = QBrush(QColor(221, 221, 221, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.NoPen)
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
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setMaximumSize(QSize(16777215, 16))
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        font10.setBold(False)
        font10.setItalic(False)
        self.creditsLabel.setFont(font10)

        self.horizontalLayout_5.addWidget(self.creditsLabel)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)
        QWidget.setTabOrder(self.btn_more, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.settingsTopBtn)
        QWidget.setTabOrder(self.settingsTopBtn, self.minimizeAppBtn)
        QWidget.setTabOrder(self.minimizeAppBtn, self.btn_5_entangle)
        QWidget.setTabOrder(self.btn_5_entangle, self.toggleLeftBox)
        QWidget.setTabOrder(self.toggleLeftBox, self.extraCloseColumnBtn)
        QWidget.setTabOrder(self.extraCloseColumnBtn, self.confocal_set_position_x)
        QWidget.setTabOrder(self.confocal_set_position_x, self.confocal_set_position_y)
        QWidget.setTabOrder(self.confocal_set_position_y, self.confocal_set_position_z)
        QWidget.setTabOrder(self.confocal_set_position_z, self.confocal_from_x)
        QWidget.setTabOrder(self.confocal_from_x, self.confocal_to_x)
        QWidget.setTabOrder(self.confocal_to_x, self.confocal_from_y)
        QWidget.setTabOrder(self.confocal_from_y, self.confocal_to_y)
        QWidget.setTabOrder(self.confocal_to_y, self.confocal_from_z)
        QWidget.setTabOrder(self.confocal_from_z, self.confocal_to_z)
        QWidget.setTabOrder(self.confocal_to_z, self.autofocus_size_xy)
        QWidget.setTabOrder(self.autofocus_size_xy, self.confocal_step_xy)
        QWidget.setTabOrder(self.confocal_step_xy, self.autofocus_size_z)
        QWidget.setTabOrder(self.autofocus_size_z, self.confocal_step_z)
        QWidget.setTabOrder(self.confocal_step_z, self.confocal_resolution)
        QWidget.setTabOrder(self.confocal_resolution, self.confocal_T_per_point)
        QWidget.setTabOrder(self.confocal_T_per_point, self.confocal_home)
        QWidget.setTabOrder(self.confocal_home, self.confocal_start)
        QWidget.setTabOrder(self.confocal_start, self.x_fix)
        QWidget.setTabOrder(self.x_fix, self.btn_3_control)
        QWidget.setTabOrder(self.btn_3_control, self.toggleButton)
        QWidget.setTabOrder(self.toggleButton, self.z_fix)
        QWidget.setTabOrder(self.z_fix, self.confocal_position_x)
        QWidget.setTabOrder(self.confocal_position_x, self.maximizeRestoreAppBtn)
        QWidget.setTabOrder(self.maximizeRestoreAppBtn, self.confocal_position_z)
        QWidget.setTabOrder(self.confocal_position_z, self.btn_adjustments)
        QWidget.setTabOrder(self.btn_adjustments, self.y_fix)
        QWidget.setTabOrder(self.y_fix, self.btn_share)
        QWidget.setTabOrder(self.btn_share, self.closeAppBtn)
        QWidget.setTabOrder(self.closeAppBtn, self.confocal_position_y)
        QWidget.setTabOrder(self.confocal_position_y, self.btn_1_confocal)
        QWidget.setTabOrder(self.btn_1_confocal, self.btn_2_magnet)
        QWidget.setTabOrder(self.btn_2_magnet, self.confocal_moveto)
        QWidget.setTabOrder(self.confocal_moveto, self.verticalSlider_2)
        QWidget.setTabOrder(self.verticalSlider_2, self.confocal_counts)
        QWidget.setTabOrder(self.confocal_counts, self.btn_logout)
        QWidget.setTabOrder(self.btn_logout, self.btn_print)
        QWidget.setTabOrder(self.btn_print, self.btn_message)
        QWidget.setTabOrder(self.btn_message, self.autofocus_01)
        QWidget.setTabOrder(self.autofocus_01, self.autofocus_005)
        QWidget.setTabOrder(self.autofocus_005, self.autofocus_001)
        QWidget.setTabOrder(self.autofocus_001, self.autofocus_start)
        QWidget.setTabOrder(self.autofocus_start, self.autofocus_save)
        QWidget.setTabOrder(self.autofocus_save, self.magnet_save_2)
        QWidget.setTabOrder(self.magnet_save_2, self.magnet_load)
        QWidget.setTabOrder(self.magnet_load, self.magnet_counts)
        QWidget.setTabOrder(self.magnet_counts, self.magnet_per_point)
        QWidget.setTabOrder(self.magnet_per_point, self.magnet_start)
        QWidget.setTabOrder(self.magnet_start, self.magnet_size)
        QWidget.setTabOrder(self.magnet_size, self.magnet_step)
        QWidget.setTabOrder(self.magnet_step, self.magnet_position_x)
        QWidget.setTabOrder(self.magnet_position_x, self.magnet_position_y)
        QWidget.setTabOrder(self.magnet_position_y, self.magnet_position_z)
        QWidget.setTabOrder(self.magnet_position_z, self.magnet_set_position_x)
        QWidget.setTabOrder(self.magnet_set_position_x, self.magnet_set_position_y)
        QWidget.setTabOrder(self.magnet_set_position_y, self.magnet_set_position_z)
        QWidget.setTabOrder(self.magnet_set_position_z, self.magnet_moveto)
        QWidget.setTabOrder(self.magnet_moveto, self.magnet_jog_backward_z)
        QWidget.setTabOrder(self.magnet_jog_backward_z, self.magnet_jog_foward_y)
        QWidget.setTabOrder(self.magnet_jog_foward_y, self.magnet_jog_backward_x)
        QWidget.setTabOrder(self.magnet_jog_backward_x, self.magnet_jog_backward_y)
        QWidget.setTabOrder(self.magnet_jog_backward_y, self.magnet_jog_foward_z)
        QWidget.setTabOrder(self.magnet_jog_foward_z, self.magnet_jog_foward_x)
        QWidget.setTabOrder(self.magnet_jog_foward_x, self.magnet_step_jog)
        QWidget.setTabOrder(self.magnet_step_jog, self.control_type)
        QWidget.setTabOrder(self.control_type, self.control_params)
        QWidget.setTabOrder(self.control_params, self.control_start)
        QWidget.setTabOrder(self.control_start, self.autofocus_in)
        QWidget.setTabOrder(self.autofocus_in, self.fit_from)
        QWidget.setTabOrder(self.fit_from, self.control_stop)
        QWidget.setTabOrder(self.control_stop, self.reps)
        QWidget.setTabOrder(self.reps, self.fit_to)
        QWidget.setTabOrder(self.fit_to, self.fit_result)
        QWidget.setTabOrder(self.fit_result, self.control_fitting)
        QWidget.setTabOrder(self.control_fitting, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.verticalSlider)
        QWidget.setTabOrder(self.verticalSlider, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.plainTextEdit)
        QWidget.setTabOrder(self.plainTextEdit, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.commandLinkButton)
        QWidget.setTabOrder(self.commandLinkButton, self.horizontalSlider)
        QWidget.setTabOrder(self.horizontalSlider, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.pushButton_spin_photon_start)
        QWidget.setTabOrder(self.pushButton_spin_photon_start, self.comboBox_laser_CH1)
        QWidget.setTabOrder(self.comboBox_laser_CH1, self.comboBox_laser_CH2)
        QWidget.setTabOrder(self.comboBox_laser_CH2, self.comboBox_WLM_ch1)
        QWidget.setTabOrder(self.comboBox_WLM_ch1, self.comboBox_WLM_ch2)
        QWidget.setTabOrder(self.comboBox_WLM_ch2, self.pushButton_CH1_connect)
        QWidget.setTabOrder(self.pushButton_CH1_connect, self.pushButton_CH2_connect)
        QWidget.setTabOrder(self.pushButton_CH2_connect, self.pushButton_laserlock_button_1)
        QWidget.setTabOrder(self.pushButton_laserlock_button_1, self.pushButton_laserlock_button_2)
        QWidget.setTabOrder(self.pushButton_laserlock_button_2, self.pushButton_change_wavelength_1)
        QWidget.setTabOrder(self.pushButton_change_wavelength_1, self.pushButton_change_wavelength_2)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"PyDracula", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Modern GUI / Flat Style", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_1_confocal.setText(QCoreApplication.translate("MainWindow", u"Confocal", None))
        self.btn_2_magnet.setText(QCoreApplication.translate("MainWindow", u"Magnet", None))
        self.btn_3_control.setText(QCoreApplication.translate("MainWindow", u"Control", None))
        self.btn_4_PLE.setText(QCoreApplication.translate("MainWindow", u"PLE", None))
        self.btn_5_entangle.setText(QCoreApplication.translate("MainWindow", u"Entangle", None))
        self.btn_6_T1.setText(QCoreApplication.translate("MainWindow", u"T1", None))
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
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#ff79c6;\">PyDracula</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#ffffff;\">An interface created using Python and PySi"
                        "de (support for PyQt), and with colors based on the Dracula theme created by Zeno Rocha.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#ffffff;\">MIT License</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:10pt; color:#bd93f9;\">Created by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#ff79c6;\">Convert UI</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:"
                        "'Segoe UI'; color:#ffffff;\">pyside6-uic main.ui &gt; ui_main.py</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#ff79c6;\">Convert QRC</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; color:#ffffff;\">pyside6-rcc resources.qrc -o resources_rc.py</span></p></body></html>", None))
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
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Confocal", None))
        self.radioButto__CW_PSB.setText(QCoreApplication.translate("MainWindow", u"CW_PSB", None))
        self.radioButton_CW_ZPL.setText(QCoreApplication.translate("MainWindow", u"CW_ZPL", None))
        self.radioButton_PUL_PSB_GR.setText(QCoreApplication.translate("MainWindow", u"PUL_PSB_GR", None))
        self.radioButton_PUL_ZPL_GR.setText(QCoreApplication.translate("MainWindow", u"PUL_ZPL_GR", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.confocal_resolution.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Per point (sec)", None))
        self.confocal_T_per_point.setText(QCoreApplication.translate("MainWindow", u"0.01", None))
        self.confocal_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.confocal_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.x_fix.setText(QCoreApplication.translate("MainWindow", u"x axis", None))
        self.confocal_to_x.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.confocal_set_position_x.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.confocal_from_x.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.z_fix.setText(QCoreApplication.translate("MainWindow", u"z axis", None))
        self.confocal_position_x.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>From (\u03bcm)</p></body></html>", None))
        self.confocal_from_z.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.confocal_position_z.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.confocal_set_position_z.setText(QCoreApplication.translate("MainWindow", u"57", None))
        self.y_fix.setText(QCoreApplication.translate("MainWindow", u"y axis", None))
        self.confocal_set_position_y.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Position", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Axis fix", None))
        self.confocal_to_z.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.confocal_position_y.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"To (\u03bcm)", None))
        self.confocal_from_y.setText(QCoreApplication.translate("MainWindow", u"11", None))
        self.confocal_to_y.setText(QCoreApplication.translate("MainWindow", u"17", None))
        self.confocal_moveto.setText(QCoreApplication.translate("MainWindow", u" Move to ", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Counts (kcps)", None))
        self.confocal_counts.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.autofocus_size_z.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Size (\u03bcm)", None))
        self.confocal_step_z.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"x y axis", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"z axis", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Step (\u03bcm)", None))
        self.confocal_step_xy.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.autofocus_size_xy.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.autofocus_01.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.autofocus_005.setText(QCoreApplication.translate("MainWindow", u"0.05", None))
        self.autofocus_001.setText(QCoreApplication.translate("MainWindow", u"0.01", None))
        self.autofocus_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.autofocus_save.setText(QCoreApplication.translate("MainWindow", u" Save", None))
        self.counter_laser_on.setText(QCoreApplication.translate("MainWindow", u"Green Laser on", None))
        self.counter_laser_on_2.setText(QCoreApplication.translate("MainWindow", u"Red 1 Laser on", None))
        self.counter_laser_on_3.setText(QCoreApplication.translate("MainWindow", u"Red 2 Laser on", None))
        self.counter_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton_AutoAlign_red.setText(QCoreApplication.translate("MainWindow", u"red AutoAlign start", None))
        self.pushButton_AutoAlign_zpl.setText(QCoreApplication.translate("MainWindow", u"zpl AutoAlign start", None))
        self.counter_average_counts.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.counter_laser_power.setText(QCoreApplication.translate("MainWindow", u"35000", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Standrad deviation", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"AutoAlign step", None))
        self.counter_counts.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Current counts (kcps)", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Per second (sec)", None))
        self.counter_autoAlign_stepSize.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.counter_laser_power_4.setText(QCoreApplication.translate("MainWindow", u"Laser power (a.u.)", None))
        self.counter_trace_length.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Average counts (kcps)", None))
        self.counter_T_per_sec.setText(QCoreApplication.translate("MainWindow", u"0.05", None))
        self.counter_standard_deviation.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Trace length (sec)", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Auto Align per sec", None))
        self.counter_AA_per_sec.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.pushButton_pulse_gen.setText(QCoreApplication.translate("MainWindow", u"pulse gen", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Magnetic field alignment", None))
        self.magnet_save_2.setText(QCoreApplication.translate("MainWindow", u" Save image", None))
        self.magnet_load.setText(QCoreApplication.translate("MainWindow", u" Load image", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Counts (kcps)", None))
        self.magnet_counts.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Per point (sec)", None))
        self.magnet_per_point.setText(QCoreApplication.translate("MainWindow", u"0.5", None))
        self.magnet_start.setText(QCoreApplication.translate("MainWindow", u" Start", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Step (mm)", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"xz axis", None))
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
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Resonant", None))
        self.comboBox_WLM_ch1.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_WLM_ch1.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_WLM_ch1.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_WLM_ch1.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_WLM_ch1.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_WLM_ch1.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_WLM_ch1.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_WLM_ch1.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))

        self.label_CH2_curr_WL.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_CH2_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.comboBox_laser_CH2.setItemText(0, QCoreApplication.translate("MainWindow", u"Newport", None))
        self.comboBox_laser_CH2.setItemText(1, QCoreApplication.translate("MainWindow", u"DLC1", None))
        self.comboBox_laser_CH2.setItemText(2, QCoreApplication.translate("MainWindow", u"DLC2", None))

        self.label_laser_ch2.setText(QCoreApplication.translate("MainWindow", u"Laser channel 2", None))
        self.label_PLE_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Device choice</span></p></body></html>", None))
        self.lineEdit_changeWL_CH1.setText(QCoreApplication.translate("MainWindow", u"637", None))
        self.lineEdit_changeWL_CH1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton_laserlock_button_1.setText(QCoreApplication.translate("MainWindow", u"laser lock", None))
        self.lineEdit_laserLock_CH1.setText(QCoreApplication.translate("MainWindow", u"637", None))
        self.lineEdit_laserLock_CH1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton_CH1_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_CH1_curr_WL.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_PLE_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:16pt;\">Laser control</span></p></body></html>", None))
        self.label_CH1_laserLock.setText(QCoreApplication.translate("MainWindow", u"WL(nm)", None))
        self.label_CH1_laserLock_5.setText(QCoreApplication.translate("MainWindow", u"laser Lock", None))
        self.comboBox_laser_CH1.setItemText(0, QCoreApplication.translate("MainWindow", u"Newport", None))
        self.comboBox_laser_CH1.setItemText(1, QCoreApplication.translate("MainWindow", u"DLC1", None))
        self.comboBox_laser_CH1.setItemText(2, QCoreApplication.translate("MainWindow", u"DLC2", None))

        self.comboBox_laser_CH1.setPlaceholderText("")
        self.label_CH1_laserLock_4.setText(QCoreApplication.translate("MainWindow", u"change wavelength", None))
        self.label_CH1_laserLock_2.setText(QCoreApplication.translate("MainWindow", u"WL(nm)", None))
        self.lineEdit_laserLock_CH2.setText(QCoreApplication.translate("MainWindow", u"637", None))
        self.lineEdit_laserLock_CH2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.label_laser_ch1.setText(QCoreApplication.translate("MainWindow", u"Laser channel 1", None))
        self.pushButton_change_wavelength_2.setText(QCoreApplication.translate("MainWindow", u"change WL", None))
        self.lineEdit_changeWL_CH2.setText(QCoreApplication.translate("MainWindow", u"637", None))
        self.lineEdit_changeWL_CH2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.label_start_WL_2.setText(QCoreApplication.translate("MainWindow", u"Laser source", None))
        self.label_CH1_laserLock_3.setText(QCoreApplication.translate("MainWindow", u"Current WL", None))
        self.comboBox_WLM_ch2.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_WLM_ch2.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_WLM_ch2.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_WLM_ch2.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_WLM_ch2.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_WLM_ch2.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_WLM_ch2.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_WLM_ch2.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))

        self.label_start_WL_3.setText(QCoreApplication.translate("MainWindow", u"WLM ch", None))
        self.pushButton_change_wavelength_1.setText(QCoreApplication.translate("MainWindow", u"change WL", None))
        self.pushButton_laserlock_button_2.setText(QCoreApplication.translate("MainWindow", u"laser lock", None))
        self.label_PLE.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">PLE scan</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Start WL(nm)", None))
        self.lineEdit_PLE_repeat.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.lineEdit_PLE_step.setText(QCoreApplication.translate("MainWindow", u"0.02", None))
        self.pushButton_PLE_repeat.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.lineEdit_PLE_end.setText(QCoreApplication.translate("MainWindow", u"637.225", None))
        self.lineEdit_PLE_start.setText(QCoreApplication.translate("MainWindow", u"637.195", None))
        self.radioButton_PLE_CH1.setText(QCoreApplication.translate("MainWindow", u"CH1", None))
        self.radioButton_PLE_CH2.setText(QCoreApplication.translate("MainWindow", u"CH2", None))
        self.pushButton_PLE_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"END WL(nm)", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"PLE steps", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Repeat PLE(N)", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"PLE", None))
        self.label_PLE_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Wavelength scan</span></p></body></html>", None))
        self.radioButton_WL_scan_CH1.setText(QCoreApplication.translate("MainWindow", u"CH1", None))
        self.radioButton_WL_scan_CH2.setText(QCoreApplication.translate("MainWindow", u"CH2", None))
        self.pushButton_wavelength_scan_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_start_WL_4.setText(QCoreApplication.translate("MainWindow", u"Start Voltage(V)", None))
        self.lineEdit_WL_start_voltage.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lineEdit_WL_start_voltage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.label_end_WL_2.setText(QCoreApplication.translate("MainWindow", u"End Voltage(V)", None))
        self.lineEdit_WL_end_voltage.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.lineEdit_WL_end_voltage.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.label_end_WL_3.setText(QCoreApplication.translate("MainWindow", u"Step Size(V)", None))
        self.lineEdit_WL_step_size.setText(QCoreApplication.translate("MainWindow", u"0.4", None))
        self.lineEdit_WL_step_size.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton_spin_photon_start.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Entanglement", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"spin-photon Ent", None))
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

        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"By: \ubc30\uace0\ud508 \uc18c\ud06c\ub77c\ud14c\uc2a4\ubcf4\ub2e4 \ubc30\ubd80\ub978 \uc18c\ud06c\ub77c\ud14c\uc2a4\uac00 \ub0ab\ub2e4", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v 1.0", None))
    # retranslateUi

