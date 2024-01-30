#51 LA ENCRIPTACIÓN DE KARACA
"""
 * Crea una función que sea capaz de encriptar y desencriptar texto utilizando el algoritmo de encriptación de Karaca (debes buscar información sobre él).
"""

chartVowels = {
    "a": 0,
    "e": 1,
    "i": 2,
    "o": 3,
    "u": 4
}

#check special characteres and case
def cleanWords(word: str)-> str:
    """clean special characters and transform to lowercase"""
    from unidecode import unidecode
    # Remove special characteres, spaces and punctuation
    cleanStr = ''.join(filter(str.isalpha, word))
    cleanStr = unidecode(cleanStr)
    # Convert to lowercase
    lowerStr = cleanStr.lower()

    return lowerStr

#encrypts
def encryptKaraca(wordToEncrypt: str)-> str:
    """function to encrypt using the Karaca algorithm"""
    #Step 1: Reverse the input:
    cleanToEncrypt = cleanWords(wordToEncrypt)
    reverseWord = cleanToEncrypt[::-1]
    #Step 2: Replace all vowels using the  chart:


    replacedVowels = []
    for i in reverseWord:
        if i in chartVowels:
            replacedVowels.append(str(chartVowels[i])) #append as text
        else:
            replacedVowels.append(i)

    replacedVowels = ''.join(replacedVowels)

    #Step 3: Add "aca" to the end of the word: "1lpp0aca"
    wordSuf = replacedVowels+"aca"
    return print(wordSuf)

#decrypt 
def decryptKaraca(wordToEncrypt: str)-> str:
    """function to dencrypt using the Karaca algorithm"""
    #remove the "aca" sufix
    removeSuf = wordToEncrypt[0:-3]

    #Replace all vowels using the chart:
    replacedNumbers = []
    for i in removeSuf:
        if i.isdigit():
            for k,v in chartVowels.items():
                if int(i) == v:
                    replacedNumbers.append(k) #append the key
        else:
            replacedNumbers.append(i)

    replacedNumbers = ''.join(replacedNumbers)
    #unreverse
    decrypt = replacedNumbers[::-1]
    return print(decrypt)

encryptKaraca("apple")
encryptKaraca("banana")
encryptKaraca("KloS'etádf")

decryptKaraca("fd0t1s3lkaca")
decryptKaraca("0n0n0baca")
decryptKaraca("1lpp0aca")


