#22 CALCULADORA.TXT
"""
 * Lee el fichero "Challenge22.txt" incluido en el proyecto, calcula su resultado e imprímelo.
 * - El .txt se corresponde con las entradas de una calculadora.
 * - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
 * - Soporta números enteros y decimales.
 * - Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
 * - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
 * - Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.
"""

#check if line is number or sign

#check if operation is admitted


def calculation(equation):
    """funciton to calculate when the equations are in a str variable"""
    if '+' in equation:
        y = equation.split('+')
        x = float(y[0]) + float(y[1])
    elif '-' in equation:
        y = equation.split('-')
        x = float(y[0]) - float(y[1])
    elif '/' in equation:
        y = equation.split('/')
        x = float(y[0]) / float(y[1])      
    elif '*' in equation:
        y = equation.split('*')
        x = float(y[0]) * float(y[1])     
    return x

def calculatorByFile(file: str) -> int:
    """function to calculate a list of numbers and signs"""
    try:
        instructions = []
        #read from file
        with open(file,'r') as file:
        # read the file with a for loop
            for line in file:
                # strip the newline character from the line
                #print(line.strip())
                instructions.append(line.strip())

        result = calculation(str(instructions[0] + instructions[1] + instructions[2]))
        i = 3
        while i < len(instructions):
            result = calculation(str(str(result) + instructions[i] + instructions[i+1]))
            #print(instructions[i] + instructions[i+1], result)
            i+=2
                
        #print result at the end
        return print(result)
    except:
        return print("Impossible to solve the operations. Check the file!")

calculatorByFile(r"D:\Python\practicas\retos2002\Retos2022Python\Challenge22.txt")

calculatorByFile(r"D:\Python\practicas\retos2002\Retos2022Python\Challenge22b.txt")

calculatorByFile(r"D:\Python\practicas\retos2002\Retos2022Python\Challenge22c.txt")


