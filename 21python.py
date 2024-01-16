#21 PARANDO EL TIEMPO
"""
 * Crea una función que sume 2 números y retorne su resultado pasados unos segundos.
 * - Recibirá por parámetros los 2 números a sumar y los segundos que debe tardar en finalizar su ejecución.
 * - Si el lenguaje lo soporta, deberá retornar el resultado de forma asíncrona, es decir, sin detener la ejecución del programa principal.
 *   Se podría ejecutar varias veces al mismo tiempo.
"""
import asyncio
async def sumWithWait(number1: int, number2: int, seconds: int) -> int:
    """function to sum 2 numbers when waiting for some seconds"""

    sumNumbers = number1 + number2
    await asyncio.sleep(seconds,result=(print(sumNumbers)))
    #print(sumNumbers)

#asyncio.run(sumWithWait(5,15,5))
#asyncio.run(sumWithWait(20,2,2))

import threading
import time

def sumWithWait2(number1: int, number2: int, seconds: int) -> int:
    """function to sum 2 numbers when waiting for some seconds"""
    sumNumbers = number1 + number2
    time.sleep(seconds)
    print(sumNumbers)

threading_sum = threading.Thread(target=sumWithWait2, args=(5,15,5))
threading_sum.start()

print("Printing while waiting")
time.sleep(2)
print("Printing while waiting")
time.sleep(2)
print("Printing while waiting")
time.sleep(2)
print("Printing while waiting (or not ;) )")



import time
import asyncio
async def sumAndWait(number1: int, number2: int, seconds: int) -> int:
    """function to sum 2 numbers when waiting for some seconds."""

    # take initial time
    init_time = time.time()
    sumNumbers = number1 + number2

    # waiting
    await asyncio.sleep(seconds)

    # take finish time
    finish_time = time.time()

    # Imprime el resultado y el tiempo que le tomó realizar la tarea en específico
    print(f"{number1} + {number2} = {sumNumbers}. \tIt Took: {round(finish_time-init_time, 3)} seconds.")


async def main():
    """calling the functions"""
    # testing
    await asyncio.gather(
        sumAndWait(1, 1, 5),
        sumAndWait(5, 5, 3),
        sumAndWait(10, 10, 1)
    )

if __name__ == "__main__":
    init_time = time.time()

    # strating main function
    asyncio.run(main())

    finish_time = time.time()

    print(f"\nAll Excecution took: {round(finish_time - init_time, 3)} seconds.")


# Result Tests

# 10 + 10 = 20.   It Took: 1.013 seconds.
# 5 + 5 = 10.     It Took: 3.009 seconds.
# 1 + 1 = 2.      It Took: 5.01 seconds.

# All Excecution took: 5.014 seconds.