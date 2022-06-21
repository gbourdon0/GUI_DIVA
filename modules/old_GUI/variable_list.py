import tkinter as tk
from tkinter import *
#from tkinter.ttk import *
import modules.GlobalVariables.global_variable as gv

class flood_selection:
    def __init__(self,master):
        self.master =master
        frame = Frame(master,bg = "#a698a0")
        frame.pack()

        self.OptionList = ["Empty"]
        self.variable = tk.StringVar(master)
        self.opt = tk.OptionMenu(self.master, self.variable, *self.OptionList)
        self.opt.config(bg = "#fef9ff")
        self.opt.config(width=90, font=('Helvetica', 12))
        self.opt.pack(side = "top")

    def refresh(self):
        self.variable.set('')
        self.opt['menu'].delete(0, 'end')
        if gv.tecplot.nb_frames != 0:
            self.OptionList = list(gv.tecplot[1].data.columns)
            try:
                default_idx = self.OptionList.index(gv.default_plt_param["flooded"])
            except:
                default_idx = 0
        else:
            self.OptionList = ["Empty"]
            default_idx = 0
        for choice in self.OptionList:
            self.opt['menu'].add_command(label=choice, command=tk._setit(self.variable, choice))
        self.variable.set(self.OptionList[default_idx])


class line1_selection:
    def __init__(self,master):
        self.master =master
        frame = Frame(master)
        frame.pack()

        self.OptionList = ["Empty"]
        self.variable = tk.StringVar(master)
        self.opt = tk.OptionMenu(self.master, self.variable, *self.OptionList)
        self.opt.config(width=90, font=('Helvetica', 12))
        self.opt.pack(side = "top")

    def refresh(self):
        self.variable.set('')
        self.opt['menu'].delete(0, 'end')
        if gv.tecplot.nb_frames != 0:
            self.OptionList = list(gv.tecplot[1].data.columns)
            try:
                default_idx = self.OptionList.index(gv.default_plt_param["lines1"])
            except:
                default_idx = 0
        else:
            self.OptionList = ["Empty"]
            default_idx = 0
        for choice in self.OptionList:
            self.opt['menu'].add_command(label=choice, command=tk._setit(self.variable, choice))
        self.variable.set(self.OptionList[default_idx])

class line2_selection:
    def __init__(self,master):
        self.master =master
        frame = Frame(master)
        frame.pack()

        self.OptionList = ["Empty"]
        self.variable = tk.StringVar(master)
        self.opt = tk.OptionMenu(self.master, self.variable, *self.OptionList)
        self.opt.config(width=90, font=('Helvetica', 12))
        self.opt.pack(side = "top")

    def refresh(self):
        self.variable.set('')
        self.opt['menu'].delete(0, 'end')
        if gv.tecplot.nb_frames != 0:
            self.OptionList = list(gv.tecplot[1].data.columns)
            try:
                default_idx = self.OptionList.index(gv.default_plt_param["lines2"])
            except:
                default_idx = 0
        else:
            self.OptionList = ["Empty"]
            default_idx = 0
        for choice in self.OptionList:
            self.opt['menu'].add_command(label=choice, command=tk._setit(self.variable, choice))
        self.variable.set(self.OptionList[default_idx])


