'''
Description: enum
Author: Rainyl
LastEditTime: 2022-08-01 20:03:59
'''
from enum import Enum
class RT(Enum):
    SELECTED_FILES = 0
    FILE_TYPE = 1
    SPEC_TYPE = 2
    MAX_SPEC_NUM = 3
    SPEC_DATA = 4
    CRT_IDX = 5
    CNN_PATH = 6
    RF_PATH = 7
    LSVM_PATH = 8

class PLOT(Enum):
    X = 0
    Y = 1

class SPEC(Enum):
    X_ORI = 0
    Y_ORI = 1

    X_RANGE = 2
    Y_RANGE = 3

    X_PP = 4
    Y_PP = 5
    
class BTN(Enum):
    CNN = 1
    RF = 2
    LSVM = 3
