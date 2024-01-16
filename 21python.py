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
