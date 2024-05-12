# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_excel("D:/DigiCrome/Project1/NewModified_dataset.xlsx")

# Data Preprocessing (Optional)
# Handle missing values
data.dropna(subset=['BasementYrBlt'], inplace=True)  # Drop rows with missing values in 'BasementYrBlt' column



# Model Selection (Optional)
# Choose appropriate machine learning models
modelOne = RandomForestRegressor()

# Step 7: Model Training
X = data.drop(columns=['BasementSqFootage'])
y = data['BasementYrBlt']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
modelOne.fit(X_train, y_train)

# Step 8: Model Evaluation
y_pred = modelOne.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)


# # Show the data visually
data.plot(x="PropertySize", y="YearRemodAdd", kind="scatter")
plt.xlabel("Property Size")
plt.ylabel("Year Remodeled")
plt.title("Relationship between Property Size and Year Remodeled")
plt.show()
