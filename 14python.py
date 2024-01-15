#14 FACTORIAL RECURSIVO
"""
Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
"""

def returnFactorial(number: int) -> int:
    """return the factorial number"""
    solve = 1
    if int(number) > 0:
        
        for i in range(1,int(number)+1):
            solve *= i 
      
    return print(solve)


def factorialRecursive(number: int) -> int:

    if number == 1:
       return 1
    else:
        return number * factorialRecursive(number-1)

    

returnFactorial(0)
returnFactorial(1)
returnFactorial(2)
returnFactorial(5)
returnFactorial(100)

print(factorialRecursive(5))
      
