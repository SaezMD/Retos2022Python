#57 PRIMO, FIBONACCI Y PAR
"""
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
"""

def PrimeNumbCheck(number):
    """Check if a number is prime"""
    if number > 1:
        for i in range(2, int(number**0.5) + 1): #take the square root of the number that we’re checking
            if number % i == 0:
                return False
        return True
    return False


def fiboList(lastNumb: int = 51) -> list:
    """this functions creates a fibonacci list"""
    x = [0,1]
    for i in range(2, lastNumb+2):
        x.append(x[i-2]+x[i-1]) 
        #print(i)
        #print(i," - ", x)
    #print(x[0:lastNumb+2])
    return x

def checkPrimeFibonacciEven(number: int)-> str:
    """function to check if a number is prime, Fibonacci and even"""

    prime = "prime"
    fibo = "Fibonacci"
    even = "even"
    #check prime
    if not PrimeNumbCheck(number):
        prime = "not prime"

    #check fibonacci
    if number not in fiboList(10):
        fibo = "not Fibonacci"

    #check even
    if number % 2 != 0:
        even = "uneven"

    return print(f"{number} is {prime}, {fibo} and is {even}.")
    

checkPrimeFibonacciEven(13)
checkPrimeFibonacciEven(12)

