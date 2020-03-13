#!/usr/bin/env python

#import packages
import numpy as np
import pandas as pd

#import visualization tool
import seaborn as sns
import matplotlib.pyplot as plt

#import Socrata for API use
from sodapy import Socrata

#get data through API with sodacra
client = Socrata("data.lacity.org", None)
results = client.get("r4ka-x5je", limit= 3142170)

#initialize with data and check general information
df=pd.DataFrame.from_records(results)
print(df.head())
print(df.describe())
df.info()
column=df.columns
print(column)

##print last few lines to double check if all the data are
#imported correctly
print(df[-3:])


type=df['rpt_dist'].apply(lambda x: isinstance(x,int))
print('number of str in rpt_dist: %s'%(type==True).count())


#first day 2019-01-01T00:00:00.000,
print(df['dispatch_date'].min())
#last day 2020-01-25T00:00:00.000
print(df['dispatch_date'].max())

print(df['area_occ'].unique())

#Eliminate 'outside' from area_occ as it does not tell information wanted
la = df[df['area_occ']!='UNK']

#basic visualization with time
sns.set_style('whitegrid')
df['distpatch_time'].hist(bins=30)
plt.plot()

sns.jointplot(x='dispatch_date',y='distpatch_time',data=df)
plt.plot()

#find correlation between variable

#sns.heatmap(la.corr(), cmap='magma' )
#plt.plot()
#Generally by Time in a day

#sns.heatmap()

#by_reason
