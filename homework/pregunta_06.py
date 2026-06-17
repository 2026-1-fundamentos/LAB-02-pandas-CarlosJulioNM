import pandas as pd

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.tsv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    # Cargamos el archivo tbl1.tsv
    df = pd.read_csv("files/input/tbl1.tsv", sep="\t")
    
    # Obtenemos los valores únicos de 'c4'
    unicos = df["c4"].unique()
    
    # Convertimos a mayúsculas, quitamos duplicados (si los hubiera) y ordenamos
    # sorted() maneja la conversión a lista y el orden alfabético
    resultado = sorted([valor.upper() for valor in unicos])
    
    return resultado
