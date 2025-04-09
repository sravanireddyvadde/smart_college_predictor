import pandas as pd
import os
import pickle
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv('dataset/eamcet_data.csv')

# Step 1: Keep required columns
basic_cols = ['Institute Name', 'Place', 'College Type', 'Branch Name', 'Tuition Fee', 'Affiliated To']
rank_cols = [col for col in df.columns if 'BOYS' in col or 'GIRLS' in col or 'EWS' in col]

# Step 2: Melt the DataFrame (convert wide to long format)
df_melted = df.melt(id_vars=basic_cols, value_vars=rank_cols,
                    var_name='Category_Gender', value_name='Closing Rank')

# Step 3: Clean the 'Closing Rank' column
df_melted['Closing Rank'] = df_melted['Closing Rank'].astype(str).str.replace(",", "")
df_melted['Closing Rank'] = df_melted['Closing Rank'].str.extract(r'(\d+)')  # Extract digits
df_melted.dropna(subset=['Closing Rank'], inplace=True)
df_melted['Closing Rank'] = df_melted['Closing Rank'].astype(int)

# Step 4: Create target = college + branch name
df_melted['Target'] = df_melted['Institute Name'] + " - " + df_melted['Branch Name']

# Step 5: Encode categorical columns
label_encoders = {}
for col in ['Institute Name', 'Place', 'College Type', 'Branch Name', 'Affiliated To', 'Category_Gender', 'Target']:
    le = LabelEncoder()
    df_melted[col] = le.fit_transform(df_melted[col])
    label_encoders[col] = le

# Step 6: Save processed data
os.makedirs('dataset', exist_ok=True)
df_melted.to_csv('dataset/processed_data.csv', index=False)
print("✅ Processed data saved to dataset/processed_data.csv")

# Step 7: Save encoders
os.makedirs('model', exist_ok=True)
with open('model/encoders.pkl', 'wb') as f:
    pickle.dump(label_encoders, f)
print("✅ Encoders saved to model/encoders.pkl")
