#Q.8 Handle missing values

import pandas as pd

# Sample data with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, None, 30, None],
    'City': ['New York', 'Los Angeles', None, 'Chicago']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)



#1. Dealing with Missing Values
#Deteceting Missing Values
print("\nCheck where values are missing:")
print(df.isnull())


#2.Removing Missing Values
#Remove rows with any missing value:
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped)


#3. Filling Missing Values
#Fill missing values with a specific value:
df_filled = df.fillna({
    'Age': df['Age'].mean(),  # Fill Age with mean
    'City': 'Unknown'         # Fill City with 'Unknown'
})
print("\nDataFrame after filling missing values:")
print(df_filled)

