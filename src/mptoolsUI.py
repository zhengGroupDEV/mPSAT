# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mptoolsUI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSplitter, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
    QWidget)

from matplotlib.backends.backend_qtagg import NavigationToolbar2QT
from src.customWidgets import QFigureCanvas
import mptools_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(884, 677)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/imgs/resources/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(11)
        self.centralwidget.setFont(font)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 6)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWelcome = QWidget()
        self.tabWelcome.setObjectName(u"tabWelcome")
        self.gridLayout_14 = QGridLayout(self.tabWelcome)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 2, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.textBrowser = QTextBrowser(self.tabWelcome)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setSource(QUrl(u"qrc:/markdown/README.md"))

        self.verticalLayout_6.addWidget(self.textBrowser)


        self.gridLayout_14.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabWelcome, "")
        self.tabInputMeta = QWidget()
        self.tabInputMeta.setObjectName(u"tabInputMeta")
        self.gridLayout_7 = QGridLayout(self.tabInputMeta)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox_2 = QGroupBox(self.tabInputMeta)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMaximumSize)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setToolTipDuration(1000)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.cboxModifyTable = QComboBox(self.groupBox_2)
        self.cboxModifyTable.setObjectName(u"cboxModifyTable")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cboxModifyTable)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.leditSname = QLineEdit(self.groupBox_2)
        self.leditSname.setObjectName(u"leditSname")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.leditSname)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.leditInsturment = QLineEdit(self.groupBox_2)
        self.leditInsturment.setObjectName(u"leditInsturment")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.leditInsturment)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.leditResolution = QLineEdit(self.groupBox_2)
        self.leditResolution.setObjectName(u"leditResolution")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.leditResolution)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.leditColor = QLineEdit(self.groupBox_2)
        self.leditColor.setObjectName(u"leditColor")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.leditColor)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_6)

        self.leditSource = QLineEdit(self.groupBox_2)
        self.leditSource.setObjectName(u"leditSource")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.leditSource)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_7)

        self.leditNote = QLineEdit(self.groupBox_2)
        self.leditNote.setObjectName(u"leditNote")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.leditNote)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnSubmit = QPushButton(self.groupBox_2)
        self.btnSubmit.setObjectName(u"btnSubmit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnSubmit.sizePolicy().hasHeightForWidth())
        self.btnSubmit.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.btnSubmit)

        self.btnClear = QPushButton(self.groupBox_2)
        self.btnClear.setObjectName(u"btnClear")
        sizePolicy2.setHeightForWidth(self.btnClear.sizePolicy().hasHeightForWidth())
        self.btnClear.setSizePolicy(sizePolicy2)
        self.btnClear.setCursor(QCursor(Qt.ArrowCursor))
        self.btnClear.setToolTipDuration(1000)

        self.horizontalLayout.addWidget(self.btnClear)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.formLayout.setLayout(8, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_9)

        self.tbroswerLog = QTextBrowser(self.groupBox_2)
        self.tbroswerLog.setObjectName(u"tbroswerLog")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.tbroswerLog)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.cboxMPID = QComboBox(self.groupBox_2)
        self.cboxMPID.setObjectName(u"cboxMPID")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cboxMPID.sizePolicy().hasHeightForWidth())
        self.cboxMPID.setSizePolicy(sizePolicy3)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cboxMPID)


        self.gridLayout_3.addLayout(self.formLayout, 0, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.groupBox = QGroupBox(self.tabInputMeta)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy4)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.leditHost = QLineEdit(self.groupBox)
        self.leditHost.setObjectName(u"leditHost")
        sizePolicy4.setHeightForWidth(self.leditHost.sizePolicy().hasHeightForWidth())
        self.leditHost.setSizePolicy(sizePolicy4)
        self.leditHost.setClearButtonEnabled(False)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.leditHost)

        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")
        sizePolicy4.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy4)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_16)

        self.leditUsername = QLineEdit(self.groupBox)
        self.leditUsername.setObjectName(u"leditUsername")
        sizePolicy4.setHeightForWidth(self.leditUsername.sizePolicy().hasHeightForWidth())
        self.leditUsername.setSizePolicy(sizePolicy4)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.leditUsername)


        self.horizontalLayout_6.addLayout(self.formLayout_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.leditPort = QLineEdit(self.groupBox)
        self.leditPort.setObjectName(u"leditPort")
        sizePolicy4.setHeightForWidth(self.leditPort.sizePolicy().hasHeightForWidth())
        self.leditPort.setSizePolicy(sizePolicy4)
        self.leditPort.setInputMask(u"")
        self.leditPort.setText(u"3306")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.leditPort)

        self.label_17 = QLabel(self.groupBox)
        self.label_17.setObjectName(u"label_17")
        sizePolicy4.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy4)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_17)

        self.leditPassword = QLineEdit(self.groupBox)
        self.leditPassword.setObjectName(u"leditPassword")
        sizePolicy4.setHeightForWidth(self.leditPassword.sizePolicy().hasHeightForWidth())
        self.leditPassword.setSizePolicy(sizePolicy4)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.leditPassword)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        sizePolicy4.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy4)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_11)


        self.horizontalLayout_6.addLayout(self.formLayout_3)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        sizePolicy4.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy4)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_14)

        self.leditDatabase = QLineEdit(self.groupBox)
        self.leditDatabase.setObjectName(u"leditDatabase")
        sizePolicy4.setHeightForWidth(self.leditDatabase.sizePolicy().hasHeightForWidth())
        self.leditDatabase.setSizePolicy(sizePolicy4)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.leditDatabase)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")
        sizePolicy4.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy4)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_18)

        self.cboxDBtype = QComboBox(self.groupBox)
        self.cboxDBtype.addItem("")
        self.cboxDBtype.addItem("")
        self.cboxDBtype.setObjectName(u"cboxDBtype")
        sizePolicy4.setHeightForWidth(self.cboxDBtype.sizePolicy().hasHeightForWidth())
        self.cboxDBtype.setSizePolicy(sizePolicy4)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.cboxDBtype)


        self.horizontalLayout_6.addLayout(self.formLayout_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.btnSaveDBConfig = QPushButton(self.groupBox)
        self.btnSaveDBConfig.setObjectName(u"btnSaveDBConfig")
        sizePolicy3.setHeightForWidth(self.btnSaveDBConfig.sizePolicy().hasHeightForWidth())
        self.btnSaveDBConfig.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.btnSaveDBConfig)

        self.btnLoadDBConfig = QPushButton(self.groupBox)
        self.btnLoadDBConfig.setObjectName(u"btnLoadDBConfig")
        sizePolicy3.setHeightForWidth(self.btnLoadDBConfig.sizePolicy().hasHeightForWidth())
        self.btnLoadDBConfig.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.btnLoadDBConfig)

        self.btnClearDBConfig = QPushButton(self.groupBox)
        self.btnClearDBConfig.setObjectName(u"btnClearDBConfig")
        sizePolicy3.setHeightForWidth(self.btnClearDBConfig.sizePolicy().hasHeightForWidth())
        self.btnClearDBConfig.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.btnClearDBConfig)

        self.btnConnectDB = QPushButton(self.groupBox)
        self.btnConnectDB.setObjectName(u"btnConnectDB")
        self.btnConnectDB.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.btnConnectDB.sizePolicy().hasHeightForWidth())
        self.btnConnectDB.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.btnConnectDB)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)

        self.line = QFrame(self.tabInputMeta)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabInputMeta, "")
        self.tabSpectra = QWidget()
        self.tabSpectra.setObjectName(u"tabSpectra")
        self.gridLayout_9 = QGridLayout(self.tabSpectra)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(6)
        self.gridLayout_9.setContentsMargins(1, 1, 1, 1)
        self.tabWidget_2 = QTabWidget(self.tabSpectra)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setTabPosition(QTabWidget.North)
        self.tabWidget_2.setTabShape(QTabWidget.Rounded)
        self.tabOSpecProcess = QWidget()
        self.tabOSpecProcess.setObjectName(u"tabOSpecProcess")
        self.gridLayout_19 = QGridLayout(self.tabOSpecProcess)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_3 = QGroupBox(self.tabOSpecProcess)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy3.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy3)
        self.gridLayout_10 = QGridLayout(self.groupBox_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.cboxPreSpecType = QComboBox(self.groupBox_3)
        self.cboxPreSpecType.addItem("")
        self.cboxPreSpecType.addItem("")
        self.cboxPreSpecType.setObjectName(u"cboxPreSpecType")
        sizePolicy3.setHeightForWidth(self.cboxPreSpecType.sizePolicy().hasHeightForWidth())
        self.cboxPreSpecType.setSizePolicy(sizePolicy3)

        self.gridLayout_10.addWidget(self.cboxPreSpecType, 0, 3, 1, 1)

        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")
        sizePolicy2.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy2)

        self.gridLayout_10.addWidget(self.label_22, 0, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelSelectedFile = QLabel(self.groupBox_3)
        self.labelSelectedFile.setObjectName(u"labelSelectedFile")
        self.labelSelectedFile.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.labelSelectedFile.sizePolicy().hasHeightForWidth())
        self.labelSelectedFile.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.labelSelectedFile)

        self.btnSelectFile = QPushButton(self.groupBox_3)
        self.btnSelectFile.setObjectName(u"btnSelectFile")
        sizePolicy2.setHeightForWidth(self.btnSelectFile.sizePolicy().hasHeightForWidth())
        self.btnSelectFile.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.btnSelectFile)


        self.gridLayout_10.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_5, 0, 4, 1, 1)

        self.line_2 = QFrame(self.groupBox_3)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_10.addWidget(self.line_2, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.tabOSpecProcess)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy3.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy3)
        self.gridLayout_11 = QGridLayout(self.groupBox_4)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_21 = QLabel(self.groupBox_4)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_5.addWidget(self.label_21)

        self.cboxPreAdjustment = QComboBox(self.groupBox_4)
        self.cboxPreAdjustment.addItem("")
        self.cboxPreAdjustment.addItem("")
        self.cboxPreAdjustment.addItem("")
        self.cboxPreAdjustment.setObjectName(u"cboxPreAdjustment")
        sizePolicy3.setHeightForWidth(self.cboxPreAdjustment.sizePolicy().hasHeightForWidth())
        self.cboxPreAdjustment.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.cboxPreAdjustment)

        self.ckbox_adjneg = QCheckBox(self.groupBox_4)
        self.ckbox_adjneg.setObjectName(u"ckbox_adjneg")
        self.ckbox_adjneg.setChecked(False)

        self.horizontalLayout_5.addWidget(self.ckbox_adjneg)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.btnPreSave = QPushButton(self.groupBox_4)
        self.btnPreSave.setObjectName(u"btnPreSave")
        sizePolicy3.setHeightForWidth(self.btnPreSave.sizePolicy().hasHeightForWidth())
        self.btnPreSave.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.btnPreSave)


        self.gridLayout_11.addLayout(self.verticalLayout_2, 0, 2, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.sliderPreSmooth = QSlider(self.groupBox_4)
        self.sliderPreSmooth.setObjectName(u"sliderPreSmooth")
        self.sliderPreSmooth.setMinimum(0)
        self.sliderPreSmooth.setMaximum(7)
        self.sliderPreSmooth.setPageStep(1)
        self.sliderPreSmooth.setValue(3)
        self.sliderPreSmooth.setOrientation(Qt.Horizontal)
        self.sliderPreSmooth.setTickPosition(QSlider.TicksBelow)
        self.sliderPreSmooth.setTickInterval(1)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.sliderPreSmooth)

        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.sliderPreBaseline = QSlider(self.groupBox_4)
        self.sliderPreBaseline.setObjectName(u"sliderPreBaseline")
        self.sliderPreBaseline.setMaximum(20)
        self.sliderPreBaseline.setValue(8)
        self.sliderPreBaseline.setOrientation(Qt.Horizontal)
        self.sliderPreBaseline.setTickPosition(QSlider.TicksBelow)
        self.sliderPreBaseline.setTickInterval(1)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.sliderPreBaseline)


        self.horizontalLayout_3.addLayout(self.formLayout_6)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelPreSmooth = QLabel(self.groupBox_4)
        self.labelPreSmooth.setObjectName(u"labelPreSmooth")
        sizePolicy2.setHeightForWidth(self.labelPreSmooth.sizePolicy().hasHeightForWidth())
        self.labelPreSmooth.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.labelPreSmooth)

        self.labelPreBaseline = QLabel(self.groupBox_4)
        self.labelPreBaseline.setObjectName(u"labelPreBaseline")
        sizePolicy2.setHeightForWidth(self.labelPreBaseline.sizePolicy().hasHeightForWidth())
        self.labelPreBaseline.setSizePolicy(sizePolicy2)

        self.verticalLayout_3.addWidget(self.labelPreBaseline)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.line_3 = QFrame(self.groupBox_4)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_3)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_19 = QLabel(self.groupBox_4)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_19)

        self.leditPreMin = QLineEdit(self.groupBox_4)
        self.leditPreMin.setObjectName(u"leditPreMin")
        sizePolicy2.setHeightForWidth(self.leditPreMin.sizePolicy().hasHeightForWidth())
        self.leditPreMin.setSizePolicy(sizePolicy2)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.leditPreMin)

        self.label_20 = QLabel(self.groupBox_4)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_20)

        self.leditPreMax = QLineEdit(self.groupBox_4)
        self.leditPreMax.setObjectName(u"leditPreMax")
        sizePolicy2.setHeightForWidth(self.leditPreMax.sizePolicy().hasHeightForWidth())
        self.leditPreMax.setSizePolicy(sizePolicy2)

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.leditPreMax)


        self.horizontalLayout_3.addLayout(self.formLayout_5)


        self.gridLayout_11.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.line_4 = QFrame(self.groupBox_4)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_11.addWidget(self.line_4, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.figOspPre = QFigureCanvas()
        self.figOspPre.setObjectName(u"figOspPre")
        self.figOspPre.setEnabled(True)
        sizePolicy.setHeightForWidth(self.figOspPre.sizePolicy().hasHeightForWidth())
        self.figOspPre.setSizePolicy(sizePolicy)
        self.figToolbarOspPre = NavigationToolbar2QT(self.figOspPre, self)
        self.figToolbarOspPre.setObjectName(u"figToolbarOspPre")
        self.figToolbarOspPre.setEnabled(True)
        self.figToolbarOspPre.setGeometry(QRect(-10, 20, 842, 10))

        self.verticalLayout_7.addWidget(self.figToolbarOspPre, stretch=1)
        self.verticalLayout_7.addWidget(self.figOspPre, stretch=200)


        self.verticalLayout.addLayout(self.verticalLayout_7)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pbarOSpPre = QProgressBar(self.tabOSpecProcess)
        self.pbarOSpPre.setObjectName(u"pbarOSpPre")
        self.pbarOSpPre.setStyleSheet(u"#pbarOSpPre {\n"
"    border: 2px solid #2196F3;/*\u8fb9\u6846\u4ee5\u53ca\u8fb9\u6846\u989c\u8272*/\n"
"    border-radius: 5px;\n"
"    background-color: #FFFFFF;\n"
"}\n"
"#pbarOSpPre::chunk {\n"
"    background-color: #2196F3;\n"
"    width: 50px; /*\u533a\u5757\u5bbd\u5ea6*/\n"
"    margin: 1px;\n"
"}")
        self.pbarOSpPre.setMinimum(0)
        self.pbarOSpPre.setMaximum(100)
        self.pbarOSpPre.setValue(0)
        self.pbarOSpPre.setTextVisible(False)
        self.pbarOSpPre.setInvertedAppearance(False)

        self.horizontalLayout_7.addWidget(self.pbarOSpPre)

        self.btn_stop_pre = QPushButton(self.tabOSpecProcess)
        self.btn_stop_pre.setObjectName(u"btn_stop_pre")

        self.horizontalLayout_7.addWidget(self.btn_stop_pre)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.gridLayout_19.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tabOSpecProcess, "")
        self.tabOSpecMatch = QWidget()
        self.tabOSpecMatch.setObjectName(u"tabOSpecMatch")
        self.gridLayout_12 = QGridLayout(self.tabOSpecMatch)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_5 = QGroupBox(self.tabOSpecMatch)
        self.groupBox_5.setObjectName(u"groupBox_5")
        sizePolicy3.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy3)
        self.gridLayout_13 = QGridLayout(self.groupBox_5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.label_23 = QLabel(self.groupBox_5)
        self.label_23.setObjectName(u"label_23")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy5)

        self.horizontalLayout_8.addWidget(self.label_23)

        self.cboxMatchType = QComboBox(self.groupBox_5)
        self.cboxMatchType.addItem("")
        self.cboxMatchType.addItem("")
        self.cboxMatchType.setObjectName(u"cboxMatchType")
        sizePolicy3.setHeightForWidth(self.cboxMatchType.sizePolicy().hasHeightForWidth())
        self.cboxMatchType.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.cboxMatchType)

        self.line_5 = QFrame(self.groupBox_5)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_5)

        self.label_24 = QLabel(self.groupBox_5)
        self.label_24.setObjectName(u"label_24")
        sizePolicy5.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy5)

        self.horizontalLayout_8.addWidget(self.label_24)

        self.cboxMatchAnalyze = QComboBox(self.groupBox_5)
        self.cboxMatchAnalyze.addItem("")
        self.cboxMatchAnalyze.addItem("")
        self.cboxMatchAnalyze.setObjectName(u"cboxMatchAnalyze")
        sizePolicy3.setHeightForWidth(self.cboxMatchAnalyze.sizePolicy().hasHeightForWidth())
        self.cboxMatchAnalyze.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.cboxMatchAnalyze)

        self.line_6 = QFrame(self.groupBox_5)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_6)

        self.label_25 = QLabel(self.groupBox_5)
        self.label_25.setObjectName(u"label_25")
        sizePolicy5.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy5)

        self.horizontalLayout_8.addWidget(self.label_25)

        self.cboxMatchRegion = QComboBox(self.groupBox_5)
        self.cboxMatchRegion.addItem("")
        self.cboxMatchRegion.addItem("")
        self.cboxMatchRegion.setObjectName(u"cboxMatchRegion")
        sizePolicy3.setHeightForWidth(self.cboxMatchRegion.sizePolicy().hasHeightForWidth())
        self.cboxMatchRegion.setSizePolicy(sizePolicy3)

        self.horizontalLayout_8.addWidget(self.cboxMatchRegion)

        self.line_7 = QFrame(self.groupBox_5)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_7)

        self.label_26 = QLabel(self.groupBox_5)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_8.addWidget(self.label_26)

        self.cboxMatchMethod = QComboBox(self.groupBox_5)
        self.cboxMatchMethod.addItem("")
        self.cboxMatchMethod.addItem("")
        self.cboxMatchMethod.addItem("")
        self.cboxMatchMethod.setObjectName(u"cboxMatchMethod")

        self.horizontalLayout_8.addWidget(self.cboxMatchMethod)

        self.btnMatchGo = QPushButton(self.groupBox_5)
        self.btnMatchGo.setObjectName(u"btnMatchGo")

        self.horizontalLayout_8.addWidget(self.btnMatchGo)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.gridLayout_13.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.groupBox_5)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.splitter = QSplitter(self.tabOSpecMatch)
        self.splitter.setObjectName(u"splitter")
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget_3 = QWidget(self.splitter)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.figOspMatch = QFigureCanvas()
        self.figOspMatch.setObjectName(u"figOspMatch")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(10)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.figOspMatch.sizePolicy().hasHeightForWidth())
        self.figOspMatch.setSizePolicy(sizePolicy6)
        self.figToolbarOspMatch = NavigationToolbar2QT(self.figOspMatch, self)
        self.figToolbarOspMatch.setObjectName(u"figToolbarOspMatch")
        self.figToolbarOspMatch.setGeometry(QRect(0, 10, 419, 10))

        self.verticalLayout_8.addWidget(self.figToolbarOspMatch)
        self.verticalLayout_8.addWidget(self.figOspMatch)

        self.splitter.addWidget(self.verticalLayoutWidget_3)
        self.tableMatch = QTableWidget(self.splitter)
        if (self.tableMatch.columnCount() < 3):
            self.tableMatch.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableMatch.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableMatch.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableMatch.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableMatch.setObjectName(u"tableMatch")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.tableMatch.sizePolicy().hasHeightForWidth())
        self.tableMatch.setSizePolicy(sizePolicy7)
        self.tableMatch.setMinimumSize(QSize(0, 0))
        self.tableMatch.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.tableMatch.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableMatch.setSortingEnabled(True)
        self.splitter.addWidget(self.tableMatch)
        self.tableMatch.horizontalHeader().setMinimumSectionSize(50)
        self.tableMatch.horizontalHeader().setDefaultSectionSize(50)
        self.tableMatch.verticalHeader().setMinimumSectionSize(30)
        self.tableMatch.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_5.addWidget(self.splitter)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)


        self.gridLayout_12.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pbarOSpMatch = QProgressBar(self.tabOSpecMatch)
        self.pbarOSpMatch.setObjectName(u"pbarOSpMatch")
        self.pbarOSpMatch.setStyleSheet(u"#pbarOSpMatch {\n"
"    border: 2px solid #2196F3;/*\u8fb9\u6846\u4ee5\u53ca\u8fb9\u6846\u989c\u8272*/\n"
"    border-radius: 5px;\n"
"    background-color: #FFFFFF;\n"
"}\n"
"#pbarOSpMatch::chunk {\n"
"    background-color: #2196F3;\n"
"    width: 50px; /*\u533a\u5757\u5bbd\u5ea6*/\n"
"    margin: 0.5px;\n"
"}")
        self.pbarOSpMatch.setMaximum(100)
        self.pbarOSpMatch.setValue(-1)
        self.pbarOSpMatch.setTextVisible(False)

        self.horizontalLayout_9.addWidget(self.pbarOSpMatch)

        self.btn_stop_match = QPushButton(self.tabOSpecMatch)
        self.btn_stop_match.setObjectName(u"btn_stop_match")

        self.horizontalLayout_9.addWidget(self.btn_stop_match)


        self.gridLayout_12.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tabOSpecMatch, "")
        self.tabOSpecSettings = QWidget()
        self.tabOSpecSettings.setObjectName(u"tabOSpecSettings")
        self.gridLayout_17 = QGridLayout(self.tabOSpecSettings)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.groupBox_6 = QGroupBox(self.tabOSpecSettings)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy4.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy4)
        self.gridLayout_16 = QGridLayout(self.groupBox_6)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.leditOSpecSettingFTIRMeta = QLineEdit(self.groupBox_6)
        self.leditOSpecSettingFTIRMeta.setObjectName(u"leditOSpecSettingFTIRMeta")

        self.gridLayout_15.addWidget(self.leditOSpecSettingFTIRMeta, 3, 1, 1, 1)

        self.leditOSpecSettingFTIRPeaks = QLineEdit(self.groupBox_6)
        self.leditOSpecSettingFTIRPeaks.setObjectName(u"leditOSpecSettingFTIRPeaks")

        self.gridLayout_15.addWidget(self.leditOSpecSettingFTIRPeaks, 1, 1, 1, 1)

        self.label_35 = QLabel(self.groupBox_6)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_15.addWidget(self.label_35, 6, 0, 1, 1)

        self.leditOSpecSettingFTIRFull = QLineEdit(self.groupBox_6)
        self.leditOSpecSettingFTIRFull.setObjectName(u"leditOSpecSettingFTIRFull")

        self.gridLayout_15.addWidget(self.leditOSpecSettingFTIRFull, 0, 1, 1, 1)

        self.btnOSpSettingFTIRPeaks = QPushButton(self.groupBox_6)
        self.btnOSpSettingFTIRPeaks.setObjectName(u"btnOSpSettingFTIRPeaks")

        self.gridLayout_15.addWidget(self.btnOSpSettingFTIRPeaks, 1, 2, 1, 1)

        self.btnOSpSettingFTIRMetaStd = QPushButton(self.groupBox_6)
        self.btnOSpSettingFTIRMetaStd.setObjectName(u"btnOSpSettingFTIRMetaStd")

        self.gridLayout_15.addWidget(self.btnOSpSettingFTIRMetaStd, 6, 2, 1, 1)

        self.btnOSpSettingFTIRMeta = QPushButton(self.groupBox_6)
        self.btnOSpSettingFTIRMeta.setObjectName(u"btnOSpSettingFTIRMeta")

        self.gridLayout_15.addWidget(self.btnOSpSettingFTIRMeta, 3, 2, 1, 1)

        self.label_31 = QLabel(self.groupBox_6)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_15.addWidget(self.label_31, 3, 0, 1, 1)

        self.btnOSpSettingFTIRFullStd = QPushButton(self.groupBox_6)
        self.btnOSpSettingFTIRFullStd.setObjectName(u"btnOSpSettingFTIRFullStd")

        self.gridLayout_15.addWidget(self.btnOSpSettingFTIRFullStd, 4, 2, 1, 1)

        self.leditOSpecSettingFTIRFullStd = QLineEdit(self.groupBox_6)
        self.leditOSpecSettingFTIRFullStd.setObjectName(u"leditOSpecSettingFTIRFullStd")

        self.gridLayout_15.addWidget(self.leditOSpecSettingFTIRFullStd, 4, 1, 1, 1)

        self.label_30 = QLabel(self.groupBox_6)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_15.addWidget(self.label_30, 0, 0, 1, 1)

        self.leditOSpecSettingFTIRMetaStd = QLineEdit(self.groupBox_6)
        self.leditOSpecSettingFTIRMetaStd.setObjectName(u"leditOSpecSettingFTIRMetaStd")

        self.gridLayout_15.addWidget(self.leditOSpecSettingFTIRMetaStd, 6, 1, 1, 1)

        self.btnOSpSettingFTIRFull = QPushButton(self.groupBox_6)
        self.btnOSpSettingFTIRFull.setObjectName(u"btnOSpSettingFTIRFull")

        self.gridLayout_15.addWidget(self.btnOSpSettingFTIRFull, 0, 2, 1, 1)

        self.label_32 = QLabel(self.groupBox_6)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_15.addWidget(self.label_32, 1, 0, 1, 1)

        self.label_34 = QLabel(self.groupBox_6)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_15.addWidget(self.label_34, 4, 0, 1, 1)

        self.label_36 = QLabel(self.groupBox_6)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_15.addWidget(self.label_36, 5, 0, 1, 1)

        self.leditOSpecSettingFTIRPeaksStd = QLineEdit(self.groupBox_6)
        self.leditOSpecSettingFTIRPeaksStd.setObjectName(u"leditOSpecSettingFTIRPeaksStd")

        self.gridLayout_15.addWidget(self.leditOSpecSettingFTIRPeaksStd, 5, 1, 1, 1)

        self.btnOSpSettingFTIRPeaksStd = QPushButton(self.groupBox_6)
        self.btnOSpSettingFTIRPeaksStd.setObjectName(u"btnOSpSettingFTIRPeaksStd")

        self.gridLayout_15.addWidget(self.btnOSpSettingFTIRPeaksStd, 5, 2, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tabOSpecSettings, "")

        self.gridLayout_9.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabSpectra, "")
        self.tabSettings = QWidget()
        self.tabSettings.setObjectName(u"tabSettings")
        self.gridLayout_18 = QGridLayout(self.tabSettings)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.tabWidget_3 = QTabWidget(self.tabSettings)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setTabPosition(QTabWidget.West)
        self.tabWidget_3.setTabsClosable(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget = QWidget(self.tab)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(40, 40, 201, 80))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.gridLayoutWidget)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_8.addWidget(self.label_33, 0, 0, 1, 1)

        self.cboxSetLoglevel = QComboBox(self.gridLayoutWidget)
        self.cboxSetLoglevel.addItem("")
        self.cboxSetLoglevel.addItem("")
        self.cboxSetLoglevel.addItem("")
        self.cboxSetLoglevel.addItem("")
        self.cboxSetLoglevel.addItem("")
        self.cboxSetLoglevel.setObjectName(u"cboxSetLoglevel")

        self.gridLayout_8.addWidget(self.cboxSetLoglevel, 0, 1, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_8.addWidget(self.label_12, 1, 0, 1, 1)

        self.cboxSetLang = QComboBox(self.gridLayoutWidget)
        self.cboxSetLang.addItem(u"English")
        self.cboxSetLang.addItem(u"\u4e2d\u6587")
        self.cboxSetLang.setObjectName(u"cboxSetLang")

        self.gridLayout_8.addWidget(self.cboxSetLang, 1, 1, 1, 1)

        self.tabWidget_3.addTab(self.tab, "")

        self.gridLayout_18.addWidget(self.tabWidget_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabSettings, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 884, 26))
        self.menubar.setFont(font)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setFont(font)
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)
        self.btnConnectDB.setDefault(False)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MPTools", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWelcome), QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Input", None))
