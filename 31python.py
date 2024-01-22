#31 MARCO DE PALABRAS
"""
 * Crea una función que reciba un texto y muestre cada palabra en una línea,
 * formando un marco rectangular de asteriscos.
 * - ¿Qué te parece el reto? Se vería así:
 *   **********
 *   * ¿Qué   *
 *   * te     *
 *   * parece *
 *   * el     *
 *   * reto?  *
 *   **********
"""

def frameTheWords(listOfWords: str) -> str:
    """function to print all the words in a different line surrounding by a frame of * """
    character = "*"
    listWords = listOfWords.split()
    maxLen = 0

    for i in listWords:
        if len(i) > maxLen:
            maxLen = len(i)

    print(character*(maxLen+2))
    for i in listWords:
        extraSpaces = maxLen - len(i)
        print(character+i+" "*extraSpaces+character)
    print(character*(maxLen+2))

frameTheWords("¿Cómo lo vamos a hacer?")
frameTheWords("Menudo el lío en el que el Sr. Theioihdiscosiasoiosiaoh se ha metido.")

