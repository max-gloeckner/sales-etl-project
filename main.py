from etl.extract import load_csv_data
from etl.transform import transform_csv_data

df = load_csv_data("data/raw/sales_data.csv")
print(df.head())

df = transform_csv_data(df)

print(df.head())