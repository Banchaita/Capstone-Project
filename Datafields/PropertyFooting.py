import pandas as pd

# Load data from Excel into a DataFrame
df = pd.read_excel('D:/DigiCrome/Project1/Datafields/PropertyClass.xlsx')

#Count the occurrences of each level of exterior material quality
exterior_quality_counts = df['PropertyFooting'].value_counts()

# Display the counts
print("PropertyFooting Counts:")
print(exterior_quality_counts)

#Extract unique PropertyFooting
unique_PropertyFooting = df['PropertyFooting'].unique()

# Count the number of unique PropertyFooting
num_unique_PropertyFooting = len(unique_PropertyFooting)

print("Number of unique PropertyFooting:", num_unique_PropertyFooting)
print("Unique PropertyFooting:", unique_PropertyFooting)

