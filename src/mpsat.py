'''
Description: mPSAT main application entry
Author: Rainyl
LastEditTime: 2022-08-04 15:58:11
'''
import sys
from PySide6.QtWidgets import QApplication

from src.mpsatApp import mPSAT
from src.splash import Splash


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = mPSAT()
    splash = Splash(mw=mainwindow)
    # splash.show()
    # splash.load_main_window()
    sys.exit(app.exec())
