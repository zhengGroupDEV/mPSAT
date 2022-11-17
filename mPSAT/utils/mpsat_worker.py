"""
Description: workers
Author: Rainyl
LastEditTime: 2022-07-31 18:48:35
"""
from typing import Tuple, Union
import os
import time
import numpy as np
from PySide6.QtCore import QObject, Signal, Slot

from mPSAT.utils.infer_base import MpInferenceBase
from mPSAT.utils.inferrer import MpInferenceOnnx


class MatchWorker(QObject):
    finished = Signal(list)

    def __init__(
        self,
        inferer: MpInferenceBase, 
        spec: np.ndarray,
        rmco2: bool, co2fac: float,
        topn: int,
    ):
        super(MatchWorker, self).__init__()
        self.inferer = inferer
        self.spec = spec
        self.rmco2 = rmco2
        self.co2fac = co2fac
        self.topn = topn

    @Slot()
    def run(self) -> None:
        out = self.inferer([self.spec], topk=self.topn)
        self.finished.emit(out)


class LoadModelWorker(QObject):
    finished = Signal(tuple)

    def __init__(self, label_name_str: str, method: int, model_path: str, device: str="cpu",):
        super(LoadModelWorker, self).__init__()
        self.label_name_str = label_name_str
        self.method = method
        self.model_path = model_path
        self.inferer: MpInferenceBase = None
        self.device = device  # TODO: add device option to GUI

    def load_model(self) -> int:
        """
        return:
            0 - success
            1 - model path not exist
            2 - method not supported
        """
        if self.method == 0:
            model_name = "cnn"
        elif self.method == 1:
            model_name = "rf"
        elif self.method == 2:
            model_name = "cnn2d"
        else:
            return 2
            # raise NotImplementedError(f"method {self.method} not implemented")
        if not os.path.exists(self.model_path):
            print(f"model path {self.model_path} not exists!")
            return 1
        self.inferer = MpInferenceOnnx(
            model_path=self.model_path,
            model_name=model_name,
            label_name=self.label_name_str,
            device=self.device,
        )
        return 0

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
