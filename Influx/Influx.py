

import requests
import time
import random
import pandas as pd
import matplotlib.pyplot as plt

#df = pd.read_csv('C:\\Users\\Daniel\\Desktop\\Server\\ss2014_04.csv',low_memory=False)

url = 'http://localhost:8086/write?db=windturbine'




while 1:
    turbine_id = str(random.randint(0, 1000))
    sw_version = str(random.randint(0, 1000))
    time1 = str(random.randint(0, 1000))
    time2 = str(random.randint(0, 1000))
    watt_hours = str(random.randint(0, 1000))
    daily_tot = str(random.randint(0, 1000))
    voltage_in = str(random.randint(0, 1000))
    voltage_dc_bus = str(random.randint(0, 1000))
    voltage_l1 = str(random.randint(0, 1000))
    voltage_l2 = str(random.randint(0, 1000))
    voltage_rise = str(random.randint(0, 1000))
    min_v_from_rpm = str(random.randint(0, 1000))
    current_out = str(random.randint(0, 1000))
    power_out = str(random.randint(0, 1000))
    power_reg = str(random.randint(0, 1000))
    power_max = str(random.randint(0, 1000))
    line_frequency = str(random.randint(0, 1000))
    inverter_frequency = str(random.randint(0, 1000))
    line_resistence = str(random.randint(0, 1000))
    rpm = str(random.randint(0, 1000))
    windspeed = str(random.randint(0, 1000))
    target_tsr = str(random.randint(0, 1000))
    ramp_rpm = str(random.randint(0, 1000))
    boost_pulswidth = str(random.randint(0, 1000))
    max_bpw = str(random.randint(0, 1000))
    current_amplitude = str(random.randint(0, 1000))
    t1 = str(random.randint(0, 1000))
    t2 = str(random.randint(0, 1000))
    t3 =  str(random.randint(0, 1000))
    event_count = str(random.randint(0, 1000))
    last_event_code = str(random.randint(0, 1000))
    event_status = str(random.randint(0, 1000))
    event_value = str(random.randint(0, 1000))
    turbine_status = str(random.randint(0, 1000))
    grid_status = str(random.randint(0, 1000))
    system_status = str(random.randint(0, 1000))
    slave_status = str(random.randint(0, 1000))
    access_status = str(random.randint(0, 1000))
    timer = str(random.randint(0, 1000))
    end_value = str(random.randint(0, 1000))

    time.sleep(5.00)
    r = requests.post(url, data = "KHSwindturbine Turbine_ID="+ turbine_id
    +"\nKHSwindturbine SW_Version="+ sw_version
    +"\nKHSwindturbine Time(sec)="+ time1
    +"\nKHSwindturbine Time(MDY:HMS)="+ time2
    +"\nKHSwindturbine Watt_hours="+ watt_hours
    +"\nKHSwindturbine Daily_Tot="+ daily_tot
    +"\nKHSwindturbine Voltage_In="+ voltage_in
    +"\nKHSwindturbine Voltage_DC_Bus="+ voltage_dc_bus
    +"\nKHSwindturbine Voltage_L1="+ voltage_l1
    +"\nKHSwindturbine Voltage_L2="+ voltage_l2
    +"\nKHSwindturbine Voltage_Rise="+ voltage_rise
    +"\nKHSwindturbine Min_V_From_RPM="+ min_v_from_rpm
    +"\nKHSwindturbine Current_Out="+ current_out
    +"\nKHSwindturbine Power_Out=" + power_out
    +"\nKHSwindturbine Power_Reg=" + power_reg
    +"\nKHSwindturbine Power_Max=" + power_max
    +"\nKHSwindturbine Line_Frequency=" + line_frequency
    +"\nKHSwindturbine Inverter_Frequency=" + inverter_frequency
    +"\nKHSwindturbine Line_Resistance=" + line_resistence
    +"\nKHSwindturbine RPM=" + rpm
    +"\nKHSwindturbine Windspeed=" +windspeed
    +"\nKHSwindturbine Target_TSR=" + target_tsr
    +"\nKHSwindturbine Ramp_RPM=" + ramp_rpm
    +"\nKHSwindturbine Boost_Pulswidth=" + boost_pulswidth
    +"\nKHSwindturbine Max_BPW=" + max_bpw
    +"\nKHSwindturbine Current_Amplitude=" + current_amplitude
    +"\nKHSwindturbine T1=" + t1
    +"\nKHSwindturbine T2=" + t2
    +"\nKHSwindturbine T3=" + t3
    +"\nKHSwindturbine Event_Count=" + event_count
    +"\nKHSwindturbine Last_Event_Code=" + last_event_code
    +"\nKHSwindturbine Event_Status=" + event_status
    +"\nKHSwindturbine Event_value=" + event_value
    +"\nKHSwindturbine Turbine_Status=" + turbine_status
    +"\nKHSwindturbine Grid_Status=" + grid_status
    +"\nKHSwindturbine System_Status=" + system_status
    +"\nKHSwindturbine Slave_Status=" + slave_status
    +"\nKHSwindturbine Access_Status=" + access_status
    +"\nKHSwindturbine Timer=" + timer
    +"\nKHSwindturbine End_Value" + end_value)



'''
        r = requests.post(url, data="KHSwindturbine Turbine_ID=" +(row[str('Turbine ID')])

        (row[str('SW Version')])
        (row[str('Time(sec)')])
        (row[str('Time(MDY:HMS)')])
        (row[str('watt-hours')])
        (row[str('DailyTot')])
        (row[str('Voltage In')])
        (row[str('Voltage DC Bus')])
        (row[str('Voltage L1')])
        (row[str('Voltage L2')])
        (row[str('voltage rise')])
        (row[str('min v from rpm')])
        (row[str('Current out')])
        (row[str('Power out')])
        (row[str('Power reg')])
        (row[str('Power max')])
        (row[str('Line Frequency')])
        (row[str('Inverter Frequency')])
        (row[str('Line Resistance')])
        (row[str('RPM')])
        (row[str('Windspeed (ref meters/sec)')])
        (row[str('TargetTSR')])
        (row[str('Ramp RPM')])
        (row[str('Boost pulswidth')])
        (row[str('Max BPW')])
        (row[str('current amplitude')])
        (row[str(' T1')])
        (row[str('T2')])
        (row[str('T3')])
        (row[str('Event count')])
        (row[str('Last event code')])
        (row[str('Event status')])
        (row[str('Event value')])
        (row[str('Turbine status')])
        (row[str('Grid status')])
        (row[str('System status')])
        (row[str('Slave Status')])
        (row[str('Access Status')])
        (row[str('Timer')])
        (row[str('Unnamed: 39')])
r = requests.post(url, data = "KHSwindturbine Turbine_ID=" + data.get ('turbine_id')
'''
