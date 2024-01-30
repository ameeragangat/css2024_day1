#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 11:51:17 2024

@author: ameeragangat
"""
import pandas

file_list = ["country_data.csv", "diab_data.csv", "housing_data.csv", "iris.csv"]

for file in file_list:
    file_selected = pandas.read_csv(file)
    print(file_selected)
    print(file_selected.info())
    print(file_selected.describe())   

"""
---------------- COUNTRY DATA ----------------- 

------------------ FILE INFO ------------------ 

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 11 entries, 0 to 10
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   Age      11 non-null     int64 
 1   Gender   11 non-null     object
 2   Country  11 non-null     object
dtypes: int64(1), object(2)
memory usage: 392.0+ bytes

----------------- FILE DESCIBE ----------------- 
             Age
count  11.000000
mean   33.363636
std     9.233339
min    22.000000
25%    27.000000
50%    30.000000
75%    39.500000
max    49.000000

------------------- DIAB DATA -----------------

------------------ FILE INFO ------------------ 

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 768 entries, 0 to 767
Data columns (total 9 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   preg_count  768 non-null    int64  
 1   glucose     768 non-null    int64  
 2   bp          768 non-null    int64  
 3   skinfold    768 non-null    int64  
 4   insulin     768 non-null    int64  
 5   BMI         768 non-null    float64
 6   predigree   768 non-null    float64
 7   age         768 non-null    int64  
 8   class       768 non-null    int64  
dtypes: float64(2), int64(7)
memory usage: 54.1 KB

----------------- FILE DESCIBE ----------------- 

       preg_count     glucose          bp  ...   predigree         age       class
count  768.000000  768.000000  768.000000  ...  768.000000  768.000000  768.000000
mean     3.845052  120.894531   69.105469  ...    0.471876   33.240885    0.348958
std      3.369578   31.972618   19.355807  ...    0.331329   11.760232    0.476951
min      0.000000    0.000000    0.000000  ...    0.078000   21.000000    0.000000
25%      1.000000   99.000000   62.000000  ...    0.243750   24.000000    0.000000
50%      3.000000  117.000000   72.000000  ...    0.372500   29.000000    0.000000
75%      6.000000  140.250000   80.000000  ...    0.626250   41.000000    1.000000
max     17.000000  199.000000  122.000000  ...    2.420000   81.000000    1.000000

------------------- HOUSING DATA --------------

------------------ FILE INFO ------------------

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 505 entries, 0 to 504
Data columns (total 14 columns):
 #   Column   Non-Null Count  Dtype  
---  ------   --------------  -----  
 0   0.00632  505 non-null    float64
 1   18       505 non-null    float64
 2   2.31     505 non-null    float64
 3   0        505 non-null    float64
 4   0.538    505 non-null    float64
 5   6.575    505 non-null    float64
 6   65.2     505 non-null    float64
 7   4.09     505 non-null    float64
 8   1        505 non-null    int64  
 9   296      505 non-null    float64
 10  15.3     505 non-null    float64
 11  396.9    505 non-null    float64
 12  4.98     505 non-null    float64
 13  24       451 non-null    float64
dtypes: float64(13), int64(1)
memory usage: 55.4 KB

----------------- FILE DESCIBE ----------------- 

          0.00632          18        2.31  ...       396.9        4.98          24
count  505.000000  505.000000  505.000000  ...  505.000000  505.000000  451.000000
mean     1.271696   13.285941    9.218812  ...  332.664158   11.550792   23.749889
std      2.400926   23.070598    7.170151  ...  125.414151    6.063900    8.818376
min      0.000000    0.000000    0.000000  ...    0.320000    1.730000    6.300000
25%      0.049810    0.000000    3.440000  ...  364.610000    6.900000   18.500000
50%      0.144760    0.000000    6.960000  ...  390.640000   10.400000   21.900000
75%      0.825260   18.100000   18.100000  ...  395.600000   15.020000   26.600000
max      9.966540  100.000000   27.740000  ...  396.900000   34.410000   50.000000

------------------- IRIS DATA -----------------

------------------ FILE INFO ------------------

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   sepal_length  150 non-null    float64
 1   sepal_width   150 non-null    float64
 2   petal_length  150 non-null    float64
 3   petal_width   150 non-null    float64
 4   species       150 non-null    object 
dtypes: float64(4), object(1)
memory usage: 6.0+ KB

----------------- FILE DESCIBE ----------------- 

       sepal_length  sepal_width  petal_length  petal_width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000
"""

file = pandas.read_csv("insurance_data.csv", skiprows=5)
print(file)

column_names = ["A", "B", "C", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
file = pandas.read_csv("housing_data.csv", names=column_names)
print(file)








