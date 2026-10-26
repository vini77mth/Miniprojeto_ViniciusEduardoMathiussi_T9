import pandas as pd

IMPORTAR_CSV = "BASE Varejo.csv"

def carregar_dados():
    df = pd.read_csv(IMPORTAR_CSV, sep=";", dtype={"CL_FHL": str, "CL_EC": str, "CO_ID": str, "CL_ID": str, "PR_ID": str})
    df["DATA"] = pd.to_datetime(df["DATA"], format="%d/%m/%Y", errors="coerce")
    return df


if __name__ == "__main__":
    df = carregar_dados()
    print(df.head())