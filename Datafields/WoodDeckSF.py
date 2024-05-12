import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from Excel file
data = pd.read_excel('D:/DigiCrome/Project1/DatasetDescription/test.xlsx')

# Separate features and target variable
X = data.drop(columns=['WoodDeckSF'])  # Features
y = data['WoodDeckSF']  # Target variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Regressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the testing set
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print("Mean Squared Error:", mse)

# Plot actual vs predicted values using seaborn
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=predictions)
plt.xlabel('WoodDeckSF')
plt.ylabel('Predicted WoodDeckSF')
plt.title('WoodDeckSF')
plt.show()
