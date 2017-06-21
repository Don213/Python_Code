import json as j

json1 = j.dumps(['Windturbine', {'turbine id': (1234, 5678, 9101)}])
print(json1)



'''for index, row in df.iterrows():
    data['time1'].append(row['Time(sec)'])

data['time1'] = list(map(int, data['time1']))

df = pd.DataFrame(data)

df['Timestamp'] = df['Time(sec)']*1000000000

print (df.head('Timestamp'))'''