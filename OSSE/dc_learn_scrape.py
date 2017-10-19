# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:31:50 2017

@author: mwatson
"""
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

def try_merge(df_1,df_2):
    df_1_c = df_1.columns
    df_2_c = df_2.columns
    df_3_c = []
    for item in df_1_c:
        if item in df_2_c:
            df_3_c.append(item)
    try:
       df_3 = df_1.merge(df_2,on=df_3_c)
    except:
       df_3 = df_1
    return(df_3)




metric_list = ['attendance','enrollment','suspensions']


empty_SA = pd.DataFrame({'org_type':['ERR','ERR'],
                        'org_code':['ERR','ERR'],
                        'year':['ERR','ERR'],
                        'group':['ERR','ERR'],
                        'population':['ERR','ERR'],
                        'seat_attendance'	:['ERR','ERR'],
                        'state_in_seat_attendance':['ERR','ERR'],
                        'average_daily_attendance'	:['ERR','ERR'],
                        'state_average_daily_attendance':['ERR','ERR']
})

empty_SE = pd.DataFrame({'org_type':['ERR','ERR'],
                         'org_code':['ERR','ERR'],
                         'grade'	:['ERR','ERR'],
                         'year':['ERR','ERR'],
                         'group':['ERR','ERR']

})

empty_SS = pd.DataFrame({'org_type':['ERR','ERR'],
                         'org_code'	:['ERR','ERR'],
                         'year'	:['ERR','ERR'],
                         'subgroup':['ERR','ERR'],
                         'population'	:['ERR','ERR'],
                         'in_seat_attendance'	:['ERR','ERR'],
                         'state_in_seat_attendance'	:['ERR','ERR'],
                         'average_daily_attendance'	:['ERR','ERR'],
                         'state_average_daily_attendance':['ERR','ERR']
})

empty_SW = pd.DataFrame({'org_type'	:['ERR','ERR'],
                         'org_code':['ERR','ERR'],
                         'month'	:['ERR','ERR'],
                         'year'	:['ERR','ERR'],
                         'population'	:['ERR','ERR'],
                         'entry':['ERR','ERR'],
                         'withdrawal'	:['ERR','ERR'],
                         'net_cumulative'	:['ERR','ERR'],
                         'state_entry'	:['ERR','ERR'],
                         'state_withdrawal'	:['ERR','ERR'],
                         'state_net_cumulative':['ERR','ERR']
})
#school_list = {'School ID':['197','3070'],'School Name':['Sela PCS','DC Scholars PCS']}
school_list = pd.read_csv('school_list_csv.csv')
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
    attendance_url = '%sattendance%s'%(start_url,end_url)
    enrollment_url = '%senrollment%s'%(start_url,end_url)
    suspensions_url = '%ssuspensions%s'%(start_url,end_url)
    withdrawl_url = '%smid_year_entry_and_withdrawl%s'%(start_url,end_url)
    mgp_url = '%smgp_scores%s'%(start_url,end_url)
    sped_url = '%sspecial_ed%s'%(start_url,end_url)

    school_attendance,response_SA = read_csv_request(attendance_url)
    school_enrollment,response_SE = read_csv_request(enrollment_url)
    school_suspensions,response_SS= read_csv_request(suspensions_url)
    school_withdrawl,response_SW = read_csv_request(withdrawl_url)


    SA = pd.DataFrame(school_attendance)

    if response_SA == 200:
        SA.columns = SA.iloc[0]
        SA = SA[1:]
    else: SA = empty_SA

    SE = pd.DataFrame(school_enrollment)
    if response_SE == 200:
        SE.columns = SE.iloc[0]
        SE = SE[1:]
    else: SE = empty_SE

    SS = pd.DataFrame(school_suspensions)
    if response_SS == 200:
        SS.columns = SS.iloc[0]
        SS = SA[1:]
    else: SS = empty_SS

    SW = pd.DataFrame(school_suspensions)
    if response_SW == 200:
        SW.columns = SS.iloc[0]
        SW = SA[1:]
    else: SW = empty_SW

    df_1 = try_merge(SA,SE)
    df_2 = try_merge(df_1,SS)
    df_3 = try_merge(df_2,SW)

    final_data_no_names = df_3
    SA['School Name'] = school_name
    SE['School Name'] = school_name
    SS['School Name'] = school_name
    SW['School Name'] = school_name
    final_data_no_names['School Name'] = school_name
    final_data = final_data_no_names

    if school_index == 0:
        SA.to_csv('dc_learn_data_attendance.csv')
        SE.to_csv('dc_learn_data_enrollment.csv')
        SS.to_csv('dc_learn_data_suspensions.csv')
        SW.to_csv('dc_learn_data_withdrawl.csv')
        #final_data.to_csv('dc_learn_data.csv')
    else:
        SA.to_csv('dc_learn_data_attendance.csv', mode='a', header=False)
        SE.to_csv('dc_learn_data_enrollment.csv', mode='a', header=False)
        SS.to_csv('dc_learn_data_suspensions.csv', mode='a', header=False)
        SW.to_csv('dc_learn_data_withdrawl.csv', mode='a', header=False)
        #final_data.to_csv('dc_learn_data.csv', mode='a', header=False)
    time.sleep(2)
    if school_index % 10 == 0:
        print('Finished %s out of %s\n'%(str(school_index),str(school_list_len)))
    school_index += 1
