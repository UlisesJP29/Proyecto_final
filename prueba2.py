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

ls = []
#find_p = soup.findAll('p')#se crea una lista para todos los datos de una etiqueta "p"
for list in find_p: #se quiere imprimir solamente los datos de find_p
    texto_con_espacio_sin_romper = list.text
    texto_con_espacio_normal = texto_con_espacio_sin_romper.replace('\xa0', ' ')
    if texto_con_espacio_sin_romper is None or list == ' ' or list == '\xa0':
        break
    else: 
      # print(texto_con_espacio_normal)
       ls.append(texto_con_espacio_normal)
#print(ls)# imprimer la lista de todos los parrafos de la pagina web
#find_p = list(filter(bool,find_p))
#print(find_p.text)