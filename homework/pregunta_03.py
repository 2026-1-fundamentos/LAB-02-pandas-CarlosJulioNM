import pandas as pd


def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64

    """
    # Cargamos el DataFrame
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    
    # Contamos los valores de la columna 'c1' y los ordenamos alfabéticamente por el índice
    conteo = df["c1"].value_counts().sort_index()
    
    return conteo
    
