import pandas as pd

IMPORTAR_CSV = "BASE Varejo.csv"

def carregar_dados():
    df = pd.read_csv(IMPORTAR_CSV, dtype={"CL_FHL": str,})
    return df

if __name__ == "__main__":
    df = carregar_dados()
    print(df.head())