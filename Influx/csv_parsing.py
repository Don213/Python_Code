import pandas as pd

df = pd.read_csv('C:\\Users\\Daniel\\Desktop\\Server\\ss2014_04.csv',low_memory=False)

a = list(df.columns.values)

for index, row in df.iterrows():
    print(row[a])
    #for columns in row[a]:
        #print(columns)


#for col in a:
#    print ("This is column: ", col)
#    df[col]
#    print (df.col)

'''for index, row in df.iterrows():
    for columns in row[]:
        print(columns)'''