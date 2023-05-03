import pandas as pd

# Crear el DataFrame
df = pd.DataFrame({'Nombre': ['Juan', 'María', 'Pedro'], 'Edad': [25, 30, 35]})

# Método append()
df = df.append({'Nombre': 'Lucía', 'Edad': 28}, ignore_index=True)
print(df)
# Propiedad loc[]
df.loc[len(df)] = ['Lucía', 28]
