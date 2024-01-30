#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:42:21 2024

@author: ameeragangat


Storing data in Python
1. Lists
2. Dictionaries
3. Data Frames
"""
#%%
age = [30, 25, 29, 46,22, 35, 22, 49, 30, 40, 30]
gender = ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"]
country = ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]

print(min(age))
print(max(age))
print(len(age))
print(sum(age))

age.insert(0,100)
print(age)

age.remove(100)
print(age)

average = sum(age)/len(age)
print(average)

print(gender[-2])
#%%
# Data Storage With Lists
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list)
print(my_list[:])

my_list.append("pi")
print(my_list)

my_list.insert(1,"pi2")
print(my_list)

my_list.remove("pi")
my_list.remove("pi2")
my_list.remove("tau")
print(my_list)
print(len(my_list))

# View a certain range of items:
print(my_list[0:3])
      
 #%%     
 import pandas as pd

# Creating a DataFrame
data = {
    'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
}

#df = data frame
df = pd.DataFrame(data)

# Displaying the DataFrame
print(df)
      
# Basic statistics
print(df['age'].min())
print(df['age'].max())
print(df['age'].mean())

# Filtering data
print(df[df['age'] > 30])

# Slicing rows and columns
print(df[1:4])  # Select rows 1 to 3 and all columns

# Adding a new column
df['new_column'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(df)

# Removing a column
df.drop(columns=['new_column'], inplace=True)
print(df)