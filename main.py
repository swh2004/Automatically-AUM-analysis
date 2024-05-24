import pandas as pd
import openpyxl
from openpyxl import load_workbook

# Read the Excel files
df1 = pd.read_excel('1.xls', usecols='B')
df1.dropna()
df2 = pd.read_excel('2.xls', usecols='B')
df2.dropna()

# Concatenate the two DataFrames
combined_df = pd.concat([df1, df2], ignore_index=True)

# Remove duplicate
combined_df = combined_df.drop_duplicates()

# Set Title and remove unrelated content
combined_df = combined_df.iloc[2:]
combined_df.columns=['Fund Name']

# Write into files
combined_df.to_excel('auto.xlsx',sheet_name='Sheet1',index=False)
