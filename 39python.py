#39 BINARIO A DECIMAL
"""
 * Crea un programa se encargue de transformar un número binario a decimal sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""

def binaryToDecimal(binaryNumb: bin) -> int:
    """fucntion to convert from binary to decimal."""
    result = 0 

    for i in range(0,len(binaryNumb)):
        temp01 = int(binaryNumb[-i-1])*2**i
        result += temp01
    
    print(f"The number decimal: {binaryNumb} in binary is: {result}")


binaryToDecimal("1010")
binaryToDecimal("1110010")
binaryToDecimal("11011")
binaryToDecimal("11111111")
binaryToDecimal("11000000")