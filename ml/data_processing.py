import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
import os

# Step 1: Load the dataset
df = pd.read_csv("dataset/eamcet_data.csv")

# Step 2: Drop missing values
df.dropna(inplace=True)

# Step 3: Clean 'Closing Rank' column
df['Closing Rank'] = df['Closing Rank'].astype(str).str.replace(",", "")
df['Closing Rank'] = df['Closing Rank'].astype(int)

# Step 4: Strip whitespace from string columns
text_columns = ['College Name', 'Branch', 'Category', 'Gender', 'Region']
for col in text_columns:
    df[col] = df[col].str.strip()

# Step 5: Add a dummy Target column
user_rank = 25000  # You can change this to simulate different predictions
df['Target'] = df['Closing Rank'].apply(lambda x: 1 if user_rank <= x else 0)

# Step 6: Encode categorical columns
label_encoders = {}
for col in text_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Step 7: Save processed data
os.makedirs("dataset", exist_ok=True)
df.to_csv("dataset/processed_data.csv", index=False)
print("Processed data saved to dataset/processed_data.csv")

# Step 8: Save encoders
os.makedirs("model", exist_ok=True)
joblib.dump(label_encoders, "model/encoders.pkl")
print("Encoders saved to model/encoders.pkl")
