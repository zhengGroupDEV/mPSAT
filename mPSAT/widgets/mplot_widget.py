"""
Description: 
Author: Rainyl
LastEditTime: 2022-07-31 21:20:42
"""
import numpy as np
import pyqtgraph as pg

from mPSAT.utils.logger import MPSATLogger


class MPlotWidget(pg.PlotWidget):
    LATEX_BASE = "<html><head/><body><p> {latex} </p></body></html>"
    logger = MPSATLogger("plotWidget")
    colors = ("#000000", "#ff4757")

    def __init__(self, parent=None):
        super(MPlotWidget, self).__init__(parent)
        self.x = self.x1 = np.linspace(0, 1, 10)
        self.y = self.y1 = np.zeros(self.x.shape[0])
        self.xlim = (0, 6000)

        self.vline = pg.InfiniteLine(angle=90, movable=False)
        self.hline = pg.InfiniteLine(angle=0, movable=False)
        self.vline.setPen(color="#2f3542", width=1)
        self.hline.setPen(color="#2f3542", width=1)
        self.addItem(self.vline, ignoreBounds=True)
        self.addItem(self.hline, ignoreBounds=True)
        self.plotItem.showGrid(x=True, y=True, alpha=0.3)

        self.crosshair_update = pg.SignalProxy(
            self.scene().sigMouseMoved, rateLimit=60, slot=self.update_crosshair
        )

    def reset_plot(self):
        self.plotItem.clearPlots()
        self.plotItem.plot()

    def update_plot(
        self,
        x: np.ndarray,
        y: np.ndarray,
        x1: np.ndarray = None,
        y1: np.ndarray = None,
        name1: str = "Original",
        name2: str = "Processed",
    ):
        # logger.debug(f"{x}, {y}, {x1}, {y1}")
        self.setTitle("mPSAT-Preprocess")
        self.plotItem.addLegend()
        pen1 = pg.mkPen(color=self.colors[0], width=3)
        pen2 = pg.mkPen(color=self.colors[1], width=3)
        self.plotItem.clearPlots()
        self.plotItem.plot(x=x, y=y, pen=pen1, name=name1)
        if not (x1 is None and y1 is None):
            self.plotItem.plot(x=x1, y=y1, pen=pen2, name=name2)

        self.plotItem.showGrid(x=True, y=True, alpha=0.3)
        self.plotItem.setXRange(min=min(x), max=max(x))
        self.plotItem.setYRange(min=min(y), max=max(y))
        self.plotItem.setLimits(xMin=0, xMax=6000, yMin=-1, yMax=1.1)
        self.plotItem.invertX()
        self.plotItem.setLabel("left", "Intensity")
        self.plotItem.setLabel("bottom", "Wavenumber (cm<sup>-1</sup>)")
        axBottom = self.plotItem.getAxis("bottom")
        axBottom.setTickSpacing(500, 25)
        axBottom = self.plotItem.getAxis("left")
        axBottom.setTickSpacing(0.2, 0.01)

    def format_latex(self, s: str):
        return self.LATEX_BASE.format(latex=s)

    def update_crosshair(self, event):
        coordinates = event[0]
        if self.sceneBoundingRect().contains(coordinates):
            mouse_point = self.plotItem.vb.mapSceneToView(coordinates)
            index = mouse_point.x()
            if index > self.xlim[0] and index <= self.xlim[1]:
                self.setTitle(
                    f"<span style='font-size: 10pt color: {self.colors[0]}'>x={mouse_point.x():.2f}</span>, \
                    <span style='color: {self.colors[1]}'>y={mouse_point.y():.2f}</span>"
                )
            self.vline.setPos(mouse_point.x())
            self.hline.setPos(mouse_point.y())
