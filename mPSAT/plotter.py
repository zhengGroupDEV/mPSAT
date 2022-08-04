'''
Description: 
Author: Rainyl
Date: 2022-07-30 16:31:07
LastEditTime: 2022-08-04 17:17:54
'''
"""
Description: plotter
Author: Rainyl
LastEditTime: 2022-07-31 11:13:14
"""
import pyqtgraph as pg
import numpy as np

from mPSAT.utils.logger import MPSATLogger

logger = MPSATLogger("plotter")


def update_pre_plot(
    fig: pg.PlotWidget,
    x: np.ndarray,
    y: np.ndarray,
    x1: np.ndarray,
    y1: np.ndarray,
):
    fig.plotItem.setTitle("")
    # logger.debug(f"{fig}, {x}, {y}, {x1}, {y1}")
    fig.plotItem.addLegend()
    pen1 = pg.mkPen(color="#000000", width=3)
    pen2 = pg.mkPen(color="#ff4757", width=3)
    fig.plotItem.clearPlots()
    fig.plotItem.plot(x=x, y=y, pen=pen1, name="Original")
    fig.plotItem.plot(x=x1, y=y1, pen=pen2, name="Processed")
    
    # fig.scene().sigMouseMoved.connect(mouseMoved)
    vLine = pg.InfiniteLine(angle=90, movable=False)
    hLine = pg.InfiniteLine(angle=0, movable=False)
    fig.plotItem.addItem(vLine, ignoreBounds=True)
    fig.plotItem.addItem(hLine, ignoreBounds=True)

    fig.plotItem.showGrid(x=True, y=True, alpha=0.3)
    fig.plotItem.setXRange(min=min(x), max=max(x))
    fig.plotItem.setYRange(min=min(y), max=max(y))
    fig.plotItem.setLimits(xMin=0, xMax=6000, yMin=-1, yMax=1.1)
    fig.plotItem.invertX()
    fig.plotItem.setLabel("left", "Intensity")
    fig.plotItem.setLabel("bottom", "Wavenumber (cm-1)")
    axBottom = fig.plotItem.getAxis("bottom")
    axBottom.setTickSpacing(500, 25)
    axBottom = fig.plotItem.getAxis("left")
    axBottom.setTickSpacing(0.2, 0.01)

    def mouseMoved(evt):
        logger.debug("mouse moved")
        pos = evt[0]  ## using signal proxy turns original arguments into a tuple
        if fig.plotItem.sceneBoundingRect().contains(pos):
            mousePoint = fig.plotItem.vb.mapSceneToView(pos)
            index = int(mousePoint.x())
            if index > 0 and index < len(x):
                fig.plotItem.setTitle(
                    f"<span style='font-size: 12pt'>x={mousePoint.x():.2f}</span>\n\
                    <span style='color: blue'>y2={mousePoint.y():.2f}</span>"
                )
            vLine.setPos(mousePoint.x())
            hLine.setPos(mousePoint.y())
    proxy = pg.SignalProxy(
        fig.scene().sigMouseMoved,
        slot=mouseMoved,
    )


def update_match_plot(
    fig: pg.PlotWidget,
    x: np.ndarray,
    y: np.ndarray,
    x1: np.ndarray,
    y1: np.ndarray,
):
    logger.debug(f"{fig}, {x}, {y}, {x1}, {y1}")
    pen1 = pg.mkPen(color="#000000", width=3)
    pen2 = pg.mkPen(color="#ff4757", width=3)
    fig.plotItem.clearPlots()
    fig.plotItem.plot(x=x, y=y, pen=pen1)
    fig.plotItem.plot(x=x1, y=y1, pen=pen2)

    fig.plotItem.showGrid(x=True, y=True, alpha=0.3)
    fig.plotItem.setXRange(min=400, max=4000)
    fig.plotItem.setLimits(xMin=0, xMax=6000, yMin=-1, yMax=1.1)
    fig.plotItem.invertX()
    axBottom = fig.plotItem.getAxis("bottom")
    axBottom.setTickSpacing(500, 25)
    axBottom = fig.plotItem.getAxis("left")
    axBottom.setTickSpacing(0.2, 0.01)
