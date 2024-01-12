#7 INVIRTIENDO CADENAS
"""
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""
def reverseString(text: str) -> str:
    """function to get the string in reverse order"""
    result = ""
    rep = len(text)
    
    while rep > 0:
        #result.append(text[rep-1])
        result += text[rep-1]
        rep -= 1
    
    return print(result)

reverseString("Campos de alubias.")
reverseString("la zorra come arroz")
reverseString("Hola mundo")