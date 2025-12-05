import pandas as pd
from src.utils import normalize_text, map_category

def run_etl(input_path, out_csv=None, sqlite_path=None):
    df = pd.read_csv(input_path)
    df['nome'] = df['nome'].apply(normalize_text).str.title()
    df['categoria_padrao'] = df['categoria'].apply(map_category)
    if out_csv:
        df.to_csv(out_csv, index=False)
    return df
