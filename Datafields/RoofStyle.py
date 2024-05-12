import pandas as pd

#  Load data from Excel into a DataFrame
df = pd.read_excel('D:/DigiCrome/Project1/Datafields/PropertyClass.xlsx')

#Extract unique roof styles
unique_roof_styles = df['RoofStyle'].unique()

# Count the number of unique roof styles
num_unique_roof_styles = len(unique_roof_styles)

print("Number of unique roof styles:", num_unique_roof_styles)
print("Unique roof styles:", unique_roof_styles)
