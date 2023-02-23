# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 15:04:46 2023

@author: Elizabeth

totals the amount of money spent on amazon orders since 1/1/2006
"""

import pandas as pd
#gets the data
df = pd.read_csv('C:/python_work/projects/amazon_orders.csv')
# looks at first five rows of data
df.head()
#gets the dimensions of the dataframe
df.shape()

#cleaning the data
#turns all the NAN values into 0
df = df.fillna(0)

#replaces all $ with nothing. Taking away the $. Then turning it into a float
df["Total Charged"] = df["Total Charged"].str.replace('$','').astype(float)

#finds sum of total charged 
df["Total Charged"].sum()

 