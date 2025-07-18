import pandas as pd

def load_csv_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        print(f"Data successfully read: {len(df)} rows from {path}")
        return df
    
    except FileNotFoundError:
        print(f"File not found: {path}")
        return pd.DataFrame()
    
    except Exception as e:
        print(f"Error loading the data: {e}")
        return pd.DataFrame()