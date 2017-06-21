import subprocess as sp
import time

#sp.run(args = ['C:\\Users\\Daniel\\Desktop\\putty'])

#KHS_Turbine = sp.call(['sudo bash', 'cd WI/resources', '/s2zcmd -z +404c0b1d dstat 1 0'], shell=False)

Turbine_Output = sp.call(['/home/pi/WI/resources/s2zcmd -z +404c0b1d dstat 1 0'], shell=True)
x = Turbine_Output
print(x)


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











'''
#cwd = 'C:\\Users\\Daniel\\Desktop\\putty'
#cwd = 'putty.exe'

#sp.Popen(['C:\\Users\\Daniel\\Desktop\\putty', 'pi@10.194.40.163 -pw raspberry'], stdout=sp.PIPE)

#sp.Popen(['pi','raspberry','sudo bash','/home/pi/WI/resources/s2zcmd -z +404c0b1d dstat 1 0'],cwd=cwd)
while(1):
    sp.Popen(['plink.exe -ssh', '/s2zcmd -z +404c0b1d dstat 1 0'], stdout=sp.PIPE, shell=True)
    text = sp.PIPE.communicate()[0]
    print(text)

#out = sp.stdout.read()
    time.sleep(30)


import paramiko
ssh = paramiko.SSHClient()
ssh.connect(hostname='10.194.40.163', username='pi',password='raspberry',key_filename='C:\\Users\\Daniel\\Desktop\\putty')
'''