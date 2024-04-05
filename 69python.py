#69 LA ESCALERA 
"""
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 *
 * Ejemplo: 4
 *         _
 *       _|
 *     _|
 *   _|
 * _|
 *

 -2
 _
  |_
    |_
      |_     

0
__

"""

def createLadder(numbersteps:int)-> str:

    if numbersteps == 0 :
        toDraw = "__"
        return print(toDraw)
    elif numbersteps > 0 :
        spaces = numbersteps*2
        print(" " * spaces + "_")
        for i in range(numbersteps+1, 1,-1):
            print(" " * (i*2 -4) + "_|")
    else:
        numbersteps = abs(numbersteps)
        print("_")
        for i in range(0, numbersteps ):
            print(" " * (i*2 +1) + "|_")


totalSteps = int(input("Number and direction of the stairs: "))
createLadder(totalSteps)
