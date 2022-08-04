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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QCommandLinkButton, QDoubleSpinBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QSplitter, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
    QWidget)

from src.widgets.mplot_widget import MPlotWidget
import mpsat_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(943, 600)
        icon = QIcon()
        icon.addFile(u":/icon/icon/micons/mpsat-logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 2, 2)
        self.widget_top = QWidget(self.centralwidget)
        self.widget_top.setObjectName(u"widget_top")
        self.widget_top.setStyleSheet(u"QFrame {\n"
"background-color: #eff6fc;\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.widget_top)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 3)
        self.splitter_left_right = QSplitter(self.widget_top)
        self.splitter_left_right.setObjectName(u"splitter_left_right")
        self.splitter_left_right.setStyleSheet(u"")
        self.splitter_left_right.setOrientation(Qt.Horizontal)
        self.splitter_left_right.setHandleWidth(0)
        self.splitter_left_right.setChildrenCollapsible(False)
        self.widget_left = QWidget(self.splitter_left_right)
        self.widget_left.setObjectName(u"widget_left")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_left.sizePolicy().hasHeightForWidth())
        self.widget_left.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        self.widget_left.setFont(font)
        self.widget_left.setStyleSheet(u"QWidget {\n"
"margin: 5px;\n"
"padding: 15px;\n"
"border: 2px solid #75878a ;\n"
"border-radius: 6px;\n"
"background-color: #e9f1f6;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: #395260;\n"
"	border-radius: 6px;\n"
"	border: none;\n"
"	color: #ffffff;\n"
"	height: 40px;\n"
"	padding: 3px;\n"
"}\n"
"\n"
"QPushButton:hover\n"
" {\n"
"	background-color: #657e8d;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
" {\n"
"	background-color: #0f2a36;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.widget_left)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.btn_hide_menu = QPushButton(self.widget_left)
        self.btn_hide_menu.setObjectName(u"btn_hide_menu")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_hide_menu.sizePolicy().hasHeightForWidth())
        self.btn_hide_menu.setSizePolicy(sizePolicy1)
        self.btn_hide_menu.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamilies([u"MiSans Demibold"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.btn_hide_menu.setFont(font1)
        self.btn_hide_menu.setStyleSheet(u"QPushButton {\n"
"height: 90px;\n"
"font-size: 14pt;\n"
"}")
        self.btn_hide_menu.setIcon(icon)
        self.btn_hide_menu.setIconSize(QSize(20, 20))

        self.verticalLayout_2.addWidget(self.btn_hide_menu)

        self.line = QFrame(self.widget_left)
        self.line.setObjectName(u"line")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy2)
        self.line.setMinimumSize(QSize(0, 0))
        self.line.setStyleSheet(u"QFrame{\n"
"	border-radius: none;\n"
"	background-color: #75878a;\n"
"	height: 3px;\n"
"}\n"
"")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.btn_left_home = QPushButton(self.widget_left)
        self.btn_left_home.setObjectName(u"btn_left_home")
        font2 = QFont()
        font2.setFamilies([u"MiSans Demibold"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.btn_left_home.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/micons/icon_home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_left_home.setIcon(icon1)
        self.btn_left_home.setIconSize(QSize(16, 16))

        self.verticalLayout_2.addWidget(self.btn_left_home)

        self.btn_left_preprocess = QPushButton(self.widget_left)
        self.btn_left_preprocess.setObjectName(u"btn_left_preprocess")
        self.btn_left_preprocess.setFont(font2)
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/micons/icon_chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_left_preprocess.setIcon(icon2)

        self.verticalLayout_2.addWidget(self.btn_left_preprocess)

        self.btn_left_match = QPushButton(self.widget_left)
        self.btn_left_match.setObjectName(u"btn_left_match")
        self.btn_left_match.setFont(font2)
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/micons/icon_process.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_left_match.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.btn_left_match)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.line_2 = QFrame(self.widget_left)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setStyleSheet(u"QFrame{\n"
"	border-radius: none;\n"
"	background-color: #75878a;\n"
"	height: 3px;\n"
"}\n"
"")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.btn_settings = QPushButton(self.widget_left)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setFont(font2)
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/micons/icon_settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon4)

        self.verticalLayout_2.addWidget(self.btn_settings)

        self.btn_about = QPushButton(self.widget_left)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setFont(font2)
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/micons/icon_info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_about.setIcon(icon5)

        self.verticalLayout_2.addWidget(self.btn_about)

        self.splitter_left_right.addWidget(self.widget_left)
        self.frame_right = QFrame(self.splitter_left_right)
        self.frame_right.setObjectName(u"frame_right")
        self.frame_right.setStyleSheet(u"QFrame {\n"
"margin: 10px;\n"
"padding: 5px;\n"
"border: 1px solid #75878a ;\n"
"border-radius: 6px;\n"
"}")
        self.frame_right.setFrameShape(QFrame.StyledPanel)
        self.frame_right.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_right)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabw_main = QTabWidget(self.frame_right)
        self.tabw_main.setObjectName(u"tabw_main")
        self.tabw_main.setEnabled(True)
        font3 = QFont()
        font3.setFamilies([u"MiSans Demibold"])
        font3.setPointSize(9)
        self.tabw_main.setFont(font3)
        self.tabw_main.setFocusPolicy(Qt.TabFocus)
        self.tabw_main.setContextMenuPolicy(Qt.NoContextMenu)
        self.tabw_main.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"padding: 0;\n"
"margin:0;\n"
"}")
        self.tabw_main.setTabPosition(QTabWidget.West)
        self.tabw_main.setDocumentMode(False)
        self.tabw_main.setTabsClosable(False)
        self.tab_home = QWidget()
        self.tab_home.setObjectName(u"tab_home")
        self.gridLayout_4 = QGridLayout(self.tab_home)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.tab_home)
        self.textBrowser.setObjectName(u"textBrowser")
        font4 = QFont()
        font4.setFamilies([u"MiSans Demibold"])
        self.textBrowser.setFont(font4)
        self.textBrowser.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.textBrowser, 1, 0, 1, 1)

        self.label_18 = QLabel(self.tab_home)
        self.label_18.setObjectName(u"label_18")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy3)
        self.label_18.setStyleSheet(u"image: url(:/icon/icon/micons/mpsat-logo.svg);\n"
"padding: 20px;")

        self.gridLayout_4.addWidget(self.label_18, 0, 0, 1, 1)

        self.tabw_main.addTab(self.tab_home, "")
        self.tab_pre = QWidget()
        self.tab_pre.setObjectName(u"tab_pre")
        self.tab_pre.setStyleSheet(u"QFrame,\n"
"{\n"
"border: none;\n"
"border-radius: 0;\n"
"margin: 0;\n"
"padding: 0;\n"
"}")
        self.gridLayout_10 = QGridLayout(self.tab_pre)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.splitter_pre_fig = QSplitter(self.tab_pre)
        self.splitter_pre_fig.setObjectName(u"splitter_pre_fig")
        sizePolicy3.setHeightForWidth(self.splitter_pre_fig.sizePolicy().hasHeightForWidth())
        self.splitter_pre_fig.setSizePolicy(sizePolicy3)
        self.splitter_pre_fig.setStyleSheet(u"")
        self.splitter_pre_fig.setOrientation(Qt.Vertical)
        self.splitter_pre_fig.setHandleWidth(3)
        self.splitter_pre_fig.setChildrenCollapsible(True)
        self.splitter_2 = QSplitter(self.splitter_pre_fig)
        self.splitter_2.setObjectName(u"splitter_2")
        sizePolicy3.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy3)
        self.splitter_2.setMinimumSize(QSize(0, 0))
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter_2.setHandleWidth(3)
        self.verticalLayoutWidget_2 = QWidget(self.splitter_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy4)
        self.groupBox_2.setFont(font3)
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"margin: 10px;\n"
"padding: 5px;\n"
"border: 1px solid #75878a ;\n"
"border-radius: 6px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"subcontrol-position: top center;\n"
"subcontrol-origin: margin;\n"
"}")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_pre_smooth = QLabel(self.groupBox_2)
        self.label_pre_smooth.setObjectName(u"label_pre_smooth")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_pre_smooth.sizePolicy().hasHeightForWidth())
        self.label_pre_smooth.setSizePolicy(sizePolicy5)

        self.gridLayout_8.addWidget(self.label_pre_smooth, 3, 2, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_8.addWidget(self.label_13, 3, 0, 1, 1)

        self.label_20 = QLabel(self.groupBox_2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_8.addWidget(self.label_20, 2, 0, 1, 1)

        self.label_pre_baseline = QLabel(self.groupBox_2)
        self.label_pre_baseline.setObjectName(u"label_pre_baseline")
        sizePolicy5.setHeightForWidth(self.label_pre_baseline.sizePolicy().hasHeightForWidth())
        self.label_pre_baseline.setSizePolicy(sizePolicy5)

        self.gridLayout_8.addWidget(self.label_pre_baseline, 4, 2, 1, 1)

        self.slider_pre_smooth = QSlider(self.groupBox_2)
        self.slider_pre_smooth.setObjectName(u"slider_pre_smooth")
        self.slider_pre_smooth.setMinimum(0)
        self.slider_pre_smooth.setMaximum(7)
        self.slider_pre_smooth.setPageStep(1)
        self.slider_pre_smooth.setValue(3)
        self.slider_pre_smooth.setOrientation(Qt.Horizontal)
        self.slider_pre_smooth.setTickPosition(QSlider.TicksBelow)
        self.slider_pre_smooth.setTickInterval(1)

        self.gridLayout_8.addWidget(self.slider_pre_smooth, 3, 1, 1, 1)

        self.btn_pre_save = QPushButton(self.groupBox_2)
        self.btn_pre_save.setObjectName(u"btn_pre_save")
        sizePolicy2.setHeightForWidth(self.btn_pre_save.sizePolicy().hasHeightForWidth())
        self.btn_pre_save.setSizePolicy(sizePolicy2)
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/micons/icon_save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pre_save.setIcon(icon6)

        self.gridLayout_8.addWidget(self.btn_pre_save, 2, 2, 1, 1)

        self.slider_pre_baseline = QSlider(self.groupBox_2)
        self.slider_pre_baseline.setObjectName(u"slider_pre_baseline")
        self.slider_pre_baseline.setMaximum(20)
        self.slider_pre_baseline.setValue(8)
        self.slider_pre_baseline.setOrientation(Qt.Horizontal)
        self.slider_pre_baseline.setTickPosition(QSlider.TicksBelow)
        self.slider_pre_baseline.setTickInterval(1)

        self.gridLayout_8.addWidget(self.slider_pre_baseline, 4, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.label_19, 1, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_8.addWidget(self.label_15, 4, 0, 1, 1)

        self.rbtn_Raman = QRadioButton(self.groupBox_2)
        self.rbtn_Raman.setObjectName(u"rbtn_Raman")
        self.rbtn_Raman.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.rbtn_Raman.sizePolicy().hasHeightForWidth())
        self.rbtn_Raman.setSizePolicy(sizePolicy2)
        self.rbtn_Raman.setCheckable(True)

        self.gridLayout_8.addWidget(self.rbtn_Raman, 0, 2, 1, 1)

        self.rbtn_FTIR = QRadioButton(self.groupBox_2)
        self.rbtn_FTIR.setObjectName(u"rbtn_FTIR")
        self.rbtn_FTIR.setChecked(True)

        self.gridLayout_8.addWidget(self.rbtn_FTIR, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)

        self.spbox_pre_min = QSpinBox(self.groupBox_2)
        self.spbox_pre_min.setObjectName(u"spbox_pre_min")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.spbox_pre_min.sizePolicy().hasHeightForWidth())
        self.spbox_pre_min.setSizePolicy(sizePolicy6)
        self.spbox_pre_min.setStyleSheet(u"")
        self.spbox_pre_min.setMaximum(6000)

        self.gridLayout_8.addWidget(self.spbox_pre_min, 1, 1, 1, 1)

        self.spbox_pre_max = QSpinBox(self.groupBox_2)
        self.spbox_pre_max.setObjectName(u"spbox_pre_max")
        sizePolicy6.setHeightForWidth(self.spbox_pre_max.sizePolicy().hasHeightForWidth())
        self.spbox_pre_max.setSizePolicy(sizePolicy6)
        self.spbox_pre_max.setMaximum(6000)
        self.spbox_pre_max.setValue(6000)

        self.gridLayout_8.addWidget(self.spbox_pre_max, 2, 1, 1, 1)

        self.ckbox_adjneg = QCheckBox(self.groupBox_2)
        self.ckbox_adjneg.setObjectName(u"ckbox_adjneg")
        self.ckbox_adjneg.setFont(font4)
        self.ckbox_adjneg.setStyleSheet(u"QCheckBox {\n"
"	spacing: 5px; \n"
"  background-color: none;\n"
"  height: 1.15em;\n"
"  border-radius: 0.15em;\n"
"}")
        self.ckbox_adjneg.setChecked(False)

        self.gridLayout_8.addWidget(self.ckbox_adjneg, 1, 2, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_8, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.verticalLayout_4.setStretch(0, 10)
        self.splitter_2.addWidget(self.verticalLayoutWidget_2)
        self.groupBox_3 = QGroupBox(self.splitter_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy4.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy4)
        self.groupBox_3.setMinimumSize(QSize(10, 50))
        self.groupBox_3.setFont(font3)
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
"margin: 10px;\n"
"padding: 5px;\n"
"border: 1px solid #75878a ;\n"
"border-radius: 6px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"subcontrol-origin: margin;\n"
"subcontrol-position: top center;\n"
"}")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.groupBox_3.setFlat(False)
        self.gridLayout_9 = QGridLayout(self.groupBox_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listw_pre_files = QListWidget(self.groupBox_3)
        self.listw_pre_files.setObjectName(u"listw_pre_files")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.listw_pre_files.sizePolicy().hasHeightForWidth())
        self.listw_pre_files.setSizePolicy(sizePolicy7)
        self.listw_pre_files.setMinimumSize(QSize(10, 50))
        self.listw_pre_files.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.listw_pre_files)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.btn_pop_pre_files = QPushButton(self.groupBox_3)
        self.btn_pop_pre_files.setObjectName(u"btn_pop_pre_files")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/micons/icon_minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pop_pre_files.setIcon(icon7)

        self.horizontalLayout_6.addWidget(self.btn_pop_pre_files)

        self.btn_select_file_dir = QPushButton(self.groupBox_3)
        self.btn_select_file_dir.setObjectName(u"btn_select_file_dir")
        sizePolicy6.setHeightForWidth(self.btn_select_file_dir.sizePolicy().hasHeightForWidth())
        self.btn_select_file_dir.setSizePolicy(sizePolicy6)
        icon8 = QIcon()
        icon8.addFile(u":/icon/icon/micons/icon_add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_select_file_dir.setIcon(icon8)

        self.horizontalLayout_6.addWidget(self.btn_select_file_dir)

        self.btn_clear_pre_files = QPushButton(self.groupBox_3)
        self.btn_clear_pre_files.setObjectName(u"btn_clear_pre_files")
        icon9 = QIcon()
        icon9.addFile(u":/icon/icon/micons/icon_clear.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear_pre_files.setIcon(icon9)

        self.horizontalLayout_6.addWidget(self.btn_clear_pre_files)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.gridLayout_9.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.splitter_2.addWidget(self.groupBox_3)
        self.splitter_pre_fig.addWidget(self.splitter_2)
        self.fig_spec_pre = MPlotWidget(self.splitter_pre_fig)
        self.fig_spec_pre.setObjectName(u"fig_spec_pre")
        self.splitter_pre_fig.addWidget(self.fig_spec_pre)

        self.gridLayout_10.addWidget(self.splitter_pre_fig, 0, 0, 1, 1)

        self.tabw_main.addTab(self.tab_pre, "")
        self.tab_match = QWidget()
        self.tab_match.setObjectName(u"tab_match")
        self.gridLayout_11 = QGridLayout(self.tab_match)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_spec_match_prev = QPushButton(self.tab_match)
        self.btn_spec_match_prev.setObjectName(u"btn_spec_match_prev")
        icon10 = QIcon()
        icon10.addFile(u":/icon/icon/micons/icon_arrow_left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_spec_match_prev.setIcon(icon10)

        self.horizontalLayout_8.addWidget(self.btn_spec_match_prev)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.ckbox_h2o = QCheckBox(self.tab_match)
        self.ckbox_h2o.setObjectName(u"ckbox_h2o")

        self.horizontalLayout_8.addWidget(self.ckbox_h2o)

        self.label_3 = QLabel(self.tab_match)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.ckbox_co2 = QCheckBox(self.tab_match)
        self.ckbox_co2.setObjectName(u"ckbox_co2")
        self.ckbox_co2.setTristate(False)

        self.horizontalLayout_8.addWidget(self.ckbox_co2)

        self.label_4 = QLabel(self.tab_match)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.dspbox_co2 = QDoubleSpinBox(self.tab_match)
        self.dspbox_co2.setObjectName(u"dspbox_co2")
        self.dspbox_co2.setMaximum(1.000000000000000)
        self.dspbox_co2.setSingleStep(0.010000000000000)
        self.dspbox_co2.setValue(0.200000000000000)

        self.horizontalLayout_8.addWidget(self.dspbox_co2)

        self.line_5 = QFrame(self.tab_match)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_5)

        self.label_24 = QLabel(self.tab_match)
        self.label_24.setObjectName(u"label_24")
        sizePolicy8 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy8)

        self.horizontalLayout_8.addWidget(self.label_24)

        self.cbox_match_analyze = QComboBox(self.tab_match)
        self.cbox_match_analyze.addItem("")
        self.cbox_match_analyze.addItem("")
        self.cbox_match_analyze.setObjectName(u"cbox_match_analyze")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.cbox_match_analyze.sizePolicy().hasHeightForWidth())
        self.cbox_match_analyze.setSizePolicy(sizePolicy9)

        self.horizontalLayout_8.addWidget(self.cbox_match_analyze)

        self.line_6 = QFrame(self.tab_match)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_6)

        self.label_26 = QLabel(self.tab_match)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_8.addWidget(self.label_26)

        self.cbox_match_method = QComboBox(self.tab_match)
        self.cbox_match_method.addItem("")
        self.cbox_match_method.addItem("")
        self.cbox_match_method.addItem("")
        self.cbox_match_method.setObjectName(u"cbox_match_method")

        self.horizontalLayout_8.addWidget(self.cbox_match_method)

        self.btn_match_go = QPushButton(self.tab_match)
        self.btn_match_go.setObjectName(u"btn_match_go")
        icon11 = QIcon()
        icon11.addFile(u":/icon/icon/micons/icon_send.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_match_go.setIcon(icon11)

        self.horizontalLayout_8.addWidget(self.btn_match_go)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.btn_spec_match_next = QPushButton(self.tab_match)
        self.btn_spec_match_next.setObjectName(u"btn_spec_match_next")
        icon12 = QIcon()
        icon12.addFile(u":/icon/icon/micons/icon_arrow_right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_spec_match_next.setIcon(icon12)

        self.horizontalLayout_8.addWidget(self.btn_spec_match_next)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.splitter_match = QSplitter(self.tab_match)
        self.splitter_match.setObjectName(u"splitter_match")
        sizePolicy3.setHeightForWidth(self.splitter_match.sizePolicy().hasHeightForWidth())
        self.splitter_match.setSizePolicy(sizePolicy3)
        self.splitter_match.setOrientation(Qt.Horizontal)
        self.splitter_match.setHandleWidth(3)
        self.verticalLayoutWidget_3 = QWidget(self.splitter_match)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.fig_spec_match = MPlotWidget(self.verticalLayoutWidget_3)
        self.fig_spec_match.setObjectName(u"fig_spec_match")
        sizePolicy10 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy10.setHorizontalStretch(6)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.fig_spec_match.sizePolicy().hasHeightForWidth())
        self.fig_spec_match.setSizePolicy(sizePolicy10)

        self.verticalLayout_8.addWidget(self.fig_spec_match)

        self.splitter_match.addWidget(self.verticalLayoutWidget_3)
        self.table_match_res = QTableWidget(self.splitter_match)
        if (self.table_match_res.columnCount() < 2):
            self.table_match_res.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_match_res.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_match_res.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_match_res.setObjectName(u"table_match_res")
        sizePolicy11 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy11.setHorizontalStretch(1)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.table_match_res.sizePolicy().hasHeightForWidth())
        self.table_match_res.setSizePolicy(sizePolicy11)
        self.table_match_res.setMinimumSize(QSize(100, 0))
        font5 = QFont()
        font5.setFamilies([u"MiSans Demibold"])
        font5.setPointSize(9)
        font5.setBold(False)
        self.table_match_res.setFont(font5)
        self.table_match_res.setEditTriggers(QAbstractItemView.SelectedClicked)
        self.table_match_res.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_match_res.setSortingEnabled(True)
        self.splitter_match.addWidget(self.table_match_res)
        self.table_match_res.horizontalHeader().setMinimumSectionSize(50)
        self.table_match_res.horizontalHeader().setDefaultSectionSize(50)
        self.table_match_res.verticalHeader().setMinimumSectionSize(30)
        self.table_match_res.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_5.addWidget(self.splitter_match)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)


        self.gridLayout_11.addLayout(self.verticalLayout_9, 0, 0, 1, 1)

        self.tabw_main.addTab(self.tab_match, "")
        self.tab_settings = QWidget()
        self.tab_settings.setObjectName(u"tab_settings")
        self.gridLayout_12 = QGridLayout(self.tab_settings)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.groupBox_6 = QGroupBox(self.tab_settings)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy12 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy12)
        self.groupBox_6.setStyleSheet(u"QGroupBox {\n"
"margin: 10px;\n"
"padding: 5px;\n"
"border: 1px solid #75878a ;\n"
"border-radius: 6px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"subcontrol-position: top center;\n"
"subcontrol-origin: margin;\n"
"}")
        self.gridLayout_16 = QGridLayout(self.groupBox_6)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_2 = QLabel(self.groupBox_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_12 = QLabel(self.groupBox_6)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_15.addWidget(self.label_12, 6, 0, 1, 1)

        self.ledit_spec_set_model_cnn = QLineEdit(self.groupBox_6)
        self.ledit_spec_set_model_cnn.setObjectName(u"ledit_spec_set_model_cnn")
        self.ledit_spec_set_model_cnn.setReadOnly(True)

        self.gridLayout_15.addWidget(self.ledit_spec_set_model_cnn, 0, 1, 1, 1)

        self.label_33 = QLabel(self.groupBox_6)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_15.addWidget(self.label_33, 5, 0, 1, 1)

        self.cbox_loglv = QComboBox(self.groupBox_6)
        self.cbox_loglv.addItem("")
        self.cbox_loglv.addItem("")
        self.cbox_loglv.addItem("")
        self.cbox_loglv.addItem("")
        self.cbox_loglv.addItem("")
        self.cbox_loglv.setObjectName(u"cbox_loglv")

        self.gridLayout_15.addWidget(self.cbox_loglv, 5, 1, 1, 1)

        self.label_30 = QLabel(self.groupBox_6)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_30, 0, 0, 1, 1)

        self.btn_spec_set_cnn = QPushButton(self.groupBox_6)
        self.btn_spec_set_cnn.setObjectName(u"btn_spec_set_cnn")
        icon13 = QIcon()
        icon13.addFile(u":/icon/icon/micons/icon_open_folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_spec_set_cnn.setIcon(icon13)

        self.gridLayout_15.addWidget(self.btn_spec_set_cnn, 0, 2, 1, 1)

        self.ledit_spec_set_model_lsvm = QLineEdit(self.groupBox_6)
        self.ledit_spec_set_model_lsvm.setObjectName(u"ledit_spec_set_model_lsvm")
        self.ledit_spec_set_model_lsvm.setReadOnly(True)

        self.gridLayout_15.addWidget(self.ledit_spec_set_model_lsvm, 3, 1, 1, 1)

        self.label_31 = QLabel(self.groupBox_6)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_31, 3, 0, 1, 1)

        self.spbox_spec_topn = QSpinBox(self.groupBox_6)
        self.spbox_spec_topn.setObjectName(u"spbox_spec_topn")
        self.spbox_spec_topn.setMinimum(1)
        self.spbox_spec_topn.setMaximum(120)
        self.spbox_spec_topn.setValue(10)

        self.gridLayout_15.addWidget(self.spbox_spec_topn, 4, 1, 1, 1)

        self.btn_spec_set_lsvm = QPushButton(self.groupBox_6)
        self.btn_spec_set_lsvm.setObjectName(u"btn_spec_set_lsvm")
        self.btn_spec_set_lsvm.setIcon(icon13)

        self.gridLayout_15.addWidget(self.btn_spec_set_lsvm, 3, 2, 1, 1)

        self.cbox_lang = QComboBox(self.groupBox_6)
        self.cbox_lang.addItem(u"English")
        self.cbox_lang.addItem(u"\u4e2d\u6587")
        self.cbox_lang.setObjectName(u"cbox_lang")

        self.gridLayout_15.addWidget(self.cbox_lang, 6, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_15.addWidget(self.label_5, 4, 0, 1, 1)

        self.btn_spec_set_rf = QPushButton(self.groupBox_6)
        self.btn_spec_set_rf.setObjectName(u"btn_spec_set_rf")
        self.btn_spec_set_rf.setIcon(icon13)

        self.gridLayout_15.addWidget(self.btn_spec_set_rf, 1, 2, 1, 1)

        self.ledit_spec_set_model_rf = QLineEdit(self.groupBox_6)
        self.ledit_spec_set_model_rf.setObjectName(u"ledit_spec_set_model_rf")
        self.ledit_spec_set_model_rf.setReadOnly(True)

        self.gridLayout_15.addWidget(self.ledit_spec_set_model_rf, 1, 1, 1, 1)

        self.btn_topn = QPushButton(self.groupBox_6)
        self.btn_topn.setObjectName(u"btn_topn")

        self.gridLayout_15.addWidget(self.btn_topn, 4, 2, 1, 1)

        self.btn_loglv = QPushButton(self.groupBox_6)
        self.btn_loglv.setObjectName(u"btn_loglv")
        self.btn_loglv.setEnabled(True)
        icon14 = QIcon()
        icon14.addFile(u":/icon/icon/micons/icon_debug.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_loglv.setIcon(icon14)

        self.gridLayout_15.addWidget(self.btn_loglv, 5, 2, 1, 1)

        self.btn_language = QPushButton(self.groupBox_6)
        self.btn_language.setObjectName(u"btn_language")
        self.btn_language.setEnabled(True)
        icon15 = QIcon()
        icon15.addFile(u":/icon/icon/micons/icon_language.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_language.setIcon(icon15)

        self.gridLayout_15.addWidget(self.btn_language, 6, 2, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 1)


        self.gridLayout_12.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.tabw_main.addTab(self.tab_settings, "")
        self.tab_about = QWidget()
        self.tab_about.setObjectName(u"tab_about")
        self.gridLayout_6 = QGridLayout(self.tab_about)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_6 = QLabel(self.tab_about)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"image: url(:/icon/icon/micons/mpsat-logo.svg);")
        self.label_6.setScaledContents(False)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_6, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.tab_about)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font3)
        self.groupBox_4.setStyleSheet(u"QGroupBox {\n"
"margin: 10px;\n"
"padding: 5px;\n"
"border: 1px solid #75878a ;\n"
"border-radius: 6px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"subcontrol-position: top center;\n"
"subcontrol-origin: margin;\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.commandLinkButton_2 = QCommandLinkButton(self.groupBox_4)
        self.commandLinkButton_2.setObjectName(u"commandLinkButton_2")
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(9)
        self.commandLinkButton_2.setFont(font6)
        icon16 = QIcon()
        icon16.addFile(u":/icon/icon/micons/numpy_logo_icon_168073.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_2.setIcon(icon16)

        self.gridLayout_13.addWidget(self.commandLinkButton_2, 1, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font4)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_10, 3, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setOpenExternalLinks(True)

        self.gridLayout_13.addWidget(self.label_7, 0, 1, 1, 1)

        self.commandLinkButton_3 = QCommandLinkButton(self.groupBox_4)
        self.commandLinkButton_3.setObjectName(u"commandLinkButton_3")
        self.commandLinkButton_3.setFont(font6)
        icon17 = QIcon()
        icon17.addFile(u":/icon/icon/micons/icon_chart1.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_3.setIcon(icon17)

        self.gridLayout_13.addWidget(self.commandLinkButton_3, 2, 0, 1, 1)

        self.commandLinkButton_6 = QCommandLinkButton(self.groupBox_4)
        self.commandLinkButton_6.setObjectName(u"commandLinkButton_6")
        self.commandLinkButton_6.setFont(font6)
        icon18 = QIcon()
        icon18.addFile(u":/icon/icon/micons/matplotlib_logo.webp", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_6.setIcon(icon18)

        self.gridLayout_13.addWidget(self.commandLinkButton_6, 5, 0, 1, 1)

        self.commandLinkButton_4 = QCommandLinkButton(self.groupBox_4)
        self.commandLinkButton_4.setObjectName(u"commandLinkButton_4")
        self.commandLinkButton_4.setFont(font6)
        icon19 = QIcon()
        icon19.addFile(u":/icon/icon/micons/scipy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_4.setIcon(icon19)

        self.gridLayout_13.addWidget(self.commandLinkButton_4, 3, 0, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.groupBox_4)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setFont(font6)
        icon20 = QIcon()
        icon20.addFile(u":/icon/icon/micons/Py-128.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon20)

        self.gridLayout_13.addWidget(self.commandLinkButton, 0, 0, 1, 1)

        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font4)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_14, 5, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font5)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_11, 4, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font4)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_16, 6, 1, 1, 1)

        self.commandLinkButton_5 = QCommandLinkButton(self.groupBox_4)
        self.commandLinkButton_5.setObjectName(u"commandLinkButton_5")
        self.commandLinkButton_5.setFont(font6)
        icon21 = QIcon()
        icon21.addFile(u":/icon/icon/micons/Scikit_learn_logo_small.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_5.setIcon(icon21)

        self.gridLayout_13.addWidget(self.commandLinkButton_5, 4, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_9, 2, 1, 1, 1)

        self.commandLinkButton_7 = QCommandLinkButton(self.groupBox_4)
        self.commandLinkButton_7.setObjectName(u"commandLinkButton_7")
        self.commandLinkButton_7.setFont(font6)
        icon22 = QIcon()
        icon22.addFile(u":/icon/icon/micons/ONNX-Runtime-logo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_7.setIcon(icon22)

        self.gridLayout_13.addWidget(self.commandLinkButton_7, 6, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font4)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_8, 1, 1, 1, 1)

        self.commandLinkButton_8 = QCommandLinkButton(self.groupBox_4)
        self.commandLinkButton_8.setObjectName(u"commandLinkButton_8")
        self.commandLinkButton_8.setFont(font6)
        icon23 = QIcon()
        icon23.addFile(u":/icon/icon/micons/qt-material.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_8.setIcon(icon23)

        self.gridLayout_13.addWidget(self.commandLinkButton_8, 7, 0, 1, 1)

        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font4)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.label_17, 7, 1, 1, 1)


        self.horizontalLayout_7.addLayout(self.gridLayout_13)


        self.gridLayout_6.addWidget(self.groupBox_4, 1, 0, 1, 1)

        self.tabw_main.addTab(self.tab_about, "")

        self.gridLayout_3.addWidget(self.tabw_main, 0, 0, 1, 1)

        self.splitter_left_right.addWidget(self.frame_right)

        self.gridLayout_2.addWidget(self.splitter_left_right, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_top, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabw_main.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"mPSAT", None))
        self.btn_hide_menu.setText(QCoreApplication.translate("MainWindow", u"mPSAT", None))
        self.btn_left_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_left_preprocess.setText(QCoreApplication.translate("MainWindow", u"Preprocess", None))
        self.btn_left_match.setText(QCoreApplication.translate("MainWindow", u"Match", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.textBrowser.setDocumentTitle("")
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'MiSans Demibold'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:18pt;\">mPSAT</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:14pt;\">(micro)Plastic Spectroscopy Analyze Tool</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; te"
                        "xt-indent:0px; font-family:'Microsoft YaHei UI'; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:11pt;\">Developer: zhengGroup@LZU</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:11pt;\">Github: </span><a href=\"https://github.com/zhengGroupDEV\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:11pt; text-decoration: underline; color:#0000ff;\">https://github.com/zhengGroupDEV</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Microsoft YaHei UI'; font-size:11pt; text-decoration: underline; color:#0000ff;\"><br /></p></body></html>", None))
        self.label_18.setText("")
        self.tabw_main.setTabText(self.tabw_main.indexOf(self.tab_home), QCoreApplication.translate("MainWindow", u"Home", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.label_pre_smooth.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Smooth:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.label_pre_baseline.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_pre_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Min:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Baseline:", None))
        self.rbtn_Raman.setText(QCoreApplication.translate("MainWindow", u"Raman", None))
        self.rbtn_FTIR.setText(QCoreApplication.translate("MainWindow", u"FTIR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Type:", None))
        self.spbox_pre_max.setPrefix("")
        self.ckbox_adjneg.setText(QCoreApplication.translate("MainWindow", u"AdjNeg", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Selected Files", None))
        self.btn_pop_pre_files.setText("")
        self.btn_select_file_dir.setText("")
        self.btn_clear_pre_files.setText("")
        self.tabw_main.setTabText(self.tabw_main.indexOf(self.tab_pre), QCoreApplication.translate("MainWindow", u"Preprocess", None))
        self.btn_spec_match_prev.setText("")
        self.ckbox_h2o.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"H<sub>2</sub>O", None))
        self.ckbox_co2.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CO<sub>2</sub>", None))
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
        self.btn_spec_match_next.setText("")
        ___qtablewidgetitem = self.table_match_res.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem1 = self.table_match_res.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"P(%)", None));
        self.tabw_main.setTabText(self.tabw_main.indexOf(self.tab_match), QCoreApplication.translate("MainWindow", u"Match", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Model Path", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"RF Path:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Language:", None))
        self.ledit_spec_set_model_cnn.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNN model path", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Log Level:", None))
        self.cbox_loglv.setItemText(0, QCoreApplication.translate("MainWindow", u"DEBUG", None))
        self.cbox_loglv.setItemText(1, QCoreApplication.translate("MainWindow", u"INFO", None))
        self.cbox_loglv.setItemText(2, QCoreApplication.translate("MainWindow", u"WARNING", None))
        self.cbox_loglv.setItemText(3, QCoreApplication.translate("MainWindow", u"ERROR", None))
        self.cbox_loglv.setItemText(4, QCoreApplication.translate("MainWindow", u"CRITICAL", None))

        self.label_30.setText(QCoreApplication.translate("MainWindow", u"CNN Path:", None))
        self.btn_spec_set_cnn.setText("")
        self.ledit_spec_set_model_lsvm.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Linear SVM path", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"LSVM Path:", None))
        self.btn_spec_set_lsvm.setText("")

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Top-n:", None))
        self.btn_spec_set_rf.setText("")
        self.ledit_spec_set_model_rf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Random Forest path", None))
        self.btn_topn.setText("")
        self.btn_loglv.setText("")
        self.btn_language.setText("")
        self.tabw_main.setTabText(self.tabw_main.indexOf(self.tab_settings), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_6.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Thanks && License", None))
        self.commandLinkButton_2.setText(QCoreApplication.translate("MainWindow", u"Numpy", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/scipy/scipy/blob/main/LICENSE.txt\"><span style=\" text-decoration: underline; color:#0000ff;\">BSD</span></a></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://wiki.qt.io/Qt_for_Python\"><span style=\" text-decoration: underline; color:#0000ff;\">LGPLv3</span></a></p></body></html>", None))
        self.commandLinkButton_3.setText(QCoreApplication.translate("MainWindow", u"PyQtGraph", None))
        self.commandLinkButton_6.setText(QCoreApplication.translate("MainWindow", u"Matplotlib", None))
        self.commandLinkButton_4.setText(QCoreApplication.translate("MainWindow", u"Scipy", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"PySide", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://matplotlib.org/stable/users/project/license.html\"><span style=\" text-decoration: underline; color:#0000ff;\">matplotlib</span></a></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/scikit-learn/scikit-learn/blob/main/COPYING\"><span style=\" text-decoration: underline; color:#0000ff;\">BSD</span></a></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/microsoft/onnxruntime/blob/master/LICENSE\"><span style=\" text-decoration: underline; color:#0000ff;\">MIT</span></a></p></body></html>", None))
        self.commandLinkButton_5.setText(QCoreApplication.translate("MainWindow", u"Scikit-learn", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/pyqtgraph/pyqtgraph/blob/master/LICENSE.txt\"><span style=\" text-decoration: underline; color:#0000ff;\">MIT</span></a></p></body></html>", None))
        self.commandLinkButton_7.setText(QCoreApplication.translate("MainWindow", u"ONNXRuntime", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://numpy.org/doc/stable/license.html\"><span style=\" text-decoration: underline; color:#0000ff;\">BSD</span></a></p></body></html>", None))
        self.commandLinkButton_8.setText(QCoreApplication.translate("MainWindow", u"Qt-Material", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://github.com/UN-GCPDS/qt-material/blob/master/LICENSE\"><span style=\" text-decoration: underline; color:#0000ff;\">BSD 2</span></a></p></body></html>", None))
        self.tabw_main.setTabText(self.tabw_main.indexOf(self.tab_about), QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

