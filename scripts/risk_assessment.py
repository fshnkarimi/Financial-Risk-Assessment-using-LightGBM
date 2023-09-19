# scripts/risk_assessment.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load the mock financial data
data = pd.read_csv('data/financial_data.csv')

# Split the data into features and target
X = data[['Income', 'Expenses']]
y = data['Risk Preference']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)

# Print the model's accuracy
print(f'Model Accuracy: {accuracy}')

# Save the trained model for later use in the FastAPI application
joblib.dump(model, 'models/risk_assessment_model.joblib')
