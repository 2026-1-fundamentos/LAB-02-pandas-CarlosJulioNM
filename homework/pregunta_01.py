import pandas as pd

def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    # Cargamos el archivo usando pandas, indicando que están separados por tabulaciones (\t)
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    
    # len() nos devuelve la cantidad de filas del DataFrame
    cantidad_filas = len(df)
    
    return cantidad_filas
