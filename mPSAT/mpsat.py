'''
Description: mPSAT main application entry
Author: Rainyl
LastEditTime: 2022-08-09 10:32:19
'''
import sys
import faulthandler
from PySide6.QtWidgets import QApplication

from mPSAT.mpsatApp import mPSAT
from mPSAT.splash import Splash

faulthandler.enable()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = mPSAT()
    splash = Splash(mw=mainwindow)
    # splash.show()
    # splash.load_main_window()
    sys.exit(app.exec())
