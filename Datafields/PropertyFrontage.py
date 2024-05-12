import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from openpyxl import load_workbook
from sklearn.impute import SimpleImputer

# Load the dataset from Excel file
file_path = 'D:/DigiCrome/Project1/Datafields/NewModified_dataset.xlsx'
df = pd.read_excel(file_path)

# Handle missing values in target variable y
imputer = SimpleImputer(strategy='mean')
df['PropertyFrontage'] = imputer.fit_transform(df['PropertyFrontage'].values.reshape(-1, 1))

# Separate features and target variable
X = df.drop(columns=['PropertyFrontage'])  # Features
y = df['PropertyFrontage']  # Target variable

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

# Save predictions to Excel file
predictions_df = pd.DataFrame({'Predicted_PropertyFrontage': predictions})
writer = pd.ExcelWriter(file_path, engine='openpyxl')
writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
predictions_df.to_excel(writer, sheet_name='Predictions', index=False)
writer.save()

