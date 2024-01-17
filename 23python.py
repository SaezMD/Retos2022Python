#23 CONJUNTOS
"""
 * Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
"""

def commonAndNoCommon(string01: str, string02: str, flag: bool) -> str:
    """function to return common elements or depends on determinate flag"""
    if flag:
        out1 = ""
        for i in string01:
            if i in string02:
                if i not in out1:
                    out1 += i
        for i in string02:
            if i in string01:
                if i not in out1:
                    out1 += i
        
        return print(out1,sep='\n')
    else:
        out1 = ""
        for i in string01:
            if i not in string02:
                if i not in out1:
                    out1 += i
        for i in string02:
            if i not in string01:
                if i not in out1:
                    out1 += i
        
        return print(out1,sep='\n')
        
commonAndNoCommon(
    "campo Naciones",
    "cosas de libros",
    True
)

commonAndNoCommon(
    "campo Naciones",
    "cosas de libros",
    False
)