'''
Description: logger
Author: Rainyl
LastEditTime: 2022-07-30 19:21:16
'''
import coloredlogs, logging


class MPSATLogger(logging.Logger):
    def __init__(self, name: str, level=logging.DEBUG):
        super(MPSATLogger, self).__init__(name=name, level=level)
        coloredlogs.install(level='DEBUG', logger=self)
