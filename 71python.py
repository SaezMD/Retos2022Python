#71 Web scraping
"""
 * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
 * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
 *
 * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
 * del día 8. Mostrando hora e información de cada uno.
 * Ejemplo: "16:00 | Bienvenida"
 *
 * Se permite utilizar librerías que nos faciliten esta tarea.

 
 https://www.freecodecamp.org/news/web-scraping-python-tutorial-how-to-scrape-data-from-a-website/
"""

import requests
from bs4 import BeautifulSoup

proxiesHW = {
   'http': 'http://proxyeurope.huawei.com:8080',
   'https': 'http://proxyeurope.huawei.com:8080',
}

res = requests.get('https://holamundo.day', verify=True,  proxies=proxiesHW)
print(res.status_code)
#print(res.text)

#res2 = requests.get('https://www.google.es/',  proxies=proxiesHW)
#print(res2.status_code)

soup = BeautifulSoup(res.content, 'html.parser')
title = soup.title.text 
print(title)

all_h1_tags = []
for element in soup.select('h2'):
    all_h1_tags.append(element.text)

seventh_p_text = soup.select('p')[6].text
print(all_h1_tags, seventh_p_text)

# Create top_items as empty list
all_links = []

# Extract and store in top_items according to instructions on the left
links = soup.select('a')
for ahref in links:
    text = ahref.text
    text = text.strip() if text is not None else ''

    href = ahref.get('href')
    href = href.strip() if href is not None else ''
    all_links.append({"href": href, "text": text})

print(all_links)


