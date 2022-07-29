'''
Description: main logic app
Author: Rainyl
LastEditTime: 2022-07-29 23:19:14
'''
from PySide6.QtWidgets import QMainWindow
from src.mpsatUI import Ui_MainWindow

class mPSAT(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(mPSAT, self).__init__()
        self.setupUi(self)

