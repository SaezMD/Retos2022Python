#52 EL RETO RANDOM
"""
 * Crea tu propio enunciado para que forme parte de los retos de 2023.
 * - Ten en cuenta que su dificultad debe ser asumible por la comunidad y seguir un estilosemejante a los que hemos realizado durante el año.
 * - Si quieres también puedes proponer tu propia solución al reto (en el lenguaje que quieras).

Flip the parentheses over.
In Santa's workshop 🎅, some Christmas messages have been written in a peculiar way: the letters inside the parentheses must be read backwards. 
Santa needs these messages to be correctly formatted. Your task is to write a function that takes a string of text and reverses the characters 
inside each pair of parentheses, removing the parentheses in the final message. However, keep in mind that nested parentheses may exist, 
so you must reverse the characters in the correct order.
"""

def decodeWrong(texToDecode: str)-> str:
    """function to decode the text with patentheses"""
    normal = []
    open = []
    close = []

    for i in range(len(texToDecode)):
        if texToDecode[i] == "(":
            open.append(i)
        elif texToDecode[i] == ")":
            close.append(i)
        else:
            normal.append(i)
    
    print("Open: ", open)
    print("Close: ", close)
    print("Normal: ", normal)

    for i in range(len(open)-1,-1,-1):
        #print(open[i])
        for j in range(len(close)):
            if close[j] > open[i]:
                print( open[i],close[j])
                break
        

def decode(message):
    import re
    msg = re.sub(r'\(([^()]*)\)', lambda match: match.group(1)[::-1], message)
    return decode(msg) if '(' in msg else msg

print(decode('hola (odnum)'))
print(decode('(olleh) (dlrow)!'))
print(decode('sa(u(cla)atn)s'))


