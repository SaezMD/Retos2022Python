#Reto #12 ELIMINANDO CARACTERES
"""
 Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
"""

def uniqueCharts(str1: str, str2: str) -> str:
    """this function gives you all characteres present in one string and not present in the other string"""
    list1 = list(str1)
    list2 = list(str2)
    #print(list1, list2)

    out1=""
    for i in list1:
        if i not in list2:
            out1 += i
    out2 = ""
    for i in list2:
        if i not in list1:
            out2 += i

    return print(out1,out2,sep='\n')

uniqueCharts("SaezMD","Saul Saez")

uniqueCharts("Carrera","vontage")
