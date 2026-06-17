import pandas as pd


def pregunta_04():
    """
    Calcule el promedio de `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: c2, dtype: float64
    """
    # Cargamos el DataFrame
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    
    # Agrupamos por 'c1', seleccionamos 'c2' y calculamos el promedio (mean)
    promedio = df.groupby("c1")["c2"].mean()
    
    return promedio
