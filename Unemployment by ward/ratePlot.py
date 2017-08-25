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


rbw = pd.read_csv('unemployment_indexed.csv')
m_y = pd.read_csv('month_year.csv')
m_y = m_y['month_year']
for i in range(186):
    x.append(i)

print(rbw.columns)
for i in range(len(rbw)):
    if rbw['Ward'][i] == 1:
        ward_1.append(rbw['Rate'][i])
    elif rbw['Ward'][i] == 2:
        ward_2.append(rbw['Rate'][i])
    elif rbw['Ward'][i] == 3:
        ward_3.append(rbw['Rate'][i])
    elif rbw['Ward'][i] == 4:
        ward_4.append(rbw['Rate'][i])
    elif rbw['Ward'][i] == 5:
        ward_5.append(rbw['Rate'][i])
    elif rbw['Ward'][i] == 6:
        ward_6.append(rbw['Rate'][i])
    elif rbw['Ward'][i] == 7:
        ward_7.append(rbw['Rate'][i])
    elif rbw['Ward'][i] == 8:
        ward_8.append(rbw['Rate'][i])

print(len(m_y))
print(len(ward_1))
plt.plot(x,ward_1,label='Ward 1')
plt.plot(x,ward_2,label='Ward 2')
plt.plot(x,ward_3,label='Ward 3')
plt.plot(x,ward_4,label='Ward 4')
plt.plot(x,ward_5,label='Ward 5')
plt.plot(x,ward_6,label='Ward 6')
plt.plot(x,ward_7,label='Ward 7')
plt.plot(x,ward_8,label='Ward 8')

years= [2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.show()
