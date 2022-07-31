"""
Description: workers
Author: Rainyl
LastEditTime: 2022-07-31 18:48:35
"""
from PySide6.QtCore import QObject, Signal


class MatchWorker(QObject):
    finished = Signal(object)

    def __init__(
        self,
    ):
        super(MatchWorker, self).__init__()

    def run(self) -> None:
        ...


class PreWorker(QObject):
    finished = Signal(object)

    def __init__(
        self,
    ):
        super(PreWorker, self).__init__()

    def run(self) -> None:
        ...
