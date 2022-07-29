# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mpsat.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QSpacerItem,
    QSplitter, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QVBoxLayout, QWidget)

from matplotlib.backends.backend_qtagg import NavigationToolbar2QT
from src.mpQFigureCanvas import QFigureCanvas
import mpsat_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(899, 677)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
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
        self.tabSpec = QWidget()
        self.tabSpec.setObjectName(u"tabSpec")
        self.gridLayout_9 = QGridLayout(self.tabSpec)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(6)
        self.gridLayout_9.setContentsMargins(1, 1, 1, 1)
        self.tabWidget_2 = QTabWidget(self.tabSpec)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setTabPosition(QTabWidget.North)
        self.tabWidget_2.setTabShape(QTabWidget.Rounded)
        self.tabOSpecProcess = QWidget()
        self.tabOSpecProcess.setObjectName(u"tabOSpecProcess")
        self.gridLayout_3 = QGridLayout(self.tabOSpecProcess)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.splitter_4 = QSplitter(self.tabOSpecProcess)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.splitter_3 = QSplitter(self.splitter_4)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.splitter_2 = QSplitter(self.splitter_3)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.groupBox = QGroupBox(self.splitter_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelSelectedFile = QLabel(self.groupBox)
        self.labelSelectedFile.setObjectName(u"labelSelectedFile")
        self.labelSelectedFile.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelSelectedFile.sizePolicy().hasHeightForWidth())
        self.labelSelectedFile.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.labelSelectedFile)

        self.btnSelectFile = QPushButton(self.groupBox)
        self.btnSelectFile.setObjectName(u"btnSelectFile")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnSelectFile.sizePolicy().hasHeightForWidth())
        self.btnSelectFile.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.btnSelectFile)

        self.rbtnFTIR = QRadioButton(self.groupBox)
        self.rbtnFTIR.setObjectName(u"rbtnFTIR")
        self.rbtnFTIR.setChecked(True)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.rbtnFTIR)

        self.rbtnRaman = QRadioButton(self.groupBox)
        self.rbtnRaman.setObjectName(u"rbtnRaman")
        self.rbtnRaman.setEnabled(False)
        self.rbtnRaman.setCheckable(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.rbtnRaman)


        self.verticalLayout_10.addLayout(self.formLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.btn_stop_pre = QPushButton(self.groupBox)
        self.btn_stop_pre.setObjectName(u"btn_stop_pre")

        self.horizontalLayout_4.addWidget(self.btn_stop_pre)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)


        self.gridLayout_2.addLayout(self.verticalLayout_10, 0, 0, 1, 1)

        self.splitter_2.addWidget(self.groupBox)
        self.groupBox_4 = QGroupBox(self.splitter_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.gridLayout_11 = QGridLayout(self.groupBox_4)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_2.addWidget(self.label_13)

        self.sliderPreSmooth = QSlider(self.groupBox_4)
        self.sliderPreSmooth.setObjectName(u"sliderPreSmooth")
        self.sliderPreSmooth.setMinimum(0)
        self.sliderPreSmooth.setMaximum(7)
        self.sliderPreSmooth.setPageStep(1)
        self.sliderPreSmooth.setValue(3)
        self.sliderPreSmooth.setOrientation(Qt.Horizontal)
        self.sliderPreSmooth.setTickPosition(QSlider.TicksBelow)
        self.sliderPreSmooth.setTickInterval(1)

        self.horizontalLayout_2.addWidget(self.sliderPreSmooth)

        self.labelPreSmooth = QLabel(self.groupBox_4)
        self.labelPreSmooth.setObjectName(u"labelPreSmooth")
        sizePolicy2.setHeightForWidth(self.labelPreSmooth.sizePolicy().hasHeightForWidth())
        self.labelPreSmooth.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.labelPreSmooth)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_2.addWidget(self.label_15)

        self.sliderPreBaseline = QSlider(self.groupBox_4)
        self.sliderPreBaseline.setObjectName(u"sliderPreBaseline")
        self.sliderPreBaseline.setMaximum(20)
        self.sliderPreBaseline.setValue(8)
        self.sliderPreBaseline.setOrientation(Qt.Horizontal)
        self.sliderPreBaseline.setTickPosition(QSlider.TicksBelow)
        self.sliderPreBaseline.setTickInterval(1)

        self.horizontalLayout_2.addWidget(self.sliderPreBaseline)

        self.labelPreBaseline = QLabel(self.groupBox_4)
        self.labelPreBaseline.setObjectName(u"labelPreBaseline")
        sizePolicy2.setHeightForWidth(self.labelPreBaseline.sizePolicy().hasHeightForWidth())
        self.labelPreBaseline.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.labelPreBaseline)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_19 = QLabel(self.groupBox_4)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_19)

        self.leditPreMin = QLineEdit(self.groupBox_4)
        self.leditPreMin.setObjectName(u"leditPreMin")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.leditPreMin.sizePolicy().hasHeightForWidth())
        self.leditPreMin.setSizePolicy(sizePolicy3)
        self.leditPreMin.setMaximumSize(QSize(60, 16777215))

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.leditPreMin)

        self.label_20 = QLabel(self.groupBox_4)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label_20)

        self.leditPreMax = QLineEdit(self.groupBox_4)
        self.leditPreMax.setObjectName(u"leditPreMax")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.leditPreMax.sizePolicy().hasHeightForWidth())
        self.leditPreMax.setSizePolicy(sizePolicy4)
        self.leditPreMax.setMaximumSize(QSize(60, 16777215))

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.leditPreMax)


        self.horizontalLayout_3.addLayout(self.formLayout_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.ckbox_adjneg = QCheckBox(self.groupBox_4)
        self.ckbox_adjneg.setObjectName(u"ckbox_adjneg")
        self.ckbox_adjneg.setChecked(False)

        self.horizontalLayout_5.addWidget(self.ckbox_adjneg)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.btnPreSave = QPushButton(self.groupBox_4)
        self.btnPreSave.setObjectName(u"btnPreSave")
        sizePolicy1.setHeightForWidth(self.btnPreSave.sizePolicy().hasHeightForWidth())
        self.btnPreSave.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.btnPreSave)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.gridLayout_11.addLayout(self.verticalLayout_3, 0, 2, 1, 1)

        self.splitter_2.addWidget(self.groupBox_4)
        self.splitter_3.addWidget(self.splitter_2)
        self.tableWidget = QTableWidget(self.splitter_3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.splitter_3.addWidget(self.tableWidget)
        self.splitter_4.addWidget(self.splitter_3)
        self.figSpecPre = QFigureCanvas(self.splitter_4)
        self.figSpecPre.setObjectName(u"figSpecPre")
        self.figSpecPre.setEnabled(True)
        sizePolicy.setHeightForWidth(self.figSpecPre.sizePolicy().hasHeightForWidth())
        self.figSpecPre.setSizePolicy(sizePolicy)
        self.figToolSpecPre = NavigationToolbar2QT(self.figSpecPre, self)
        self.figToolSpecPre.setObjectName(u"figToolSpecPre")
        self.figToolSpecPre.setEnabled(True)
        self.figToolSpecPre.setGeometry(QRect(-10, 20, 842, 10))
        self.splitter_4.addWidget(self.figSpecPre)

        self.gridLayout_3.addWidget(self.splitter_4, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tabOSpecProcess, "")
        self.tabOSpecMatch = QWidget()
        self.tabOSpecMatch.setObjectName(u"tabOSpecMatch")
        self.gridLayout_12 = QGridLayout(self.tabOSpecMatch)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btnSpecMatchPrev = QPushButton(self.tabOSpecMatch)
        self.btnSpecMatchPrev.setObjectName(u"btnSpecMatchPrev")

        self.horizontalLayout_8.addWidget(self.btnSpecMatchPrev)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.checkBox = QCheckBox(self.tabOSpecMatch)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_8.addWidget(self.checkBox)

        self.ckboxCO2 = QCheckBox(self.tabOSpecMatch)
        self.ckboxCO2.setObjectName(u"ckboxCO2")
        self.ckboxCO2.setTristate(False)

        self.horizontalLayout_8.addWidget(self.ckboxCO2)

        self.line_5 = QFrame(self.tabOSpecMatch)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_5)

        self.label_24 = QLabel(self.tabOSpecMatch)
        self.label_24.setObjectName(u"label_24")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy5)

        self.horizontalLayout_8.addWidget(self.label_24)

        self.cboxMatchAnalyze = QComboBox(self.tabOSpecMatch)
        self.cboxMatchAnalyze.addItem("")
        self.cboxMatchAnalyze.addItem("")
        self.cboxMatchAnalyze.setObjectName(u"cboxMatchAnalyze")
        sizePolicy1.setHeightForWidth(self.cboxMatchAnalyze.sizePolicy().hasHeightForWidth())
        self.cboxMatchAnalyze.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.cboxMatchAnalyze)

        self.line_6 = QFrame(self.tabOSpecMatch)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_6)

        self.label_26 = QLabel(self.tabOSpecMatch)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_8.addWidget(self.label_26)

        self.cboxMatchMethod = QComboBox(self.tabOSpecMatch)
        self.cboxMatchMethod.addItem("")
        self.cboxMatchMethod.addItem("")
        self.cboxMatchMethod.addItem("")
        self.cboxMatchMethod.setObjectName(u"cboxMatchMethod")

        self.horizontalLayout_8.addWidget(self.cboxMatchMethod)

        self.btnMatchGo = QPushButton(self.tabOSpecMatch)
        self.btnMatchGo.setObjectName(u"btnMatchGo")

        self.horizontalLayout_8.addWidget(self.btnMatchGo)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.btnSpecMatchNext = QPushButton(self.tabOSpecMatch)
        self.btnSpecMatchNext.setObjectName(u"btnSpecMatchNext")

        self.horizontalLayout_8.addWidget(self.btnSpecMatchNext)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

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
        self.figSpecMatch = QFigureCanvas(self.verticalLayoutWidget_3)
        self.figSpecMatch.setObjectName(u"figSpecMatch")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(10)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.figSpecMatch.sizePolicy().hasHeightForWidth())
        self.figSpecMatch.setSizePolicy(sizePolicy6)
        self.figSpecMatch.setMinimumSize(QSize(600, 0))
        self.figToolSpecMatch = NavigationToolbar2QT(self.figSpecMatch, self)
        self.figToolSpecMatch.setObjectName(u"figToolSpecMatch")
        self.figToolSpecMatch.setGeometry(QRect(0, 10, 419, 10))

        self.verticalLayout_8.addWidget(self.figSpecMatch)

        self.splitter.addWidget(self.verticalLayoutWidget_3)
        self.tableMatchRes = QTableWidget(self.splitter)
        if (self.tableMatchRes.columnCount() < 3):
            self.tableMatchRes.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableMatchRes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableMatchRes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableMatchRes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableMatchRes.setObjectName(u"tableMatchRes")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(1)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.tableMatchRes.sizePolicy().hasHeightForWidth())
        self.tableMatchRes.setSizePolicy(sizePolicy7)
        self.tableMatchRes.setMinimumSize(QSize(0, 0))
        self.tableMatchRes.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.tableMatchRes.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableMatchRes.setSortingEnabled(True)
        self.splitter.addWidget(self.tableMatchRes)
        self.tableMatchRes.horizontalHeader().setMinimumSectionSize(50)
        self.tableMatchRes.horizontalHeader().setDefaultSectionSize(50)
        self.tableMatchRes.verticalHeader().setMinimumSectionSize(30)
        self.tableMatchRes.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_5.addWidget(self.splitter)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)


        self.gridLayout_12.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tabOSpecMatch, "")
        self.tabOSpecSettings = QWidget()
        self.tabOSpecSettings.setObjectName(u"tabOSpecSettings")
        self.gridLayout_17 = QGridLayout(self.tabOSpecSettings)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.groupBox_6 = QGroupBox(self.tabOSpecSettings)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy8)
        self.gridLayout_16 = QGridLayout(self.groupBox_6)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_30 = QLabel(self.groupBox_6)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_30, 0, 0, 1, 1)

        self.leditOSpecSettingFTIRPeaks = QLineEdit(self.groupBox_6)
        self.leditOSpecSettingFTIRPeaks.setObjectName(u"leditOSpecSettingFTIRPeaks")

        self.gridLayout_15.addWidget(self.leditOSpecSettingFTIRPeaks, 1, 1, 1, 1)

        self.leditOSpecSettingFTIRMeta = QLineEdit(self.groupBox_6)
        self.leditOSpecSettingFTIRMeta.setObjectName(u"leditOSpecSettingFTIRMeta")

        self.gridLayout_15.addWidget(self.leditOSpecSettingFTIRMeta, 3, 1, 1, 1)

        self.btnSpecSetRF = QPushButton(self.groupBox_6)
        self.btnSpecSetRF.setObjectName(u"btnSpecSetRF")

        self.gridLayout_15.addWidget(self.btnSpecSetRF, 1, 2, 1, 1)

        self.label_31 = QLabel(self.groupBox_6)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_31, 3, 0, 1, 1)

        self.btnSpecSetLSVM = QPushButton(self.groupBox_6)
        self.btnSpecSetLSVM.setObjectName(u"btnSpecSetLSVM")

        self.gridLayout_15.addWidget(self.btnSpecSetLSVM, 3, 2, 1, 1)

        self.label = QLabel(self.groupBox_6)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label, 1, 0, 1, 1)

        self.btnSpecSetCNN = QPushButton(self.groupBox_6)
        self.btnSpecSetCNN.setObjectName(u"btnSpecSetCNN")

        self.gridLayout_15.addWidget(self.btnSpecSetCNN, 0, 2, 1, 1)

        self.leditSpecSetCNN = QLineEdit(self.groupBox_6)
        self.leditSpecSetCNN.setObjectName(u"leditSpecSetCNN")

        self.gridLayout_15.addWidget(self.leditSpecSetCNN, 0, 1, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tabOSpecSettings, "")

        self.gridLayout_9.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabSpec, "")
        self.tabSettings = QWidget()
        self.tabSettings.setObjectName(u"tabSettings")
        self.gridLayout_18 = QGridLayout(self.tabSettings)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.tabSet = QTabWidget(self.tabSettings)
        self.tabSet.setObjectName(u"tabSet")
        self.tabSet.setTabPosition(QTabWidget.West)
        self.tabSet.setTabsClosable(False)
        self.tabSetSys = QWidget()
        self.tabSetSys.setObjectName(u"tabSetSys")
        self.gridLayoutWidget = QWidget(self.tabSetSys)
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

        self.tabSet.addTab(self.tabSetSys, "")

        self.gridLayout_18.addWidget(self.tabSet, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabSettings, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 899, 26))
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

        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabSet.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"mPSAT", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
