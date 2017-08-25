import pandas as pd
import matplotlib.pyplot as plt


ward_1 = []
ward_2 = []
ward_3 = []
ward_4 = []
ward_5 = []
ward_6 = []
ward_7 = []
ward_8 = []
x = []
vline_loc_6 = []
vline_loc_12 = []

rbw = pd.read_csv('unemployment_indexed.csv')
m_y = pd.read_csv('month_year.csv')
m_y = m_y['month_year']
for i in range(len(m_y)):
    x.append(i+1)
    if i%6 == 0:
        vline_loc_6.append(i+1)
    if i%12 == 0:
        vline_loc_12.append(i+1)

print(len(x))

# Selects which column to plot
# Options are: Labor Force , Employment , Unemployment, Rate
plot_var = 'Rate'
final_month_year = 'Jul-2017'
for i in range(len(rbw)):
    if rbw['Ward'][i] == 1:
        ward_1.append(rbw[plot_var][i])
    elif rbw['Ward'][i] == 2:
        ward_2.append(rbw[plot_var][i])
    elif rbw['Ward'][i] == 3:
        ward_3.append(rbw[plot_var][i])
    elif rbw['Ward'][i] == 4:
        ward_4.append(rbw[plot_var][i])
    elif rbw['Ward'][i] == 5:
        ward_5.append(rbw[plot_var][i])
    elif rbw['Ward'][i] == 6:
        ward_6.append(rbw[plot_var][i])
    elif rbw['Ward'][i] == 7:
        ward_7.append(rbw[plot_var][i])
    elif rbw['Ward'][i] == 8:
        ward_8.append(rbw[plot_var][i])


plt.plot(x,ward_1,label='Ward 1')
plt.plot(x,ward_2,label='Ward 2')
plt.plot(x,ward_3,label='Ward 3')
plt.plot(x,ward_4,label='Ward 4')
plt.plot(x,ward_5,label='Ward 5')
plt.plot(x,ward_6,label='Ward 6')
plt.plot(x,ward_7,label='Ward 7')
plt.plot(x,ward_8,label='Ward 8')

# Plot vertical lines for every 12 months
for i in range(len(vline_loc_6)):
    plt.axvline(x=vline_loc_6[i],linestyle='dotted')
for i in range(len(vline_loc_12)):
    plt.axvline(x=vline_loc_12[i],linestyle='dotted',color='red')

years= [2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.ylabel(plot_var)
plt.xlabel('Time index representing month/year (dotted red is January, dotted blue is July)')
plt.title('%s vs Time index by Ward( Jan-2002 to %s)'%(plot_var,final_month_year))
plt.show()
