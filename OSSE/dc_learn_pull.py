import requests
import pandas as pd
import csv, time

def read_csv_request(CSV_URL):
    with requests.Session() as s:
        download = s.get(CSV_URL)

        decoded_content = download.content.decode('utf-8')

        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
    response = download.status_code

    return(my_list,response)

def metric_pull(metric):
    school_list = {'School ID':['197','3070'],'School Name':['Sela PCS','DC Scholars PCS']}
    #school_list = pd.read_csv('school_list_csv.csv')
    school_index = 0
    school_list_len = len(school_list)
    for school_index in range(school_list_len):
        school_id = str(school_list['School ID'][school_index])
        school_name = school_list['School Name'][school_index]
        org_code = str(school_id.zfill(4))
        with open('log.txt','a') as f:
            f.write('School ID: %s, School Name: %s\n'%(school_id,school_name))
        f.close()

        start_url = 'https://learndc-api.herokuapp.com//api/exhibit/'
        end_url = '.csv?s[][org_type]=school&s[][org_code]=%s&sha=promoted'%(org_code)
        metric_url = '%s%s%s'%(start_url,metric,end_url)


        school_metric,response = read_csv_request(metric_url)
        metric_dataframe = pd.DataFrame(school_metric)

        if response == 200:
            metric_dataframe.columns = metric_dataframe.iloc[0]
            metric_dataframe = metric_dataframe[1:]
        else: break

        metric_dataframe['School Name'] = school_name


        if school_index == 0:
            metric_dataframe.to_csv('dc_learn_data_attendance.csv')
        else:
            metric_dataframe.to_csv('dc_learn_data_attendance.csv', mode='a', header=False)

        time.sleep(2)
        if school_index % 10 == 0:
            print('Finished %s out of %s\n'%(str(school_index),str(school_list_len)))
        school_index += 1


metric_list = '1) attendance\n2) enrollment\n3) Special education\n4) suspensions\n5)mid-year entrance and withdrawl\n6)median growth percentile'
val = input('What metric would you like to pull? We have\n%s'%metric_list)
