import pandas as pd

# Load data from Excel into a DataFrame
df = pd.read_excel('D:/DigiCrome/Project1/Datafields/PropertyClass.xlsx')

# Count occurrences of each Masonry veneer type
veneer_counts = df['ExteriorCladdingType'].value_counts()

# Display the counts
print(veneer_counts)
