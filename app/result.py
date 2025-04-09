import pandas as pd

def get_prediction(rank, gender, caste, region):
    df = pd.read_csv('tseamcet.csv')

    df_filtered = df[
        (df['gender'].str.lower() == gender.lower()) &
        (df['caste'].str.lower() == caste.lower()) &
        (df['region'].str.lower() == region.lower()) &
        (df['rank'] >= rank)
    ]

    if df_filtered.empty:
        return pd.DataFrame()

    top_colleges = df_filtered.sort_values(by='rank').head(10)
    return top_colleges[['college', 'branch', 'rank', 'seat_category', 'fee']]
