"""
Description: settings
Author: Rainyl
LastEditTime: 2022-08-01 15:38:27
"""
from dynaconf import loaders
from dynaconf import Dynaconf
from config import msettings

mpsat_settings = msettings.from_env("deploy")


class DefaultSettings(object):
    spec_type = "FTIR"
    rmin = 400
    rmax = 4000
    smooth = 3
    baseline = 8
    adjneg = False

    h2o = False
    co2 = True
    co2fac = 0.2
    analyze = 0  # 0: processed, 1: original
    method = 0  # 0: CNN, 1: RF, 2: LSVM

    cnn = ""
    rf = ""
    lsvm = ""
    topn = 10
    loglv = 0
    lang = "English"

    LANGS = {
        0: "English",
        1: "简体中文",
        "English": 0,
        "简体中文": 1,
    }


def save_config(set: Dynaconf, env="deploy"):
    loaders.write("settings.json", data=set.to_dict(), env=env)
