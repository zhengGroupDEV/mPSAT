'''
Description: enum
Author: Rainyl
LastEditTime: 2022-07-31 20:03:56
'''
from enum import Enum
class RT(Enum):
    SELECTED_FILES = 0
    FILE_TYPE = 1
    SPEC_TYPE = 2
    MAX_SPEC_NUM = 3
    SPEC_DATA = 4
    CRT_IDX = 5


class PP(Enum):
    SMOOTH = 0
    BASELINE = 1
    MIN = 2
    MAX = 3
    ADJ_NEG = 4

class MC(Enum):
    ...

class PLOT(Enum):
    X = 0
    Y = 1
    PRE_DATA = 2
    MC_DATA = 3

class SPEC(Enum):
    X_ORI = 0
    Y_ORI = 1

    X_RANGE = 2
    Y_RANGE = 3

    X_PP = 4
    Y_PP = 5
    
