"""
Description: spectroscopy
Author: Rainyl
LastEditTime: 2022-07-31 18:07:30
"""
from typing import Dict
import numpy as np
from scipy.signal import savgol_filter

from src.enum import SPEC, PLOT


class Spectrum(object):
    SPEC_DATA: Dict[SPEC, np.ndarray] = {
        SPEC.X_ORI: np.array([]),
        SPEC.Y_ORI: np.array([]),
        SPEC.X_RANGE: np.array([]),
        SPEC.Y_RANGE: np.array([]),
        SPEC.X_PP: np.array([]),
        SPEC.Y_PP: np.array([]),
    }

    def __init__(self):
        ...

    def set_spec(
        self,
        x: np.ndarray,
        y: np.ndarray,
        range_min: float = 0,
        range_max: float = 6000,
    ) -> None:
        self.SPEC_DATA[SPEC.X_ORI] = x
        self.SPEC_DATA[SPEC.Y_ORI] = y
        self.update_range(range_min=range_min, range_max=range_max)

    def update_range(self, range_min: float = 0, range_max: float = 6000):
        x = self.SPEC_DATA[SPEC.X_ORI]
        y = self.SPEC_DATA[SPEC.Y_ORI]
        if len(x) == 0 or len(y) == 0:
            return
        idx = np.where((range_min <= x) & (x <= range_max))
        wavenum = x[idx]
        absorb = y[idx]
        self.SPEC_DATA[SPEC.X_RANGE] = wavenum
        self.SPEC_DATA[SPEC.Y_RANGE] = absorb

    def adj_negative(self, x):
        if not isinstance(x, np.ndarray):
            x = np.array(x)
        # x[x < 0] = 0
        # x = x + abs(x.min()) + 1 if x.min() < 1 else x
        x = x + abs(x.min()) if x.min() < 0 else x
        return x

    def minmax(self, x: np.ndarray) -> np.ndarray:
        if not isinstance(x, np.ndarray):
            x = np.array(x)
        return (x - min(x)) / (max(x) - min(x))

    def iModPolyFit(self, x, y, n: int) -> np.ndarray:
        if not all([isinstance(x, np.ndarray), isinstance(y, np.ndarray)]):
            x, y = np.array(x), np.array(y)
        wavesOriginal = x
        devPrev = 0
        firstIter = True
        criteria = False
        while not criteria:
            paramVector = np.polynomial.Polynomial.fit(x, y, n)
            mod_poly = paramVector(x)
            residuals = y - mod_poly
            dev_curr = residuals.std(ddof=1)

            if firstIter:
                peaks = []
                for i in range(y.shape[0]):
                    if y[i] > mod_poly[i] + dev_curr:
                        peaks.append(i)
                peaks = np.array(peaks)
                y = np.delete(y, peaks)
                mod_poly = np.delete(mod_poly, peaks)
                x = np.delete(x, peaks)
                firstIter = False
            for j in range(y.shape[0]):
                if mod_poly[j] + dev_curr > y[j]:
                    pass
                else:
                    y[j] = mod_poly[j]
            criteria = abs((dev_curr - devPrev) / dev_curr) <= 0.05

            if criteria:
                t = np.interp(wavesOriginal, x, y)
                return t.flatten()
            devPrev = dev_curr

    def preprocess(self, smooth: int, baseline: int, adj_neg: bool = False):
        wavenum: np.ndarray = self.SPEC_DATA[SPEC.X_RANGE]
        absorb: np.ndarray = self.SPEC_DATA[SPEC.Y_RANGE]
        if adj_neg:
            absorb = self.adj_negative(absorb)
        if smooth == 0:
            smoothed = absorb
        else:
            smoothed: np.ndarray = savgol_filter(
                x=absorb, window_length=11, polyorder=smooth
            )
        if baseline != 0:
            baselineRemove = smoothed - self.iModPolyFit(wavenum, smoothed, baseline)
        else:
            baselineRemove = smoothed
        baselineRemove = self.minmax(baselineRemove)
        self.SPEC_DATA[SPEC.X_PP] = wavenum
        self.SPEC_DATA[SPEC.Y_PP] = baselineRemove
        res = {PLOT.X: self.SPEC_DATA[SPEC.X_PP], PLOT.Y: self.SPEC_DATA[SPEC.Y_PP]}
        return res

    @property
    def x(self):
        return self.SPEC_DATA[SPEC.X_PP]

    @property
    def y(self):
        return self.SPEC_DATA[SPEC.Y_PP]

    @property
    def x_ori(self):
        return self.SPEC_DATA[SPEC.X_ORI]

    @property
    def y_ori(self):
        return self.SPEC_DATA[SPEC.Y_ORI]

    @property
    def x_rg(self):
        return self.SPEC_DATA[SPEC.X_RANGE]

    @property
    def y_rg(self):
        return self.SPEC_DATA[SPEC.Y_RANGE]
