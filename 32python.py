#32 AÑOS BISIESTOS
"""
 * Crea una función que imprima los 30 próximos años bisiestos siguientes a uno dado.
 * - Utiliza el menor número de líneas para resolver el ejercicio.
"""

def leapYearsBetweenDates(date1: str) -> int:
    """function to get number of leap years between 2 dates"""
    for i in range(date1,date1+31):
        if i % 4 == 0:
            if i % 100 != 0 or i % 400 == 0:
                print(i)

leapYearsBetweenDates(2024)

