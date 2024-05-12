import pandas as pd

# Read the Excel file into a pandas DataFrame
df = pd.read_excel("D:/DigiCrome/Project1/NewModified_dataset.xlsx")

# Specify the column names you want to process
columns_to_process = ['PropertySize', 'YearBuilt', 'YearRemodAdd','BsmntFinSty1','BsmtUnfSF','BsmntSqFtage','1stFlrSF','2ndFlrSF','GrLivArea','BasementYrBlt','SaleYr','PropPrice']

# Loop through each column name and remove commas
for column_name in columns_to_process:
    # Convert the column to string type
    df[column_name] = df[column_name].astype(str)
    # Remove commas from the values in the specified column
    df[column_name] = df[column_name].str.replace(',', '')

# Write the modified DataFrame back to an Excel file
df.to_excel("Final.xlsx", index=False)

