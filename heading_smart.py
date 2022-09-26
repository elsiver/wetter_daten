import pandas as pd
import glob
import os

# CHANGE HEADER OF EACH CSV FILE IN FOLDER

path_to_raw=r'C:\Users\Elisabeth.Verwuester\Documents\LIFE\00_Dachgarten_Berechnungen\wetter_daten\GOVEE_Daten\HMW'


# CHANGE HEADER OF FILE

smart_header='Timestamp_HMW,Temperature_Celsius,Relative_Humidity\n'

def heading(path, header):
    with open(path, 'rt', encoding='utf-8-sig') as f:
        lines = f.readlines()
        lines[0]=header
    with open(path, 'wt', encoding='utf-8-sig') as f:
        f.writelines(lines)
    return path


for filename in os.listdir(path_to_raw):
    filepath = os.path.join(path_to_raw, filename)
    heading(filepath, smart_header)




