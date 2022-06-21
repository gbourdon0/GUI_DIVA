import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from modules.GUI.plotter import Plotter
import modules.GUI.menu_bar as menu_bar
import modules.GUI.variable_list as v_list
  # clam is a quite nice theme
class App(tk.Tk):
    def __init__(self):

        super().__init__()
        # Create a style
        # Import the tcl file with the tk.call method
        self.title("Quick tecplot files visualizer")
        self.geometry("400x600")
        self.configure(bg = '#676577')
        self.menu_bar_obj = menu_bar.menu_bar(self)
        self.config(menu=self.menu_bar_obj)
        self.flood_list = v_list.flood_selection(self)
        self.lines1_list = v_list.line1_selection(self)
        self.lines2_list = v_list.line2_selection(self)
        return None

if __name__ == "__main__":
    app =App()
    app.mainloop()