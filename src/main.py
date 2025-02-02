# G:\Meu Drive\Programação\PDCA_NL\PDCA_NL_Project\src\main.py

import pandas as pd

def load_data(file_path):
    return pd.read_excel(file_path)

def main():
    data_path = r'G:\Meu Drive\Programação\PDCA_NL\1_Excel\PDCA_Logic_Demandas.xlsx'
    df = load_data(data_path)
    print(df.head())

if __name__ == "__main__":
    main()