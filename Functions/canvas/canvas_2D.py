from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt
import numpy as np

class canvas_2D(FigureCanvas):
    def __init__(self, func):
        self.func = func
        self.fig = plt.Figure(figsize=(10, 10), dpi=100)
        plt.rcParams['font.size'] = 12
        plt.rcParams['font.family'] = 'Segoe UI Semibold'
        plt.rcParams['font.family'] = 'Gulim'
        plt.rcParams['xtick.color'] = 'White'
        plt.rcParams['ytick.color'] = 'White'
        plt.rcParams['axes.labelcolor'] = 'White'
        self.fig.set_facecolor((40 / 255, 44 / 255, 52 / 255))
        self.fig.set_tight_layout(0)
        self.axes = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        self.setStyleSheet(
            "FigreCanvas{background-color:rgb(40, 44, 52); bord-radius:10px solid rgb(200, 50, 200);}"
        )
        self.blit()
        
        # parameter in func -> counts
        self.counts = np.zeros((10 + 1, 10 + 1))
        self.image = self.axes.imshow(self.counts, cmap='magma')
        self.divider = make_axes_locatable(self.axes)
        self.cax = self.divider.append_axes("right", size='5%', pad=0.5)
        self.colorbar = self.fig.colorbar(self.image, cax=self.cax)
        # self.colorbar = self.fig.colorbar(self.image, ax=self.axes)
        self.draw()
        self.axes.tick_params(axis='both', labelsize=20)
        self.mpl_connect('motion_notify_event', self.pos_cursor)
        self.mpl_connect('button_press_event', self.moveTo_cursor)

    def pos_cursor(self, event):
        if event.inaxes != self.axes:
            return
        try:
            x = int(event.xdata); y = int(event.ydata)
            if self.func.__class__.__name__ == 'confocal':
                self.func.ui.confocal_set_position_x.setText(str(self.func.positions[y][x]['x']))
                self.func.ui.confocal_set_position_y.setText(str(self.func.positions[y][x]['y']))
                self.func.ui.confocal_set_position_z.setText(str(self.func.positions[y][x]['z']))
                self.func.ui.confocal_counts.setText(str(self.func.counts[y][x]))
            elif self.func.__class__.__name__ == 'B_align':
                self.func.ui.magnet_set_position_x.setText(str(self.func.positions[y][x]['x']))
                self.func.ui.magnet_set_position_y.setText(str(self.func.positions[y][x]['y']))
                self.func.ui.magnet_set_position_z.setText(str(self.func.positions[y][x]['z']))
                self.func.ui.magnet_counts.setText(str(round(self.func.counts[y][x])))
        except Exception:
            pass

    def moveTo_cursor(self, event):
        if event.inaxes != self.axes and self.start_flag == False:
            return
        self.func.pressedMove()