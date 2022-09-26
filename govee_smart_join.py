from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import glob
import os

#
# SCRIPT TO CREATE DATAFRAME FROM GOVEE SMART DATA
# 
path_to_raw=r'C:\Users\Elisabeth.Verwuester\Documents\LIFE\00_Dachgarten_Berechnungen\wetter_daten\GOVEE_Daten\HMW'


# JOIN ALL FILES IN HMW FOLDER

joined_files= os.path.join(path_to_raw, 'Smart_1*.csv')
joined_list = glob.glob(joined_files)
df_1 = pd.concat(map(pd.read_csv, joined_list))

joined_files= os.path.join(path_to_raw, 'Smart_2*.csv')
joined_list = glob.glob(joined_files)
df_2 = pd.concat(map(pd.read_csv, joined_list))

joined_files= os.path.join(path_to_raw, 'Smart_XL*.csv')
joined_list = glob.glob(joined_files)
df_xl = pd.concat(map(pd.read_csv, joined_list))



# SETTING TIMESTAMP TO PROPER FORMAT
# SETTING TIMESTAMP AS DATA FRAME INDEX
# RENAMING THE COLUMNS FOR EACH SENSOR 1,2,XL

df_1['Timestamp_HMW']=pd.to_datetime(df_1['Timestamp_HMW'])
df_1.set_index('Timestamp_HMW', inplace=True)
df_1.rename(columns={'Temperature_Celsius':'Temperature_Celsius_1', 'Relative_Humidity':'Relative_Humidity_1'}, inplace=True)

df_2['Timestamp_HMW']=pd.to_datetime(df_2['Timestamp_HMW'])
df_2.set_index('Timestamp_HMW', inplace=True)
df_2.rename(columns={'Temperature_Celsius':'Temperature_Celsius_2', 'Relative_Humidity':'Relative_Humidity_2'}, inplace=True)

df_xl['Timestamp_HMW']=pd.to_datetime(df_xl['Timestamp_HMW'])
df_xl.set_index('Timestamp_HMW', inplace=True)
df_xl.rename(columns={'Temperature_Celsius':'Temperature_Celsius_xl', 'Relative_Humidity':'Relative_Humidity_xl'}, inplace=True)


# MERGING ALL DATAFRAMES INTO ONE

df_merged=pd.concat([df_1, df_2, df_xl], axis=0, join='outer')
print(df_merged)



# EXPORT DATA FRAME TO CSV FILE
df_merged.to_csv(r'C:\Users\Elisabeth.Verwuester\Documents\LIFE\00_Dachgarten_Berechnungen\wetter_daten\GOVEE_Daten\merge_test.csv')

# STATS



# PLOTTING 
def main():
    
    plt.figure()
    ax=df_merged['Temperature_Celsius_1'].plot(color='red', label='smart_1')
    ax=df_merged['Temperature_Celsius_2'].plot(color='steelblue', label='smart_2')
    ax=df_merged['Temperature_Celsius_xl'].plot(color='green', label='smart_xl')
    plt.legend(loc='upper left')
    ax.set_ylabel('Temperature_Celsius')
    ax.set_title('smart 1, 2, xl comparison')

    #ax = df_1_7.plot(secondary_y=['Relative_Humidity'])
    #ax.set_ylabel('Temperature_Celsius')
    #ax.right_ax.set_ylabel('Relative_Humidity')
    #ax.set_title('temp vs. rel.hum.')



    plt.show()

if __name__ == "__main__":
	main()




