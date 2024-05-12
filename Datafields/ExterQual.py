import pandas as pd

# Load data from Excel into a DataFrame
df = pd.read_excel('D:/DigiCrome/Project1/Datafields/PropertyClass.xlsx')

#Count the occurrences of each level of exterior material quality
exterior_quality_counts = df['ExterQual'].value_counts()

# Display the counts
print("Exterior Material Quality Counts:")
print(exterior_quality_counts)

#Extract unique ExterQual
unique_roof_styles = df['ExterQual'].unique()

# Count the number of unique ExterQual
num_unique_roof_styles = len(unique_roof_styles)

print("Number of unique ExterQual:", num_unique_roof_styles)
print("Unique ExterQual:", unique_roof_styles)

