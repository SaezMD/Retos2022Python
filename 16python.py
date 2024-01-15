#16 ¿CUÁNTOS DÍAS?
"""
 * Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
"""

def leapYearsBetweenDates(date1: str, date2: str) -> int:
    """function to get number of leap years between 2 dates"""
    year01 = int(date1[-4:])
    year02 = int(date2[-4:])
    leapYears = 0 

    for i in range(year01,year02):
        if i % 4 == 0:
            if i % 100 != 0 or i % 400 == 0:
                leapYears += 1
    print(leapYears)
    return leapYears

def difDates(date1: str, date2: str) -> int:
    """function to get the difference between 2 dates"""
    dictMonthslengh= {
        "01" : 31,
        "02" : 28, 
        "03" : 31,
        "04" : 30,
        "05" : 31,
        "06" : 30,
        "07" : 31,
        "08" : 31,
        "09" : 30,
        "10" : 31,
        "11" : 30,
        "12" : 31
    }

    #Diff days
    days = int(date1[:2]) - int(date2[:2])
    
    #Diff months
    months = int(date1[3:5]) - int(date2[3:5])
    for i in range(abs(months)):
        

    #Diff years
    years = int(date1[-4:]) - int(date2[-4:])

    #Leap Year. Number of leap years between 2 dates
    leapYears = leapYearsBetweenDates(date1, date2)

    # Sum the days
    yearstotal = abs(years)*365 + leapYears*366
    totalDays = days + months + yearstotal
    

difDates("01/01/2020", "02/02/2020")
difDates("01/01/2020", "02/02/2020")
difDates("01/01/2020", "01/01/2021")




leapYearsBetweenDates("01/01/2020", "01/01/2027")
leapYearsBetweenDates("01/01/0499", "01/01/0501")