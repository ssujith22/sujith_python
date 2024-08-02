import pandas as pd
import numpy as np

#Exercise 1
df = pd.read_csv("iris.csv") #reading the csv using pandas
print("first 10 rows of the dataset")
print(df.head(10))
print("\ndatatypes for all the columns")
print(df.dtypes)

#Exercise 2
print("\nsummary statistics for each feature")
print(df.describe())
print("\nThe mean sepal length for each species")
print(df[["Sepal.Length"]].mean())

#Exercise 3:

#Exercise 4:
print("\ninclude only rows where the sepal length is greater than 5.0.")
filterdata_sepal=(df[df['Sepal.Length']>5.0])
print(filterdata_sepal)

print("\ninclude only rows of the species 'Setosa'")
filterdata_setosa= filterdata_sepal[filterdata_sepal['Species']== 'setosa']
print(filterdata_setosa)

#Exercise 5:
print("Mean-Median-Standard deviation Petal Length by Species:")
mean_petal_length = df.groupby('Species')['Petal.Length'].mean()
median_petal_length = df.groupby('Species')['Petal.Length'].median()
std_petal_length = df.groupby('Species')['Petal.Length'].std()
print(mean_petal_length)
print(median_petal_length)
print(std_petal_length)

print("\nNumber of Occurrences of Each Species:")
species_count = df['Species'].value_counts()
print(species_count)

min_petal_width = df.groupby('Species')['Petal.Width'].min()
max_petal_width = df.groupby('Species')['Petal.Width'].max()

print("\nMinimum Petal Width by Species:")
print(min_petal_width)
print("\nMaximum Petal Width by Species:")
print(max_petal_width)

average_sepal_width = df.groupby('Species')['Sepal.Width'].mean()
species_with_highest_avg_sepal_width = average_sepal_width.idxmax()
print(f"\nSpecies with the Highest Average Sepal Width: {species_with_highest_avg_sepal_width}")


'''
Exercise 3: Data Cleaning

Check
for missing values.
Replace
any missing values with the mean of the respective column (if any).

Exercise 6: Data Transformation

Normalize
the numerical features (sepal length, sepal width, petal length, petal
width) to a range of 0 to 1.
Create
a new column that is the ratio of petal length to petal width.

Exercise 7: Advanced Data Aggregation

Calculate
the 25th, 50th, and 75th percentiles of sepal length for each species.
Determine
the range (max - min) of petal length for each species.

Exercise 8: Merging and Joining

Create
a new DataFrame with additional information about each species (e.g.,
typical habitat).
Merge
this new DataFrame with the original Iris DataFrame.

Exercise 9: Applying Custom Functions

Create
a custom function that categorizes flowers as 'small', 'medium', or
'large' based on petal length.
Apply
this function to create a new column in the dataset.
'''
