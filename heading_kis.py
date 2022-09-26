import pandas as pd
import glob
import os
import csv

# CHANGE HEADER OF EACH CSV FILE IN FOLDER

# KIS WEATHER STATION DATA
path_to_raw_kis=r'C:\Users\Elisabeth.Verwuester\Documents\LIFE\00_Dachgarten_Berechnungen\wetter_daten\KIS_StadtLaborGraz\HMW_raw_data'
kis_header='Timestamp_HMW,Temperature_Celsius,,Relative_Humidity,,Pressure_HPa,,Wind_Speed_m_per_s,,Wind_Direction,,Rain_Vol_L,,Rain_Hi_mm,,\n'


def heading(path, header):
    with open(path, 'rt', encoding='utf-8-sig') as f:
        lines = f.readlines()
        lines[0]=header
    with open(path, 'wt', encoding='utf-8-sig') as f:
        f.writelines(lines)
    return path

for filename in os.listdir(path_to_raw_kis):
    filepath = os.path.join(path_to_raw_kis, filename)
    heading(filepath, kis_header)





# # CHANGE SEPARATOR FORMAT
#with open(r'C:\Users\Elisabeth.Verwuester\Documents\LIFE\00_Dachgarten_Berechnungen\wetter_daten\KIS_StadtLaborGraz\Juli_HMW_raw.csv','rt', encoding='utf-8-sig') as fin:
#    with open(r'C:\Users\Elisabeth.Verwuester\Documents\LIFE\00_Dachgarten_Berechnungen\wetter_daten\KIS_StadtLaborGraz\Juli_HMW.csv', 'wt') as fout:
#        for line in fin:
#            fout.write(line.replace(';', ',').replace(',,', ','))














