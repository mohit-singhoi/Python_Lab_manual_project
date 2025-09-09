# Q.7 Pandas for data manipulation (Load a dataset in CSV files, basic analysis).

import pandas as pd
#load 
df = pd.read_csv("DataSets/Student.csv")
print(df)
#Basic data Analysis
print(df.head(2)) #first 2 rows
print(df.tail()) #last 5 rows
# print(df.info()) #info about the data 
print(df.columns) #columns
# print(df.index) #index
print(df.shape) #shape of the data
# print(df.dtypes) #data types

print(df.describe()) #statistical summary  

#print(df["NAME"])
#print(df["MARKS"])

#print(df.loc[1])       # By label/index
#print(df.iloc[1])      # By position

#Filter rows (e.g., Marks > 80):
# high_scores = df[df["MARKS"] > 90]
# print(high_scores)


# Adding and Modifying Columns
# df["TOTAL"] = df["MARKS"] + 2
# df["NAME"] = df["NAME"].str.lower()  # Convert names to uppercase
# print(df)

# Add a Grade column
df["Grade"] = ["A", "B+", "B", "A+"]
print(df)

# # Modify Age column
# df["Age"] = df["Age"] + 1
