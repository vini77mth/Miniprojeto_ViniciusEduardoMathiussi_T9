import pandas as pd


def numero_br (valor, casas_decimais=0):
    texto = f"{valor:,.{casas_decimais}f}"
    texto =texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return texto