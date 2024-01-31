# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:57:05 2024

@author: radzi
"""

import pandas as FR
file = FR.read_csv("C:/Users/radzi/Downloads/CSM/D2/data_02/data_02/iris.csv")
"""
Absolute Path:
C:/Users/radzi/Downloads/CSM/D2/data_02/data_02/iris.csv

Relative Path:
iris.csv

"""

file = FR.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

url = "https://raw.githubusercontent.com/FulufheloRadzilani/css2024_day01/main/iris.csv"

file = FR.read_csv(url)

column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]

file = FR.read_csv(url, header=None, names = column_names)
file = FR.read_csv("data_02/data_02/Geospatial Data.txt", sep=";")

file = FR.read_excel("data_02/data_02/residentdoctors.xlsx")

file = FR.read_json("data_02/data_02/student_data.json")
print(file)

#df = dataframe
#df = FR.read_csv(url)
#print(fr.info())
#print(df.describe())

#df FR.read_csv("data_02/data_02/country_data_index.csv", index_col=0)
df = FR.read_excel("data_02/data_02/residentdoctors.xlsx")
print(df.info())
#To insert a column you do the following
#Added as a string
#Regular expresion used on Python ("\d+)-")
df["LOWER_AGE"] = df["AGEDIST"].str.extract("(\d+)-")
df["UPPER_AGE"] = df["AGEDIST"].str.extract("(\d+)-")
print(df.info())
#added as an integer
df["LOWER_AGE"] = df["LOWER_AGE"].astype(int)
print(df.info())

"""
working with dates

30-01-2024 - SA/UK

01-30-2024 - US
"""
df = FR.read_csv("data_02/data_02/time_series_data.csv", index_col=0)
print(df.info())

#df["Date"] = FR.to_datetime(df["Date"], format="%d-%m-%Y")
df["Date"] = FR.to_datetime(df["Date"])
#df["Date"] = FR.to_datetime(df["Date"], format="%d-%m-%Y")

print(df.info())

df["Year"] = df["Date"].dt.year

"""
.str
.extract
.astype
"""

dr = FR.read_csv("data_02/data_02/patient_data_dates.csv")
df = FR.read_csv("data_02/data_02/patient_data_dates.csv", index_col=0)

df["Date"] = df["Date"].replace({"":"-"})

df.drop(index=26, inplace=True)
df["Date"] = FR.to_datetime(df["Date"])
print(df.info())

avg_cal = df["Calories"].mean()
#df["Calories"].fillna(avg_cal, inplace = True)

"""
Best practices
"""

df.dropna(inplace = True)

#The duration in row 22 can be replaced (removed comppletely).
df = df.reset_index(drop=True)
#df.loc[7, "Duration"] = 45

df["Duration"] = df["Duration"].replace([450], 50)

print(FR)

#FR.set_option("display.maX_rows", None)

###
df = FR.read_csv("data_02/data_02/iris.csv")

col_names = df.columns.tolist()

print(col_names)
df["sepal_length_sq"] = df["sepal_length"]**2

df["sepal_length_sq_2"] = df["sepal_length"].apply(lambda x: x**2)

grouped = df.groupby("class")
mean_square_value = grouped["sepal_length_sq"].mean()
print(mean_square_value)

###

df1 = FR.read_csv("data_02/data_02/person_split1.csv")
df2 = FR.read_csv("data_02/data_02/person_split2.csv")

df = FR.concat([df1, df2], ignore_index=True)

###

#df1 = FR.read_csv("data_02/data_02/person_education.csv")
#df2 = FR.read_csv("data_02/data_02/person_work.csv")

#Inner join

#df_merge_inner = FR.merge(df1, df2, on="id")

print(df)

df["class"] = df["class"].str.replace("Iris-", "")

df = df[df["sepal_length"] > 5]

df = df[df["class"]=="virginica"]

df.to_csv("output/pulsar.csv")

























