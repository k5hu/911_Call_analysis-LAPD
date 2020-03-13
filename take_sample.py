#!/usr/bin/env python

#import packages
import numpy as np
import pandas as pd

#import Socrata for API use
from sodapy import Socrata

#get data through API with sodacra
client = Socrata("data.lacity.org", None)
results = client.get("r4ka-x5je", limit= 3142170)

#initialize with data and check general information
df=pd.DataFrame.from_records(results)
#check general information of origin DataFrame
print(df.head())
print(df.describe())
df.info()
column=df.columns
print(column)

print(df['dispatch_date'].min())#first day 2019-01-01T00:00:00.000,

print(df['dispatch_date'].max())#last day 2020-01-25T00:00:00.000

print(df['area_occ'].unique()) #=21 area in la and 'outside','UNK'

#take a random dataset of 1000
df=df.sample(1000)
df.to_csv('./911_call_random_sample.csv',index=False)
