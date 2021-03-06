import requests
import time
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\Daniel\\Desktop\\Server\\ss2014_04.csv',low_memory=False)

#df = pd.read_csv('C:\\Users\\Daniel\\Desktop\\Server\\Kodiak Island Borough School District_ss2016_12.csv',low_memory=False)

#print(df.dtypes)


data = {
    'turbine_id' : [] ,
    'sw_version' : [],
    'time1' : [],
    'time2' : [],
    'watt_hours' : [],
    'daily_tot' : [],
    'voltage_in' : [],
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

#List of column names
a = list(df.columns.values)


#This is the dictionary input for the data input into the server


for index, row in df.iterrows():
    data['turbine_id'].append(row['Turbine ID'])
    data['sw_version'].append(row['SW Version'])
    data['time1'].append(row['Time(sec)'])
    data['time2'].append(row['Time(MDY:HMS)'])
    data['watt_hours'].append(row['watt-hours'])
    data['daily_tot'].append(row['DailyTot'])
    data['voltage_in'].append(row['Voltage In'])
    data['voltage_dc_bus'].append(row['Voltage DC Bus'])
    data['voltage_l1'].append(row['Voltage L1'])
    data['voltage_l2'].append(row['Voltage L2'])
    data['voltage_rise'].append(row['voltage rise'])
    data['min_v_from_rpm'].append(row['min v from rpm'])
    data['current_out'].append(row['Current out'])
    data['power_out'].append(row['Power out'])
    data['power_reg'].append(row['Power reg'])
    data['power_max'].append(row['Power max'])
    data['line_frequency'].append(row['Line Frequency'])
    data['inverter_frequency'].append(row['Inverter Frequency'])
    data['line_resistance'].append(row['Line Resistance'])
    data['rpm'].append(row['RPM'])
    data['windspeed'].append(row['Windspeed (ref meters/sec)'])
    data['target_tsr'].append(row['TargetTSR'])
    data['ramp_rpm'].append(row['Ramp RPM'])
    data['boost_pulswidth'].append(row['Boost pulswidth'])
    data['max_bpw'].append(row['Max BPW'])
    data['current_amplitude'].append(row['current amplitude'])
    data['t1'].append(row[' T1'])
    data['t2'].append(row['T2'])
    data['t3'].append(row['T3'])
    data['event_count'].append(row['Event count'])
    data['last_event_code'].append(row['Last event code'])
    data['event_status'].append(row['Event status'])
    data['event_value'].append(row['Event value'])
    data['turbine_status'].append(row['Turbine status'])
    data['grid_status'].append(row['Grid status'])
    data['system_status'].append(row['System status'])
    data['slave_status'].append(row['Slave Status'])
    data['access_status'].append(row['Access Status'])
    data['timer'].append(row['Timer'])
    data['end_value'].append(row['Unnamed: 39'])
    data['timestamp'].append(int(row['Time(sec)'])*1000000000)

print('Done appending dictionary')

#data.values()

data['turbine_id'] = list(map(str, data['turbine_id']))
data['sw_version'] = list(map(str, data['sw_version']))
data['time1'] = list(map(str, data['time1']))
data['time2'] = list(map(str, data['time2']))
data['watt_hours'] = list(map(str, data['watt_hours']))
data['daily_tot'] = list(map(str, data['daily_tot']))
data['voltage_in'] = list(map(str, data['voltage_in']))
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

'''
for x in data['last_event_code']:
    data['last_event_code'] = x.lstrip()
    for element in x:
        data['last_event_code'] = element
'''

print('Done converting')
print(data['timestamp'])
#df = pd.DataFrame({k : pd.Series(v) for k, v in data.items()})
df = pd.DataFrame(data)

print('Done converting into df')



url = 'http://localhost:8086/write?db=windturbine'

#I have commented out the rows that have values that include things besides numbers & things that are not needed
#The Turbine ID comes first in the data set but i have switched it with SW Version so that i could block easily

for index, row in df.iterrows():

    Data_String = ("KHSwindturbine SW_Version=" + (row['sw_version']) + " " + (row['timestamp'])
    #+ "\nKHSwindturbine Turbine_ID=" + (row['turbine_id']) + " " + (row['timestamp'])
    #+ "\nKHSwindturbine Time(sec)=" + (row['time1']) + " " + (row['timestamp'])
    #+ "\nKHSwindturbine Time(MDY:HMS)=" + (row['time2']) + " " + (row['timestamp'])
    #+ "\nKHSwindturbine Watt_hours=" + (row['watt_hours']) + " " + (row['timestamp'])
    + "\nKHSwindturbine Daily_Tot=" + (row['daily_tot']) + " " + (row['timestamp'])
    + "\nKHSwindturbine Voltage_In=" + (row['voltage_in']) + " " + (row['timestamp'])
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
    #+ "\nKHSwindturbine Event_Count=" + (row['event_count']) + " " + (row['timestamp'])
    #+ "\nKHSwindturbine Last_Event_Code=" + (row['last_event_code']) + " " + (row['timestamp'])
    #+ "\nKHSwindturbine Event_Status=" + (row['event_status']) + " " + (row['timestamp'])
    + "\nKHSwindturbine Event_value=" + (row['event_value']) + " " + (row['timestamp'])
    + "\nKHSwindturbine Turbine_Status=" + (row['turbine_status']) + " " + (row['timestamp'])
    + "\nKHSwindturbine Grid_Status=" + (row['grid_status']) + " " + (row['timestamp'])
    + "\nKHSwindturbine System_Status=" + (row['system_status']) + " " + (row['timestamp'])
    + "\nKHSwindturbine Slave_Status=" + (row['slave_status']) + " " + (row['timestamp'])
    + "\nKHSwindturbine Access_Status=" + (row['access_status']) + " " + (row['timestamp'])
    + "\nKHSwindturbine Timer=" + (row['timer']) + " " + (row['timestamp']))
    #+ "\nKHSwindturbine End_Value=" + (row['end_value']) + " " + (row['timestamp']))

    r = requests.post(url, data=Data_String)

#This is a testing code to see where there are errors when sending data





    if r.status_code == 204 or r.status_code == 200:
        print('True')
    elif r.status_code == 400:
        print('False')
    else:
        print('idk')





