# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 23:57:41 2016
"""

t_cwd = "/home/singh/dwhelper/IITC/Fall2016/machine_learning/projects/old/data/clean_weather_data/"

break_end = '<br />'
newline = '\n'
comma = ','

year = "2016"
month_day = {'4' : '30', '5': '31', '6' : '30'}

base_dir = t_cwd

out_file = "weather_all.csv"
first_line = "Date,TripCount,TimeCDT,TemperatureF,Dew PointF,Humidity,Sea Level PressureIn,VisibilityMPH,Wind Direction,Wind SpeedMPH,Gust SpeedMPH,PrecipitationIn,Events,Conditions,WindDirDegrees,DateUTC\n"
ofile = open(out_file, 'w')
ofile.write(first_line)

trip_count_data = 'trip_count_data.csv'
tfile = open(trip_count_data, 'r')

for m, d in sorted(month_day.items()):
    for i in range(int(d)):
        date_fmt = str(m)+ '-' + str(i + 1) + '-' + year
        ifile_n = base_dir + year + "_" + str(m) + "_" + str(i + 1) + ".csv"
        ifile = open(ifile_n, 'r')
        for i in range(24):
            weather_in = ifile.readline()
            trip_count = tfile.readline()
            line = str(date_fmt).strip(newline) + ',' + str(trip_count).strip(newline) + ',' + weather_in
            ofile.write(line)
        ifile.close()

ofile.close()
tfile.close()
