'''
@author : G.Bourdon
@Date : 07/02/2022
@Description : A class that import/read plt files from tecplot
'''

import pandas as pd
import numpy as np
import struct
from modules.tecplot import tecplotPltReader as tpr


class plt:
    def __init__(self,filename: str) -> None:
        #Variables
        self.name: str = ''
        self.time: float = 0
        self.time_step: float = 0
        self.data: type(pd.DataFrame()) = pd.DataFrame()
        self.mesh_dim: tuple = (0, 0, 0)

        #Initialization function
        self.Reading_plt(filename)

    def Reading_plt(self, filename: str) ->None:
        '''
        @Description : Import a plt file in python and put data in pandas
        @Input :
            - filename : path of the plt file
        '''
        self.name = filename.replace(".plt", "")
        print(f"Reading file : {filename}")
        try:
            file_to_read = open(filename, "rb")
            bytes_list = file_to_read.read()
            infos, read_binary = tpr.read_data(bytes_list, file_to_read)
            file_to_read.close()
        except :
            print("No .plt file founded")

        # Attributing info
        self.time = float(infos["Zones"][0]["ZoneName"].split(",")[1].split("=")[1])
        self.time_step = float(infos["Zones"][0]["ZoneName"].split(",")[0].split("=")[1])
        self.mesh_dim = (infos["Zones"][0]["Imax"], infos["Zones"][0]["Jmax"], infos["Zones"][0]["Kmax"])

        # Getting the data
        for var in infos["VarNames"]:
            self.data[var] = np.array(read_binary["Zones"][0][var])

    def __getitem__(self, name : str):
        return np.array(self.data[name])

if __name__ == "__main__":
    test = plt()
    print(test["Temperature"])
