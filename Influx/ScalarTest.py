'''
import pandas as pd

df = pd.DataFrame()
'''


a = ['1','2','3','4','  5']

for x in a:
    a = x.lstrip()
    for element in a:
        x = element


print(a)

'''
new_list = []
for integer in data['time1']:
      data['timestamp'].append(integer*2)

print(data['timestamp'])'''

'''
d = json.dumps(data)

loaded_data = json.loads(d)

print(loaded_data)
'''