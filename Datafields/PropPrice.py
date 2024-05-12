import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform
import joblib
import matplotlib.pyplot as plt

# Load the dataset from Excel file
data = pd.read_excel("D:/DigiCrome/Project1/Datafields/NewModified_dataset.xlsx")

# Data preprocessing
# Handle missing values
data.dropna(inplace=True)

# Feature selection (if needed)
X = data.drop("PropPrice", axis=1)  # Features
y = data["PropPrice"]  # Target variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model training
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Model evaluation
y_pred = model.predict(X_test_scaled)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Save the best model
joblib.dump(model, "property_price_prediction_model.pkl")

# Plotting
# Assuming X_test is a single feature, you can plot its PDF
x_range = np.linspace(X_test.min(), X_test.max(), 100)  # Generate 100 points within the range of X_test
pdf_best = uniform.pdf(x_range)  # Compute the PDF for the best model
plt.plot(x_range, pdf_best, label='Best Model PDF')
plt.xlabel('Feature Value')
plt.ylabel('Probability Density')
plt.title('Probability Density Function of Best Model')
plt.legend()
plt.show()
