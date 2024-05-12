import pandas as pd

df = pd.read_excel('D:/DigiCrome/Project1/Datafields/PropertyClass.xlsx')

#  Identify unique values
unique_coverings = df['Roof2Material'].unique()

# Count the number of unique types
num_unique_types = len(unique_coverings)

# Display or store the result
print("Number of unique exterior covering types:", num_unique_types)
print("Unique covering types:", unique_coverings)
