#11 EXPRESIONES EQUILIBRADAS
"""
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
"""

def checkDelimiters(expression: str) -> str:
    """this function checks if the delimeters are OK: open/close, order and make sense"""
    #remove all except delimiters () {} []
    delimiters="(){}[]"
    opener ="{[("
    closers="}])"
    cleanStr=[]

    for i in expression:
        if i in list(opener) or i in list(closers):
            cleanStr.append(i)

    #check1: Openers==Closers
    openerCount = 0 
    closerCount = 0
    for deli in cleanStr:
        if deli in opener:
            openerCount += 1
        elif deli in closers:
            closerCount += 1
    
    if openerCount != closerCount:
        return "Unbalanced"

    #Check2: openers position < closers position
    box = []
    for i in expression:
        if i in list(opener):
            box.append(i)
        elif i in list(closers):
            pos = (list(closers)).index(i)
            if ((len(box) > 0) and ((list(opener))[pos] == box[len(box)-1])):
                box.pop()
            else:
                return "Unbalanced"
            
    if len(box) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


print(checkDelimiters("{ [ a * ( c + d ) ] - 5 }")) # OK
print(checkDelimiters("{ [ a * ( c + d ) ] ( )- 5 }")) # OK
print(checkDelimiters("{ [ a * ( c + d ) ] {}( )- 5 }")) # OK
print(checkDelimiters("{ ([ a * ( c + d ) ]) {}( )- 5 }")) # OK


print(checkDelimiters("{ a * ( c + d ) ] - 5 }")) # NO
print(checkDelimiters(" [ a * ( c + d ) ] - 5 }")) # NO
print(checkDelimiters("{ [ a * ( c + d ) ] ( - 5 }")) # NO
print(checkDelimiters("{ [ a * ( c + d  ] ) - 5 }")) # OK
