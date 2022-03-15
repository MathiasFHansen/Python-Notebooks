from ast import Index
import zipfile
import pandas as pd
import numpy as np
import requests

if __name__ == '__main__':

    data = pd.read_csv('API_EN.ATM.CO2E.KT_DS2_en_csv_v2_1345584.csv', skiprows=4)
    columns_names = data.columns
    countries = data['Country Name']
    data[:3]
    #1
    mask_emission = pd.Series(data = data['2014'].values,index=data['Country Name'])
    #print(mask_emission)

    #2
    test = mask_emission.sort_values(ascending=[False])
    print(test[:10])