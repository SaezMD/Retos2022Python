#33 EL SEGUNDO
"""
Dado un listado de números, encuentra el SEGUNDO más grande
"""

def secondBiggest(listNumb: list)-> int:
    """function to return the second biggest number"""
    for i in range(0,len(listNumb)):
        for j in range(i+1, len(listNumb)):
            if listNumb[i] <= listNumb[j]:
                listNumb[i],listNumb[j] = listNumb[j], listNumb[i]

    return print(listNumb[1])

secondBiggest([2, 20, 1, 10, 8, 9, 100, 50, 5])
secondBiggest([2, 20, 1, 10, 8, 9, 50, 5])