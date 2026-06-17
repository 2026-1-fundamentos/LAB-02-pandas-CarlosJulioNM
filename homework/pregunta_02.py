import pandas as pd


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    # Cargamos el archivo de la misma ruta que el ejercicio anterior
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")

    # .shape[1] extrae la cantidad de columnas del DataFrame
    cantidad_columnas = df.shape[1]

    return cantidad_columnas
    
