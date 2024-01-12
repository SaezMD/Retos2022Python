#15 ¿ES UN NÚMERO DE ARMSTRONG?
"""
 * Escribe una función que calcule si un número dado es un número de Armstrong (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información al respecto.
"""

def isAmstrong(number: int) -> bool:
    """this function retuns if a number is Amstrong or not. Armstrong number is the number in any given number base, 
    which forms the total of the same number, when each of its digits is raised to the power of the number of digits in the number. 
    ie: 153 = 1³ + 5³ + 3³"""

    if number >0:

        numberStr = str(number)
        sumSquares = 0
        for i in list(numberStr):
            sumSquares += int(i)**3
        
        if sumSquares == number:
            print("Yes")
            return True
    print("No")
    return False

isAmstrong(0)
isAmstrong(12)
isAmstrong(100)
isAmstrong(153)
isAmstrong(1634)




