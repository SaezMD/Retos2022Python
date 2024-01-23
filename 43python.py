#43 CONVERSOR DE TEMPERATURA
"""
 * Crea una función que transforme grados Celsius en Fahrenheit y viceversa.
 * - Para que un dato de entrada sea correcto debe poseer un símbolo "°" y su unidad ("C" o "F").
 * - En caso contrario retornará un error.
"""

def changeBetweenCelsiusFarenheit(temperature: str)-> str:
    """"function to convert from Fahrenheit to Celsius and viceversa"""
    #check if entry is OK
    if temperature[-2:] == "ºC":
        fahren = int(temperature[0:-2]) * 1.8 + 32
        return print(f"{temperature} are: {'{:0.2f}'.format(fahren)}ºF")
    elif temperature[-2:] == "ºF":        
        celsius = (int(temperature[0:-2]) - 32) / 1.8
        return print(f"{temperature} are: {'{:0.2f}'.format(celsius)}ºC")
    else:
       raise Exception("Error in the units! Please check it.")

changeBetweenCelsiusFarenheit("20ºC")
changeBetweenCelsiusFarenheit("200ºF")

