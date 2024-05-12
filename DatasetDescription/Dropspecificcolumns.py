import pandas as pd

# Load the dataset
data = pd.read_csv("D:/DigiCrome/Project1/Property_data.csv")

# Step 2: Drop specific columns
columns_to_drop = ['PropertyZone', 'SaleType', 'SaleCondn','Street','Alley','PropertyShape','Elevation','Amenities','Orientation','Grade','Neighborhood','Condition1','Condition2','BldgType','PropertyStyle','RoofStyle','RoofMatl','Roof1Material','Roof2Material','ExteriorCladdingType','ExterQual','BsmntMaintenance','BsmntFinish','ExterCond','BsmntFinRat1','BsmntFinQual1','Heating','HeatingEfficiency','CentralAir','Electrical','KitchenQual','Functional','QualFireplace','BasementType','BasementFinish','AddFeatures','BoundaryFeatures','PavedDrive','BasementQual','PropertyFooting','BsmntVisibility','BasementCond','PoolQC']  # List the column names you want to drop
data = data.drop(columns_to_drop, axis=1)

# Step 3: Write the modified DataFrame to a new Excel file
data.to_excel("NewModified_dataset.xlsx", index=False)