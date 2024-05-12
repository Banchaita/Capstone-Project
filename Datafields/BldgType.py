import pandas as pd

# Step 1: Load data from Excel into a DataFrame
df = pd.read_excel('D:/DigiCrome/Project1/Datafields/PropertyClass.xlsx')

# Step 2: Extract unique roof styles
unique_Bldg_Type = df['BldgType'].unique()

# Step 3: Count the number of unique roof styles
num_unique_Bldg_Type = len(unique_Bldg_Type)

print("Number of unique Bldg_Type:", num_unique_Bldg_Type)
print("Unique ldg_Type:", unique_Bldg_Type)