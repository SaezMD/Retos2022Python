#2 ¿ES UN ANAGRAMA?
"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 """

def isAnagrama(txt1: str, txt2: str) -> bool:
    """function to check anagram"""
    if txt1 == txt2:
        return False
    if txt1 == txt2[::-1]: #reverse string in Python
        return True
    return False


print(isAnagrama("casa", "caso"))
print(isAnagrama("sopa", "apos"))
print(isAnagrama("calor","calor"))


