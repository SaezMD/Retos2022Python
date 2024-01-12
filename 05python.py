#5 ÁREA DE UN POLÍGONO
"""
 * Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 """

def areaPoligon(type: str, base: int, alt: int) -> int:
    """function to get the area of a poligon"""
    if type == "square" and base != alt:
        return print("This is not a square poligon! Please check it.")

    if type == "triangle":
        area=base*alt/2
    else: 
        area=base*alt

    return print(f"The area of the {type} is: {int(area)} squared units.")

areaPoligon("triangle", 1.5, 12)
areaPoligon("square", 2, 2)
areaPoligon("rectangle", 2, 3)
areaPoligon("square", 5, 10)





