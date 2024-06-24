from pathlib import Path
import pandas as pd

# Ruta de la carpeta donde se encuentran los archivos
ruta_carpeta = Path(r"C:\Users\luisr\Downloads\2021-2") # Path(r"C:\Users\luisr\Downloads\Tasas")

# Nombre del archivo consolidado
nombre_archivo_consolidado = "XCONSOLIDADO.xlsx"

# Lista para almacenar los datos
datos_consolidados = []

# Recorrer los archivos de la carpeta
for archivo in ruta_carpeta.iterdir():

    # Abrir el archivo de Excel
    df = pd.read_excel(archivo)

    # Extraer las columnas A y B
    columnas_c_ac = df.iloc[:,0:30]  # Selecciona todas las filas (:), y las columnas hasta la 2 (0 y 1) columnas_c_ac = df.iloc[:,[2,12]]

    # Agregar los datos al DataFrame consolidado
    datos_consolidados.append(columnas_c_ac)

# Crear un DataFrame con los datos consolidados
df_consolidado = pd.concat(datos_consolidados)

# Guardar el archivo consolidado
df_consolidado.to_excel(ruta_carpeta / nombre_archivo_consolidado, index=False)

print("¡Archivo consolidado creado exitosamente!")



