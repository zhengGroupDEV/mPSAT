"""
Description: busy dialog
Author: Rainyl
LastEditTime: 2022-08-04 10:29:21
"""
from PySide6.QtCore import QEventLoop, QTimer
from PySide6.QtWidgets import QDialog
from mPSAT.widgets.busy_dialogUI import Ui_Dialog


class BusyDialog(QDialog):
    def __init__(self, parent=None) -> None:
        super(BusyDialog, self).__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def set_label(self, label: str="Loading..."):
        self.ui.label_info.setText(label)

    def close(self, sig: int=0):
        if sig == 0:
            self.setWindowTitle("Success")
            self.ui.label_info.setText(f"Success!")
        elif sig == 1:
            self.setWindowTitle("Error")
            self.ui.label_info.setText(f"Model path error!")
        elif sig == 2:
            self.setWindowTitle("Error")
            self.ui.label_info.setText(f"Model not supported!")
        else:
            self.setWindowTitle("Error")
            self.ui.label_info.setText(f"Unknown error")
        loop = QEventLoop()
        QTimer.singleShot(1000, loop.quit)
        loop.exec()
        super().close()
