# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 22:18:36 2016
"""

import os
import pandas as pd
from collections import Counter
from datetime import datetime

data_dir = "/data"
weather_data = "/weather_data"
weather_file = "/2016_4_1.csv"

t_cwd = "/home/singh/dwhelper/IITC/Fall2016/machine_learning/projects/old/data/"

break_end = '<br />'
newline = '\n'
comma = ','

src_dir = "weather_data/"
dst_dir = "clean_weather_data/"

first_line = "TimeCDT,TemperatureF,Dew PointF,Humidity,Sea Level PressureIn,VisibilityMPH,Wind Direction,Wind SpeedMPH,Gust SpeedMPH,PrecipitationIn,Events,Conditions,WindDirDegrees,DateUTC\n"

import glob
cwd = t_cwd + src_dir
os.chdir(cwd)
for file in glob.glob("*.csv"):
    print(file)
    ifname = file
    print("ifname = ", ifname)

    ofname = str(t_cwd) + str(dst_dir) + str(file)
    print("ofname = ", ofname)

    df = pd.read_csv(ifname)
    x = Counter(df['TimeCDT'])
    objects = x.keys()
    TimeCDT = {}
    
    read_file = open(ifname, 'r')
    write_file = open(ofname, 'w')

#    write_file.write(first_line)
    
    lines = read_file.readlines()
    for l in lines:
        l = l.replace(break_end, '')
        st = l.split(comma, 1)
        if st[0] in objects:
            ob = datetime.strptime(st[0], "%I:%M %p")
            ob = datetime.strftime(ob, "%H:%M")
            hh, mm = ob.split(':')
            if hh not in TimeCDT:
                TimeCDT[hh] = 1
                st[0] = hh + comma
                stt = ''.join(st)
                print(stt)
                write_file.write(stt)
    read_file.close()
    write_file.close()
