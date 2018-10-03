import requests
import pandas as pd
import time

total = 1520
for i in range(total):
    i +=1
    page_num = i
    url = "https://b6.caspio.com/dp/d32d2000473e383a0b7f45b6a4ac?cpipage=%i"%(page_num)
    req = requests.get(url)
    print(url)
    print(req)
    req_text = req.text
    current_data = pd.read_html(req_text,header=0)
    current_data = current_data[0]
    #current_data.to_csv('output.csv',mode="a")
    if i == 1:
        full_data = current_data
    else:
        full_data = full_data.append(current_data)
    time.sleep(10)

full_data.to_csv('all_salaries.csv')
