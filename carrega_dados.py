import pandas as pd

IMPORTAR_CSV = "BASE Varejo.csv"
IMPORTAR_CSV2 = "dados_limpos.csv"

# Função para carregar os dados do arquivo CSV, tratar a coluna de data e definir os tipos de dados das colunas, transformando os números necessários em string
def carregar_dados():
    df = pd.read_csv(IMPORTAR_CSV, sep=";", dtype={"CL_FHL": str, "CL_EC": str, "CO_ID": str, "CL_ID": str, "PR_ID": str})
    df["DATA"] = pd.to_datetime(df["DATA"], format="%d/%m/%Y", errors="coerce")
    return df

def carregar_dados_limpos():
    return pd.read_csv(IMPORTAR_CSV2, sep=";", dtype={"CL_FHL": str, "CL_EC": str, "CO_ID": str, "CL_ID": str, "PR_ID": str})

if __name__ == "__main__":
    df = carregar_dados()
    print(df.head())


