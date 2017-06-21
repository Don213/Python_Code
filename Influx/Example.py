# Proof of concept - Intelecell Download Script

import requests
import pandas as pd
import matplotlib.pyplot as plt

data = {'fields[]':['cf5c71dabb0f8a9ffa20abc3b194b990','db7817085234d28451b2b999f5c1b2b6','8b269ebb06edcefa2d00305a034460c1'],
        'startdate': '2016-06-01',
        'enddate':'2016-06-28',
        'timezone':'gmt',
        'time_format':'rfc3339',
        'sort':'ASC',
        'format':'csv',
        'submit':'1'
        }

url = 'http://www.intelesense.net/data/intelecell/9999999900040000/view/download/'
data_url = 'https://www.intelesense.net/website-live/userdata/temp/-gefs_kodiak.csv'

r = requests.post(url, data = data)

columns = ['Date','x','y','z','unknown']
df = pd.read_csv(data_url,names=columns)
df = df.drop(df.index[[0]])
df = df.apply(lambda x: pd.to_numeric(x, errors='ignore'))
df.index = pd.to_datetime(df['Date'], utc=True)
df.drop('Date', inplace=True, axis=1)
df.drop('unknown', inplace=True, axis=1)

df = df.apply(lambda x: pd.to_numeric(x, errors='ignore'))

print(df.head())
#df = df.resample('60S').mean()  # re-sample at 1 Second intervals
#df = df.interpolate().dropna(how='any', axis=0)  # interpolate any missing data and delete bad rows
print(df.dtypes)
#exit(0)
df.plot()

plt.show()

#r.text.find('\"https://www.intelesense.net/website-live/userdata/temp/')

#d = requests.get(data_url)
#print (d.content)

#r = requests.Request('POST','http://www.intelesense.net/data/intelecell/9999999900040000/view/download/', data=data)

#prepared = r.prepare()
#print (r.content)
#s = requests.session()
#s.send(prepared)

#print (r.content)
#print (r.text)