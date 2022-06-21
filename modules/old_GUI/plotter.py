import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

class Plotter:
    def __init__(self,parent):
        #dim is the dimension of the plot (1D,2D,3D)
        self.parent = parent #parent frame
        super().__init__()
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        y = [xx ** 2 for xx in x]

        # Create a figure
        figure = Figure()
        figures_canvas = FigureCanvasTkAgg(figure, self)
        NavigationToolbar2Tk(figures_canvas, self)
        axes = figure.add_subplot()
        axes.plot(x, y)
        axes.set_xlabel("x")
        axes.set_ylabel("y")
        figures_canvas.get_tk_widget().pack()

    def plots(self,dim,Tecplot_obj):
        if dim ==1 or dim == 3:
            raise NotImplementedError("1D or 3D plots are not implemented yet.")
        if dim == 2:
            self.plot_2D(Tecplot_obj)
        return None

    def plot_2D(self):
        return None
if __name__ == "__main__":
    plots = Plotter(1)