#if QT_CONFIG(shortcut)
        self.actionQuit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWelcome), QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Select", None))
        self.labelSelectedFile.setText(QCoreApplication.translate("MainWindow", u"Click to select file...", None))
        self.btnSelectFile.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
        self.rbtnFTIR.setText(QCoreApplication.translate("MainWindow", u"FTIR", None))
        self.rbtnRaman.setText(QCoreApplication.translate("MainWindow", u"Raman", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Stop Precoss", None))
        self.btn_stop_pre.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Preprocess", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Smoothing:", None))
        self.labelPreSmooth.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Baseline:", None))
        self.labelPreBaseline.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.leditPreMin.setInputMask("")
        self.leditPreMin.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.leditPreMax.setInputMask("")
        self.leditPreMax.setText(QCoreApplication.translate("MainWindow", u"6000", None))
        self.ckbox_adjneg.setText(QCoreApplication.translate("MainWindow", u"AdjNeg", None))
        self.btnPreSave.setText(QCoreApplication.translate("MainWindow", u"Save Spectrum", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabOSpecProcess), QCoreApplication.translate("MainWindow", u"Preprocess", None))
        self.btnSpecMatchPrev.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"H2O", None))
        self.ckboxCO2.setText(QCoreApplication.translate("MainWindow", u"CO2", None))
