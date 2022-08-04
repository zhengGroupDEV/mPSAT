# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'busy_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QWidget)

from src.widgets.progress import CircularProgress

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(230, 160)
        font = QFont()
        font.setFamilies([u"MiSans Demibold"])
        Dialog.setFont(font)
        Dialog.setStyleSheet(u"background-color: rgb(233, 241, 246);")
        self.progressBar = CircularProgress(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(70, 20, 100, 100))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: #395260;\n"
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
        self.progressBar.setValue(-1)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.label_info = QLabel(Dialog)
        self.label_info.setObjectName(u"label_info")
        self.label_info.setGeometry(QRect(12, 128, 211, 21))
        sizePolicy.setHeightForWidth(self.label_info.sizePolicy().hasHeightForWidth())
        self.label_info.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"MiSans Demibold"])
        font1.setPointSize(11)
        self.label_info.setFont(font1)
        self.label_info.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_info.setText(QCoreApplication.translate("Dialog", u"Loading...", None))
    # retranslateUi

