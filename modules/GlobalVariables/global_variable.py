from modules.tecplot.Tecplot import Tecplot as tp
#class contenant les data a plot
data = None
tecplot = tp()
#default plot
default_plt_param = {
    "type":None,
    "dim":2,
    "cmap":"blue",
    "linewidths":2,
    "zorder": 10,
    "flooded":"Temperature",
    "lines1":"Phi",
    "lines2":"Phi_solid",
    "x_data":"R",
    "y_data": "Z"
}

plt_param = default_plt_param