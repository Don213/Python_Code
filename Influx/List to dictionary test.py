data = {
    'turbine_id': [],
    'sw_version': [],
    'time2': [],
    'watt_hours': [],
    'daily_tot': [],
    'voltage_dc_bus': [],
    'voltage_l1': [],
    'voltage_l2': [],
    'voltage_rise': [],
    'min_v_from_rpm': [],
    'current_out': [],
    'power_out': [],
    'power_reg': [],
    'power_max': [],
    'line_frequency': [],
    'inverter_frequency': [],
    'line_resistance': [],
    'rpm': [],
    'windspeed': [],
    'target_tsr': [],
    'ramp_rpm': [],
    'boost_pulswidth': [],
    'max_bpw': [],
    'current_amplitude': [],
    't1': [],
    't2': [],
    't3': [],
    'event_count': [],
    'last_event_code': [],
    'event_status': [],
    'event_value': [],
    'turbine_status': [],
    'grid_status': [],
    'system_status': [],
    'slave_status': [],
    'access_status': [],
    'timer': [],
    'end_value': [],
    'timestamp': []
}
# This is the dictionary input for the data input into the server

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
data['timestamp'].append(int(Turbine_StringList[2] * 1000000000))

print('Done appending dictionary')