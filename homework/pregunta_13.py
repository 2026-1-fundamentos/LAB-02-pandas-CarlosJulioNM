
import pandas as pd

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    # Cargamos los archivos
    df0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    df2 = pd.read_csv("files/input/tbl2.tsv", sep="\t")
    
    # Realizamos un merge (unión) usando 'c0' como clave
    merged_df = pd.merge(df0, df2, on="c0")
    
    # Agrupamos por 'c1', seleccionamos 'c5b' y sumamos
    resultado = merged_df.groupby("c1")["c5b"].sum()
    
    return resultado
