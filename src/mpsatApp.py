"""
Description: main logic app
Author: Rainyl
LastEditTime: 2022-07-30 17:21:53
"""
import numpy as np
import pyqtgraph as pg
from typing import Dict, List, Union
from PySide6.QtCore import QSettings, Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QButtonGroup,
    QAbstractButton,
    QFileDialog,
    QListWidgetItem,
    QMessageBox,
)
from src.spectroscopy import Spectrum
from src.enum import RT, PP, MC, PLOT
from src.mpsatUI import Ui_MainWindow
from src.logger import MPSATLogger


class mPSAT(QMainWindow, Ui_MainWindow):
    param_runtime: Dict[RT, Union[List, str, int]] = {
        RT.SELECTED_FILES: [],
        RT.SPEC_DATA: [],
        RT.CRT_IDX: -1,
        RT.SPEC_TYPE: "FTIR",
        RT.MAX_SPEC_NUM: 100,
    }
    param_preprocess: Dict[PP, Union[int, bool]] = {
        PP.MIN: 0,
        PP.MAX: 6000,
        PP.SMOOTH: 3,
        PP.BASELINE: 8,
        PP.ADJ_NEG: False,
    }
    param_match = {}
    param_plot: Dict[PLOT, Union[list, int, Dict[PLOT, np.ndarray]]] = {
        PLOT.PRE_DATA: {
            PLOT.X: np.array([]),
            PLOT.Y: np.array([]),
        },
        PLOT.MC_DATA: {
            PLOT.X: np.array([]),
            PLOT.Y: np.array([]),
        },
    }
    logger = MPSATLogger("main")
    spectrum = Spectrum()

    def __init__(self) -> None:
        pg.setConfigOption("background", "w")
        pg.setConfigOption("foreground", "k")
        super(mPSAT, self).__init__()
        self.settings = QSettings("zhengGroup", "mpsat")
        self.setupUi(self)
        self.set_signals()
        self.restore_settings()

    def set_signals(self):
        # spec/preprocess
        self.btn_pop_pre_files.clicked.connect(self.btn_pop_pre_files_clicked)
        self.btn_select_file_dir.clicked.connect(self.btn_select_file_dir_clicked)
        self.btn_clear_pre_files.clicked.connect(self.btn_pre_clear_clicked)
        self.listw_pre_files.currentRowChanged.connect(
            self.on_pre_listw_current_row_changed
        )
        # self.btn_stop_pre.clicked.connect(self.btn_stop_pre_clicked)
        self.slider_pre_smooth.valueChanged.connect(self.slider_presmooth_changed)
        self.slider_pre_baseline.valueChanged.connect(self.slider_prebaseline_changed)
        self.ledit_pre_min.editingFinished.connect(self.ledit_pre_min_finished)
        self.ledit_pre_max.editingFinished.connect(self.ledit_pre_max_finished)
        self.ckbox_adjneg.stateChanged.connect(self.ckbox_adjneg_changed)
        self.btn_pre_save.clicked.connect(self.btn_save_pre_spec_clicked)
        # spec/match
        self.btn_spec_match_prev.clicked.connect(self.btn_match_prev_clicked)
        self.btn_spec_match_next.clicked.connect(self.btn_match_next_clicked)
        self.ckbox_co2.stateChanged.connect(self.ckbox_rm_co2_h2o)
        self.cbox_match_analyze.currentIndexChanged.connect(self.cmbox_analyze_changed)
        self.cbox_match_method.currentIndexChanged.connect(self.cmbox_method_changed)
        self.btn_match_go.clicked.connect(self.btn_match_clicked)

        self.btngrp_spec_set_browse = QButtonGroup(self)
        self.btngrp_spec_set_browse.addButton(self.btn_spec_set_cnn)
        self.btngrp_spec_set_browse.addButton(self.btn_spec_set_lsvm)
        self.btngrp_spec_set_browse.addButton(self.btn_spec_set_rf)
        self.btngrp_spec_set_browse.buttonClicked.connect(
            self.spec_set_browse_btn_clicked
        )

    def restore_settings(self):
        ...

    def btn_pop_pre_files_clicked(self):
        cur_row = self.listw_pre_files.currentRow()
        self.logger.debug(
            f"cur_row: {cur_row}, max: {len(self.param_runtime[RT.SELECTED_FILES])}"
        )
        if 0 <= cur_row < len(self.param_runtime[RT.SELECTED_FILES]):
            self.param_runtime[RT.SELECTED_FILES].pop(cur_row)
            self.param_runtime[RT.SPEC_DATA].pop(cur_row)
            self.listw_pre_files.takeItem(cur_row)

    def btn_pre_clear_clicked(self):
        self.param_runtime[RT.SELECTED_FILES].clear()
        self.param_runtime[RT.SPEC_DATA].clear()
        self.listw_pre_files.clear()

    def btn_select_file_dir_clicked(self):
        file_names = QFileDialog.getOpenFileNames(
            self,
            caption="Select Files",
            dir=".",
            filter="csv Files (*.csv);;images (*.jpg *.png)",
            # filter="csv Files (*.csv);;images (*.jpg *.png)",
        )
        files, fmt = file_names
        if RT.FILE_TYPE in self.param_runtime:
            if self.param_runtime[RT.FILE_TYPE] != fmt:
                self.param_runtime[RT.FILE_TYPE] = fmt
                self.param_runtime[RT.SELECTED_FILES].clear()
        else:
            self.param_runtime[RT.FILE_TYPE] = fmt
        if self.check_max_spec_num:
            for p in files:
                csv_data = self.read_csv(p)
                if csv_data:
                    self.param_runtime[RT.SELECTED_FILES].append(p)
                    self.param_runtime[RT.SPEC_DATA].append(csv_data)
                else:
                    self.show_warning_msg(f"csv file {p} not valid!")
            self.update_list_pres()

    def show_warning_msg(self, msg):
        QMessageBox(
            QMessageBox.Warning,
            f"Warning",
            f"{msg}",
            buttons=QMessageBox.Ok,
            parent=self,
        ).exec()

    def check_max_spec_num(self, new_files):
        now = len(self.param_runtime[RT.SELECTED_FILES])
        max_ = self.param_runtime[RT.MAX_SPEC_NUM]
        if now + len(new_files) > max_:
            self.show_warning_msg(
                f"The selected spectral files reached the maximum number [{max_}]"
            )
            return False
        return True

    def update_list_pres(self):
        self.listw_pre_files.clear()
        self.listw_pre_files.addItems(self.param_runtime[RT.SELECTED_FILES])

    def btn_stop_pre_clicked(self):
        ...

    def ckbox_adjneg_changed(self, state: int):
        if state == Qt.CheckState.Checked:
            self.param_preprocess[PP.ADJ_NEG] = True
        elif state == Qt.CheckState.Unchecked:
            self.param_preprocess[PP.ADJ_NEG] = False
        else:
            self.logger.warning(f"checkbox adjneg stat is 1")
        self.update_pre_plot()

    def slider_presmooth_changed(self, val: int):
        self.param_preprocess[PP.SMOOTH] = val
        self.label_pre_smooth.setText(f"{val}")
        self.update_pre_plot()

    def slider_prebaseline_changed(self, val: int):
        self.param_preprocess[PP.BASELINE] = val
        self.label_pre_baseline.setText(f"{val}")
        self.update_pre_plot()

    def ledit_pre_min_finished(self):
        ledit_min = self.ledit_pre_min.text()
        if len(ledit_min) != 0:
            self.param_preprocess[PP.MIN] = int(ledit_min)
            self.update_pre_plot()

    def ledit_pre_max_finished(self):
        ledit_max = self.ledit_pre_max.text()
        if len(ledit_max) != 0:
            self.param_preprocess[PP.MAX] = int(ledit_max)
            self.update_pre_plot()

    def btn_save_pre_spec_clicked(self):
        if len(self.spectrum.x) == 0:
            self.show_warning_msg(f"no data to save!")
            return
        filename = QFileDialog.getSaveFileName(
            self,
            caption="Save",
            dir=".",
            filter="csv (*.csv)",
        )
        fname = filename[0]
        if fname:
            data = np.vstack((self.spectrum.x, self.spectrum.y)).T
            np.savetxt(
                fname,
                data,
                fmt="%.2f",
                delimiter=",",
                comments="",
                header="wavenum,intensity",
            )

    def btn_match_prev_clicked(self):
        ...

    def btn_match_next_clicked(self):
        ...

    def ckbox_rm_co2_h2o(self, state: int):
        ...

    def cmbox_analyze_changed(self, idx: int):
        ...

    def cmbox_method_changed(self, idx: int):
        ...

    def btn_match_clicked(self):
        ...

    def spec_set_browse_btn_clicked(self, btn: QAbstractButton):
        ...

    def read_csv(self, fpath: str) -> Union[Dict[PLOT, np.ndarray], bool]:
        try:
            d = np.loadtxt(
                fpath,
                dtype=np.float32,
                comments=None,
                delimiter=",",
                skiprows=1,
            )
            x = d.T[0]
            y = d.T[1]
            return {PLOT.X: x, PLOT.Y: y}
        except Exception as e:
            self.logger.warning(f"csv file [{fpath}] is not valid!, error: [{e}]")
            return False

    def update_pre_plot(self):
        cur_row = self.listw_pre_files.currentRow()
        if cur_row == -1:
            return
        x = self.param_runtime[RT.SPEC_DATA][cur_row][PLOT.X]
        y = self.param_runtime[RT.SPEC_DATA][cur_row][PLOT.Y]
        rmin = self.param_preprocess[PP.MIN]
        rmax = self.param_preprocess[PP.MAX]
        smooth = self.param_preprocess[PP.SMOOTH]
        baseline = self.param_preprocess[PP.BASELINE]
        adj_neg = self.param_preprocess[PP.ADJ_NEG]
        self.spectrum = Spectrum()
        self.spectrum.set_spec(x=x, y=y, range_min=rmin, range_max=rmax)
        self.spectrum.preprocess(smooth=smooth, baseline=baseline, adj_neg=adj_neg)
        self.fig_spec_pre.update_pre_plot(
            x=self.spectrum.x_rg,
            y=self.spectrum.y_rg,
            x1=self.spectrum.x,
            y1=self.spectrum.y,
        )

    def on_pre_listw_current_row_changed(self, row: int):
        if row == -1:
            self.fig_spec_pre.reset_plot()
        else:
            self.update_pre_plot()
