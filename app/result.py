import pandas as pd

def get_prediction(rank, gender, caste, region):
    print("📥 Loading data...")
    df = pd.read_csv('tseamcet.csv')

    print("✅ Columns in dataset:", list(df.columns))

    # Normalize string columns
    df['gender'] = df['gender'].str.strip().str.lower()
    df['caste'] = df['caste'].str.strip().str.lower()
    df['region'] = df['region'].str.strip().str.lower()

    gender = gender.strip().lower()
    caste = caste.strip().lower()
    region = region.strip().lower()

    print("🔍 Filtering based on input criteria...")
    filtered = df[
        (df['gender'] == gender) &
        (df['caste'] == caste) &
        (df['region'] == region) &
        (df['rank'] >= rank)
    ]

    print(f"🧮 Records matching filters: {len(filtered)}")
    if filtered.empty:
        print("🚫 No matching colleges found for given inputs.")
        return pd.DataFrame()

    top = filtered.sort_values(by='rank').head(10)
    print("✅ Top 10 results selected.")

    return top[['college', 'branch', 'rank', 'seat_category', 'fee']]
