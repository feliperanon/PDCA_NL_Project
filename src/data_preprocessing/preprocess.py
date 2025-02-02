import pandas as pd

def preprocess_data(df):
    # Implementar a limpeza e preparação dos dados
    df.fillna('', inplace=True)
    return df