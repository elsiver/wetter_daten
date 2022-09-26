#import csv
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter

import pandas as pd
import kis # data frame crearted from KIS eeather data in kis.py
import govee_smart_join as gs #data frame created from govee_smart sensor data in govee_smart.py


# READ IN DATA FRAMES

df_kis=kis.df_kis
df_1=gs.df_1
df_2=gs.df_2
df_xl=gs.df_xl

#print(df_kis.head())

# PLOTTING 
# ALL SMART
fig= plt.figure(figsize=(12,8)) # fig = plt.figure() creates a figure object, that holds all graphs in it as a container

ax_smart_all=df_1['Temperature_Celsius_1'].plot(color='red', label='smart_1')
ax_smart_all=df_2['Temperature_Celsius_2'].plot(color='steelblue', label='smart_2')
ax_smart_all=df_xl['Temperature_Celsius_xl'].plot(color='green', label='smart_xl')
plt.legend(loc='upper left')
ax_smart_all.set_ylabel('Temperature_Celsius')
ax_smart_all.set_title('smart 1, 2, xl comparison')




# KIS DATA
plt.figure()
date_form=DateFormatter("%y-%m-%d")
fig, ax_kis = plt.subplots(figsize=(12, 12))
ax_kis = df_kis['Temperature_Celsius'].plot(label='kis')
ax_kis.xaxis.set_major_formatter(date_form)
ax_kis.set_xlim([datetime.date(2022,6,27), datetime.date(2022,8,1)])
ax_kis.set_title('kis')

# TEMP VS REL HUM
#plt.figure()
#ax = df_1.plot(secondary_y=['Relative_Humidity'])
#ax.set_ylabel('Temperature_Celsius')
#ax.right_ax.set_ylabel('Relative_Humidity')
#ax.set_title('temp vs. rel.hum.')


# SMART VS KIS
date_form=DateFormatter("%y-%m-%d")
fig, ax = plt.subplots()
ax2 = ax.twinx()
df_kis['Temperature_Celsius'].plot(ax=ax, label='kis')
ax.xaxis.set_major_formatter(date_form)
ax.set_xlim([datetime.date(2022,6,27), datetime.date(2022,8,1)])
df_1['Temperature_Celsius_1'].plot(ax=ax2, label='smart_1', ls='--', color='green')
ax.set_ylabel('Temperature_Celsius')
ax.set_title('kis vs. smart')
plt.legend(loc='upper left')

# WÄRMEEINTRAG LUFTSCHACHT? SMART_1 (BEET1) VS SMART_2 (LUFTSCHACHT)
date_form=DateFormatter("%y-%m-%d-%h")
fig2, ax3 = plt.subplots()
ax4 = ax3.twinx()
df_1['Temperature_Celsius_1'].plot(ax=ax3, label='smart_1_beet_1', color='black')
ax3.xaxis.set_major_formatter(date_form)
ax3.set_xlim([datetime.date(2022,7,26), datetime.date(2022,8,2)])
df_2['Temperature_Celsius_2'].plot(ax=ax4, label='smart_2_m_air', ls='--', color='green')
ax3.set_ylabel('Temperature_Celsius')
ax3.set_title('smart1 vs. smart2')
plt.legend(loc='upper left')







plt.show()





