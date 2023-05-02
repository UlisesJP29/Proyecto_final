import requests
from bs4 import BeautifulSoup
import pandas  as pd
import numpy as np

#--------primero vamos a seleccionar la URL del alumno
#URL = "https://portafoliosfit.um.edu.mx/kimberlygarcia/relaciones-interpersonales/"
URL = "https://portafoliosfit.um.edu.mx/geovannidzul/integracion/"
page = requests.get(URL)

#-------- segundo  Ahora vamos a limpiar los datos extraifos con beautifullsoup
soup = BeautifulSoup(page.content, "html.parser")
#print(soup.prettify())

ls = []
find_p = soup.findAll('p')#se crea una lista para todos los datos de una etiqueta "p"
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

p_texts = [p.text for p in find_p] # creanmos una lista con la datos extraidos de find_p (solo los textos)

df = pd.DataFrame(p_texts, columns=['Text']) # creamos una tabla con los comentarios
df = df.replace('\xa0', ' ', regex=True)
#print(df)
# Reemplazar los espacios vacíos con valores nulos (NaN) en el DataFrame
df = df.replace(r'^\s*$', np.nan, regex=True)
# Eliminar las filas que tienen valores nulos en cualquier columna
df = df.dropna()
print(df)
# Iterar en el DataFrame y buscar una cadena específica en la columna "A"
mask = df['Text'].str.contains('Reflex')
# Filter the dataframe based on the mask
filtered_df = df[mask]
filtered_df.dropna()
print(filtered_df)

filtered_df.to_csv('comentarios.csv',index=False,encoding='cp1252')# guarda en un csv todos los comentarios

#print(df.head(10))
#---------tercero vamos a revisar como analizar el sentimiento de los comentarios guardados
from textblob import TextBlob
import csv, re, time, string
from googletrans import Translator

def clean_text(text):
  text = re.sub(r'^RT[\s]+', '', text)
  text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)
  text = re.sub(r'#', '', text)
  text = re.sub(r'@[A-Za-z0-9]+', '', text)
  return text

filtered_df['clean_text'] = filtered_df['Text'].apply(clean_text)
filtered_df.dropna()
print(filtered_df['clean_text'])

def get_polarity(text):
  print(text)
  analysis = TextBlob(text)
  if text != '':
    result = analysis.translate(from_lang = 'es', to = 'en').sentiment.polarity
    time.sleep(5)
    return result

filtered_df['polarity'] = filtered_df['clean_text'].apply(get_polarity)
print(filtered_df['polarity'].head(3))

filtered_df.to_csv('comentarios2.csv',index=False,encoding='cp1252')# guarda en un csv todos los comentarios
