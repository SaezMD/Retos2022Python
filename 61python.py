#61 EL GENERADOR PSEUDOALEATORIO
"""
Crea un generador de números pseudoaleatorios entre 0 y 100.
- No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.

Es más complicado de lo que parece...
"""

from datetime import datetime
print(datetime.now())

listNumbers = [22,33,59,157,147,1,2,69999,6987,5155,4478,1147,2256,47,10004,545,58]

#Sum year and second for seed number
seedNumber = datetime.now().year + datetime.now().second

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def calMinor100(number):
    try:
        while number > 100:
            number = number / 7
    except:
        number = 0 

    print(int(number))
    return int(number)

# multiply seed by the sum of the numbers of the microseconds and multiply by the number in the list(based on the sum of the seconds)
multiplier = sum_digits(datetime.now().microsecond)
seed2 = seedNumber * multiplier * listNumbers[sum_digits(datetime.now().second)]

# divide by 7 until random number is <= 100

randomBySaez = calMinor100(seed2)




