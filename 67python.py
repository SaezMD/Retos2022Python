#67 OCTAL Y HEXADECIMAL
"""
 * Crea una función que reciba un número decimal y lo trasforme a Octal y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que realicen esas operaciones directamente.
"""


def convertOctalAndHexa(numberDecimal: int)-> str:
    """function to convert from decimal to octal and hexadecimal"""
    decimalNumber = int(numberDecimal)
    initialNumber = int(numberDecimal)
    octalResult = []

    #octal conversion from decimal
    while numberDecimal >= 8:
        octalResult.append(numberDecimal % 8)
        numberDecimal //= 8
    
    octalResult.append(numberDecimal)
    octalResult.reverse()
    #convert to string
    octalResult = ''.join(map(str, octalResult))
    

    #hexadecimal
    hexaResult = []
    while initialNumber >= 16:
        hexaResult.append(initialNumber % 16)
        initialNumber //= 16

    hexaResult.append(initialNumber)
    hexaResult.reverse()
    
    #print(hexaResult)
    #Change >9 to letters:
    letter = ["A","B","C","D","E","F"]

    for i in range(len(hexaResult)):
        if hexaResult[i] > 9:
            hexaResult[i] = letter[hexaResult[i]-10]


    #convert to string
    hexaResult = ''.join(map(str, hexaResult))
    return print(f" {decimalNumber} {octalResult} {hexaResult}")    


convertOctalAndHexa(214)
convertOctalAndHexa(4253)
convertOctalAndHexa(88)
convertOctalAndHexa(501)



