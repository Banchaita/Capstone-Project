import pandas as pd

# Step 1: Load data from Excel into a DataFrame
df = pd.read_excel('D:/DigiCrome/Project1/Datafields/PropertyClass.xlsx')


# Count occurrences of each present condition
condition_counts = df['ExterCond'].value_counts()

# Display the counts
print("Occurrences of each present condition of the material on the exterior:")
print(condition_counts)


#Extract unique ExterCond
unique_ExterCond = df['ExterCond'].unique()

# Count the number of unique ExterCond
num_unique_ExterCond = len(unique_ExterCond)

print("Number of unique ExterCond:", num_unique_ExterCond)
print("Unique ExterCond:", unique_ExterCond)
