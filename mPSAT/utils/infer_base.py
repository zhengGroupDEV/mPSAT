"""
Description: inference base class
Author: Rainyl
Date: 2022-07-06 19:11:17
"""
import json
import os
import warnings
import numpy as np
from numpy.typing import NDArray
from typing import List, Union, Dict


class MpInferenceBase(object):
    xx = np.arange(400, 4000, 1).astype(np.float32)

    def __init__(
        self, model_path: str, model_name: str, label_name: str, num_class: int = 200
    ):
        self.model = self.load_model(model_path)
        self.model_name = model_name
        self.num_class = num_class
        self.label_name_hash = self.load_label_name(label_name)

    def minmax(self, x: NDArray[np.float32]) -> NDArray[np.float32]:
        return (x - min(x)) / (max(x) - min(x))

    def normalize(self, x: NDArray[np.float32], mean=0.5, std=0.5):
        return (x - mean) / std

    def softmax(self, x: NDArray[np.float32], axis=1) -> NDArray[np.float32]:
        # x: (B, num_class)
        return np.exp(x) / np.sum(np.exp(x), axis=axis, keepdims=True)

    # def adj_negative(self, x):
    #     if not isinstance(x, np.ndarray):
    #         x = np.array(x)
    #     # x[x < 0] = 0
    #     # x = x + abs(x.min()) + 1 if x.min() < 1 else x
    #     x = x + abs(x.min()) if x.min() < 0 else x
    #     return x

    # def iModPolyFit(self, x, y, n: int) -> NDArray[np.float32]:  # type: ignore
    #     if not all([isinstance(x, np.ndarray), isinstance(y, np.ndarray)]):
    #         x, y = np.array(x), np.array(y)
    #     wavesOriginal = x
    #     devPrev = 0
    #     firstIter = True
    #     criteria = False
    #     while not criteria:
    #         paramVector = np.polynomial.Polynomial.fit(x, y, n)
    #         mod_poly = paramVector(x)
    #         residuals = y - mod_poly
    #         dev_curr = residuals.std(ddof=1)

    #         if firstIter:
    #             peaks = []
    #             for i in range(y.shape[0]):
    #                 if y[i] > mod_poly[i] + dev_curr:
    #                     peaks.append(i)
    #             peaks = np.array(peaks)
    #             y = np.delete(y, peaks)
    #             mod_poly = np.delete(mod_poly, peaks)
    #             x = np.delete(x, peaks)
    #             firstIter = False
    #         for j in range(y.shape[0]):
    #             if mod_poly[j] + dev_curr > y[j]:
    #                 pass
    #             else:
    #                 y[j] = mod_poly[j]
    #         criteria = abs((dev_curr - devPrev) / dev_curr) <= 0.05

    #         if criteria:
    #             t = np.interp(wavesOriginal, x, y)
    #             return t.flatten()  # type: ignore
    #         devPrev = dev_curr

    # def specy_prep(
    #     self, wavenum, absorb, smooth: int = 0, baseline: int = 0, adj_neg: bool = False
    # ):
    #     if adj_neg:
    #         absorb = self.adj_negative(absorb)
    #     if smooth == 0:
    #         smoothed = absorb
    #     else:
    #         smoothed: NDArray[np.float32] = savgol_filter(
    #             x=absorb,
    #             window_length=11,
    #             polyorder=smooth,
    #         )  # type: ignore
    #     if baseline != 0:
    #         baselineRemove = smoothed - self.iModPolyFit(wavenum, smoothed, baseline)  # type: ignore
    #     else:
    #         baselineRemove = smoothed
    #     baselineRemove = self.minmax(baselineRemove)
    #     return baselineRemove

    # def load_label_name(self, p: str):
    #     label_name_hash: Dict[str, List[str]] = {
    #         str(i): [str(i)] for i in range(self.num_class)
    #     }
    #     if not os.path.exists(p):
    #         warnings.warn(f"label to name file {p} not exists!", ResourceWarning)
    #         return label_name_hash
    #     with open(p, "r") as f:
    #         label_name_hash = json.load(f)
    #     return label_name_hash

    def load_label_name(self, p: str):
        # label_name_hash: Union[None, Dict[str, List[str]]] = None
        # if os.path.exists(p):
        #     warnings.warn(f"label to name file {p} not exists!", ResourceWarning)
        # with open(p, "r") as f:
        #     label_name_hash = json.load(f)
        try:
            label_name_hash = json.loads(p)
        except Exception as e:
            print(f"ERROR: label to name error, fallback to label only, error; [{e}]")
            label_name_hash = {f"{i}": "i" for i in range(120)}
        return label_name_hash

    def label2name(self, labels: List[List[int]]) -> List[List[List[str]]]:
        if self.label_name_hash is None:
            return labels  # type: ignore
        if not all([all([c in self.label_name_hash for c in row]) for row in labels]):
            warnings.warn(f"some label not in label_name_hash table!", ResourceWarning)
        names = [[self.label_name_hash[str(c)] for c in row] for row in labels]
        return names

    def rm_co2(self, y: NDArray[np.float32], x=None):
        if x is not None:
            assert isinstance(x, np.ndarray) and x.shape == y.shape
            idx = np.argsort(x)
            x_, y_ = x[idx], y[idx]
            y = np.interp(self.xx, x_, y_, left=0, right=0)
        c1 = (self.xx >= 2280) & (self.xx <= 2400)
        c2 = (self.xx >= 3570) & (self.xx <= 3750)
        # idxs = (c1 | c2)
        # replace with a line
        min1 = min(y[c1])
        min2 = min(y[c2])
        y[c1] = min1
        y[c2] = min2
        # scale by fac
        # idxs = (c1 | c2)
        # y[idxs] = y[idxs] * fac
        y[y < 0] = 0
        return y

    def load_model(self, p: str):
        raise NotImplementedError()

    def __call__(
        self,
        spec: List[NDArray[np.float32]],
        topk: int,
        return_score: bool,
    ):
        raise NotImplementedError()

    def preprocess(
        self,
        spec: List[NDArray[np.float32]],
        openspecy: bool = False,
        smooth: int = 3,
        baseline: int = 8,
    ):
        new_spec = []
        for s in spec:
            assert len(s.shape) == 2, f"the shape of spec is {s.shape}"
            if not isinstance(s, np.ndarray):
                s = np.asarray(s, dtype=np.float32)
            # sort
            idx = np.argsort(s.T[0])
            s = s[idx]
            # drop
            s1 = s[s.T[0] >= 500]
            # interpolate
            yy = np.interp(self.xx, s1.T[0], s1.T[1], left=0, right=0)
            # openspecy
            if openspecy:
                yy = self.specy_prep(self.xx, yy, smooth=smooth, baseline=baseline)
            # rmco2
            yy = self.rm_co2(yy)
            yy = self.minmax(yy)
            new_spec.append(yy)
        x = np.asarray(new_spec, dtype=np.float32)
        return x
