# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow2qzlxwh.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5 import QtGui, uic, QtCore



class Ui_MainWindow(QtWidgets.QMainWindow):
    refresh_plt_signal = QtCore.pyqtSignal()
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        uic.loadUi('layout/MainWindow2.ui', self)
        self.show()

        # other Widgets :
        from modules.GUI.Widget_Plot import Widget_Plot
        self.plot = Widget_Plot(parent=self)
        self.Layout_plot.addWidget(self.plot)

        #Connect signals
        self.refresh_plt_signal.connect(self.plot.refresh_graph)

        #CombBox pressed action
        self.comboBox_flood.activated.connect(self.refresh_plt_signal)
        self.comboBox_contour.activated.connect(self.refresh_plt_signal)
        self.comboBox_vectorX.activated.connect(self.refresh_plt_signal)
        self.comboBox_vectorY.activated.connect(self.refresh_plt_signal)
        self.comboBox_vectorZ.activated.connect(self.refresh_plt_signal)
        self.comboBox_coord_sysX.activated.connect(self.refresh_plt_signal)
        self.comboBox_coord_sysY.activated.connect(self.refresh_plt_signal)
        self.comboBox_coord_sysZ.activated.connect(self.refresh_plt_signal)

        #Add clicked action
        self.display_flood.clicked.connect(self.refresh_plt_signal)
        self.display_mesh.clicked.connect(self.refresh_plt_signal)
        self.display_vector.clicked.connect(self.refresh_plt_signal)
        self.display_contour.clicked.connect(self.refresh_plt_signal)

        #Menu actions
        self.menu_load.triggered.connect(self.load_file)



    def load_file(self):

        fname = QFileDialog.getOpenFileNames(self, "Open File","", "tecplot (*.plt);; All Files (*) ")
        if fname:
            #File type choice
            if fname[1] == "tecplot (*.plt)":

                self.load_plt(fname)
    #Load function
    def load_plt(self,fname):
        from modules.tecplot.Tecplot import Tecplot as tp
        from modules.GlobalVariables import global_variable as gv
        from modules.GlobalVariables.plot_options import plot_param
        gv.data = tp()
        path = fname[0]
        QApplication.setOverrideCursor(Qt.WaitCursor)

        for files in path:
            gv.data.add_frame(files)
        #Reassign things:
        frame1 = gv.data[1]
        if "R" in frame1.data.columns and "Z" in frame1.data.columns:
            plot_param["type"] ="2D_axi"
            plot_param["dim"] = 2
            for elem in frame1.data.columns:
                if elem == "R" or elem =="Z":
                    self.comboBox_coord_sysX.addItem(elem)
                    self.comboBox_coord_sysY.addItem(elem)
                else:
                    self.comboBox_flood.addItem(elem)
                    self.comboBox_contour.addItem(elem)
                    self.comboBox_vectorX.addItem(elem)
                    self.comboBox_vectorY.addItem(elem)

            self.comboBox_coord_sysZ.addItem("--")
            self.comboBox_vectorZ.addItem("--")
            self.comboBox_vectorX.setCurrentIndex(0)
            self.comboBox_vectorY.setCurrentIndex(1)
            self.comboBox_coord_sysX.setCurrentIndex(0)
            self.comboBox_coord_sysY.setCurrentIndex(1)

            try:
                index = self.comboBox_flood.findText("Temperature")
                self.comboBox_flood.setCurrentIndex(index)
                index = self.comboBox_contour.findText("Phi")
                self.comboBox_contour.setCurrentIndex(index)
                index = self.comboBox_vectorX.findText("U_r")
                self.comboBox_vectorX.setCurrentIndex(index)
                index = self.comboBox_vectorY.findText("U_z")
                self.comboBox_vectorY.setCurrentIndex(index)

            except:
                pass
            self.plot.refresh_plot_param()
            # do lengthy process
            QApplication.restoreOverrideCursor()

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication, QMainWindow

    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()

    sys.exit(app.exec_())

