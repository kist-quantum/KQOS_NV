from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt
import numpy as np

class canvas_1D(FigureCanvas):
    def __init__(self, func):
        self.fig = plt.Figure(figsize=(10, 1), dpi=150)
        self.axes = self.fig.add_subplot(111)
        self.axes.set_facecolor((40 / 255, 44 / 255, 52 / 255))
        self.axes.grid()
        self.fig.set_facecolor((40 / 255, 44 / 255, 52 / 255))
        self.canvas = FigureCanvas(self.fig)
        FigureCanvas.__init__(self, self.fig)
        self.canvas.setStyleSheet(
            "FigreCanvas{background-color:rgb(40, 44, 52); bord-radius:10px solid rgb(200, 50, 200);}"
        )
        
    def current_cursor(self, event):
        pass
    
    def setRange(self, event):
        if event.inaxes != self.axes:
            return

        if event.button == 1:
            self.ui.form.lineEdit_measurements_From.setText(str(round(event.xdata, 4)))

        if event.button == 3:
            self.ui.form.lineEdit_measurements_To.setText(str(round(event.xdata, 4)))