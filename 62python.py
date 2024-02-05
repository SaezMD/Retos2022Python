#62 HETEROGRAMA, ISOGRAMA Y PANGRAMA
"""
 * Crea 3 funciones, cada una encargada de detectar si una cadena de texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
"""
import string

def cleanWords(word: str)-> str:
    """clean special characters and transform to lowercase"""
    from unidecode import unidecode
    # Remove special characteres, spaces and punctuation
    cleanStr = ''.join(filter(str.isalpha, word))
    cleanStr = unidecode(cleanStr)
    # Convert to lowercase
    lowerStr = cleanStr.lower()

    return lowerStr

def checkHeterograma(text: str)-> bool:
  """function to detect if a text is heterogram (A word or phrase in which each letter occurs only one time. No repeated letters.)"""
  listOfWord = list(text.lower())
  listOfWord.sort()
  
  for i in range(0,len(listOfWord)-1):
    if listOfWord[i] == listOfWord[i+1]:
      return False
    else:
      return True


def checkIsogramsMoure(word: str) -> bool:
  """function to detect if a word is isogram (A word or phrase in which each letter occurs the same number of times.)"""
  listOfWord = cleanWords(word)
  
  wordDict = dict()
  for character in listOfWord:
    wordDict[character] = wordDict.get(character,0) + 1

  isogram = True
  values = list(wordDict.values())
  isogramLen = values[0]
  for wordCount in values:
    if wordCount != isogramLen:
      isogram = False
      break
  
  return isogram


def checkPangrama(text: str) -> bool:
  """function to detect if string contains all the letters of the dictionary"""
  pangrama = True

  lowercase = list(string.ascii_lowercase)	
  spanishDictinaryLower = lowercase + ["ñ"]

  for letter in spanishDictinaryLower:
    if letter not in text.lower():
      pangrama = False
      break
      
  return pangrama


def checkWords(textToCheck: str) -> str:
  """check 2 words if they are: palindromes, anagrams or/and isograms"""
  print(f"{textToCheck} Pangrama: ", checkPangrama(textToCheck))
  print(f"{textToCheck} Heterogram: ", checkHeterograma(textToCheck))
  print(f"Isograms: {textToCheck}: {checkIsogramsMoure(textToCheck)}") 


checkWords("El pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frío, añoraba a su querido cachorro.")
checkWords("Campo")
checkWords("bilabial")
