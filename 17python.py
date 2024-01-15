#17 EN MAYÚSCULA
"""
Crea una función que reciba un String de cualquier tipo y se encargue de poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""

def firstInUpper(string: str) -> str:
    """function to change first character of a word to uppercase"""
    wordsList =  string.split()
    resultList = []

    for i in wordsList:
        wordUp = i[:1].upper() + i[1:]
        resultList.append(wordUp)

    result = " ".join(resultList)
    print(result)
    return result


firstInUpper("hola coca cola, por la carretera.")