'''
import datetime as dt
import pytz
import time



dt_utc = dt.datetime.now(tz=pytz.UTC)
#print(dt_utc)
'''
'''
# This displays the current alaska time while being time zone aware of the UTC time
dt_alaska = dt_utc.astimezone(pytz.timezone('US/Alaska'))
print(dt_alaska)

d = dt_alaska

unixtime = time.mktime(d.timetuple())
print(unixtime)
'''
'''
import datetime as dt
import pytz
import time



a = "11/3/16 13:05"

time_list1 = a.split(' ')
# print (time_list1)

time_list2 = time_list1[0].split('/')
print(time_list2)

time_list3 = time_list1[1].split(':')
print(time_list3)

year1 = int('20'+ time_list2[2])
print(year1)
month1 = int(time_list2[0])
print(month1)
day1 = int(time_list2[1])
print(day1)
hour1 = int(time_list3[0])
print(hour1)
minute1 = int(time_list3[1])
print(minute1)
second1 = 00
microsecond1 = 00000

Almost_Unix = dt.datetime(year=year1, month=month1, day=day1, hour=hour1, minute=minute1, second=second1, microsecond=microsecond1)
print(Almost_Unix)


# Almost_Unix = Almost_Unix.astimezone(pytz.timezone('US/Alaska'))
End_Time = time.mktime(Almost_Unix.timetuple())
print (End_Time)
'''


