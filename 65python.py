#65 VIERNES 13
"""
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
"""

import datetime

def checkFriday13InMonthAndYear(monthToCheck: int, yearToCheck: int)-> bool:
    """funcion to check if month and year contains Friday13"""

    month = monthToCheck
    year = yearToCheck

    dayOfTheWeek = datetime.datetime(year, month, 13).weekday()
    if dayOfTheWeek == 4: #if Friday
        print("True")
        return True
    else:
        print("False")
        return False


checkFriday13InMonthAndYear(10, 2023)

checkFriday13InMonthAndYear(2, 2024)


