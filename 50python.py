#50 EL DETECTOR DE HANDLES
"""
 * Crea una función que sea capaz de detectar y retornar todos los handles de un texto usando solamente Expresiones Regulares.
 * Debes crear una expresión regular para cada caso:
 * - Handle usuario: Los que comienzan por "@"
 * - Handle hashtag: Los que comienzan por "#"
 * - Handle web: Los que comienzan por "www.", "http://", "https://" y finalizan con un dominio (.com, .es...)
"""
import re

def handleRegularExpressions(text: str)-> str:
    """function to hadle with several regex: starting with @, starting with #, webs..."""

    #starting with @
    users = []
    users_regex = re.compile(r"\B@[a-zA-Z]*")

    for match in users_regex.finditer(text):
        users.append(match.group())

    print(users)

    #starting with #
    hastags = []
    hastags_regex = re.compile(r"\B#[a-zA-Z]*")

    for match in hastags_regex.finditer(text):
        hastags.append(match.group())

    print(hastags)

    #webs
    webs = []
    webs_regex  = re.compile(r"https?:\/\/[\w.-]+\.[a-zA-Z]{2,4}|w{3}.{1}[\w.-]+\.[a-zA-Z]{2,4}")

    for match in webs_regex.finditer(text):
        webs.append(match.group())
    
    print(webs)


handleRegularExpressions("www.hast.com campos.net @mariam @altro #tres ssdf")
handleRegularExpressions("www.hast.es  #sdfg #jjaula #caen  @love saul@saez.com")
handleRegularExpressions("www.hast.int ")
handleRegularExpressions("www.hast.int www.hast.com http://www.campo.net https://www.campo.es ")