#if QT_CONFIG(tooltip)
        self.label_24.setToolTip(QCoreApplication.translate("MainWindow", u"which spectrum you want to analyze.", None))
#endif // QT_CONFIG(tooltip)
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Analyze on:", None))
        self.cboxMatchAnalyze.setItemText(0, QCoreApplication.translate("MainWindow", u"Processed", None))
        self.cboxMatchAnalyze.setItemText(1, QCoreApplication.translate("MainWindow", u"Original", None))

        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Method:", None))
        self.cboxMatchMethod.setItemText(0, QCoreApplication.translate("MainWindow", u"CNN", None))
        self.cboxMatchMethod.setItemText(1, QCoreApplication.translate("MainWindow", u"RF", None))
        self.cboxMatchMethod.setItemText(2, QCoreApplication.translate("MainWindow", u"LSVM", None))

        self.btnMatchGo.setText(QCoreApplication.translate("MainWindow", u"Match", None))
        self.btnSpecMatchNext.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        ___qtablewidgetitem = self.tableMatchRes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"NO.", None));
        ___qtablewidgetitem1 = self.tableMatchRes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableMatchRes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"r", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabOSpecMatch), QCoreApplication.translate("MainWindow", u"Match", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Model Path", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"CNN Path:", None))
        self.btnSpecSetRF.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"LSVM Path:", None))
        self.btnSpecSetLSVM.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"RF Path:", None))
        self.btnSpecSetCNN.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabOSpecSettings), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSpec), QCoreApplication.translate("MainWindow", u"Spectroscopy", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Log Level:", None))
        self.cboxSetLoglevel.setItemText(0, QCoreApplication.translate("MainWindow", u"DEBUG", None))
        self.cboxSetLoglevel.setItemText(1, QCoreApplication.translate("MainWindow", u"INFO", None))
        self.cboxSetLoglevel.setItemText(2, QCoreApplication.translate("MainWindow", u"WARNING", None))
        self.cboxSetLoglevel.setItemText(3, QCoreApplication.translate("MainWindow", u"ERROR", None))
        self.cboxSetLoglevel.setItemText(4, QCoreApplication.translate("MainWindow", u"CRITICAL", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Language:", None))

        self.tabSet.setTabText(self.tabSet.indexOf(self.tabSetSys), QCoreApplication.translate("MainWindow", u"System", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSettings), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

