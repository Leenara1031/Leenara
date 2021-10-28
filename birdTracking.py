import cartopy.crs
import pandas as pd

birdata = pd.read_csv('bird_tracking.csv')
birdata.columns

ix = birdata.bird_name == "Sanne"
data = birdata.date_time[ix]
print(data[:1])

data = birdata.date_time[ix]
print(data[-1:])

import datetime as dt
dt.datetime.today()

time1 = dt.datetime.today()
time2 = dt.datetime.today()
time2 - time1


timestamps = []
for k in range(len(birdata)):
    timestamps.append(dt.datetime.strptime(birdata.date_time.iloc[k][:-3], '%Y-%m-%d %H:%M:%S'))

birdata['timestamp'] = pd.Series(timestamps, index = birdata.index)

times = birdata.timestamp[birdata.bird_name == 'Eric']
elapsed = [time - times[0] for time in times]
elapsed[100]

print(elapsed[0])
print(elapsed[1])
print(elapsed[100])

elapsed[100] / dt.timedelta(days=1)

import matplotlib.pyplot as plt
import numpy as np
plt.plot(np.array(elapsed) / dt.timedelta(days=1))
plt.xlabel('Observation')
plt.ylabel('Elapsed(days)')

ix = birdata.bird_name == "Eric"
speed = birdata.speed_2d[ix]
print(speed.head())

speed = np.array(speed)
print(np.isnan(speed))

np.isnan(speed).any()

for name in bird_names:
    ix = birdata['bird_name'] == name
    x, y = birdata.longitude[ix], birdata.latitude[ix]
    ax.plot(x, y, '.', transform=ccrs.Geodetic(), label=name)
plt.legend(loc='upper left')
