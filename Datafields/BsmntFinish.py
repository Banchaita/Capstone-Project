import pandas as pd

# Load data from Excel into a DataFrame
df = pd.read_excel('D:/DigiCrome/Project1/Datafields/PropertyClass.xlsx')

#Count the occurrences of each level of exterior material quality
exterior_quality_counts = df['BsmntFinish'].value_counts()

# Display the counts
print("BsmntFinish Counts:")
print(exterior_quality_counts)

#Extract unique BsmntFinish
unique_BsmntFinish = df['BsmntFinish'].unique()

# Count the number of unique BsmntFinish
num_unique_BsmntFinish = len(unique_BsmntFinish)

print("Number of unique BsmntFinish:", num_unique_BsmntFinish)
print("Unique BsmntFinish:", unique_BsmntFinish)

