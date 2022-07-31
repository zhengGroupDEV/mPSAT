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
    QFrame, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QSplitter, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
    QWidget)

from src.mplot_widget import MPlotWidget
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
        self.gridLayout_7 = QGridLayout(self.tabOSpecProcess)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.splitter_3 = QSplitter(self.tabOSpecProcess)
        self.splitter_3.setObjectName(u"splitter_3")
        sizePolicy.setHeightForWidth(self.splitter_3.sizePolicy().hasHeightForWidth())
        self.splitter_3.setSizePolicy(sizePolicy)
        self.splitter_3.setOrientation(Qt.Vertical)
        self.splitter_2 = QSplitter(self.splitter_3)
        self.splitter_2.setObjectName(u"splitter_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy1)
        self.splitter_2.setMinimumSize(QSize(0, 200))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.verticalLayoutWidget_2 = QWidget(self.splitter_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.groupBox = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(0, 50))
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rbtn_Raman = QRadioButton(self.groupBox)
        self.rbtn_Raman.setObjectName(u"rbtn_Raman")
        self.rbtn_Raman.setEnabled(False)
        self.rbtn_Raman.setCheckable(True)

        self.gridLayout_2.addWidget(self.rbtn_Raman, 0, 1, 1, 1)

        self.rbtn_FTIR = QRadioButton(self.groupBox)
        self.rbtn_FTIR.setObjectName(u"rbtn_FTIR")
        self.rbtn_FTIR.setChecked(True)

        self.gridLayout_2.addWidget(self.rbtn_FTIR, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.groupBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_3.addWidget(self.label_15, 1, 4, 1, 1)

        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 0, 0, 1, 1)

        self.slider_pre_smooth = QSlider(self.groupBox_2)
        self.slider_pre_smooth.setObjectName(u"slider_pre_smooth")
        self.slider_pre_smooth.setMinimum(0)
        self.slider_pre_smooth.setMaximum(7)
        self.slider_pre_smooth.setPageStep(1)
        self.slider_pre_smooth.setValue(3)
        self.slider_pre_smooth.setOrientation(Qt.Horizontal)
        self.slider_pre_smooth.setTickPosition(QSlider.TicksBelow)
        self.slider_pre_smooth.setTickInterval(1)

        self.gridLayout_3.addWidget(self.slider_pre_smooth, 0, 5, 1, 1)

        self.label_pre_baseline = QLabel(self.groupBox_2)
        self.label_pre_baseline.setObjectName(u"label_pre_baseline")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_pre_baseline.sizePolicy().hasHeightForWidth())
        self.label_pre_baseline.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.label_pre_baseline, 1, 6, 1, 1)

        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_3.addWidget(self.label_20, 1, 0, 1, 1)

        self.label_pre_smooth = QLabel(self.groupBox_2)
        self.label_pre_smooth.setObjectName(u"label_pre_smooth")
        sizePolicy4.setHeightForWidth(self.label_pre_smooth.sizePolicy().hasHeightForWidth())
        self.label_pre_smooth.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.label_pre_smooth, 0, 6, 1, 1)

        self.ledit_pre_min = QLineEdit(self.groupBox_2)
        self.ledit_pre_min.setObjectName(u"ledit_pre_min")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.ledit_pre_min.sizePolicy().hasHeightForWidth())
        self.ledit_pre_min.setSizePolicy(sizePolicy5)
        self.ledit_pre_min.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_3.addWidget(self.ledit_pre_min, 0, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_3.addWidget(self.label_13, 0, 4, 1, 1)

        self.ledit_pre_max = QLineEdit(self.groupBox_2)
        self.ledit_pre_max.setObjectName(u"ledit_pre_max")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.ledit_pre_max.sizePolicy().hasHeightForWidth())
        self.ledit_pre_max.setSizePolicy(sizePolicy6)
        self.ledit_pre_max.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_3.addWidget(self.ledit_pre_max, 1, 1, 1, 1)

        self.slider_pre_baseline = QSlider(self.groupBox_2)
        self.slider_pre_baseline.setObjectName(u"slider_pre_baseline")
        self.slider_pre_baseline.setMaximum(20)
        self.slider_pre_baseline.setValue(8)
        self.slider_pre_baseline.setOrientation(Qt.Horizontal)
        self.slider_pre_baseline.setTickPosition(QSlider.TicksBelow)
        self.slider_pre_baseline.setTickInterval(1)

        self.gridLayout_3.addWidget(self.slider_pre_baseline, 1, 5, 1, 1)

        self.ckbox_adjneg = QCheckBox(self.groupBox_2)
        self.ckbox_adjneg.setObjectName(u"ckbox_adjneg")
        self.ckbox_adjneg.setChecked(False)

        self.gridLayout_3.addWidget(self.ckbox_adjneg, 0, 7, 1, 1)

        self.btn_pre_save = QPushButton(self.groupBox_2)
        self.btn_pre_save.setObjectName(u"btn_pre_save")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.btn_pre_save.sizePolicy().hasHeightForWidth())
        self.btn_pre_save.setSizePolicy(sizePolicy7)

        self.gridLayout_3.addWidget(self.btn_pre_save, 1, 7, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.splitter_2.addWidget(self.verticalLayoutWidget_2)
        self.groupBox_3 = QGroupBox(self.splitter_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_5 = QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listw_pre_files = QListWidget(self.groupBox_3)
        self.listw_pre_files.setObjectName(u"listw_pre_files")
        self.listw_pre_files.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.listw_pre_files)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.btn_pop_pre_files = QPushButton(self.groupBox_3)
        self.btn_pop_pre_files.setObjectName(u"btn_pop_pre_files")

        self.horizontalLayout.addWidget(self.btn_pop_pre_files)

        self.btn_select_file_dir = QPushButton(self.groupBox_3)
        self.btn_select_file_dir.setObjectName(u"btn_select_file_dir")
        sizePolicy4.setHeightForWidth(self.btn_select_file_dir.sizePolicy().hasHeightForWidth())
        self.btn_select_file_dir.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.btn_select_file_dir)

        self.btn_clear_pre_files = QPushButton(self.groupBox_3)
        self.btn_clear_pre_files.setObjectName(u"btn_clear_pre_files")

        self.horizontalLayout.addWidget(self.btn_clear_pre_files)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.splitter_2.addWidget(self.groupBox_3)
        self.splitter_3.addWidget(self.splitter_2)
        self.fig_spec_pre = MPlotWidget(self.splitter_3)
        self.fig_spec_pre.setObjectName(u"fig_spec_pre")
        self.splitter_3.addWidget(self.fig_spec_pre)

        self.gridLayout_7.addWidget(self.splitter_3, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tabOSpecProcess, "")
        self.tabOSpecMatch = QWidget()
        self.tabOSpecMatch.setObjectName(u"tabOSpecMatch")
        self.gridLayout_12 = QGridLayout(self.tabOSpecMatch)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_spec_match_prev = QPushButton(self.tabOSpecMatch)
        self.btn_spec_match_prev.setObjectName(u"btn_spec_match_prev")

        self.horizontalLayout_8.addWidget(self.btn_spec_match_prev)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.ckbox_h2o = QCheckBox(self.tabOSpecMatch)
        self.ckbox_h2o.setObjectName(u"ckbox_h2o")

        self.horizontalLayout_8.addWidget(self.ckbox_h2o)

        self.ckbox_co2 = QCheckBox(self.tabOSpecMatch)
        self.ckbox_co2.setObjectName(u"ckbox_co2")
        self.ckbox_co2.setTristate(False)

        self.horizontalLayout_8.addWidget(self.ckbox_co2)

        self.line_5 = QFrame(self.tabOSpecMatch)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_5)

        self.label_24 = QLabel(self.tabOSpecMatch)
        self.label_24.setObjectName(u"label_24")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy8)

        self.horizontalLayout_8.addWidget(self.label_24)

        self.cbox_match_analyze = QComboBox(self.tabOSpecMatch)
        self.cbox_match_analyze.addItem("")
        self.cbox_match_analyze.addItem("")
        self.cbox_match_analyze.setObjectName(u"cbox_match_analyze")
        sizePolicy7.setHeightForWidth(self.cbox_match_analyze.sizePolicy().hasHeightForWidth())
        self.cbox_match_analyze.setSizePolicy(sizePolicy7)

        self.horizontalLayout_8.addWidget(self.cbox_match_analyze)

        self.line_6 = QFrame(self.tabOSpecMatch)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_6)

        self.label_26 = QLabel(self.tabOSpecMatch)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_8.addWidget(self.label_26)

        self.cbox_match_method = QComboBox(self.tabOSpecMatch)
        self.cbox_match_method.addItem("")
        self.cbox_match_method.addItem("")
        self.cbox_match_method.addItem("")
        self.cbox_match_method.setObjectName(u"cbox_match_method")

        self.horizontalLayout_8.addWidget(self.cbox_match_method)

        self.btn_match_go = QPushButton(self.tabOSpecMatch)
        self.btn_match_go.setObjectName(u"btn_match_go")

        self.horizontalLayout_8.addWidget(self.btn_match_go)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.btn_spec_match_next = QPushButton(self.tabOSpecMatch)
        self.btn_spec_match_next.setObjectName(u"btn_spec_match_next")

        self.horizontalLayout_8.addWidget(self.btn_spec_match_next)


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
        self.fig_spec_match = MPlotWidget(self.verticalLayoutWidget_3)
        self.fig_spec_match.setObjectName(u"fig_spec_match")

        self.verticalLayout_8.addWidget(self.fig_spec_match)

        self.splitter.addWidget(self.verticalLayoutWidget_3)
        self.table_match_res = QTableWidget(self.splitter)
        if (self.table_match_res.columnCount() < 3):
            self.table_match_res.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_match_res.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_match_res.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_match_res.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_match_res.setObjectName(u"table_match_res")
        sizePolicy9 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(1)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.table_match_res.sizePolicy().hasHeightForWidth())
        self.table_match_res.setSizePolicy(sizePolicy9)
        self.table_match_res.setMinimumSize(QSize(0, 0))
        self.table_match_res.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.table_match_res.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_match_res.setSortingEnabled(True)
        self.splitter.addWidget(self.table_match_res)
        self.table_match_res.horizontalHeader().setMinimumSectionSize(50)
        self.table_match_res.horizontalHeader().setDefaultSectionSize(50)
        self.table_match_res.verticalHeader().setMinimumSectionSize(30)
        self.table_match_res.verticalHeader().setDefaultSectionSize(30)

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
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy10)
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

        self.ledit_spec_set_model_rf = QLineEdit(self.groupBox_6)
        self.ledit_spec_set_model_rf.setObjectName(u"ledit_spec_set_model_rf")

        self.gridLayout_15.addWidget(self.ledit_spec_set_model_rf, 1, 1, 1, 1)

        self.ledit_spec_set_model_lsvm = QLineEdit(self.groupBox_6)
        self.ledit_spec_set_model_lsvm.setObjectName(u"ledit_spec_set_model_lsvm")

        self.gridLayout_15.addWidget(self.ledit_spec_set_model_lsvm, 3, 1, 1, 1)

        self.btn_spec_set_rf = QPushButton(self.groupBox_6)
        self.btn_spec_set_rf.setObjectName(u"btn_spec_set_rf")

        self.gridLayout_15.addWidget(self.btn_spec_set_rf, 1, 2, 1, 1)

        self.label_31 = QLabel(self.groupBox_6)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_31, 3, 0, 1, 1)

        self.btn_spec_set_lsvm = QPushButton(self.groupBox_6)
        self.btn_spec_set_lsvm.setObjectName(u"btn_spec_set_lsvm")

        self.gridLayout_15.addWidget(self.btn_spec_set_lsvm, 3, 2, 1, 1)

        self.label = QLabel(self.groupBox_6)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label, 1, 0, 1, 1)

        self.btn_spec_set_cnn = QPushButton(self.groupBox_6)
        self.btn_spec_set_cnn.setObjectName(u"btn_spec_set_cnn")

        self.gridLayout_15.addWidget(self.btn_spec_set_cnn, 0, 2, 1, 1)

        self.ledit_spec_set_model_cnn = QLineEdit(self.groupBox_6)
        self.ledit_spec_set_model_cnn.setObjectName(u"ledit_spec_set_model_cnn")

        self.gridLayout_15.addWidget(self.ledit_spec_set_model_cnn, 0, 1, 1, 1)


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
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
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
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Spectrum Type", None))
        self.rbtn_Raman.setText(QCoreApplication.translate("MainWindow", u"Raman", None))
        self.rbtn_FTIR.setText(QCoreApplication.translate("MainWindow", u"FTIR", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Baseline:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_pre_baseline.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.label_pre_smooth.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.ledit_pre_min.setInputMask("")
        self.ledit_pre_min.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Smooth:", None))
        self.ledit_pre_max.setInputMask("")
        self.ledit_pre_max.setText(QCoreApplication.translate("MainWindow", u"6000", None))
        self.ckbox_adjneg.setText(QCoreApplication.translate("MainWindow", u"AdjNeg", None))
        self.btn_pre_save.setText(QCoreApplication.translate("MainWindow", u"Save Spectrum", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Selected Files", None))
        self.btn_pop_pre_files.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btn_select_file_dir.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btn_clear_pre_files.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabOSpecProcess), QCoreApplication.translate("MainWindow", u"Preprocess", None))
        self.btn_spec_match_prev.setText(QCoreApplication.translate("MainWindow", u"Prev", None))
        self.ckbox_h2o.setText(QCoreApplication.translate("MainWindow", u"H2O", None))
        self.ckbox_co2.setText(QCoreApplication.translate("MainWindow", u"CO2", None))
#if QT_CONFIG(tooltip)
        self.label_24.setToolTip(QCoreApplication.translate("MainWindow", u"which spectrum you want to analyze.", None))
#endif // QT_CONFIG(tooltip)
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Analyze on:", None))
        self.cbox_match_analyze.setItemText(0, QCoreApplication.translate("MainWindow", u"Processed", None))
        self.cbox_match_analyze.setItemText(1, QCoreApplication.translate("MainWindow", u"Original", None))

        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Method:", None))
        self.cbox_match_method.setItemText(0, QCoreApplication.translate("MainWindow", u"CNN", None))
        self.cbox_match_method.setItemText(1, QCoreApplication.translate("MainWindow", u"RF", None))
        self.cbox_match_method.setItemText(2, QCoreApplication.translate("MainWindow", u"LSVM", None))

        self.btn_match_go.setText(QCoreApplication.translate("MainWindow", u"Match", None))
        self.btn_spec_match_next.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        ___qtablewidgetitem = self.table_match_res.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"NO.", None));
        ___qtablewidgetitem1 = self.table_match_res.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.table_match_res.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"r", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabOSpecMatch), QCoreApplication.translate("MainWindow", u"Match", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Model Path", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"CNN Path:", None))
        self.btn_spec_set_rf.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"LSVM Path:", None))
        self.btn_spec_set_lsvm.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"RF Path:", None))
        self.btn_spec_set_cnn.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
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

