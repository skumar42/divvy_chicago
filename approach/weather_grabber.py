# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 23:24:09 2016
"""

#https://www.wunderground.com/history/airport/KORD/2016/04/01/DailyHistory.html?format=1

import urllib.request

weather_csv_url_1 = "https://www.wunderground.com/history/airport/KORD/"
weather_csv_url_2 = "DailyHistory.html?format=1"

year = "2016"
month_day = {'4' : '30', '5': '31', '6' : '30'}

base_dir = '/home/singh/dwhelper/IITC/Fall2016/machine_learning/projects/weather_data/'
for m, d in sorted(month_day.items()):
    for i in range(int(d)):
        chicago_weather_url = weather_csv_url_1 + year + "/" + str(m) + "/" + str(i + 1) + "/" + weather_csv_url_2
        with urllib.request.urlopen(chicago_weather_url) as url:
            data_link = url.read().decode('utf-8')
            file_name = base_dir + year + "_" + str(m) + "_" + str(i + 1) + ".csv"
            f = open(file_name, 'w')
            f.write(str(data_link))
            print("writing file : ", file_name)
            f.close()
