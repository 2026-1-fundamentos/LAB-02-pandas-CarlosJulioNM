import pandas as pd

def pregunta_07():
    """
    Calcule la suma de la `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: c2, dtype: int64
    """
    # Cargamos el DataFrame
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    
    # Agrupamos por 'c1', seleccionamos 'c2' y calculamos la suma (sum)
    suma_total = df.groupby("c1")["c2"].sum()
    
    return suma_total
