import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Load processed data
df = pd.read_csv("dataset/processed_data.csv")

# ✅ Replace '\n' with space in Category_Gender
df['Category_Gender'] = df['Category\nGender'].str.replace('\n', ' ')

# ✅ Encode Category_Gender
category_gender_encoder = LabelEncoder()
df['Category_Gender_Encoded'] = category_gender_encoder.fit_transform(df['Category_Gender'])

# ✅ Features and label
X = df[['Category_Gender_Encoded', 'Closing Rank']]  # Ensure correct column names
y = df['Target']  # Example: "Institute - Branch"

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Save model and encoder
os.makedirs("model", exist_ok=True)
joblib.dump(clf, "model/classifier.pkl")
joblib.dump({'Category_Gender': category_gender_encoder}, "model/encoders.pkl")

# Accuracy check (optional)
print("✅ Training Accuracy:", clf.score(X_train, y_train))
print("✅ Testing Accuracy:", clf.score(X_test, y_test))
print("✅ Model and encoder saved in 'model/'")
