import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Step 1: Load data from Excel into a DataFrame
df = pd.read_excel('D:/DigiCrome/Project1/Datafields/PropertyClass.xlsx')

# Step 2: Preprocessing
# Encode categorical variable "Condition2" into numerical values
label_encoder = LabelEncoder()
df['Condition2_encoded'] = label_encoder.fit_transform(df['Condition2'])

# Step 3: Split data into features and target variable
X = df.drop(['Condition2', 'Condition2_encoded'], axis=1)  # Features
y = df['Condition2_encoded']  # Target variable

# Step 4: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Choose a machine learning model
model = RandomForestClassifier()

# Step 6: Train the model
model.fit(X_train, y_train)

# Step 7: Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Step 8: Make predictions (if needed)
# You can use the trained model to make predictions on new data
