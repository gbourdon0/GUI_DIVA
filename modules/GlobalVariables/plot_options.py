
plot_param_default = {
#What to plot
"flooded": False,
"contour": False,
"mesh": False,
"vector": False,

# Variable choice
"flooded_c": '',
"contour_c": [],
"vector_c": ('','',''),
"coord_sys_c":('','', ''),

# General info
    "type": None, #2D_axi,2D,3D
    "dim": 2,
    "current_frame":1,

#Default contour flood
"f_cmap": "jet",
#Default param contour
"c_linewidths": 2,
"c_zorder": 10,
"c_linestyle":"-",
"c_levels":[0],
"c_colors":"k"

}
plot_param=plot_param_default