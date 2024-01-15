#20 CONVERSOR TIEMPO
"""
 * Crea una función que reciba días, horas, minutos y segundos (como enteros)
 * y retorne su resultado en milisegundos.
"""

def convertToMiliseconds(days :int, hours :int, minutes :int, seconds :int) -> int:
    """function to convert time into miliseconds"""
    #Convert days
    daysT = days*24*60*60
    #Convert hours
    hoursT = hours*60*60
    #Convert minutes
    minutesT = minutes*60
    #Convert seconds
    allSeconds = daysT + hoursT + minutesT + seconds
    #Convert to miliseconds
    miliSec = allSeconds * 1000

    print(miliSec)
    return miliSec


convertToMiliseconds(2,5,30,15)
convertToMiliseconds(0,0,0,1)
convertToMiliseconds(1,0,0,0)
