#35 LOS NÚMEROS PERDIDOS
"""
 * Dado un array de enteros ordenado y sin repetidos, crea una función que calcule y retorne todos los que faltan entre el mayor y el menor.
 * - Lanza un error si el array de entrada no es correcto.
"""

def missingNumbers(numbers: list) -> list:
    """function to return the missing number from a list of sorted and not repeated numbers"""
    result = []

    #Check all numbers
    for i in numbers:
        if not isinstance(i,int):
            raise Exception("All values should be a digit.")
        
    #Check sorted numbers
    if numbers != sorted(numbers) and numbers != sorted(numbers,reverse=True):
        raise Exception("Values should be shorted.")
    
    #Check no repeated
    for i in range(0,len(numbers)-1):
        if numbers[i] == numbers[i+1]:
            raise Exception("Values should not be repeated.")

    for i in range(0,len(numbers)-1):
        diff = numbers[i+1] - numbers[i]
        for j in range(0, diff-1):
            result.append(numbers[i]+j+1)


    print("Missing numbers are:",result)

missingNumbers([1,2,3,4,5,6,8,10,11,15,21])
missingNumbers([1,4,5,8,10,11,15,21])
missingNumbers([1,2,3,4,8,10,11,15,20,21])
