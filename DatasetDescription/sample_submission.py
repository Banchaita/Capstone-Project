
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

#  Load the data
train_df = pd.read_excel("D:/DigiCrome/Project1/train.xlsx")
test_df = pd.read_excel("D:/DigiCrome/Project1/test.xlsx")

# Step 3: Data Preprocessing
# Handle missing values for numeric columns
numeric_cols = train_df.select_dtypes(include=['number']).columns
train_df[numeric_cols] = train_df[numeric_cols].fillna(train_df[numeric_cols].mean())
test_df[numeric_cols] = test_df[numeric_cols].fillna(test_df[numeric_cols].mean())

# Encode categorical variables (if any)

# Split features and target variable
X = train_df.drop(columns=['PropPrice'])
y = train_df['PropPrice']

#  Model Building
# Split data into train and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Define and train the model
model = make_pipeline(StandardScaler(), LinearRegression())
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_val)
mse = mean_squared_error(y_val, y_pred)
print("Mean Squared Error:", mse)

#  Submission Preparation
# Prepare submission file
submission_preds = model.predict(test_df.drop(columns=['PropPrice']))  # Exclude 'PropPrice' column

# Create a submission DataFrame
submission_df = pd.DataFrame({
    'PropertyID': test_df['PropertyID'],  # Assuming 'Id' column exists in test_df
    'PropPrice': submission_preds
})

# Save to CSV
submission_df.to_csv('submission.csv', index=False)

