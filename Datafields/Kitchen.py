import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#  Load data from Excel into a DataFrame
data = pd.read_excel('D:/DigiCrome/Project1/DatasetDescription/test.xlsx')


# For example, handle missing values
data.fillna(data.mode().iloc[0], inplace=True)  # Filling missing values with mode

# Split data into features and target variable
X = data.drop('KitchenUpLev', axis=1)  # Features
y = data['KitchenUpLev']  # Target variable

#  Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#  Choose a machine learning model
model = RandomForestClassifier()

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


# Count the occurrences of each level of exterior material quality
exterior_quality_counts = data['KitchenUpLev'].value_counts()

# Display the counts
print("KitchenUpLev Counts:")
print(exterior_quality_counts)

#Extract unique BsmntFinish
unique_BsmntFinish = data['KitchenUpLev'].unique()

# Count the number of unique BsmntFinish
num_unique_KitchenUpLev = len(unique_BsmntFinish)

print("Number of unique KitchenUpLev:", num_unique_KitchenUpLev)
print("Unique KitchenUpLev:", unique_BsmntFinish)
