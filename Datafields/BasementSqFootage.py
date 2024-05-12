# Step 1: Data Preprocessing
import pandas as pd
# Step 3: Model Selection and Training
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression  
from sklearn.metrics import mean_squared_error


# Load dataset
data = pd.read_excel("D:/DigiCrome/Project1/DatasetDescription/test.xlsx")


# Split data into train and test sets
X = data[['BasementCars']]  # Feature(s)
y = data['BasementCars']  # Target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Model Evaluation

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
# Create a DataFrame with predictions
predictions_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

# Export predictions to Excel
predictions_df.to_excel("predictions.xlsx", index=False)
