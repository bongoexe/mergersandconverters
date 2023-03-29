import os
import glob
import pandas as pd
import codecs

# Set the directory where the CSV files are located
directory_path = ''

# Set the file extension of the CSV files
file_extension = '.csv'

# Get a list of all CSV files in the directory
csv_files = glob.glob(os.path.join(directory_path, '*' + file_extension))

# Initialize an empty list to store all dataframes
dfs = []

# Loop through each CSV file and append its dataframe to the list of dataframes
for file in csv_files:
    with codecs.open(file, 'r', encoding='utf-8', errors='ignore') as f:
        df = pd.read_csv(f)
        dfs.append(df)

# Concatenate all dataframes into a single one
merged_df = pd.concat(dfs, ignore_index=True)

# Export the merged dataframe to a new CSV file
merged_df.to_csv(os.path.join(directory_path, 'merged.csv'), index=False, encoding='utf-8-sig')


