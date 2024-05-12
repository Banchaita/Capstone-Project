import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error



# Load the dataset
data = pd.read_csv("D:/DigiCrome/Project1/Property_data.csv")

# EDA (Explore the data)
print(data.head())
print(data.info())
print(data.describe())

# Check data types of all columns
print("Data types of all columns:")
print(data.dtypes)

# Load the new data set

dataOne = pd.read_excel("D:/DigiCrome/Project1/NewModified_dataset.xlsx")

X = dataOne.drop("PropertySize", axis=1)
y = dataOne["PropertySize"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Choose a model
model = RandomForestClassifier()

# Train the model
model.fit(X_train, y_train)

# Step 6: Model evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)








