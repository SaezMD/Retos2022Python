#10 CÓDIGO MORSE
"""
 * Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
"""

def convertMorse(stringToConvert: str) -> str:
    """this function converts a text to MORSE code and MORSE CODE to text"""

    # Dictionary representing the morse code chart
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                        'C':'-.-.', 'D':'-..', 'E':'.',
                        'F':'..-.', 'G':'--.', 'H':'....',
                        'I':'..', 'J':'.---', 'K':'-.-',
                        'L':'.-..', 'M':'--', 'N':'-.',
                        'O':'---', 'P':'.--.', 'Q':'--.-',
                        'R':'.-.', 'S':'...', 'T':'-',
                        'U':'..-', 'V':'...-', 'W':'.--',
                        'X':'-..-', 'Y':'-.--', 'Z':'--..',
                        '1':'.----', '2':'..---', '3':'...--',
                        '4':'....-', '5':'.....', '6':'-....',
                        '7':'--...', '8':'---..', '9':'----.',
                        '0':'-----', ', ':'--..--', '.':'.-.-.-',
                        '?':'..--..', '/':'-..-.', '-':'-....-',
                        '(':'-.--.', ')':'-.--.-',
                        ' ':' ',                        
                        }

    key_list = list(MORSE_CODE_DICT.keys())
    val_list = list(MORSE_CODE_DICT.values())
    solution=""

    #Detect type of string
    if stringToConvert[0:1] == "." or stringToConvert[0:1] == "-":
        print("Converting MORSE CODE to text")
        #Convert morse to text
        words = stringToConvert.split("  ")

        for item in words:
            position = val_list.index(item)
            letter = key_list[position]
            solution += letter

    else:
        print("Converting text to MORSE CODE")
        #Convert text to morse
        words = list(stringToConvert)

        for item in words:
            position = key_list.index(item)
            code = val_list[position]
            solution += code + " "

    return print(words, "\n", solution)

convertMorse("-.-.  .-  ...  ---") #CASO
convertMorse("CASO ROBIN") # -.-.  .-  ...  ---

