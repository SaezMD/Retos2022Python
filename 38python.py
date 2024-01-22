#38 LOS LANZAMIENTOS DE "THE LEGEND OF ZELDA"
"""
 * ¡Han anunciado un nuevo "The Legend of Zelda"!
 * Se llamará "Tears of the Kingdom" y se lanzará el 12 de mayo de 2023.
 * Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos "The Legend of Zelda" de la historia?
 * Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda que tú selecciones.
 * - Debes buscar cada uno de los títulos y su día de lanzamiento (si no encuentras el día exacto puedes usar el mes, o incluso inventártelo)
"""

def dayAsNumber(dateFormat: str) -> int:
    """function to convert the date formated to int number as in Excel. Ref 0000 = 1600"""
    dictMonthslengh= {
        1 : 31,
        2 : 28, 
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 : 31
    }

    #Calculate years and leap years
    year = int(dateFormat[-4:]) 
    backYear = dateFormat[:-4] + str(year-1) # Remove the actual year because is not completed
    #print(backYear)
    yearDiff = int(backYear[-4:]) - 1600 # Count from 1600
    years = yearDiff  * 365

    #Calculate months
    month = int(dateFormat[3:5])
    i = month - 1
    daysInMonth = 0 
    while i > 0:
        daysInMonth += dictMonthslengh[i]
        i -= 1
    #print(daysInMonth)
    months = daysInMonth

    #Calculate days
    days =  int(dateFormat[:2]) 

    #All sum:
    allDays = days + months + years
    #print(allDays)
    return allDays


def timeBtwnZeldaLaunch(game01: str, game02: str) -> str:
    """function to calculate the time in years and days between 2 launch dates of the games """

    dictZeldaLaunch={
        "The Legend of Zelda": "15/11/1987",
        "The Legend of Zelda: Tears of the Kingdom": "12/05/2023",
    }

    date01 = dictZeldaLaunch[game01]
    date02 = dictZeldaLaunch[game02]

    diffDays = dayAsNumber(date01) - dayAsNumber(date02)

    formatDays = "The difference are: " + str(int(abs(diffDays)/365)) + " years and " + str(diffDays%365) + " days." 

    print(formatDays)








timeBtwnZeldaLaunch("The Legend of Zelda","The Legend of Zelda: Tears of the Kingdom")



