import pandas as pd

def pregunta_10():
    """
    Construya una tabla que contenga `c1` y una lista separada por ':' de los
    valores de la columna `c2` para el archivo `tbl0.tsv`.

    Rta/
                                c2
    c1
    A              1:1:2:3:6:7:8:9
    B              1:3:4:5:6:8:9
    C                  0:5:6:7:9
    D              1:2:3:5:5:7
    E    1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    # Cargamos el DataFrame
    df = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    
    # 1. Aseguramos que c2 sea string para poder concatenar
    # 2. Ordenamos el dataframe por c1 y c2 para que al unir queden ordenados
    df_ordenado = df.sort_values(["c1", "c2"])
    
    # 3. Agrupamos por c1, seleccionamos c2, convertimos a string y unimos con ':'
    resultado = df_ordenado.groupby("c1")["c2"].apply(lambda x: ":".join(x.astype(str)))
    
    # 4. Convertimos a DataFrame para que coincida con el formato de salida
    resultado = resultado.to_frame()
    
    return resultado
