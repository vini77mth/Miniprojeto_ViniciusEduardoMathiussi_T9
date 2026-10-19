import pandas as pd

CAMINHO_CSV = "BASE Varejo.csv"

def carregar_dados():
    df = pd.read_csv(CAMINHO_CSV, dtype={"CL_FHL": str,})
    return df

if __name__ == "__main__":
    df = carregar_dados()
    print(df.head())