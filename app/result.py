import pandas as pd

def get_prediction(rank, gender, caste, region):
    print("📥 Loading data...")
    df = pd.read_csv("tseamcet.csv")

    # Check column names
    print("✅ Columns in dataset:", df.columns.tolist())

    # Convert strings to lowercase for consistent filtering
    df['gender'] = df['gender'].str.lower()
    df['caste'] = df['caste'].str.lower()
    df['region'] = df['region'].str.lower()

    print("🔍 Filtering based on input criteria...")
    filtered_df = df[
        (df['gender'] == gender.lower()) &
        (df['caste'] == caste.lower()) &
        (df['region'] == region.lower()) &
        (df['rank'] >= rank)
    ]

    print(f"🧮 Records matching filters: {len(filtered_df)}")

    if filtered_df.empty:
        print("🚫 No matching colleges found for given inputs.")
        return pd.DataFrame()

    result = filtered_df.sort_values(by='rank').head(10)
    return result[['college', 'branch', 'rank', 'seat_category', 'fee']]
