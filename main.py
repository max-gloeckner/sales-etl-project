from etl.extract import load_csv_data

df = load_csv_data("data/raw/sales_data.csv")
print(df.head())