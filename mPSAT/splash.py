"""
Description: splash screen
Author: Rainyl
LastEditTime: 2022-08-02 15:19:02
"""
import sys
from typing import Any, Tuple
from PySide6.QtCore import (
    Qt,
    QTimer,
    Signal,
    QThread,
    Slot,
    QEventLoop,
    QFile,
    QIODeviceBase,
)
from PySide6.QtWidgets import (
    QMainWindow,
    QGraphicsDropShadowEffect,
    QApplication,
)
from PySide6.QtGui import QColor

from mPSAT.mpsatApp import mPSAT
from mPSAT.splashUI import Ui_Splash
from mPSAT.utils.mpsat_worker import LoadModelWorker


class Splash(QMainWindow):
    def __init__(self, mw: mPSAT):
        super(Splash, self).__init__()
        self.ui = Ui_Splash()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        self.ui.btn_close.clicked.connect(self.close)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor("#2f3542"))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        self.mainwndow = mw

        self.show()
        self.load_main_window()

    def load_main_window(self):
        label_name = QFile(":/json/data/label_name.json")
        label_name.open(QIODeviceBase.ReadOnly)
        label_name_str = label_name.readAll().toStdString()
        settings = self.mainwndow.settings
        method = settings.METHOD
        if method == 0:  # CNN
            model_path = settings.CNN
        elif method == 1:  # RF
            model_path = settings.RF
        elif method == 2:
            model_path = settings.CNN2D
        else:
            self.ui.label_loading.setText(f"model method {method} not supported!")
            return

        self.th = QThread(self)
        self.worker = LoadModelWorker(
            label_name_str=label_name_str,
            method=method,
            model_path=model_path,
        )
        self.worker.moveToThread(self.th)
        self.worker.finished.connect(self.th.quit)
        self.worker.finished.connect(self.th.deleteLater)
        self.worker.finished.connect(self.show_mainwindow)
        self.th.started.connect(self.worker.run)
        self.th.start()

    @Slot()
    def show_mainwindow(self, res: Tuple[int, Any]):
        r, model = res
        self.mainwndow.inferer = model
        if r == 0:
            self.ui.label_loading.setText(
                f'<span style=" font-size:12pt;">Welcome!</span>'
            )
        elif r == 1:
            self.ui.label_loading.setText(
                f'<span style=" font-size:12pt; color: #db5a6b;">Model path error, check the settings!</span>'
            )
        elif r == 2:
            self.ui.label_loading.setText(
                f'<span style=" font-size:12pt; color: #db5a6b;">Model not supported!</span>'
            )
        loop = QEventLoop()
        QTimer.singleShot(1000, loop.quit)
        loop.exec()
        self.mainwndow.finish_init()
        self.mainwndow.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = mPSAT()
    splash = Splash(mainwindow=mainwindow)
    splash.show()
    splash.load_main_window()
    sys.exit(app.exec())
