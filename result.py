import pandas as pd

def get_prediction(rank, gender, caste, region):
    print("📥 Loading data...")
    df = pd.read_csv("tseamcet.csv")

    print("✅ Columns in dataset:", list(df.columns))

    print("🔍 Filtering based on input criteria...")
    filtered_df = df[
        (df['gender'] == gender) &
        (df['caste'] == caste) &
        (df['region'] == region) &
        (df['rank'] >= rank)
    ]

    print(f"🧮 Records matching filters: {len(filtered_df)}")

    if filtered_df.empty:
        print("🚫 No matching colleges found for given inputs.")
        return pd.DataFrame()

    filtered_df = filtered_df.sort_values(by='rank').head(10)
    return filtered_df[['college', 'branch', 'rank', 'seat_category', 'fee']]
