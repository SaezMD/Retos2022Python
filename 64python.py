#64 PARÁMETROS URL
"""
 * Dada una URL con parámetros, crea una función que obtenga sus valores.
 * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
 
 * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0 los parámetros serían ["2023", "0"]
 
"""

#from = and &
#from = to the end

import re

def getParametersFromURL(urlWithParameters: str)-> list:
    """get a list of parameters from a URL"""
    listOfParameters = re.findall(r'=(.*?)(?=&|$)', urlWithParameters)

    print(listOfParameters)


getParametersFromURL("https://retosdeprogramacion.com?year=2023&challenge=0")
getParametersFromURL("www.foobar.com/?first=1&second=12&third=5")
