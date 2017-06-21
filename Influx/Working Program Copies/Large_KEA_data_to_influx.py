import pandas as pd
import requests

def Time_converter(a):


    def Month_Number(b):
        if b == "Jan":
            return 1
        elif b == 'Feb':
            return 2
        elif b == 'Mar':
            return 3
        elif b == 'Apr':
            return 4
        elif b == 'May':
            return 5
        elif b == 'Jun':
            return 6
        elif b == 'Jul':
            return 7
        elif b == 'Aug':
            return 8
        elif b == 'Sep':
            return 9
        elif b == 'Oct':
            return 10
        elif b == 'Nov':
            return 11
        elif b == 'Dec':
            return 12
        else:
            pass

    import datetime as dt
    import pytz
    import time

    time_list1 = a.split(' ')
    #print (time_list1)

    time_list3 = time_list1[3].split(':')
    #print(time_list3)


    year1 = int(time_list1[2])
    #print(year1)
    month1 = int(Month_Number(time_list1[0]))
    #print(month1)
    day1 = int(time_list1[1].strip(','))
    #print(day1)
    hour1 = int(time_list3[0])
    #print(hour1)
    minute1 = int(time_list3[1])
    #print(minute1)
    second1 = 00
    microsecond1 = 00000

    Almost_Unix = dt.datetime(year=year1, month=month1, day=day1, hour=hour1, minute=minute1, second= second1, microsecond=microsecond1)

    # Almost_Unix = Almost_Unix.astimezone(pytz.timezone('US/Alaska'))
    End_Time = int(time.mktime(Almost_Unix.timetuple())*1000000000)

    return End_Time


df = pd.read_csv('C:\\Users\\Daniel\\Desktop\\June to Nov 2016 kwh.csv',low_memory=False)

a = list(df.columns.values)
#print(a)


Time_List = []

data = {
    'timestamp': [],
    'HYD 1 kwh': [],
    'HYD 2 kwh': [],
    'HYD 3 kwh': [],
    'KPH D1 kwh': [],
    'KPH D2 kwh': [],
    'KPH D3 kwh': [],
    'KPH D4 kwh': [],
    'NYMN 1 kwh': [],
    'NYMN 2 kwh': [],
    'SWPH 1 IN kwh': [],
    'SWPH 1 OUT kwh': [],
    'SWPH 2 IN kwh': [],
    'SWPH 3 OUT kwh': [],
    'SWPH 3 OUT kwh 2': []
}

#print(type(data['timestamp']))

for index, row in df.iterrows():
    data['timestamp'].append(Time_converter(row['Time']))
    data['HYD 1 kwh'].append(row['HYD 1 kwh'])
    data['HYD 2 kwh'].append(row['HYD 2 kwh'])
    data['HYD 3 kwh'].append(row['HYD 3 kwh'])
    data['KPH D1 kwh'].append(row['KPH D1 kwh'])
    data['KPH D2 kwh'].append(row['KPH D2 kwh'])
    data['KPH D3 kwh'].append(row['KPH D3 kwh'])
    data['KPH D4 kwh'].append(row['KPH D4 kwh'])
    data['NYMN 1 kwh'].append(row['NYMN 1 kwh'])
    data['NYMN 2 kwh'].append(row['NYMN 2 kwh'])
    data['SWPH 1 IN kwh'].append(row['SWPH 1 IN kwh'])
    data['SWPH 2 IN kwh'].append(row['SWPH 2 IN kwh'])
    data['SWPH 3 OUT kwh'].append(row['SWPH 3 OUT kwh'])
    data['SWPH 3 OUT kwh 2'].append(row['SWPH 3 OUT kwh.1'])

print(data['timestamp'])

data['timestamp'] = list(map(str, data['timestamp']))
data['HYD 1 kwh'] = list(map(str, data['HYD 1 kwh']))
data['HYD 2 kwh'] = list(map(str, data['HYD 2 kwh']))
data['HYD 3 kwh'] = list(map(str, data['HYD 3 kwh']))
data['KPH D1 kwh'] = list(map(str, data['KPH D1 kwh']))
data['KPH D2 kwh'] = list(map(str, data['KPH D2 kwh']))
data['KPH D3 kwh'] = list(map(str, data['KPH D3 kwh']))
data['KPH D4 kwh'] = list(map(str, data['KPH D4 kwh']))
data['NYMN 1 kwh'] = list(map(str, data['NYMN 1 kwh']))
data['NYMN 2 kwh'] = list(map(str, data['NYMN 2 kwh']))
data['SWPH 1 IN kwh'] = list(map(str, data['SWPH 1 IN kwh']))
data['SWPH 2 IN kwh'] = list(map(str, data['SWPH 2 IN kwh']))
data['SWPH 3 OUT kwh'] = list(map(str, data['SWPH 3 OUT kwh']))
data['SWPH 3 OUT kwh 2'] = list(map(str, data['SWPH 3 OUT kwh 2']))


df = pd.DataFrame({k : pd.Series(v) for k, v in data.items()})

#df = pd.DataFrame(data)
#print(df)

url = 'http://10.194.40.100:8086/write?db=KEA'


for index, row in df.iterrows():
    Data_String = ("KEAdata HYD_1_kwh=" + (row['HYD 1 kwh']) + " " + (row['timestamp'])
    + "\nKEAdata HYD_2_kwh=" + (row['HYD 2 kwh']) + " " + (row['timestamp'])
    + "\nKEAdata HYD_3_kwh=" + (row['HYD 3 kwh']) + " " + (row['timestamp'])
    + "\nKEAdata KPH_D1_kwh=" + (row['KPH D1 kwh']) + " " + (row['timestamp'])
    + "\nKEAdata KPH_D2_kwh=" + (row['KPH D2 kwh']) + " " + (row['timestamp'])
    + "\nKEAdata KPH_D3_kwh=" + (row['KPH D3 kwh']) + " " + (row['timestamp'])
    + "\nKEAdata KPH_D4_kwh=" + (row['KPH D4 kwh']) + " " + (row['timestamp'])
    + "\nKEAdata NYMN_1_kwh=" + (row['NYMN 1 kwh']) + " " + (row['timestamp'])
    + "\nKEAdata NYMN_2_kwh=" + (row['NYMN 2 kwh']) + " " + (row['timestamp'])
    + "\nKEAdata SWPH_1_IN_kwh=" + (row['SWPH 1 IN kwh']) + " " + (row['timestamp'])
    + "\nKEAdata SWPH_2_IN_kwh=" + (row['SWPH 2 IN kwh']) + " " + (row['timestamp'])
    + "\nKEAdata SWPH_3_OUT_kwh=" + (row['SWPH 3 OUT kwh']) + " " + (row['timestamp'])
    + "\nKEAdata SWPH_3_OUT_kwh_2=" + (row['SWPH 3 OUT kwh 2']) + " " + (row['timestamp']))

    r = requests.post(url, data=Data_String)
#This is a testing code to see where there are errors when sending data
    print(r.status_code)


    if r.status_code == 204 or r.status_code == 200:
        print('True')
    elif r.status_code == 400:
        print('False')
    else:
        print('idk')



