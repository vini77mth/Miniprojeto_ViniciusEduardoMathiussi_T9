import pandas as pd
from rich.panel import Panel
# Relaciona a propriedade console criada na página formatação com essa página
from rich import console
# Relaciona o código feita na etapa1 com essa página
from carrega_dados import carregar_dados_limpos

from formatacao import console, numero_br


def resumo_varejo(df):
    total_registros = len(df)
    total_clientes = df["CL_ID"].nunique()
    total_produtos = df["PR_ID"].nunique()
    total_compras = df["CO_ID"].nunique()
    media_filhos = df["CL_FHL"].mean()
    


    texto =(
         
       f"[bold] Total deRegistros: [/] { numero_br(total_registros)}\n"
       f"[bold] Total de Clientes: [/] { numero_br(total_clientes)}\n"
       f"[bold] Total de Produtos: [/] { numero_br(total_produtos)}\n"
       f"[bold] Total de Compras: [/] { numero_br(total_compras)}\n"
       f"[bold] Média de Filhos: [/] { numero_br(media_filhos)}\n"
)
    console.print(Panel(texto, title="Resumo Varejo", expand=False))

if __name__ == "__main__":
    df = carregar_dados_limpos()
    resumo_varejo(df)

