#47 ¿DÓNDE ESTÁ EL ROBOT?
"""
 * Calcula dónde estará un robot (sus coordenadas finales) que se encuentra en una cuadrícula representada por los ejes "x" e "y".
 * - El robot comienza en la coordenada (0, 0).
 * - Para idicarle que se mueva, le enviamos un array formado por enteros (positivos o negativos) que indican la secuencia de pasos a dar.
 * - Por ejemplo: [10, 5, -2] indica que primero se mueve 10 pasos, se detiene, luego 5, se detiene, y finalmente 2.
 *   El resultado en este caso sería (x: -5, y: 12)
 * - Si el número de pasos es negativo, se desplazaría en sentido contrario al que está mirando.
 * - Los primeros pasos los hace en el eje "y". Interpretamos que está mirando hacia la parte positiva del eje "y".
 * - El robot tiene un fallo en su programación: cada vez que finaliza una secuencia de pasos gira 90 grados en el sentido contrario a las agujas del reloj.
"""

def movementRobot(instructions: list) -> str:
    """ function to get the last position for a robot that moves in X and Y matrix """
    x = 0
    y = 0 
    for i in range(0,len(instructions)):
        modulusFour = i % 4 
        if modulusFour == 0:
            y += instructions[i]
        elif modulusFour == 1:
            x -= instructions[i]
        elif modulusFour == 2:
            y -= instructions[i]
        elif modulusFour == 3:
            x += instructions[i]

    #print(f"X: {x}, Y: {y}")
    return "X: "+ str(x) +", Y: " + str(y)


def test_case(movements: list, expected: str):
    returned = movementRobot(movements)
    if returned != expected:
        raise Exception(
            f"Case with movements {movements}, returns {returned} but it should be {expected}"
        )

def main():
    
    test_case([10, 5, -2], "X: -5, Y: 12")
    test_case([20, 5, -2, 10, -5, 100, 99], "X: -95, Y: -82")
    test_case([20, 5, -2, 10, -5, 100, 99,100, -2, 88, 18, 22, -3, -1, -1, 1, 0], "X: -59, Y: -104")

    print("All cases passed!")


if __name__ == '__main__':
    main()
