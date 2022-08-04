"""
Description: main logic app
Author: Rainyl
LastEditTime: 2022-07-30 17:21:53
"""
import os
import numpy as np
import pyqtgraph as pg
from typing import Dict, List, Tuple, Union
from PySide6.QtCore import Qt, QFile, QIODeviceBase, Signal, QThread, Slot
from PySide6.QtWidgets import (
    QMainWindow,
    QButtonGroup,
    QAbstractButton,
    QFileDialog,
    QMessageBox,
    QTableWidgetItem,
)

from mPSAT.utils.spectroscopy import Spectrum
from mPSAT.utils.enum import RT, PLOT, BTN
from mPSAT.mpsatUI import Ui_MainWindow
from mPSAT.utils.logger import MPSATLogger
from mPSAT.utils.infer_base import MpInferenceBase
from mPSAT.utils.infer_nn import MpInferenceNNONNX
from mPSAT.utils.infer_skl import MpInferenceSKL
from mPSAT.utils.msettings import MpsatSettings
from mPSAT.widgets.busy_dialog import BusyDialog
from mPSAT.utils.mpsat_worker import LoadModelWorker


class mPSAT(QMainWindow, Ui_MainWindow):
    param_runtime: Dict[RT, Union[List, str, int]] = {
        RT.SELECTED_FILES: [],
        RT.SPEC_DATA: [],
        RT.CRT_IDX: -1,
        RT.SPEC_TYPE: "FTIR",
        RT.MAX_SPEC_NUM: 100,
    }

    logger = MPSATLogger("main")
    spectrum = Spectrum()
    inferer: MpInferenceBase = None
    __init_finished__ = False

    def __init__(self) -> None:
        pg.setConfigOption("background", "w")
        pg.setConfigOption("foreground", "k")
        super(mPSAT, self).__init__()
        # self.settings = QSettings("zhengGroup", "mpsat")
        self.settings = MpsatSettings()
        self.setupUi(self)
        self.set_signals()
        self.restore_settings()

    def set_signals(self):
        # self.btn_close.clicked.connect(self.close)
        # self.btn_minimize.clicked.connect(self.showMinimized)
        # self.btn_maximize.clicked.connect(self.showMaximized)
        # home
        self.btn_hide_menu.clicked.connect(lambda: self.tabw_main.setCurrentIndex(0))
        self.btn_left_home.clicked.connect(lambda: self.tabw_main.setCurrentIndex(0))
        self.btn_left_preprocess.clicked.connect(
            lambda: self.tabw_main.setCurrentIndex(1)
        )
        self.btn_left_match.clicked.connect(lambda: self.tabw_main.setCurrentIndex(2))
        self.btn_settings.clicked.connect(lambda: self.tabw_main.setCurrentIndex(3))
        self.btn_about.clicked.connect(lambda: self.tabw_main.setCurrentIndex(4))
        # spec/preprocess
        self.btn_pop_pre_files.clicked.connect(self.btn_pop_pre_files_clicked)
        self.btn_select_file_dir.clicked.connect(self.btn_select_file_dir_clicked)
        self.btn_clear_pre_files.clicked.connect(self.btn_pre_clear_clicked)
        self.listw_pre_files.currentRowChanged.connect(
            self.on_pre_listw_current_row_changed
        )
        self.slider_pre_smooth.valueChanged.connect(self.slider_presmooth_changed)
        self.slider_pre_smooth.valueChanged.connect(self.settings.sync)
        self.slider_pre_baseline.valueChanged.connect(self.slider_prebaseline_changed)
        self.slider_pre_baseline.valueChanged.connect(self.settings.sync)
        self.spbox_pre_min.valueChanged.connect(self.pre_min_finished)
        self.spbox_pre_min.valueChanged.connect(self.settings.sync)
        self.spbox_pre_max.valueChanged.connect(self.pre_max_finished)
        self.spbox_pre_max.valueChanged.connect(self.settings.sync)
        self.ckbox_adjneg.stateChanged.connect(self.ckbox_adjneg_changed)
        self.ckbox_adjneg.stateChanged.connect(self.settings.sync)
        self.btn_pre_save.clicked.connect(self.btn_save_pre_spec_clicked)
        # spec/match
        self.btn_spec_match_prev.clicked.connect(self.btn_match_prev_clicked)
        self.btn_spec_match_next.clicked.connect(self.btn_match_next_clicked)
        self.ckbox_co2.stateChanged.connect(self.ckbox_rm_co2)
        self.ckbox_co2.stateChanged.connect(self.settings.sync)
        self.ckbox_h2o.stateChanged.connect(self.ckbox_rm_h2o)
        self.ckbox_h2o.stateChanged.connect(self.settings.sync)
        self.dspbox_co2.valueChanged.connect(self.dspbox_co2_changed)
        self.dspbox_co2.valueChanged.connect(self.settings.sync)
        self.cbox_match_analyze.currentIndexChanged.connect(self.cmbox_analyze_changed)
        self.cbox_match_analyze.currentIndexChanged.connect(self.settings.sync)
        self.cbox_match_method.currentIndexChanged.connect(self.cmbox_method_changed)
        self.cbox_match_method.currentIndexChanged.connect(self.settings.sync)
        self.btn_match_go.clicked.connect(self.btn_match_clicked)
        self.spbox_spec_topn.valueChanged.connect(self.topn_finished)
        self.spbox_spec_topn.valueChanged.connect(self.settings.sync)

        # settings
        self.btngrp_spec_set_browse = QButtonGroup(self)
        self.btngrp_spec_set_browse.addButton(self.btn_spec_set_cnn, id=BTN.CNN.value)
        self.btngrp_spec_set_browse.addButton(self.btn_spec_set_rf, id=BTN.RF.value)
        self.btngrp_spec_set_browse.addButton(self.btn_spec_set_lsvm, id=BTN.LSVM.value)
        self.btngrp_spec_set_browse.buttonClicked.connect(
            self.spec_set_browse_btn_clicked
        )
        self.btngrp_spec_set_browse.buttonClicked.connect(self.settings.sync)

        self.cbox_loglv.currentIndexChanged.connect(self.cbox_loglv_changed)
        self.cbox_loglv.currentIndexChanged.connect(self.settings.sync)
        self.cbox_lang.currentIndexChanged.connect(self.cbox_lang_changed)
        self.cbox_lang.currentIndexChanged.connect(self.settings.sync)

        self.btn_loglv.clicked.connect(self.show_busy_dialog)

        self.busydialog = BusyDialog(self)

    def restore_settings(self):
        self.settings.load()
        self.spbox_pre_min.setValue(self.settings.RMIN)
        self.spbox_pre_max.setValue(self.settings.RMAX)
        self.slider_pre_smooth.setValue(self.settings.SMOOTH)
        self.slider_pre_baseline.setValue(self.settings.BASELINE)
        self.ckbox_adjneg.setChecked(self.settings.ADJNEG)

        self.ckbox_h2o.setChecked(self.settings.H2O)
        self.ckbox_co2.setChecked(self.settings.CO2)
        self.cbox_match_analyze.setCurrentIndex(self.settings.ANALYZE)
        self.cbox_match_method.setCurrentIndex(self.settings.METHOD)

        self.ledit_spec_set_model_cnn.setText(self.settings.CNN)
        self.ledit_spec_set_model_rf.setText(self.settings.RF)
        self.ledit_spec_set_model_lsvm.setText(self.settings.LSVM)
        self.spbox_spec_topn.setValue(self.settings.TOPN)

        self.cbox_loglv.setCurrentIndex(self.settings.LOGLV)
        lang = self.settings.LANG
        lang = self.settings.LANGS.get(lang, 0)
        self.cbox_lang.setCurrentIndex(lang)

        self.splitter_match.setStretchFactor(0, 8)  # match, fig & table
        self.splitter_match.setStretchFactor(1, 1)
        self.splitter_pre_fig.setStretchFactor(0, 1)
        self.splitter_pre_fig.setStretchFactor(1, 6)

        self.table_match_res.setColumnWidth(0, 100)
        self.table_match_res.setColumnWidth(1, 10)

        self.tabw_main.tabBar().hide()
        # self.apply_theme(self.settings.THEME)

    def apply_theme(self, p: str):
        if os.path.exists(p):
            with open(p, "r") as f:
                style_str = f.read()
                self.setStyleSheet(style_str)
        else:
            self.logger.error(f"theme {p} not exist")

    def finish_init(self):
        self.__init_finished__ = True

    #########################################
    # Slots
    #########################################

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

    def ckbox_adjneg_changed(self, state: int):
        if state == Qt.CheckState.Checked:
            self.settings.ADJNEG = True
        elif state == Qt.CheckState.Unchecked:
            self.settings.ADJNEG = False
        else:
            self.logger.warning(f"checkbox adjneg stat is 1")
        self.update_pre_plot()

    def slider_presmooth_changed(self, val: int):
        self.settings.SMOOTH = val
        self.label_pre_smooth.setText(f"{val}")
        self.update_pre_plot()

    def slider_prebaseline_changed(self, val: int):
        self.settings.BASELINE = val
        self.label_pre_baseline.setText(f"{val}")
        self.update_pre_plot()

    def pre_min_finished(self):
        ledit_min = self.spbox_pre_min.value()
        if ledit_min > self.settings.RMAX:
            self.show_warning_msg(f"invalid min wavenumber!")
            return
        self.settings.RMIN = ledit_min
        self.update_pre_plot()

    def pre_max_finished(self):
        ledit_max = self.spbox_pre_max.value()
        if ledit_max < self.settings.RMIN:
            self.show_warning_msg(f"invalid max wavenumber!")
            return
        self.settings.RMAX = ledit_max
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
        cur_row = self.param_runtime[RT.CRT_IDX]
        if cur_row - 1 < 0:
            return
        cur_row = max(cur_row - 1, 0)
        self.param_runtime[RT.CRT_IDX] = cur_row
        self.infer_one_spec(idx=cur_row)

    def btn_match_next_clicked(self):
        cur_row = self.param_runtime[RT.CRT_IDX]
        max_len = len(self.param_runtime[RT.SPEC_DATA]) - 1
        if cur_row + 1 > max_len:
            return
        cur_row = min(cur_row + 1, max_len)
        self.param_runtime[RT.CRT_IDX] = cur_row
        self.infer_one_spec(idx=cur_row)

    def ckbox_rm_co2(self, state: int):
        if state == Qt.CheckState.Checked:
            self.settings.CO2 = True
        elif state == Qt.CheckState.Unchecked:
            self.settings.CO2 = False
        else:
            self.logger.warning(f"checkbox co2 stat is 1")

    def dspbox_co2_changed(self, v: float):
        self.settings.CO2FAC = v

    def ckbox_rm_h2o(self, state: int):
        if state == Qt.CheckState.Checked:
            self.settings.H2O = True
        elif state == Qt.CheckState.Unchecked:
            self.settings.H2O = False
        else:
            self.logger.warning(f"checkbox co2 stat is 1")

    def cmbox_analyze_changed(self, idx: int):
        self.settings.ANALYZE = idx

    def cmbox_method_changed(self, idx: int):
        self.settings.METHOD = idx
        if not self.__init_finished__:
            return
        self.show_busy_dialog(msg=f"Loading...", title="Loading model")

        self.inferer = None
        label_name = QFile(":/json/data/label_name.json")
        label_name.open(QIODeviceBase.ReadOnly)
        label_name_str = label_name.readAll().toStdString()
        method = self.settings.METHOD
        if method == 0:  # CNN
            model_path = self.settings.CNN
        elif method == 1:  # RF
            model_path = self.settings.RF
        elif method == 2:
            model_path = self.settings.LSVM
        else:
            self.logger.error(f"model method {method} not supported!")
            return

        self.th = QThread(self)
        self.worker = LoadModelWorker(
            label_name_str=label_name_str,
            method=method,
            model_path=model_path,
        )
        self.worker.moveToThread(self.th)
        self.worker.finished.connect(self.th.quit)
        self.worker.finished.connect(self.th.deleteLater)
        self.worker.finished.connect(self.load_model_finished)
        self.th.started.connect(self.worker.run)
        self.th.start()

    @Slot()
    def load_model_finished(self, res: Tuple[int, MpInferenceBase]):
        self.logger.debug(f"load model result: {res}")
        self.inferer = res[1]
        self.busydialog.close(res[0])

    def topn_finished(self):
        self.settings.TOPN = self.spbox_spec_topn.value()

    def btn_match_clicked(self):
        idx = self.listw_pre_files.currentRow()
        self.infer_one_spec(idx=idx)

    def spec_set_browse_btn_clicked(self, btn: QAbstractButton):
        idx = self.btngrp_spec_set_browse.id(btn)
        filename = QFileDialog.getOpenFileName(
            self,
            caption="Select Model",
            dir=".",
            filter="ONNX (*.onnx);;Pickle (*.pkl)",
        )
        fpath = filename[0]
        if not fpath:
            return
        if idx == BTN.CNN.value:
            self.settings.CNN = fpath
            self.ledit_spec_set_model_cnn.setText(fpath)
        elif idx == BTN.RF.value:
            self.settings.RF = fpath
            self.ledit_spec_set_model_rf.setText(fpath)
        elif idx == BTN.LSVM.value:
            self.settings.LSVM = fpath
            self.ledit_spec_set_model_lsvm.setText(fpath)
        else:
            self.logger.warning(f"button idx {idx} not specified")

    def cbox_loglv_changed(self, idx: int):
        self.settings.LOGLV = idx

    def cbox_lang_changed(self, idx: int):
        lang = self.settings.idx_to_lang(idx)
        self.settings.LANG = "English" if lang == -1 else lang

    #######################################
    # Functions
    #######################################
    def update_model(self) -> int:
        """
        return:
            0 - success
            1 - model path not exist
            2 - method not supported
        """
        self.inferer = None
        label_name = QFile(":/json/data/label_name.json")
        label_name.open(QIODeviceBase.ReadOnly)
        label_name_str = label_name.readAll().toStdString()
        method = self.settings.METHOD
        if method == 0:  # CNN
            model_path = self.settings.CNN
            self.logger.debug(f"switching model to [{model_path}]")
            if not os.path.exists(model_path):
                self.logger.error(f"model path {model_path} not exists!")
                return 1
            self.inferer = MpInferenceNNONNX(
                model_path=model_path,
                label_name=label_name_str,
            )
            return 0
        elif method == 1:  # RF
            model_path = self.settings.RF
        elif method == 2:  # LSVM
            model_path = self.settings.LSVM
        else:
            self.logger.error(f"method [{method}] not supported")
            self.show_warning_msg(f"method [{method}] not supported")
            return 2
        if not os.path.exists(model_path):
            self.logger.error(f"model path {model_path} not exists!")
            return 1
        self.logger.debug(f"switching model to [{model_path}]")
        self.inferer = MpInferenceSKL(
            model_path=model_path,
            label_name=label_name_str,
        )
        return 0

    def infer_one_spec(self, idx):
        if self.inferer is None:
            self.show_warning_msg(f"model error, check the model path")
            return
        if idx < 0 or idx >= len(self.param_runtime[RT.SPEC_DATA]):
            self.show_warning_msg(f"No data selected!")
            return
        xy = self.get_current_spec(cur_row=idx)
        if isinstance(xy[0], bool) and not xy[0]:
            self.show_warning_msg(f"Get spectrum failed!")
            return
        analyze = self.settings.ANALYZE
        if analyze == 0:  # processed
            self.preprocess_one_spec(x=xy[0], y=xy[1])
        xy = (self.spectrum.x, self.spectrum.y)
        spec = np.vstack(xy).T
        rmco2 = self.settings.CO2
        co2fac = self.settings.CO2FAC
        topn = self.settings.TOPN
        im = self.inferer.read_plot_csv(spec=spec, rmco2=rmco2, fac=co2fac)
        out = self.inferer([im], topk=topn)
        self.logger.debug(out)
        self.table_match_res.setRowCount(0)
        for i, row in enumerate(out):
            r = "+".join(row[0])
            self.table_match_res.insertRow(i)
            self.table_match_res.setItem(i, 0, QTableWidgetItem(r))
            self.table_match_res.setItem(i, 1, QTableWidgetItem(f"{row[1]*100:.2f}"))
        self.setWindowTitle(f"mPSAT - {self.param_runtime[RT.SELECTED_FILES][idx]}")
        self.update_match_plot()

    def get_current_spec(self, cur_row: int = None):
        if cur_row is None:
            cur_row = self.param_runtime[RT.CRT_IDX]
        if cur_row == -1:
            return (False, False)
        x: np.ndarray = self.param_runtime[RT.SPEC_DATA][cur_row][PLOT.X]
        y: np.ndarray = self.param_runtime[RT.SPEC_DATA][cur_row][PLOT.Y]
        return (x, y)

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

    def update_match_plot(self):
        name1 = "Original"
        x = self.spectrum.x_rg
        y = self.spectrum.y_rg
        if self.settings.ANALYZE == 0:
            name1 = "Processed"
            x = self.spectrum.x
            y = self.spectrum.y
        xy = np.vstack((x, y)).T
        x_co2, y_co2 = self.inferer.rm_co2(xy, self.settings.CO2FAC).T
        self.fig_spec_match.update_plot(
            x=x,
            y=y,
            name1=name1,
            x1=x_co2,
            y1=y_co2,
            name2="CO<sub>2</sub> removed",
        )

    def preprocess_one_spec(self, x: np.ndarray, y: np.ndarray) -> None:
        rmin = self.settings.RMIN
        rmax = self.settings.RMAX
        smooth = self.settings.SMOOTH
        baseline = self.settings.BASELINE
        adj_neg = self.settings.ADJNEG
        self.spectrum.set_spec(x=x, y=y, range_min=rmin, range_max=rmax)
        self.spectrum.preprocess(smooth=smooth, baseline=baseline, adj_neg=adj_neg)

    def update_pre_plot(self):
        x, y = self.get_current_spec()
        if isinstance(x, bool) and not x:
            return
        self.preprocess_one_spec(x=x, y=y)
        self.fig_spec_pre.update_plot(
            x=self.spectrum.x_rg,
            y=self.spectrum.y_rg,
            x1=self.spectrum.x,
            y1=self.spectrum.y,
        )

    def on_pre_listw_current_row_changed(self, row: int):
        self.param_runtime[RT.CRT_IDX] = row
        if row == -1:
            self.fig_spec_pre.reset_plot()
        else:
            self.update_pre_plot()

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

    def show_warning_msg(self, msg):
        QMessageBox(
            QMessageBox.Warning,
            f"Warning",
            f"{msg}",
            buttons=QMessageBox.Ok,
            parent=self,
        ).exec()

    def show_busy_dialog(self, msg: str = "Loading...", title: str = "dialog"):
        self.busydialog.setWindowTitle(title)
        self.busydialog.set_label(msg)
        self.busydialog.show()
