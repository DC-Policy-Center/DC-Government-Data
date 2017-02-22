import requests
'''
Pulls cash report PDF files from the cfo.dc.gov site
'''

monthList = ['January','February','March','April','May','June','July','August','September','October','November','December']
base_url = 'http://cfo.dc.gov/sites/default/files/dc/sites/ocfo/publication/attachments'
i = 0
#                 NAMING CONVENTION COMMENT
''' Some of the naming conventions for files used
a) /Cash Report - {MONTH} FY {FY}.pdf
b) /Cash Report_{MONTH} FY {FY}.pdf
c) /Cash Report_{MONTH} FY{FY}.pdf
d) /{MONTH} {CY} Cash Report_Uncompressed.pdf
'''#           END OF NAMING CONVENTION COMMENT
for i in range(len(monthList)):

    req_url = '/Cash Report - %s FY 2016.pdf'%(monthList[i])
    full_url = base_url+req_url
    print(full_url)
    res = requests.get(full_url)
    pdf_filename = '.\Source PDF\Cash Report - %s FY 2016.pdf'%(monthList[i])
    with open(pdf_filename,'wb') as f:
        f.write(res.content)
    f.close()
