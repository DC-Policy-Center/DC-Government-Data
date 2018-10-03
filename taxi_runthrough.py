import pandas as pd

def sum_check(d,header):
    err_list = []
    sum_val = 0
    str_count = 0
    for i in range(len(d)):
        if isinstance(d[header][i],str):
            try:
                f_val = float(d[header][i])
                sum_val += f_val
            except:
                str_count += 1
                err_list.append(d[header][i])   
        else:
            sum_val += d[header][i]
    print(str_count)
    return(sum_val)


d1 = pd.read_csv('taxi_201701.txt',sep='|') 
print('\n\n----\nLoaded File 1')
d2 = pd.read_csv('taxi_201702.txt',sep='|')  
print('\nLoaded File 2')
d3 = pd.read_csv('taxi_201703.txt',sep='|')
print('\nLoaded File 3')

headers = list(d1)
METERFARE = headers[3]
TIP = headers[4]
SURCHARGE = headers[5]
EXTRAS = headers[6]
TOTALAMOUNT = headers[8]

d1_len = len(d1)
d2_len = len(d2)
d3_len = len(d3)
rides = d1_len + d2_len + d3_len

print('\nSumming up METERFARE\n')
d1_fare_sum = sum_check(d1,METERFARE)
d2_fare_sum = sum_check(d2,METERFARE)
d3_fare_sum = sum_check(d3,METERFARE)
meterfare = d1_fare_sum + d2_fare_sum + d3_fare_sum
print(meterfare)

print('\nSumming up TIP\n')
d1_tip_sum = sum_check(d1,TIP)
d2_tip_sum = sum_check(d2,TIP)
d3_tip_sum = sum_check(d3,TIP)
tip = d1_tip_sum + d2_tip_sum + d3_tip_sum
print(tip)


print('\nSumming up SURCHARGE\n')
d1_surcharge_sum = sum_check(d1,SURCHARGE)
d2_surcharge_sum = sum_check(d2,SURCHARGE)
d3_surcharge_sum = sum_check(d3,SURCHARGE)
surcharge = d1_surcharge_sum + d2_surcharge_sum + d3_surcharge_sum
print(surcharge)


print('\nSumming up EXTRAS\n')
d1_extras_sum = sum_check(d1,EXTRAS)
d2_extras_sum = sum_check(d2,EXTRAS)
d3_extras_sum = sum_check(d3,EXTRAS)
extras = d1_extras_sum + d2_extras_sum + d3_extras_sum 
print(extras)

print('\nSumming up TOTALAMOUNT\n')
d1_total_sum = sum_check(d1,TOTALAMOUNT)
d2_total_sum = sum_check(d2,TOTALAMOUNT)
d3_total_sum = sum_check(d3,TOTALAMOUNT)
total = d1_total_sum + d2_total_sum + d3_total_sum
print(total)


print('Writing output now')
with open('taxi_output.txt','a') as f:
    f.write('Rides = %s'%rides)
    f.write('\nMeterfare = %s'%str(meterfare) )
    f.write('\nTips = %s'%str(tip))
    f.write('\nSurcharge = %s'%str(surcharge))
    f.write('\nExtras = %s'%str(extras))
    f.write('\nTotal = %s'%str(total))




    