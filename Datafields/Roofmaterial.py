import pandas as pd

# Load the data from Excel into a DataFrame
data = pd.read_excel('D:/DigiCrome/Project1/Datafields/PropertyClass.xlsx')

# Count the number of unique roof materials
num_types = data['Roof1Material'].nunique()

print("Number of unique roof materials:", num_types)
