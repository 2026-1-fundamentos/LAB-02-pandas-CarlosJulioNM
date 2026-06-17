import pandas as pd

def pregunta_11():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
         c0      c4
    0     0   b,f,g
    1     1   a,c,f
    2     2 a,c,e,f
    3     3     a,b
    ...
    37   37 a,c,e,f
    38   38     d,e
    39   39   a,d,f
    """
    # Cargamos el archivo tbl1.tsv
    df = pd.read_csv("files/input/tbl1.tsv", sep="\t")
    
    # 1. Ordenamos por c0 y c4 para que, al agrupar, las letras queden en orden
    df_ordenado = df.sort_values(["c0", "c4"])
    
    # 2. Agrupamos por c0, seleccionamos c4 y unimos con ','
    # .reset_index() se usa para devolver c0 a ser una columna normal
    resultado = df_ordenado.groupby("c0")["c4"].apply(lambda x: ",".join(x)).reset_index()
    
    return resultado
