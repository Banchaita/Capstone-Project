import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from openpyxl import load_workbook

# Load the dataset from Excel file
data = pd.read_excel('D:/DigiCrome/Project1/Datafields/PropertyClass.xlsx')


# Separate features and target variable
X = data.drop(columns=['PavedDrive'])  # Features
y = data['PavedDrive']  # Target variable

# Convert categorical variable to numerical using one-hot encoding
X_encoded = pd.get_dummies(X)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Initialize the Logistic Regression model
model = LogisticRegression(max_iter=1000, multi_class='multinomial', random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the testing set
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_report(y_test, predictions))


