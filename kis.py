import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import datetime
import glob
import os

#
# SCRIPT TO CREATE  DATAFRAME OUT OF KIS WEATHER RAW DATA
#

# PATH TO RAW DATA
path_to_raw = r'C:\Users\Elisabeth.Verwuester\Documents\LIFE\00_Dachgarten_Berechnungen\wetter_daten\KIS_StadtLaborGraz\HMW_raw_data'


# # CHANGE SEPARATOR FORMAT
# with open(r'C:\Users\Elisabeth.Verwuester\Documents\LIFE\00_Dachgarten_Berechnungen\wetter_daten\KIS_StadtLaborGraz\Juli_HMW_raw.csv','rt', encoding='utf-8-sig') as fin:
#     with open(r'C:\Users\Elisabeth.Verwuester\Documents\LIFE\00_Dachgarten_Berechnungen\wetter_daten\KIS_StadtLaborGraz\Juli_HMW.csv', 'wt') as fout:
#         for line in fin:
#             fout.write(line.replace(';', ',').replace(',,', ','))




# JOIN ALL FILES IN HMW FOLDER

joined_files= os.path.join(path_to_raw, '*.csv')
joined_list = glob.glob(joined_files)



df_kis = pd.concat(map(pd.read_csv, joined_list))


print(df_kis.head())
print(df_kis.dtypes)





# CREATION OF DATA FRAME
#df_kis = pd.read_csv(kis_file, sep=',')
# SETTING TIMESTAMP TO PROPER FORMAT AND AS INDEX
df_kis['Timestamp_HMW']=pd.to_datetime(df_kis['Timestamp_HMW'])
df_kis.set_index('Timestamp_HMW', inplace=True)
#df_kis['Wind_Speed_m_per_s']=pd.to_numeric(df_kis['Wind_Speed_m_per_s'])
#df_kis.Wind_Speed_m_per_s=pd.to_numeric(df_kis.Wind_Speed_m_per_s)

# missing rain and wind data due to type error





# PLOTTING
def main():
    
    # TEMPERATURE  
    date_form=DateFormatter("%y-%m-%d")
    fig, ax = plt.subplots(figsize=(12,12))
    ax = df_kis['Temperature_Celsius'].plot()
    ax.xaxis.set_major_formatter(date_form)
    ax.set_xlim([datetime.date(2022,6,27), datetime.date(2022,8,1)])

    # RAIN
    # fig, ax2 = plt.subplots()
    # df_kis['Rain_Hi_mm'].plot(label='kis')
    # ax2.xaxis.set_major_formatter(date_form)
    # ax2.set_xlim([datetime.date(2022,6,27), datetime.date(2022,8,1)])
    # ax2.set_ylabel('rain [mm]')
    # ax2.set_title('kis rain high')

    # fig, ax3 = plt.subplots()
    # df_kis['Rain_Vol_L'].plot(label='kis')
    # ax3.xaxis.set_major_formatter(date_form)
    # ax3.set_xlim([datetime.date(2022,6,27), datetime.date(2022,8,1)])
    # ax3.set_ylabel('rain')
    # ax3.set_title('kis')

    #plt.show()

if __name__ == "__main__":
	main()
