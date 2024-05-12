import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load the dataset from an Excel file
file_path = 'D:/DigiCrome/Project1/Datafields/PropertyClass.xlsx'
print("Loading data from:", file_path)
df = pd.read_excel(file_path)

# Handle missing values if any
print("Original DataFrame size:", df.shape)
df.dropna(inplace=True)
print("DataFrame size after dropping missing values:", df.shape)

# Encode categorical variables
le = LabelEncoder()
df['PropertyZone'] = le.fit_transform(df['PropertyZone'])

# Split the data into features and target variable
X = df.drop(columns=['PropertyZone'])
y = df['PropertyZone']

# Check the size of your dataset
dataset_size = len(df)
if dataset_size == 0:
    print("Error: Dataset is empty. Please check your data.")
else:
    # Determine the appropriate test size
    test_size = min(0.2, 1 / dataset_size)  # Setting a maximum test size of 20% or 1 sample

    # Split data into training and testing sets with the adjusted test size
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

    # Initialize and train a Random Forest Classifier
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    # Make predictions on the testing set
    y_pred = clf.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    # Now you can use this trained model to predict 'PropertyZone' for new data
