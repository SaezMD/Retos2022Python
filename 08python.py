#8 CONTANDO PALABRAS
"""
 * Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
"""
def repeatedWords(text: str) -> dict:
    import re

    #remove the puntuaction signs
    new_string = re.sub(r'[^\w\s]', '', text)
    print(new_string)

    #split the text into words
    words = new_string.split()

    #convert to lowercase
    lower = []
    for i in words:
        i = i.lower()
        lower.append(i)

    print(lower)

    #create a dict with the words and the repeated appears
    dictWords={}
    for i in lower:
        if i in dictWords:
            dictWords[i] += 1
        else:
            dictWords[i] = 1

    #sorting the dict by descendent repetitions
    sortedWords = sorted(dictWords.items(),key=lambda x:x[1],reverse=True)
    sortedDict = dict(sortedWords)

    return sortedDict


print(repeatedWords("uno Dos dos DOS dos DoS 2. en el en el campo campo coleGa colega Colega marca marcA otro Aotr? "))


