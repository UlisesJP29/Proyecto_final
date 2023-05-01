import requests
from bs4 import BeautifulSoup
import pandas  as pd

#primeor vamos a seleccionar la URL del alumno
URL = "https://portafoliosfit.um.edu.mx/kimberlygarcia/auto-financiamiento/"
page = requests.get(URL)

#Ahora vamos a limpiar los datos extraifos con beautifullsoup
soup = BeautifulSoup(page.content, "html.parser")
#print(soup.prettify())
ls = []
find_p = soup.findAll('p')
for list in find_p:
    if list is None or list == '':
        break
    else: ls.append(list.text)
print(ls)
#find_p = list(filter(bool,find_p))
#print(find_p.text)

p_texts = [p.text for p in find_p]

df = pd.DataFrame(p_texts, columns=['Text'])
df.to_csv('file_name.csv',index=False,encoding='latin1')