#if QT_CONFIG(tooltip)
        self.label_8.setToolTip(QCoreApplication.translate("MainWindow", u"Which Table to be Modified", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.label_8.setStatusTip(QCoreApplication.translate("MainWindow", u"Which Table to be Modified", None))
#endif // QT_CONFIG(statustip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Table:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sample Name:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Instrument:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Resolution:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Color:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Source:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Note:", None))
#if QT_CONFIG(statustip)
        self.btnSubmit.setStatusTip(QCoreApplication.translate("MainWindow", u"Submit data and commit to database", None))
#endif // QT_CONFIG(statustip)
        self.btnSubmit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
#if QT_CONFIG(tooltip)
        self.btnClear.setToolTip(QCoreApplication.translate("MainWindow", u"Clear all input above", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btnClear.setStatusTip(QCoreApplication.translate("MainWindow", u"Clear all input above", None))
#endif // QT_CONFIG(statustip)
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Log:", None))
        self.tbroswerLog.setDocumentTitle("")
        self.tbroswerLog.setMarkdown("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"MPID:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Database", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Host:", None))
        self.leditHost.setText("")
        self.leditHost.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X.X.X.X OR example.com", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.leditPort.setPlaceholderText(QCoreApplication.translate("MainWindow", u"3306", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Port:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Database:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"DBType:", None))
        self.cboxDBtype.setItemText(0, QCoreApplication.translate("MainWindow", u"MySQL", None))
        self.cboxDBtype.setItemText(1, QCoreApplication.translate("MainWindow", u"MariaDB", None))

        self.btnSaveDBConfig.setText(QCoreApplication.translate("MainWindow", u"save DB Config", None))
        self.btnLoadDBConfig.setText(QCoreApplication.translate("MainWindow", u"load DB Config", None))
        self.btnClearDBConfig.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.btnConnectDB.setText(QCoreApplication.translate("MainWindow", u"Connect DB", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInputMeta), QCoreApplication.translate("MainWindow", u"InputMeta", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.cboxPreSpecType.setItemText(0, QCoreApplication.translate("MainWindow", u"FTIR", None))
        self.cboxPreSpecType.setItemText(1, QCoreApplication.translate("MainWindow", u"Raman", None))

        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Spectrum Type:", None))
        self.labelSelectedFile.setText(QCoreApplication.translate("MainWindow", u"Click button to select a file...", None))
        self.btnSelectFile.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Preprocess", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Adjustment:", None))
        self.cboxPreAdjustment.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.cboxPreAdjustment.setItemText(1, QCoreApplication.translate("MainWindow", u"Transmittance", None))
        self.cboxPreAdjustment.setItemText(2, QCoreApplication.translate("MainWindow", u"Reflectance", None))

        self.ckbox_adjneg.setText(QCoreApplication.translate("MainWindow", u"AdjNeg", None))
        self.btnPreSave.setText(QCoreApplication.translate("MainWindow", u"Save Spectrum", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Smoothing:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Baseline:", None))
        self.labelPreSmooth.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.labelPreBaseline.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.leditPreMin.setInputMask("")
        self.leditPreMin.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.leditPreMax.setInputMask("")
        self.leditPreMax.setText(QCoreApplication.translate("MainWindow", u"6000", None))
        self.btn_stop_pre.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabOSpecProcess), QCoreApplication.translate("MainWindow", u"Preprocess", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Match Settings", None))
#if QT_CONFIG(tooltip)
        self.label_23.setToolTip(QCoreApplication.translate("MainWindow", u"The Spectrum type you selected.", None))
#endif // QT_CONFIG(tooltip)
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Type:", None))
        self.cboxMatchType.setItemText(0, QCoreApplication.translate("MainWindow", u"Std", None))
        self.cboxMatchType.setItemText(1, QCoreApplication.translate("MainWindow", u"FTIR", None))

#if QT_CONFIG(tooltip)
        self.label_24.setToolTip(QCoreApplication.translate("MainWindow", u"which spectrum you want to analyze.", None))
#endif // QT_CONFIG(tooltip)
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Analyze on:", None))
        self.cboxMatchAnalyze.setItemText(0, QCoreApplication.translate("MainWindow", u"Processed", None))
        self.cboxMatchAnalyze.setItemText(1, QCoreApplication.translate("MainWindow", u"Original", None))

#if QT_CONFIG(tooltip)
        self.label_25.setToolTip(QCoreApplication.translate("MainWindow", u"the ", None))
#endif // QT_CONFIG(tooltip)
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Region:", None))
        self.cboxMatchRegion.setItemText(0, QCoreApplication.translate("MainWindow", u"Full", None))
        self.cboxMatchRegion.setItemText(1, QCoreApplication.translate("MainWindow", u"Peaks", None))

        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Method:", None))
        self.cboxMatchMethod.setItemText(0, QCoreApplication.translate("MainWindow", u"R2", None))
        self.cboxMatchMethod.setItemText(1, QCoreApplication.translate("MainWindow", u"MSE", None))
        self.cboxMatchMethod.setItemText(2, QCoreApplication.translate("MainWindow", u"Pearson", None))

        self.btnMatchGo.setText(QCoreApplication.translate("MainWindow", u"Match", None))
        ___qtablewidgetitem = self.tableMatch.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"NO.", None));
        ___qtablewidgetitem1 = self.tableMatch.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableMatch.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"r", None));
        self.pbarOSpMatch.setFormat("")
        self.btn_stop_match.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabOSpecMatch), QCoreApplication.translate("MainWindow", u"Match", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Lib Settings", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"FTIR Meta Std:", None))
        self.btnOSpSettingFTIRPeaks.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.btnOSpSettingFTIRMetaStd.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.btnOSpSettingFTIRMeta.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"FTIR Meta:", None))
        self.btnOSpSettingFTIRFullStd.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"FTIR Full:", None))
        self.btnOSpSettingFTIRFull.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"FTIR Peaks:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"FTIR Full Std:", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"FTIR Peaks Std:", None))
        self.btnOSpSettingFTIRPeaksStd.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabOSpecSettings), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSpectra), QCoreApplication.translate("MainWindow", u"Spectra", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Log Level:", None))
        self.cboxSetLoglevel.setItemText(0, QCoreApplication.translate("MainWindow", u"DEBUG", None))
        self.cboxSetLoglevel.setItemText(1, QCoreApplication.translate("MainWindow", u"INFO", None))
        self.cboxSetLoglevel.setItemText(2, QCoreApplication.translate("MainWindow", u"WARNING", None))
        self.cboxSetLoglevel.setItemText(3, QCoreApplication.translate("MainWindow", u"ERROR", None))
        self.cboxSetLoglevel.setItemText(4, QCoreApplication.translate("MainWindow", u"CRITICAL", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Language:", None))

        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"System", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSettings), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

