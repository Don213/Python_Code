'''import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except:
    print("Error occurred, ignoring...")
    pass
'''
'''
import datetime as dt
import pytz

#This displays the current UTC time

dt_utc= dt.datetime.now(tz= pytz.UTC)
print(dt_utc)



year = dt.timedelta(days=365)

year.total_seconds()
'''
