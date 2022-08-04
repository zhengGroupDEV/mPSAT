"""
Description: workers
Author: Rainyl
LastEditTime: 2022-07-31 18:48:35
"""
import os
import time
from typing import Tuple, Union
from PySide6.QtCore import QObject, Signal, Slot

from src.infer_base import MpInferenceBase
from src.infer_nn import MpInferenceNNONNX
from src.infer_skl import MpInferenceSKL


class MatchWorker(QObject):
    finished = Signal(object)

    def __init__(self):
        super(MatchWorker, self).__init__()

    @Slot()
    def run(self) -> None:
        ...


class LoadModelWorker(QObject):
    finished = Signal(tuple)

    def __init__(self, label_name_str: str, method: int, model_path: str):
        super(LoadModelWorker, self).__init__()
        self.label_name_str = label_name_str
        self.method = method
        self.model_path = model_path
        self.inferer: MpInferenceBase = None

    def load_model(self) -> int:
        """
        return:
            0 - success
            1 - model path not exist
            2 - method not supported
        """
        if self.method == 0:  # CNN
            if not os.path.exists(self.model_path):
                print(f"model path {self.model_path} not exists!")
                return 1
            self.inferer = MpInferenceNNONNX(
                model_path=self.model_path,
                label_name=self.label_name_str,
            )
            return 0
        elif self.method == 1 or self.method == 2:
            if not os.path.exists(self.model_path):
                print(f"model path {self.model_path} not exists!")
                return 1
            self.inferer = MpInferenceSKL(
                model_path=self.model_path,
                label_name=self.label_name_str,
            )
            return 0
        else:
            print(f"method [{self.method}] not supported")
            return 2

    @Slot()
    def run(self):
        try:
            time.sleep(1)  # avoid to stuck main thread
            r = self.load_model()
            self.finished.emit((r, self.inferer))
        except Exception as e:
            print(f"load model error: [{e}]")


class PreWorker(QObject):
    finished = Signal(object)

    def __init__(self):
        super(PreWorker, self).__init__()

    @Slot()
    def run(self) -> None:
        ...
