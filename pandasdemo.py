import pandas as pd
import numpy as np
df = pd.read_csv("income.csv")
print(df)
print("\n")
income_dc = df.columns#all data columns from the income dataset
print(income_dc)
print("\n")
#first 2 columns from the income dataset
print(income_dc[:2])
print("\n")
#find datatypes for all the columns
print(df.dtypes)
print("\n")
df.Y2008 = df.Y2008.astype(float)#converts interger type into float datatype
print(df.dtypes)
print("\n")
print("total number of rows and columns:",df.shape)
print("total number of rows:",df.shape[0])
print("total number of columns:",df.shape[1])
print("First five rows from income dataset")
print(df.head())
print("First three rows from income dataset")
print(df.tail(3))
print(df.iloc[0:5])
print(df[0:5])
