#30 ORDENA LA LISTA
"""
 * Crea una función que ordene y retorne una matriz de números.
 * - La función recibirá un listado (por ejemplo [2, 4, 6, 8, 9]) y un parámetro adicional "Asc" o "Desc" para indicar si debe ordenarse de menor a mayor o de mayor a menor.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
"""

def orderList(listNumb: list, order: str) -> list:
    """function to sort the list based in a parameter"""

    if order == "Desc":
        for i in range(0,len(listNumb)):
            for j in range(i+1, len(listNumb)):
                if listNumb[i] <= listNumb[j]:
                    listNumb[i],listNumb[j] = listNumb[j], listNumb[i]
    elif order == "Asc":
        for i in range(0,len(listNumb)):
            for j in range(i+1, len(listNumb)):
                if listNumb[i] >= listNumb[j]:
                    listNumb[i],listNumb[j] = listNumb[j], listNumb[i]        
    else:
        return print("Check order type. Only possible to use: 'Asc' or 'Desc'.")

                
    return print(listNumb)

orderList([2, 4, 6, 8, 9], "Asc")
orderList([2, 1, 10, 8, 9], "Asc")
orderList([2, 4, 6, 8, 9], "Desc")


