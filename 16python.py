#16 ¿CUÁNTOS DÍAS?
"""
 * Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
"""
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

def checkDatesFormats(date: str) -> bool:
    import re
    # All numbers must be possitives, only 2 "/" signs, 
    if not re.match("^\d{2}\/\d{2}\/\d{4}$", date):
        raise Exception("Sorry, date format is not correct. Format should be: 'dd/MM/yyyy'")
    # months <12, days <31 
    month = int(date[3:5])
    if month > 12:
        raise Exception("Sorry, wrong month number. Max: 12")
    
    #month limit by dict
    monthLimit = dictMonthslengh[month]
    day = int(date[:2])
    if day > monthLimit:
        raise Exception(f"Sorry, too many days in the month. Max for this month({month}): {monthLimit}")

    # Years over 1600 DC
    if int(date[-4:]) < 1600:
        print(f"Some date is too old. Try with dates after 1600 DC")
        return False

    return True

def leapYear(date: str) -> bool:
    year = int(date[-4:])
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
    return False

def leapYearsBetweenDates(date1: str, date2: str) -> int:
    """function to get number of leap years between 2 dates"""
    year01 = int(date1[-4:])
    year02 = int(date2[-4:])
    leapYears = 0 
    for i in range(year01,year02+1):
        if i % 4 == 0:
            if i % 100 != 0 or i % 400 == 0:
                leapYears += 1
    #print(leapYears)
    return leapYears

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
    leapYears = leapYearsBetweenDates("01/01/2012",backYear) #Calculate number of leap days from last year until 1600
    yearDiff = int(backYear[-4:]) - 1600 # Count from 1600
    years = (yearDiff - leapYears) * 365 + leapYears * 366

    #Calculate months
    month = int(dateFormat[3:5])
    i = month - 1
    daysInMonth = 0 
    while i > 0:
        daysInMonth += dictMonthslengh[i]
        i -= 1
    #print(daysInMonth)
    months = daysInMonth
    #Current leap year
    currentLeap = 0 
    if leapYear(dateFormat) and month > 2:
        currentLeap = 1

    #Calculate days
    days =  int(dateFormat[:2]) 

    #All sum:
    allDays = days + months + years + currentLeap
    #print(allDays)
    return allDays


def difDatesNumb(date1: str, date2: str) -> int:
    """function to get the difference as number between 2 dates"""
    #Check date format
    if checkDatesFormats(date1) and checkDatesFormats(date2):
        print("dates OK")

    #Diff between dates
    diffDates = abs(dayAsNumber(date1) - dayAsNumber(date2))
    print(diffDates)
    return diffDates

difDatesNumb("01/01/2020", "33/24/2020")
difDatesNumb("01/01/2020", "01/02/2020")
difDatesNumb("01/01/2020", "02/02/2020")
difDatesNumb("01/01/2020", "02/03/2020")
difDatesNumb("01/01/2020", "01/01/2021")
difDatesNumb("01/01/2000", "01/01/2026")
difDatesNumb("01/01/1492", "01/01/2026")

def difDates(date1: str, date2: str) -> int:
    """function to get the difference between 2 dates"""
    #Diff days
    days = int(date1[:2]) - int(date2[:2])
    
    #Diff months
    months = int(date1[3:5]) - int(date2[3:5])
    for i in range(abs(months)):
        continue
        

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
leapYearsBetweenDates("01/01/1600", "01/01/2025")