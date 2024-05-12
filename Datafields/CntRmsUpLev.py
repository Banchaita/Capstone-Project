import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Step 1: Load data from Excel into a DataFrame
data = pd.read_excel('D:/DigiCrome/Project1/DatasetDescription/test.xlsx')

# Step 2: Preprocessing (if needed)
# For example, handling missing values
data.fillna(data.mean(), inplace=True)

# Step 3: Split data into features and target variable
X = data.drop('CntRmsUpLev', axis=1)  # Features
y = data['CntRmsUpLev']  # Target variable

# Step 4: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Choose a machine learning model
model = LinearRegression()

# Step 6: Train the model
model.fit(X_train, y_train)

# Step 7: Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# Step 8: Make predictions (if needed)
# You can use the trained model to make predictions on new data
