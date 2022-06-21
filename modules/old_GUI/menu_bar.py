import tkinter as tk
from tkinter import *
import modules.GlobalVariables.global_variable as gv
import sys
from modules.tecplot.plt_obj import plt as tecplot
class menu_bar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        fileMenu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=fileMenu)
        fileMenu.add_command(label="Load", underline=1, command=self.browseFiles)
        fileMenu.add_command(label="Save", underline=1, command=self.quit)
        fileMenu.add_command(label="Save_jpeg", underline=1, command=self.quit)
    def quit(self):
        sys.exit(0)

    def browseFiles(self):
        filename = tk.filedialog.askopenfilenames(initialdir=".",
                                              title="Select a File",
                                              filetypes=(("Text files",
                                                          "*.plt*"),
                                                         ("all files",
                                                          "*.*")))
        for files in filename:
            gv.tecplot.add_frame(tecplot(files))
            print(gv.tecplot.nb_frames)

        #Refreshing list
        self.master.flood_list.refresh()
        self.master.lines1_list.refresh()
        self.master.lines2_list.refresh()
        return filename

