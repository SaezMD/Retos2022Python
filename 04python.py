#4 ¿ES UN NÚMERO PRIMO?
"""
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
"""

def listPrimeNumbers(total:int):
    """create a list of prime numbers"""
    for i in range(2,total+1):
        if i in (2,3,5,7):
            print(i)

        if i % 2 == 0 or i % 3==0 or i % 5==0 or i % 7==0:
            continue
        print(i)

        #if i % 1 == 0 and i % i == 0:   
            #print(i)

listPrimeNumbers(100)

def PrimeNumbCheck(number):
    """Check if a number is prime"""
    if number > 1:
        for i in range(2, int(number**0.5) + 1): #take the square root of the number that we’re checking
            if number % i == 0:
                return False
        return True
    return False

print(PrimeNumbCheck(2011))

def betterListPrimeNumbers(total: int) -> list:
    """return a list of prime numbers"""
    listPrimes = []
    for i in range(0, total+1):
        if PrimeNumbCheck(i) == True:
            listPrimes.append(i)

    return listPrimes

print(betterListPrimeNumbers(100))
