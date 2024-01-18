#24 MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO
"""
 * Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""

def primeDescomp(n):
    """function to get the prime numbers"""
    prime = []
    for i in range(2, n + 1):
        while n % i == 0:
            prime.append(i)
            n = n / i
    #print(prime)
            
    primeDict={}   
    for i in range(len(prime)):
        if prime[i] not in primeDict.keys():
            primeDict[prime[i]] = 1
        else:
            primeDict[prime[i]] += 1

        #print(prime[i])
    #print(primeDict)

    return primeDict


def multiplyInsideDicts(dictToMult: dict)-> int:
    """function to calculate inside the dict. Each key elevate to the value and sum all of them"""
    result = 1
    for key, value in dictToMult.items():
        result *= key**value
    #print(result)
    return result


def maxCommonDivisor(number1: int, number2: int) -> int:
    """function to obtain the maximun common divisor"""
    desc01 = primeDescomp(number1)
    desc02 = primeDescomp(number2)
    #print(desc01,desc02)

    #get the commond factors
    commonFactors = {}
    for number, exponent in desc01.items():
        if number in desc02.keys():
            # get the minumun pow for the commom factors
            commonFactors[number] = min(desc02.get(number), exponent)
    
    #print(commonFactors)
    mcdResult = multiplyInsideDicts(commonFactors)
    print(mcdResult)
    return mcdResult

maxCommonDivisor(15,10)
maxCommonDivisor(102,72)
maxCommonDivisor(300,198)
maxCommonDivisor(5,3)
maxCommonDivisor(200,300)

def minCommonMultipler(number1: int, number2: int) -> int:
    """fucntion to get the minimun common multiplier"""
    desc01 = primeDescomp(number1)
    desc02 = primeDescomp(number2)
    #print(desc01,desc02)

    #get the non commond and commond factors with the max. exponent
    factors = {}
    for number, exponent in desc01.items():
        if number in desc02.keys():
            factors[number] = max(desc02.get(number), exponent)
        else:
            factors[number] = exponent
    
    for number, exponent in desc02.items():
        if number not in factors.keys():
            factors[number] = exponent

    #print(factors)
    mcm = multiplyInsideDicts(factors)
    print(f"Minimun Common Multiplier of: {number1} & {number2} is: {mcm}")
    return mcm

minCommonMultipler(12,8)
minCommonMultipler(61,10)
