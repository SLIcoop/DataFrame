#!/usr/bin/env python3
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
'''
class CanadaTable():
    def __init__(self):
        df = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx', sheet_name='Canada by Citizenship', skiprows=range(20), skipfooter=2)
        df.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
        df.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
        df.set_index('Country')
        self.head = df.head

    def create_table(self):
        return print(self.head)
'''
'''
class PlotLib():
    def __init__(self):
        self.years = list(range(1980, 2014))

        self.loc = df.loc['Switzerland', years].plot()
        self.title = plt.title('Immigration from Switzerland')
        self.yl = plt.ylabel('Number of immigrants')
        self.xl = plt.xlabel('Years')
        self.sv = plt.savefig("temp.png")

    def create_plt(self):
        return (self.loc, self.title, self.yl, self.xl, self.sv)
'''
class CanadaTable(object):
    def __init__(self):
        df = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx', sheet_name='Canada by Citizenship', skiprows=range(20), skipfooter=2)
        df.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
        df.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
        df.set_index('Country')
        self.head = df.head
    
    def crt_tbl(self):
        return(self.head)

c = CanadaTable()
print(c.crt_tbl())
#print(df.loc['Switzerland', years])
#print(df.head())


