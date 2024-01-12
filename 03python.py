#3 LA SUCESIÓN DE FIBONACCI
"""
 * Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""

def fiboList(startNumb: int = 0, lastNumb: int = 51) -> list:
    """this functions creates a fibonacci list"""
    x = [0,1]
    for i in range(2, lastNumb+2):
        x.append(x[i-2]+x[i-1]) 
        print(i)
        #print(i," - ", x)
    return print(x[startNumb:lastNumb+2])
    
fiboList(4,10)


def fiboPrint(lastNumb: int = 50) -> list:
    """this functions creates a fibonacci list"""
    x = 0
    y = 1
    for i in range(0, lastNumb+1):
        if i == 0:
            print(0)
        if i == 1:
            print(1)
        print(x+y)
        y = x+y
        x = y-x
        #print(i," - ", x)
  
fiboPrint(50)

