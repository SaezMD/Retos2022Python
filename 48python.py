#48 VOCAL MÁS COMÚN
"""
/*
 * Crea un función que reciba un texto y retorne la vocal que más veces se repita.
 * - Ten cuidado con algunos casos especiales.
 * - Si no hay vocales podrá devolver vacío.
 */
"""

def cleanWords(word: str)-> str:
    """clean special characters and transform to lowercase"""
    from unidecode import unidecode
    # Remove special characteres, spaces and punctuation
    cleanStr = ''.join(filter(str.isalpha, word))
    cleanStr = unidecode(cleanStr)
    # Convert to lowercase
    lowerStr = cleanStr.lower()

    return lowerStr

def countCharacteresInText(textlines: str) -> dict:
    """function to count the number of repetitions"""
    counterCharacteres = {}
    cleanText = cleanWords(textlines)
    
    for i in cleanText:
        if i in counterCharacteres:
            counterCharacteres[i] += 1
        else:
            counterCharacteres[i] = 1
    
    print(counterCharacteres)
    return counterCharacteres

def orderDictOnlyVocals(dictionaryLetters: dict)-> str:
    """function to order the vocals and get the max number """
    maximun = 0 
    maximunVocals = []

    charactersCounter = countCharacteresInText(dictionaryLetters)
    print(charactersCounter)

    for k,v in charactersCounter.items():
        if k in "aeiou":
            if v > maximun:
                maximun = v
    
    for k,v in charactersCounter.items():
        if v == maximun:
            maximunVocals.append(k)
    
    print(f"More commond vocal is/are: {maximunVocals} with: {maximun} repeats.")



orderDictOnlyVocals("This sentence must be counted.")
orderDictOnlyVocals("aaaaa EEEEE IIIII uuuuuu OOOOO IIIIIIIIIIIIII UUUUUUUUUUUUUUUUUUUUUUUuuuuuuuuuuuuuu ashkdjfhluiaenbck")
orderDictOnlyVocals("aaaeeeiiiooouuu")








