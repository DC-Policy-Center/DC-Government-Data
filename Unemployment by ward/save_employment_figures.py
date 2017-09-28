'''
Dependencies: pandas, matplotlib
Uses employment/unemployment numbers from scraped PDF files by ward.
Source:https://does.dc.gov/page/unemployment-data-dc-wards#overlay-context=page/labor-statistics
|Signature-------------------------------------------|
|Written for DC Policy Center by Michael Watson; 2017|
|www.DCPolicyCenter.org / DC-Policy-Center.github.io |
|github:M-Watson & MW-DC-Policy-Center               |
|----------------------------------------------------|

'''

import pandas as pd
import matplotlib.pyplot as plt


#-------------- Selector variables -----------------
# Selects which column to plot
# Options are: Labor Force , Employment , Unemployment, Rate

variable_list = ['Labor Force' , 'Employment' , 'Unemployment', 'Rate']
# This just changes the date range on the figure, does not check or correct anything at the data level
final_month_year = 'Aug-2017'

import employment_data_by_ward_plot as unemp
for item in variable_list:
    plot_var = item
    print(item)
    unemp.plot_unemployment(plot_var,final_month_year,False,True)
