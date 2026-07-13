from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

class canvas_3D(FigureCanvas):
    def __init__(self, func):
        self.func = func

        self.fig = plt.figure(figsize=(1, 1), dpi=100)
        FigureCanvas.__init__(self, self.fig)

        self.axes = self.fig.add_subplot(projection='3d')
        self.fig.patch.set_facecolor((40/255, 44/255, 52/255))  # Figure 배경색 설정
        self.axes.set_facecolor((40/255, 44/255, 52/255))       # 3D 축 배경색 설정
        self.blit()
        
        # x, y축 생성
        x = np.arange(0, 20, 1)
        y = np.arange(0, 20, 1)
        self.hist, self.xedges, self.yedges = np.histogram2d(x, y, bins=20)
        self.hist = np.random.randint(20, 30, size=(20, 20))
        
        # 각 히스토그램 막대의 위치 및 크기 설정
        self.xpos, self.ypos = np.meshgrid(self.xedges[:-1] + 0.25, self.yedges[:-1] + 0.25, indexing="ij")
        self.xpos = self.xpos.ravel()
        self.ypos = self.ypos.ravel()
        self.zpos = np.zeros_like(self.xpos)

        # 히스토그램 막대의 폭과 높이 설정
        self.dx = self.dy = 0.3 * np.ones_like(self.zpos)
        self.dz = self.hist.ravel()

        # 3D 히스토그램 그리기
        self.axes.bar3d(self.xpos, self.ypos, self.zpos, 
                        self.dx, self.dy, self.dz, zsort='average', color='coral', edgecolor='black')

        # 축 설정
        self.axes.set_xlabel('pillar x #', labelpad=10, fontsize=15)
        self.axes.set_ylabel('pillar y #', labelpad=10, fontsize=15)
        self.axes.set_zlabel('contrast (%)', labelpad=10, fontsize=15)

        # ticks 설정
        self.axes.set_xticks([0, 10, 20])
        self.axes.set_yticks([0, 10, 20])
        self.axes.set_zticks([0, 10, 20, 30])
        self.axes.tick_params(axis='x', labelsize=15)
        self.axes.tick_params(axis='y', labelsize=15)
        self.axes.tick_params(axis='z', labelsize=15)

        self.axes.view_init(elev=30, azim=180)

        self.draw()