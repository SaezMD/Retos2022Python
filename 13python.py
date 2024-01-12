#13 ¿ES UN PALÍNDROMO?
"""
 * Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
"""
from unidecode import unidecode

def isPalindrome(text: str) -> bool:
    """this function returns TRUE if the text is palindrome"""

    # Remove special characteres, spaces and punctuation
    cleanStr = ''.join(filter(str.isalpha, text))
    cleanStr = unidecode(cleanStr)
    # Convert to lowercase
    lowerStr = cleanStr.lower()

    #Check palindrome
    if lowerStr == lowerStr[::-1]:
        print("True")
        return True
    else:
        print("False")
        return False

isPalindrome("reconocer")
isPalindrome("Allí ves Sevilla")
isPalindrome("Allí si María avisa y así va a ir a mi silla")
isPalindrome("Dábale arroz a la zorra el abad")
isPalindrome("Eva usaba rímel y le miraba suave")
isPalindrome("Ligar es ser ágil")
isPalindrome("A mamá Roma le aviva el amor a papá y a papá Roma le aviva el amor a mamá")
isPalindrome("""Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, 
             acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, 
             de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, 
             ya ni giros elimina, ya ni poeta, ya ni vida""")


isPalindrome("NO es Palíndromo")