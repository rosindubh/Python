# program to produce graphs of electtricity useage for june 2021

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# create a dataframe from csv file
df = pd.read_csv('/home/phil/Documents/electricity_meter_readings.csv')

# create 4 variables
date = df.DATE
day = df.DAY
night = df.NIGHT
_24hours = df['24 HOURS']

# plot graph for daytime
plt.bar(date, day)
plt.title('Daytime')
plt.xlabel('June 2021')
plt.ylabel('kW/h')
plt.show()

# plot graph for nightime
plt.bar(date, night)
plt.title('Nightime')
plt.xlabel('June 2021')
plt.ylabel('kW/h')
plt.show()

# plot graph for 24 hours
plt.bar(date, _24hours)
plt.title('24 Hours')
plt.xlabel('June 2021')
plt.ylabel('kW/h')
plt.show()

print('Average daily use', day.mean(), 'kWh')
print('Average night use', night.mean(), 'kWh')
print('Average 24hr use', _24hours.mean(), 'kWh')
