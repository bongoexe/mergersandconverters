import pandas as pd

# Read the first file
df1 = pd.read_excel("")

# Read the second file
df2 = pd.read_excel("")

# Select the columns to compare
column1 = ""  # replace with the actual column name in file1
column2 = ""  # replace with the actual column name in file2

# Convert all the words in the columns to lowercase and remove any leading/trailing spaces
df1[column1] = df1[column1].str.lower().str.strip()
df2[column2] = df2[column2].str.lower().str.strip()

# Find the common words between the two columns
common_words = set(df1[column1]).intersection(set(df2[column2]))

# Create a new dataframe to store the results
result = pd.DataFrame({"common_word": list(common_words)})

# Write the results to a new Excel file
result.to_excel("result.xlsx", index=False)
