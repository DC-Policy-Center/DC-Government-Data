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
plot_var = 'Rate'

# This just changes the date range on the figure, does not check or correct anything at the data level
final_month_year = 'Aug-2017'

def plot_unemployment(plot_var,final_month_year,show_figure,save_figure):
    #-------------- Initializing lists ------------------
    ward_1 = []
    ward_2 = []
    ward_3 = []
    ward_4 = []
    ward_5 = []
    ward_6 = []
    ward_7 = []
    ward_8 = []
    years= [2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017] # used for x labels
    x = []
    vline_loc_july = []
    vline_loc_january = []
    year_x_label = []
    # importing unemployment data and month_year data
    rbw = pd.read_csv('unemployment_indexed.csv')
    m_y = pd.read_csv('month_year.csv')
    m_y = m_y['month_year'] # This is currently a single column dataframe, so removing the extra selection layer
    j = 0
    # Creating indexes for usage
    for i in range(len(m_y)):
        x.append(i+1)                         # x value for plotting
        if i%6 == 0:
            vline_loc_july.append(i+1)        # July virtical line
        if i%12 == 0:
            vline_loc_january.append(i+1)     # January virtical line
            year_x_label.append(years[j])     # builds a list for x labels
            j+=1
        else:
            year_x_label.append('')



    # build lists of data based on variable selected by ward
    for i in range(len(rbw)):
        datum = float(rbw[plot_var][i])
        if rbw['Ward'][i] == 1:
            ward_1.append(datum)
        elif rbw['Ward'][i] == 2:
            ward_2.append(datum)
        elif rbw['Ward'][i] == 3:
            ward_3.append(datum)
        elif rbw['Ward'][i] == 4:
            ward_4.append(datum)
        elif rbw['Ward'][i] == 5:
            ward_5.append(datum)
        elif rbw['Ward'][i] == 6:
            ward_6.append(datum)
        elif rbw['Ward'][i] == 7:
            ward_7.append(datum)
        elif rbw['Ward'][i] == 8:
            ward_8.append(datum)

    # -------------- Plotting ------------------
    # plot each selected variable by ward
    fig = plt.figure()
    plt.plot(x,ward_1,label='Ward 1')
    plt.plot(x,ward_2,label='Ward 2')
    plt.plot(x,ward_3,label='Ward 3')
    plt.plot(x,ward_4,label='Ward 4')
    plt.plot(x,ward_5,label='Ward 5')
    plt.plot(x,ward_6,label='Ward 6')
    plt.plot(x,ward_7,label='Ward 7')
    plt.plot(x,ward_8,label='Ward 8')

    # Plot vertical lines for every 12 months
    for i in range(len(vline_loc_july)):
        plt.axvline(x=vline_loc_july[i],linestyle='dotted')
    for i in range(len(vline_loc_january)):
        plt.axvline(x=vline_loc_january[i],linestyle='dotted',color='red')

    # formatting figure
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.ylabel(plot_var)
    plt.xlabel('Year')
    plt.xticks(x, year_x_label, rotation='vertical')
    plt.title('%s vs Year by Ward( Jan-2002 to %s)'%(plot_var,final_month_year))


    # show plot
    if show_figure == True:
        plt.show()
    if save_figure == True:
        fig.savefig('%s.png'%plot_var,bbox_inches='tight')
