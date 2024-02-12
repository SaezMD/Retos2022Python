#68 AUREBESH
"""
 * Crea una función que sea capaz de transformar Español al lenguaje básico del universo Star Wars: el "Aurebesh".
 * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
 * - También tiene que ser capaz de traducir en sentido contrario.
 *
 * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
 *
 * ¡Que la fuerza os acompañe!
"""

def translateToAurebesh(textToTranslate: str)-> str:
    """function to translate from latin to Aurebesh and viceversa"""

    basic_alphabet = {
        "a": "aurek", "b": "besh", "c": "cresh", "d": "dorn", "e": "esk", "f": "forn", "g": "grek", "h": "herf",
        "i": "isk", "j": "jenth", "k": "krill", "l": "leth", "m": "merm", "n": "nern", "o": "osk", "p": "peth", "q": "qek",
        "r": "resh", "s": "senth", "t": "trill", "u": "usk", "v": "vev", "w": "wesk", "x": "xesh", "y": "yirt", "z": "zerek",
        "ae": "enth", "eo": "onith", "kh": "krenth", "ng": "nen", "oo": "orenth", "sh": "sen", "th": "thesh"}

    cleanText = textToTranslate.lower()

    aurebesh = ""
    i = 0
    while i < len(cleanText):
    #for i in range(len(cleanText)):
        if cleanText[i] not in basic_alphabet:
            aurebesh = aurebesh + cleanText[i] + " "
            i += 1
        else:
            if cleanText[i:i+2] in basic_alphabet.keys():
                aurebesh = aurebesh + basic_alphabet[cleanText[i:i+2]] + " "
                #print("YES")
                i += 2
            else: 
                #print("OK",cleanText[i:i+2])
                aurebesh = aurebesh + basic_alphabet[cleanText[i]] + " "
                i += 1
            #print(basic_alphabet[cleanText[i]])
    
    print(aurebesh)


translateToAurebesh("Hello! We are eo ñere.")

translateToAurebesh("eo kh oo")
