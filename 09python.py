#9 DECIMAL A BINARIO
"""
 * Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""

def fromDecimalToBinary(number: int) -> str:
    """function to convert from decimal to binary"""

    result=""
    quotient = number

    if quotient == 0:
        result="0"

    while quotient > 0:
        reminder = int(quotient % 2)
        quotient = int(quotient / 2)
        #print(quotient)
        #print(reminder)
        result += str(reminder)

    print(f"The decimal number: {number}, in binary is: {result[::-1]}")

fromDecimalToBinary(12)
fromDecimalToBinary(174)
fromDecimalToBinary(0)
fromDecimalToBinary(1)
fromDecimalToBinary(2)
fromDecimalToBinary(10)


