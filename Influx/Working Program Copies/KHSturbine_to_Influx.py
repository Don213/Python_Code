import requests
import pandas as pd
import subprocess as sp
import time



#Make sure the server programs are running. This program will not successfully record to influx if they are not running


while(1):
    try:

        Turbine_Output = sp.check_output(['/home/pi/WI/resources/s2zcmd -z +404c0b1d dstat 1 0'], shell=True)
        Turbine_Output = Turbine_Output.decode("utf-8")

        import time
        import datetime as dt
        import pytz

        # This displays the current UTC time

        dt_utc = dt.datetime.now(tz=pytz.UTC)
        print(dt_utc)

        # This displays the current alaska time while being time zone aware of the UTC time
        dt_alaska = dt_utc.astimezone(pytz.timezone('US/Alaska'))
        print(dt_alaska)

        d = dt_alaska
        unixtime = time.mktime(d.timetuple())

        print(unixtime)

        Turbine_StringList = Turbine_Output.split(',')

        def cutit(s,n):
           return s[n:]

        Turbine_StringList[0] = cutit(Turbine_StringList[0],17)

        #print(type(Turbine_StringList))

        List2 = Turbine_StringList[1].split(' ')

        Turbine_StringList[1] = List2[0]

        Turbine_StringList.insert(2, List2[1])
        #print(List2)

        Turbine_StringList[1] = cutit(Turbine_StringList[1],5)


        print (Turbine_StringList)

        #print(len(Turbine_StringList))
        #print(type(Turbine_StringList))

        data = {
            'turbine_id' : [] ,
            'sw_version' : [],
            'time1' : [],
            'watt_hours' : [],
            'daily_tot' : [],
            'voltage_dc_bus' : [],
            'voltage_l1' : [],
            'voltage_l2' : [],
            'voltage_rise' : [],
            'min_v_from_rpm' : [],
            'current_out' : [],
            'power_out' : [],
            'power_reg' : [],
            'power_max' : [],
            'line_frequency' : [],
            'inverter_frequency' : [],
            'line_resistance' : [],
            'rpm' : [],
            'windspeed' : [],
            'target_tsr' : [],
            'ramp_rpm' : [],
            'boost_pulswidth' : [],
            'max_bpw' : [],
            'current_amplitude' : [],
            't1' : [],
            't2' : [],
            't3' : [],
            'event_count' : [],
            'last_event_code' : [],
            'event_status' : [],
            'event_value' : [],
            'turbine_status' : [],
            'grid_status' : [],
            'system_status' : [],
            'slave_status' : [],
            'access_status' : [],
            'timer' : [],
            'end_value' : [],
            'timestamp' : []
        }
        #This is the dictionary input for the data input into the server

        data['turbine_id'].append(Turbine_StringList[0])
        data['sw_version'].append(Turbine_StringList[1])
        data['time1'].append(Turbine_StringList[2])
        data['watt_hours'].append(Turbine_StringList[3])
        data['daily_tot'].append(Turbine_StringList[4])
        data['voltage_dc_bus'].append(Turbine_StringList[5])
        data['voltage_l1'].append(Turbine_StringList[6])
        data['voltage_l2'].append(Turbine_StringList[7])
        data['voltage_rise'].append(Turbine_StringList[8])
        data['min_v_from_rpm'].append(Turbine_StringList[9])
        data['current_out'].append(Turbine_StringList[10])
        data['power_out'].append(Turbine_StringList[11])
        data['power_reg'].append(Turbine_StringList[12])
        data['power_max'].append(Turbine_StringList[13])
        data['line_frequency'].append(Turbine_StringList[14])
        data['inverter_frequency'].append(Turbine_StringList[15])
        data['line_resistance'].append(Turbine_StringList[16])
        data['rpm'].append(Turbine_StringList[17])
        data['windspeed'].append(Turbine_StringList[18])
        data['target_tsr'].append(Turbine_StringList[19])
        data['ramp_rpm'].append(Turbine_StringList[20])
        data['boost_pulswidth'].append(Turbine_StringList[21])
        data['max_bpw'].append(Turbine_StringList[22])
        data['current_amplitude'].append(Turbine_StringList[23])
        data['t1'].append(Turbine_StringList[24])
        data['t2'].append(Turbine_StringList[25])
        data['t3'].append(Turbine_StringList[26])
        data['event_count'].append(Turbine_StringList[27])
        data['last_event_code'].append(Turbine_StringList[28])
        data['event_status'].append(Turbine_StringList[29])
        data['event_value'].append(Turbine_StringList[30])
        data['turbine_status'].append(Turbine_StringList[31])
        data['grid_status'].append(Turbine_StringList[32])
        data['system_status'].append(Turbine_StringList[33])
        data['slave_status'].append(Turbine_StringList[34])
        data['access_status'].append(Turbine_StringList[35])
        data['timer'].append(Turbine_StringList[36])
        data['end_value'].append(Turbine_StringList[37])
        data['timestamp'].append(int(unixtime)*1000000000)

        print ('Done appending dictionary')

        #data.values()

        data['turbine_id'] = list(map(str, data['turbine_id']))
        data['sw_version'] = list(map(str, data['sw_version']))
        data['time1'] = list(map(str, data['time1']))
        data['watt_hours'] = list(map(str, data['watt_hours']))
        data['daily_tot'] = list(map(str, data['daily_tot']))
        data['voltage_dc_bus'] = list(map(str, data['voltage_dc_bus']))
        data['voltage_l1'] = list(map(str, data['voltage_l1']))
        data['voltage_l2'] = list(map(str, data['voltage_l2']))
        data['voltage_rise'] = list(map(str, data['voltage_rise']))
        data['min_v_from_rpm'] = list(map(str, data['min_v_from_rpm']))
        data['current_out'] = list(map(str, data['current_out']))
        data['power_out'] = list(map(str, data['power_out']))
        data['power_reg'] = list(map(str, data['power_reg']))
        data['power_max'] = list(map(str, data['power_max']))
        data['line_frequency'] = list(map(str, data['line_frequency']))
        data['inverter_frequency'] = list(map(str, data['inverter_frequency']))
        data['line_resistance'] = list(map(str, data['line_resistance']))
        data['rpm'] = list(map(str, data['rpm']))
        data['windspeed'] = list(map(str, data['windspeed']))
        data['target_tsr'] = list(map(str, data['target_tsr']))
        data['ramp_rpm'] = list(map(str, data['ramp_rpm']))
        data['boost_pulswidth'] = list(map(str, data['boost_pulswidth']))
        data['max_bpw'] = list(map(str, data['max_bpw']))
        data['current_amplitude'] = list(map(str, data['current_amplitude']))
        data['t1'] = list(map(str, data['t1']))
        data['t2'] = list(map(str, data['t2']))
        data['t3'] = list(map(str, data['t3']))
        data['event_count'] = list(map(str, data['event_count']))
        data['last_event_code'] = list(map(str, data['last_event_code']))
        data['event_status'] = list(map(str, data['event_status']))
        data['event_value'] = list(map(str, data['event_value']))
        data['turbine_status'] = list(map(str, data['turbine_status']))
        data['grid_status'] = list(map(str, data['grid_status']))
        data['system_status'] = list(map(str, data['system_status']))
        data['slave_status'] = list(map(str, data['slave_status']))
        data['access_status'] = list(map(str, data['access_status']))
        data['timer'] = list(map(str, data['timer']))
        data['end_value'] = list(map(str, data['end_value']))
        data['timestamp'] = list(map(str, data['timestamp']))

        #Trying to take the space out of data['last_event_code']
        #It does not work


        print ('Done converting')

        df = pd.DataFrame({k : pd.Series(v) for k, v in data.items()})
        #df = pd.DataFrame(data)
        # print(df.dtypes)

        print('Done converting into df')



        url =  'http://10.194.40.100:8086/write?db=windturbine'

        #I have commented out the rows that have values that include things besides numbers & things that are not needed
        #The Turbine ID comes first in the data set but i have switched it with SW Version so that i could block easily
        #Running this from the pi i remove the bad parts of the string to allow sending of the Turbine ID
        #Last Event code still has a bad string, and so does the ending value. This value is not useful in any way thou

        for index, row in df.iterrows():

            Data_String = ("KHSwindturbine SW_Version=" + (row['sw_version']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Turbine_ID=" + (row['turbine_id']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Time(sec)=" + (row['time1']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Watt_hours=" + (row['watt_hours']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Daily_Tot=" + (row['daily_tot']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Voltage_DC_Bus=" + (row['voltage_dc_bus']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Voltage_L1=" + (row['voltage_l1']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Voltage_L2=" + (row['voltage_l2']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Voltage_Rise=" + (row['voltage_rise']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Min_V_From_RPM=" + (row['min_v_from_rpm']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Current_Out=" + (row['current_out']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Power_Out=" + (row['power_out']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Power_Reg=" + (row['power_reg']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Power_Max=" + (row['power_max']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Line_Frequency=" + (row['line_frequency']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Inverter_Frequency=" + (row['inverter_frequency']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Line_Resistance=" + (row['line_resistance']) + " " + (row['timestamp'])
            + "\nKHSwindturbine RPM=" + (row['rpm']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Windspeed=" +(row['windspeed']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Target_TSR=" + (row['target_tsr']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Ramp_RPM=" + (row['ramp_rpm']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Boost_Pulswidth=" + (row['boost_pulswidth']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Max_BPW=" + (row['max_bpw']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Current_Amplitude=" + (row['current_amplitude']) + " " + (row['timestamp'])
            + "\nKHSwindturbine T1=" + (row['t1']) + " " + (row['timestamp'])
            + "\nKHSwindturbine T2=" + (row['t2']) + " " + (row['timestamp'])
            + "\nKHSwindturbine T3=" + (row['t3']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Event_Count=" + (row['event_count']) + " " + (row['timestamp'])
            #+ "\nKHSwindturbine Last_Event_Code=" + (row['last_event_code']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Event_Status=" + (row['event_status']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Event_value=" + (row['event_value']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Turbine_Status=" + (row['turbine_status']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Grid_Status=" + (row['grid_status']) + " " + (row['timestamp'])
            + "\nKHSwindturbine System_Status=" + (row['system_status']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Slave_Status=" + (row['slave_status']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Access_Status=" + (row['access_status']) + " " + (row['timestamp'])
            + "\nKHSwindturbine Timer=" + (row['timer']) + " " + (row['timestamp']))
            #+ "\nKHSwindturbine End_Value=" + (row['end_value']) + " " + (row['timestamp']))

            r = requests.post(url, data=Data_String)

        print ('Going to sleep')
        time.sleep(10)
    except:
        print ('An error occurred. Ignoring')
        pass
        #This is a testing code to see where there are errors when sending data
        '''
            if r.status_code == 204 or r.status_code == 200:
                print('True')
            elif r.status_code == 400:
                print('False')
            else:
                print('idk')
        '''

