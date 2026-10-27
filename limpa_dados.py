
import pandas as pd

from carrega_dados import carregar_dados

EXPORTAR_CSV = "dados_limpos.csv"


def remover_nulos(df, colunas=None):
    return df.dropna(subset=colunas)


def preencher_nulos(df, colunas=None, valor=0):
    df = df.copy()

    if colunas is None:
        return df.fillna(value=valor)

    df[colunas] = df[colunas].fillna(value=valor)
    return df


def remover_duplicados(df):
    return df.drop_duplicates()


if __name__ == "__main__":
    df = carregar_dados()

    # Remove colunas completamente vazias
    df = df.dropna(axis=1, how="all")

    print("Valores nulos antes da limpeza:")
    print(df.isnull().sum())

    print("\nPrimeiras linhas:")
    print(df.head())

    colunas_obrigatorias = [
        "DATA",
        "CO_ID",
        "CL_ID",
        "CL_GENERO",
        "CL_EC",
        "CL_FHL",
        "CL_SEG",
        "PR_ID",
        "PR_CAT",
        "PR_NOME"
    ]

    for coluna in colunas_obrigatorias:
        df = remover_nulos(df, colunas=[coluna])

        print(f"\nApós remover nulos na coluna {coluna}:")
        print(df.isnull().sum())

    # Remove registros duplicados
    quantidade_inicial = len(df)
    df = remover_duplicados(df)
    duplicados_removidos = quantidade_inicial - len(df)

    print(f"\nRegistros duplicados removidos: {duplicados_removidos}")
    print(f"Total de registros restantes: {len(df)}")

df.to_csv(
    df.to_csv(
        EXPORTAR_CSV,
        sep=";",
        index=False,
        encoding="utf-8-sig",
        date_format="%d/%m/%Y",
    )
)