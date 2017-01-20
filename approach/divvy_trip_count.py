# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 02:26:54 2016
"""


import pandas as pd



def datendtime(stri):
    test=stri.replace('/','-')
    test1=test.replace(':','')
    length = len(test1)
    test2=test1[:length-2]

    words=test2.split()

    dt=words[0]
    tm=words[1]
    return dt,tm

def read_file(name):
    df= pd.read_csv(name)
    return df

def cnstrnt(df):
    
    flt=df[((df['from_station_id'] == 76) |(df['to_station_id'] == 76))]
    
    return flt
    
def create_header(filename):
    myCsvRow="date,starttime,from_station_id,to_station_id\n"
    fd = open(filename,'w')
    fd.write(myCsvRow)
    return fd

    
def create_header_data(filename):
    myCsvRow="date,Time,TripCount\n"
    fd = open(filename,'w')
    fd.write(myCsvRow)
    return fd
    
def create_file(flt, fd):

    
    for index,row in flt.iterrows():
        st=""
        arg = row['starttime']
        dt,tm = datendtime(arg)

        src = str(row['from_station_id'])
        des = str(row['to_station_id'])
        st= dt+","+tm+","+src+","+des+"\n"
        fd.write(st)

    
files=['Divvy_Trips_2016_04.csv','Divvy_Trips_2016_05.csv','Divvy_Trips_2016_06.csv']
src = []
index = 0;
for fl in files:
    src.append('./584/workspace/project/Divvy_Trips_2016_Q1Q2/'+fl)

dst = './584/workspace/document_new.csv'
print(src)
fd = create_header(dst)
for fl in src:
    df = read_file(fl)
    flt = cnstrnt(df)
    create_file(flt, fd)
fd.close()


src = './584/workspace/document_new.csv'
dst = './584/workspace/project/Divvy_Trips_2016_Q1Q2/trip_count.csv'
df1= pd.read_csv(src)
fd = create_header_data(dst)
#for april
my_dict ={}
for i in range(24):
    my_dict[i] = 0
for i in range(30):
    dt ="%d-" % (i+1)
    date="4-"+dt+"2016"
    flt=df1[(df1['date'] == date)]
    for index,row in flt.iterrows():
            my_dict[row['starttime']] +=1
    for i in range(24):
        st =""
        st = date+","+str(i)+","+str(my_dict[i])+"\n"
        fd.write(st)
    for i in range(24):
        my_dict[i] = 0

#for may
for i in range(24):
    my_dict[i] = 0
for i in range(31):
    dt ="%d-" % (i+1)
    date="5-"+dt+"2016"
    flt=df1[(df1['date'] == date)]
    for index,row in flt.iterrows():
            my_dict[row['starttime']] +=1
    for i in range(24):
        st =""
        st = date+","+str(i)+","+str(my_dict[i])+"\n"
        fd.write(st)
    for i in range(24):
        my_dict[i] = 0

for i in range(24):
    my_dict[i] = 0
for i in range(30):
    dt ="%d-" % (i+1)
    date="6-"+dt+"2016"
    flt=df1[(df1['date'] == date)]
    for index,row in flt.iterrows():
            my_dict[row['starttime']] +=1
    for i in range(24):
        st =""
        st = date+","+str(i)+","+str(my_dict[i])+"\n"
        fd.write(st)
    for i in range(24):
        my_dict[i] = 0       
fd.close()    