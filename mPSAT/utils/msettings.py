"""
Description: settings
Author: Rainyl
LastEditTime: 2022-08-01 15:38:27
"""
import json
import os
import sys
from typing import Dict, Union


class MpsatSettings(object):
    settings_path = "config/settings.json"
    SPEC_TYPE = "FTIR"
    RMIN = 400
    RMAX = 4000
    SMOOTH = 3
    BASELINE = 8
    ADJNEG = False

    H2O = False
    CO2 = True
    CO2FAC = 0.2
    ANALYZE = 0  # 0: processed, 1: original
    METHOD = 0  # 0: CNN, 1: RF, 2: LSVM

    CNN = ""
    RF = ""
    LSVM = ""
    TOPN = 10
    LOGLV = 0
    LANG = "English"

    THEME = "theme/qss/light_blue.qss"

    LANGS = {
        0: "English",
        1: "简体中文",
        "English": 0,
        "简体中文": 1,
    }

    def __init__(self, path: str = None) -> None:
        home_dir = os.path.expanduser("~")
        if sys.platform == "win32":
            self.settings_path = home_dir + "\\.config\\mPSAT\\settings.json"
        elif sys.platform == "linux":
            self.settings_path = home_dir + "/.config/mPSAT/settings.json"
        else:
            raise NotImplementedError(f"platform {sys.platform} not supported!")
        if path is not None:
            self.settings_path = path
        if not os.path.exists(self.settings_path):
            print(f"config file not exist, created at {self.settings_path}")
            os.makedirs(os.path.dirname(self.settings_path), exist_ok=True)
            self.sync()

    def load(self, p: str = None):
        p = self.settings_path if p is None else p
        if os.path.exists(p):
            try:
                with open(p, "r") as f:
                    settings: Dict[str, Union[int, str]] = json.load(f)
            except Exception as e:
                self.sync()
                return
            for k, v in settings.items():
                try:
                    getattr(self, k)
                    setattr(self, k, v)
                except AttributeError:
                    ...
        else:
            self.sync()

    def sync(self):
        settings = {
            "SPEC_TYPE": self.SPEC_TYPE,
            "RMIN": self.RMIN,
            "RMAX": self.RMAX,
            "SMOOTH": self.SMOOTH,
            "BASELINE": self.BASELINE,
            "ADJNEG": self.ADJNEG,
            "H2O": self.H2O,
            "CO2": self.CO2,
            "CO2FAC": self.CO2FAC,
            "ANALYZE": self.ANALYZE,
            "METHOD": self.METHOD,
            "CNN": self.CNN,
            "RF": self.RF,
            "LSVM": self.LSVM,
            "TOPN": self.TOPN,
            "LOGLV": self.LOGLV,
            "LANG": self.LANG,
            "THEME": self.THEME,
        }
        with open(self.settings_path, "w") as f:
            json.dump(settings, f, indent=4)

    def lang_to_idx(self, lang: str):
        return self.LANGS.get(lang, -1)

    def idx_to_lang(self, idx: int):
        return self.LANGS.get(idx, -1)
