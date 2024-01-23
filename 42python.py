#42 LA LEY DE OHM
"""
 * Crea una función que calcule el valor del parámetro perdido correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará el valor del tercero (redondeado a 2 decimales).
 * - Si los parámetros son incorrectos o insuficientes, la función retornará la cadena de texto "Invalid values".

V = R * I
R = V / I
I = V / R

"""

def calculateOhmLaw(volt: float='', resis: float='', inten: float='')-> str:
    """function to calculate the Ohm Law"""
    if volt == "":
        volt = resis * inten
        return print(f"Voltage is: {volt}")
    elif resis=="":
        resis = volt / inten
        return print(f"Resistance is: {resis}")
    elif inten=="":
        inten = volt / resis
        return print(f"Intensity is : {inten}")
    else:
        return print("Some data is not OK!")
    

calculateOhmLaw(resis=10, inten=20)
calculateOhmLaw(volt=100, inten=200)
calculateOhmLaw(volt=100, resis=4, )





