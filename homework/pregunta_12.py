import pandas as pd

def pregunta_12():
    """
    Construya una tabla que contenga `c0` y una lista separada por ','
    de los valores de la columna `c5a`  y `c5b` (unidos por ':') de la
    tabla `tbl2.tsv`.

    Rta/
         c0                           c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1        aaa:3,ccc:2,ddd:0,hhh:9
    2     2        ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                      eee:0,fff:2,hhh:6
    38   38                      eee:0,fff:9,iii:2
    39   39                      ggg:3,hhh:8,jjj:5
    """
    # Cargamos el archivo tbl2.tsv
    df = pd.read_csv("files/input/tbl2.tsv", sep="\t")
    
    # 1. Creamos la columna combinada 'c5' usando c5a y c5b
    df["c5"] = df["c5a"] + ":" + df["c5b"].astype(str)
    
    # 2. Ordenamos por c0 y c5a para que al agrupar las claves queden ordenadas
    df_ordenado = df.sort_values(["c0", "c5a"])
    
    # 3. Agrupamos por c0 y unimos los valores de 'c5' con ','
    resultado = df_ordenado.groupby("c0")["c5"].apply(lambda x: ",".join(x)).reset_index()
    
    return resultado
