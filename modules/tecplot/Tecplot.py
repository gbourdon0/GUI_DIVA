import pandas as pd
import numpy as np
import os#It is supposed that frames are added by growing time
from modules.tecplot.plt_obj import plt as tecplot

class Tecplot:
    def __init__(self):
        self.nb_frames = 0
        self.frames = {}
        self.time_to_frame = {}
        self.time = []


    def open_folder(self,path):
        #supposed that everything is sort by growing time
        print(f"Opening plt in {path}")
        filelist = os.listdir(path)

        for files in filelist:
            if not ".plt" in files:
                pass
            else:
                self.add_frame(tecplot(path+"/"+files))
        print(f"{self.nb_frames} plots imported.")
    def add_frame(self,path):
        frame = tecplot(path)
        self.nb_frames +=1
        #frame should be a plt_obj
        self.frames[self.nb_frames] = frame
        self.time_to_frame[frame.time] = self.nb_frames

        return None

    def remove_frame(self,time = 0, frame = 0):
        if time !=0:
            idx = self.time_to_frame(time)
            self.frames.pop(idx)
            self.time_to_frame.pop(time)
        elif frame !=0:
            time = self.frames[frame].time
            self.frames.pop(frame)
            self.time_to_frame.pop(time)
        else:
            raise Exception("No Input. No frame has been removed")
        return None

    def get_frame_time(self,look_time : float):
        #Return the frame with the nearest time
        keys = np.array(list(self.time_to_frame.keys()))#get time list
        dif = np.absolute(keys-look_time)
        return self.frames[dif.argmin()+1]#since we began to enumerate frame from 1, and numpy from 0



    def __getitem__(self,framenumber):
        try:
            return self.frames[framenumber]
        except:
            print(f"{framenumber} not in plt loaded. Should be between 1 and {self.nb_frames}")
            return None
