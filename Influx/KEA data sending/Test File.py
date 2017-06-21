

A_Time = "Nov 03, 2016 17:00:00"


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

print (Time_converter(A_Time))






















