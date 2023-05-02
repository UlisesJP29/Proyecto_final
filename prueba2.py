import pandas as pd
import numpy as np

# Crear un DataFrame de ejemplo con algunos caracteres \xa0
df = pd.DataFrame({'A': ['\xa0', 'adiós', ' \xa0buenos días ', ' ', '']})

# Reemplazar los caracteres \xa0 con un espacio normal en todo el DataFrame
df = df.replace('\xa0', ' ', regex=True)
print(df)
# Reemplazar los espacios vacíos con valores nulos (NaN) en el DataFrame
df = df.replace(r'^\s*$', np.nan, regex=True)

# Eliminar las filas que tienen valores nulos en cualquier columna
df = df.dropna()

# Imprimir el DataFrame resultante
print(df)