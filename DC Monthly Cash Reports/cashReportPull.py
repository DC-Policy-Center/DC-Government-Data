'''
Dependencies: Requests 
Pulls cash report PDF files from https://cfo.dc.gov/page/dc-revenue-reports


|Signature-------------------------------------------|
|Written for DC Policy Center by Michael Watson; 2017|
|www.DCPolicyCenter.org / DC-Policy-Center.github.io |
|github:M-Watson & MW-DC-Policy-Center               |
|----------------------------------------------------|

'''


import requests

#Initializing variables used
monthList = ['January','February','March','April','May','June','July','August','September','October','November','December']
base_url = 'http://cfo.dc.gov/sites/default/files/dc/sites/ocfo/publication/attachments'  #base CFO document url
i = 0  #A bad habit from my physics days using 'i' as my indexing variable
namingConvention = 'a' #currently the only naming convention that will do anything
#                 NAMING CONVENTION COMMENT
''' Some of the naming conventions for files used
a) /Cash Report - {MONTH} FY {FY}.pdf
b) /Cash Report_{MONTH} FY {FY}.pdf
c) /Cash Report_{MONTH} FY{FY}.pdf
d) /{MONTH} {CY} Cash Report_Uncompressed.pdf
'''#           END OF NAMING CONVENTION COMMENT


for i in range(len(monthList)):  #for loop through the months of the year
    if namingConvention = 'a':
        req_url = '/Cash Report - %s FY 2016.pdf'%(monthList[i])                       #naming convention 'a' requested url builder
        full_url = base_url+req_url                                                    #build url from base and requested url
    print(full_url)
    res = requests.get(full_url)'

#PDF naming convention should not change !FIX!(I want to make the FY a variable as well)
    pdf_filename = '.\Source PDF\Cash Report - %s FY 2016.pdf'%(monthList[i])
    with open(pdf_filename,'wb') as f: #opening pdf file
        f.write(res.content)
    f.close()
