
import matplotlib
import numpy as np

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar, FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.collections import LineCollection


import matplotlib.pyplot as plt
class Widget_Plot(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):

        self.parent =parent
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        super(Widget_Plot, self).__init__(self.fig)

        self.setStyleSheet(u"background-color: rgb(128, 128, 128")
        toolbar = NavigationToolbar(self,self)
        toolbar.setStyleSheet(u"background-color: rgb(128, 128, 128")
        X = [1,2]
        Y = [10,15]
        self.ax.plot(X,Y)
        return None
    def refresh_graph(self):
        from modules.GlobalVariables.plot_options import plot_param
        self.refresh_plot_param()
        if plot_param["type"] == "2D_axi":
            self.plot_2D_axi()


    def refresh_plot_param(self):
        from modules.GlobalVariables.plot_options import plot_param
        plot_param["flooded"] = self.parent.display_flood.isChecked()
        plot_param["mesh"] = self.parent.display_mesh.isChecked()
        plot_param["vector"] = self.parent.display_vector.isChecked()
        plot_param["contour"] = self.parent.display_contour.isChecked()
        plot_param["contour"] = self.parent.display_contour.isChecked()
        plot_param["flooded_c"] = self.parent.comboBox_flood.currentText()
        plot_param["contour_c"] = self.parent.comboBox_contour.currentText()
        plot_param["vector_c"] = (self.parent.comboBox_vectorX.currentText(),self.parent.comboBox_vectorY.currentText(),self.parent.comboBox_vectorZ.currentText())
        plot_param["coord_sys_c"] = (self.parent.comboBox_coord_sysX.currentText(), self.parent.comboBox_coord_sysY.currentText(),self.parent.comboBox_coord_sysZ.currentText())


    def plot_2D_axi(self):

        from modules.GlobalVariables.global_variable import data
        from modules.GlobalVariables.plot_options import plot_param
        self.ax.cla()
        self.fig.clf()
        self.ax = self.fig.add_subplot(111)
        frame = data[plot_param["current_frame"]]
        extent = [min(frame[plot_param["coord_sys_c"][0]]), max(frame[plot_param["coord_sys_c"][0]]), min(frame[plot_param["coord_sys_c"][1]]), max(frame[plot_param["coord_sys_c"][1]])]

        if plot_param["flooded"]:
            flood = frame[plot_param["flooded_c"]]
            flood = flood.reshape(frame.mesh_dim[0],frame.mesh_dim[1])
            img = self.ax.imshow(flood, extent=extent, origin="lower",cmap = plot_param["f_cmap"])
            clb = self.fig.colorbar(img)
            clb.ax.set_label(plot_param["flooded_c"])

        if plot_param["contour"]:
            contour = frame[plot_param["contour_c"]]
            contour = contour.reshape(frame.mesh_dim[0], frame.mesh_dim[1])
            self.ax.contour(contour, levels=plot_param["c_levels"], colors=plot_param["c_colors"], linestyles=plot_param["c_linestyle"],
                            linewidths=plot_param['c_linewidths'], zorder= plot_param["c_zorder"],extent=extent)

        if plot_param["vector"]:

            v_x = frame[plot_param["vector_c"][0]]
            v_y = frame[plot_param["vector_c"][1]]
            x = frame[plot_param["coord_sys_c"][0]]
            y = frame[plot_param["coord_sys_c"][1]]
            self.ax.quiver(x,y,v_x,v_y,scale = 0.1)

        if plot_param["mesh"]:
            print("mesh")
            x = frame[plot_param["coord_sys_c"][0]]
            y = frame[plot_param["coord_sys_c"][1]]
            X,Y = np.meshgrid(x,y)


        self.ax.set_xlim(0,extent[1])
        self.ax.set_ylim(extent[2],extent[3])
        self.ax.set_xlabel(plot_param["coord_sys_c"][0] + " [m]",fontsize = 18)
        self.ax.set_ylabel(plot_param["coord_sys_c"][1] + " [m]",fontsize = 18)
        #self.ax.axis('equal')
        plt.gca().set_aspect("equal", adjustable = 'box')
        self.fig.canvas.draw_idle()


        return None


