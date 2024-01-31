#56 EL GENERADOR DE CONTRASEÑAS
"""
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
"""
import string
import secrets

"""generate list of letters, symbols, ..."""

lowercase = list(string.ascii_lowercase)	
uppercase = list(string.ascii_uppercase)	
digits = list(string.digits)
specialSymbols = list(string.punctuation) + ["ñ", "Ñ", "¡", "ª", "¿"]


def generatePassword(long: int, upper: str, numbers: str, symbols: str)-> str:
    """function to generate passwords with several optional parameters: uppercase, numbers, symbols"""
    finalPass = []
    listToCreatePass = lowercase

    if upper == "yes":
        listToCreatePass = listToCreatePass + uppercase

    if numbers == "yes":
        listToCreatePass = listToCreatePass + digits

    if symbols == "yes":
        listToCreatePass = listToCreatePass + specialSymbols

    print(listToCreatePass)

    for i in range(0,long):
        char = secrets.choice(listToCreatePass)
        finalPass.append(char)
        
    finalPass = ''.join(finalPass)

    return print(finalPass)


generatePassword(long = 10, upper = "yes", numbers = "yes", symbols = "yes")
generatePassword(long = 15, upper = "yes", numbers = "no", symbols = "yes")
generatePassword(long = 13, upper = "no", numbers = "no", symbols = "yes")
generatePassword(long = 8, upper = "no", numbers = "no", symbols = "no")

