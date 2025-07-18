import pandas as pd

def transform_csv_data(df: pd.DataFrame) -> pd.DataFrame:
    df_clean = df.dropna(subset=["Customer", "Product", "Amount", "Price"])

    df_clean = df_clean.drop_duplicates()

    df_clean["Total"] = df_clean["Amount"].astype(float) * df_clean["Price"].astype(float)

    return df_clean