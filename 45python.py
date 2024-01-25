#45 BUMERANES
"""
 * Crea una función que retorne el número total de bumeranes de un array de números enteros e imprima cada uno de ellos.
 * - Un bumerán (búmeran, boomerang) es una secuencia formada por 3 números seguidos, en el que el primero y el último son iguales, y el segundo es diferente. 
 Por ejemplo [2, 1, 2].
 * - En el array [2, 1, 2, 3, 3, 4, 2, 4] hay 2 bumeranes ([2, 1, 2] y [4, 2, 4]).
"""

def checkBoomerang(listOfNumbers: list) -> list:
    """function to check boomerang numbers in a list of numbers"""
    boomerangs = []
    for i in range(0,len(listOfNumbers)-2):
        #print(listOfNumbers[i],listOfNumbers[i+1],listOfNumbers[i+2])
        if listOfNumbers[i] == listOfNumbers[i+2] and listOfNumbers[i] != listOfNumbers[i+1]:
            boomerangs.append([listOfNumbers[i],listOfNumbers[i+1],listOfNumbers[i+2]])
    if boomerangs:
        print(boomerangs)
    else:
        print("No boomerangs in the list.")


checkBoomerang([2, 1, 2, 3, 3, 4, 2, 4] )
checkBoomerang([2, 2, 2, 3, 3, 4, 4, 4] )
checkBoomerang([2, 2, 3, 1, 3, 4, 4, 4] )
