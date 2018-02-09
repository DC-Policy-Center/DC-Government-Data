# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:57:35 2018

@author: mwatson
"""
import pandas as pd
import requests
import io
import matplotlib.pyplot as plt
import pygal


def get_list_of_key_in_dict(d,key):
    list_of_keys = []
    for item in d[key]:
        if item not in list_of_keys:
            list_of_keys.append(item)
    return(list_of_keys)

def request_to_pdcsv(url,year):
    s=requests.get(url).content
    c=pd.read_csv(io.StringIO(s.decode('utf-8')))
    c['Year'] = year
    return(c)

def import_data_by_api(api_year):
         
    api_urls = {
     '2018' : 'https://opendata.arcgis.com/datasets/85bf98d3915f412c8a4de706f2d13513_8.csv',
     '2017' : 'https://opendata.arcgis.com/datasets/714d5f8b06914b8596b34b181439e702_36.csv',
     '2016' : 'https://opendata.arcgis.com/datasets/82ab09c9541b4eb8ba4b537e131998ce_22.csv',
     '2015' : 'https://opendata.arcgis.com/datasets/4c4d6b4defdf4561b737a594b6f2b0dd_23.csv',
     '2014' : 'https://opendata.arcgis.com/datasets/d7aa6d3a3fdc42c4b354b9e90da443b7_1.csv',
     '2013' : 'https://opendata.arcgis.com/datasets/a8434614d90e416b80fbdfe2cb2901d8_2.csv',
     '2012' : 'https://opendata.arcgis.com/datasets/c4368a66ce65455595a211d530facc54_3.csv'
     }
    if api_year == 'all_keys':
        return(api_urls.keys())
    else:
        df = request_to_pdcsv(api_urls[str(api_year)],api_year)
    return(df)

 
    
def import_data_by_csv(csv_year):    
    bbl = pd.read_csv('Basic_Business_License_in_' + str(csv_year) + '.csv')
    bbl['Year'] = str(csv_year)
    return(bbl)    
    
def count_of_lic_in_ward(bbl):
    bward = {}
    ward_count = 1
    licCount = {}
    row = 0
    for row in range(len(bbl)):
        LC = bbl['LICENSECATEGORY'].loc[row]
        ward = str(bbl['WARD'].loc[row])
        active_status = bbl['LICENSESTATUS'].loc[row]
        if LC not in licCount:
            licCount[bbl['LICENSECATEGORY'].loc[row]] = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}
        
        if active_status == 'ACTIVE':licCount[LC][ward] +=1
        row += 1
    return(licCount)

# ne method to combine lists

bbl18 = import_data_by_api(2018)
count_18 = count_of_lic_in_ward(bbl18)
wards = [1,2,3,4,5,6,7,8]
y = []
x = []
lic_select = 'General Business Licenses'
for item in count_18[lic_select]:
    x.append(item)
    y.append(count_18[lic_select][item])
    
'''      
plt.bar(x,y,align='edge')
plt.show()
'''

bar_chart = pygal.Bar()
bar_chart.add('Ward',y)
bar_chart.x_labels = map(str, wards)
bar_chart.render_to_file('bar.svg')
bar_chart.render_in_browser()
