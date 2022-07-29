from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
# import matplotlib
# matplotlib.use('QtAgg')
# matplotlib.rcParams['backend']='PySide6'
# import os
# os.environ["QT_API"] = 'PySide6'


class QFigureCanvas(FigureCanvasQTAgg):
    figure = None
    def __init__(self, figure=None):
        super(QFigureCanvas, self).__init__()
        self.ax = self.figure.add_subplot(111)

    def setFigure(self, figure):
        if isinstance(figure, Figure):
            self.figure = figure
            return True
        return False

    def test(self):
        import random
        self.ax.clear()
        x = [1,2,3,4,5,6,7,8,9]
        y = [random.randint(0, 20) for _ in range(len(x))]
        self.ax.plot(x, y)
