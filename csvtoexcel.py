import pandas as pd

# Read the CSV file
df = pd.read_csv('/home/leo/Desktop/noclasspharma/databases/world list.csv')

# Write the DataFrame to an Excel file
df.to_excel("list1000th.xlsx", index=False)