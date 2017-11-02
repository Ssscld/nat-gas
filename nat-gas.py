
'''
Package to discover alphas in nat gas futures. 

'''
import pandas as pd
import matplotlib.pyplot as plt

sheets = ['NG Prices']

df = pd.read_excel('BIG TIME.xlsx', sheetname=sheets[0])
 
print("Column headings:")
print(df.columns)
df.set_index(pd.to_datetime(df['Trade_Date'], format='%d-%b-%y'), inplace = True)
print(df.head())

plt.figure()

df.plot(x='Trade_Date', y='Imbalance')

plt.show()





