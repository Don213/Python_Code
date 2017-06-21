'''import datetime

ts = datetime.datetime.utcnow()

print(ts)
time_string = ts.replace(tzinfo = datetime.timezone.utc)
print()

print(time_string)

time_string = str(int(ts.replace(tzinfo = datetime.timezone.utc).timestamp()))
print(time_string)

time_string = str(int(ts.replace(tzinfo = datetime.timezone.utc).timestamp() * 1000000000))
print(time_string)

reverse_conversion = int(time_string) / 1000000000
print(reverse_conversion)

'''

'''import subprocess

p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print(line),
retval = p.wait()
'''

import datetime as dt
import pytz

date = dt.datetime.now(tz = pytz.UTC)
print(date)
#This provides the current date and time for utc
'''
date = dt.datetime.now(tz=pytz.UTC)
print(date)
#This prints out the current UTC time while being timezone aware

tdelta = dt.timedelta(weeks= 1, days=7)
print(date - tdelta)
#This prints out the difference of time that you specify in the function above
#2016-12-11 09:20:44.496994+00:00
#2016-11-27 09:20:44.496994+00:00
'''
'''
#This displays the current UTC time
dt_utc= dt.datetime.now(tzinfo= pytz.UTC)
print(dt_utc)
#This displays the current alaska time while being time zone aware of the UTC time
dt_alaska= dt_utc.astimezone(pytz.timezone('US/Alaska'))
print(dt_alaska)
'''
'''
#This prints the time given to it
example_time = dt.datetime(2016, 12, 26, 12, 36, 100000)
#Formating is as follows: [year, month, day, hours, minutes, seconds, microseconds]
print(example_time)
'''
#You can not pass a list into a datetime fucntion
time_list = [2016, 12, 26, 12, 36, 100000]
example_time = dt.datetime(time_list)
print(example_time)

#strftime = Datetime to String
#strptime = String to Datetime
#You can find the formatting codes for the type of time that is displayed by searching for it