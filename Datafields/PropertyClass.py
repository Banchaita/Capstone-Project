import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset from Excel file
data = pd.read_excel('D:/DigiCrome/Project1/Datafields/NewModified_dataset.xlsx', sheet_name='Sheet1')

#  Data Preprocessing - Handle missing values
data.dropna(inplace=True)  # Drop rows with missing values

# Assuming 'PropertyClass' is the target variable and other columns are features
X = data.drop('PropertyClass', axis=1)
y = data['PropertyClass']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

#  Model Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

