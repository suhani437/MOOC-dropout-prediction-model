# Step 1: Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
import pickle

# Step 2: Load Dataset
df = pd.read_csv("mooc.csv")

# Step 3: Fill missing values with 0
df = df.fillna(0)

# Step 4: Feature Engineering
# Total activity across all types
activity_cols = ['navigate','access','page_close','problem','video','discussion','wiki','server','browser']
df['total_activity'] = df[activity_cols].sum(axis=1)

# Engagement timing features
df['early_mid_late'] = df['early events'] + df['mid events'] + df['late events']

# Days active
df['active_days'] = df['study days']

# Duration of activity
df['activity_duration'] = df['lastlog-firstlog']

# Step 5: Create target variable using multiple factors
def compute_risk(row):
    risk_count = 0
    if row['total_activity'] < 50:
        risk_count += 1
    if row['active_days'] < 5:
        risk_count += 1
    if row['video'] < 3:
        risk_count += 1
    if row['problem'] < 3:
        risk_count += 1
    # If 2 or more conditions are true → At Risk
    return 1 if risk_count >= 2 else 0

df['at_risk'] = df.apply(compute_risk, axis=1)

# Step 6: Select features and target
feature_cols = ['total_activity', 'early_mid_late', 'active_days', 'activity_duration', 'video', 'discussion', 'problem']
X = df[feature_cols]
y = df['at_risk']

# Step 7: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training set size:", X_train.shape)
print("Testing set size:", X_test.shape)

# Step 8: Train the Random Forest Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 9: Test the model
y_pred = model.predict(X_test)

# Step 10: Evaluate the model
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Step 11: Save the trained model for real-time predictions
pickle.dump(model, open('mooc_risk_model.pkl', 'wb'))

print("\nModel saved as 'mooc_risk_model.pkl'. You can now use it for predicting new students.")
