#54 EL "LENGUAJE HACKER"
"""
 * Escribe un programa que reciba un texto y transforme lenguaje natural a "lenguaje hacker" (conocido realmente como "leet" o "1337"). 
 Este lenguaje se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet) con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
"""

dictLeet = {'a': "4", 'b': "13", 'c': "[", 'd': ")", 'e': "3", 'f': "|=", 'g': "&", 'h': "#", 'i': "1", 'j': ",_|", 'k': ">|", 'l': "1", 'm': r'/\/\ ',
            'n': "^/", 'o': "0", 'p': "|*", 'q': "(_,)", 'r': "I2", 's': "5", 't': "7", 'u': "(_)", 'v': "\/", 'w': "\/\/", 'x': "><", 'y': "j", 'z': "2",
            '1': "L", '2': "R", '3': "E", '4': "A", '5': "S", '6': "b", '7': "T", '8': "B", '9': "g", '0': "o"
}

def cleanWords(word: str)-> str:
    """clean special characters and transform to lowercase"""
    from unidecode import unidecode
    # Remove special characteres, spaces and punctuation
    cleanStr = ''.join(filter(str.isalpha, word))
    cleanStr = unidecode(cleanStr)
    # Convert to lowercase
    lowerStr = cleanStr.lower()

    return lowerStr

def dictionaryConvert(toConvert: str)-> str:
    """convert letters and numbers to leet languaje"""
    return dictLeet[toConvert]

def changeToLeet(text: str)-> str:
    """"function to change text to hacker language: LEET"""
    translated = []
    for letter in text:
        if letter.isalnum():
            clean = cleanWords(letter)
            #change to leet dict
            translated.append(dictionaryConvert(letter))
        else:
            translated.append(letter)
    print(translated)


changeToLeet("banana")
changeToLeet("malaga antonio")
changeToLeet("doce 12 catorce 13 quince")

