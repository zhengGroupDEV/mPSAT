'''
Description: mPSAT main application entry
Author: Rainyl
LastEditTime: 2022-07-29 23:18:25
'''
import sys
from PySide6.QtWidgets import QApplication

from src.mpsatApp import mPSAT


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mPSAT()
    window.show()
    sys.exit(app.exec())
