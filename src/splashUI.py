# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

from src.widgets.progress import CircularProgress
import mpsat_rc

class Ui_Splash(object):
    def setupUi(self, Splash):
        if not Splash.objectName():
            Splash.setObjectName(u"Splash")
        Splash.resize(680, 399)
        self.centralwidget = QWidget(Splash)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
"	background-color: #065279;	\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"} ")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 90, 661, 61))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: #FFFFFF;")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 150, 661, 31))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: #d6ecf0;")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = CircularProgress(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(290, 210, 80, 80))
        self.progressBar.setLayoutDirection(Qt.LeftToRight)
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: #0a3b56;\n"
"	color: #FFFFFF;\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: #e3f9fd;\n"
"}")
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 320, 661, 21))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"color: #e3f9fd;")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(20, 350, 621, 21))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        self.label_credits.setFont(font3)
        self.label_credits.setStyleSheet(u"color: #f3f9f1;")
        self.label_credits.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame_btns = QFrame(self.dropShadowFrame)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setGeometry(QRect(610, 10, 51, 21))
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setStyleSheet(u"border: none;")
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"    color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icon/micons/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)
        self.btn_minimize.setIconSize(QSize(12, 12))
        self.btn_minimize.setAutoDefault(False)

        self.horizontalLayout_3.addWidget(self.btn_minimize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"    color: #FFFFFF;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {		\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/micons/close.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setIconSize(QSize(12, 12))

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.verticalLayout.addWidget(self.dropShadowFrame)

        Splash.setCentralWidget(self.centralwidget)

        self.retranslateUi(Splash)

        QMetaObject.connectSlotsByName(Splash)
    # setupUi

    def retranslateUi(self, Splash):
        Splash.setWindowTitle(QCoreApplication.translate("Splash", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("Splash", u"<html><head/><body><p>mPSAT</p></body></html>", None))
        self.label_description.setText(QCoreApplication.translate("Splash", u"<html><head/><body><p>(micro)Plastic Spectroscopy Analyze Tool</p></body></html>", None))
        self.progressBar.setFormat(QCoreApplication.translate("Splash", u"0", None))
        self.label_loading.setText(QCoreApplication.translate("Splash", u"<html><head/><body><p><span style=\" font-size:12pt;\">Loading...</span></p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("Splash", u"<html><head/><body><p><span style=\" font-weight:700;\">By zhengGroup @ LZU</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("Splash", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("Splash", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
    # retranslateUi

