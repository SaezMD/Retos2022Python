#27  CUADRADO Y TRIÁNGULO 2D
"""
 * Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 * - EXTRA: ¿Eres capaz de dibujar más figuras?
 """

def drawTriangleIsos(size: str) -> str:
    """function to draw the triangle shape based in the size number"""
    character = "*"

    i = 1
    spaces = int(size/2)
    while i < size+1:
        print(spaces*" "+i*character+spaces*" ")

        i += 2
        spaces -= 1
    #print(size*character)
   
def drawTriangle(size: str) -> str:
    """function to draw the triangle shape based in the size number"""
    character = "* "
    i = 1
    while i < size+1:
        print(character*i)
        i += 1

def drawSquare(size: str) -> str:
    """function to draw the square shape based in the size number"""
    character = "* "
    for i in range(1,size+1):
        print(character*size)


def identifyShape(shape: str, size: int) -> str:
    """function to identify the shape of the figure and the total size"""
    if shape == "triangle":
        return drawTriangle(size)
    if shape == "triangle Isos":
        return drawTriangleIsos(size)
    elif shape == "square":
        return drawSquare(size) 
    else:
        return print(f"{shape} is not correct. Please use: triangle or square")


identifyShape("square",5)
identifyShape("triangle",5)
identifyShape("triangle Isos",21)