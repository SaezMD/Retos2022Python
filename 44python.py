#44 TRUCO O TRATO
"""
 * Este es un reto especial por Halloween.
 * Deberemos crear un programa al que le indiquemos si queremos realizar "Truco o Trato" y un listado (array) de personas con las siguientes propiedades:
 * - Nombre de la niña o niño
 * - Edad
 * - Altura en centímetros
 *
 * Si las personas han pedido truco, el programa retornará sustos (aleatorios) siguiendo estos criterios:
 * - Un susto por cada 2 letras del nombre por persona
 * - Dos sustos por cada edad que sea un número par
 * - Tres sustos por cada 100 cm de altura entre todas las personas
 * - Sustos: 🎃 👻 💀 🕷 🕸 🦇
 *
 * Si las personas han pedido trato, el programa retornará dulces (aleatorios) siguiendo estos criterios:
 * - Un dulce por cada letra de nombre
 * - Un dulce por cada 3 años cumplidos hasta un máximo de 10 años por persona
 * - Dos dulces por cada 50 cm de altura hasta un máximo de 150 cm por persona
 * - Dulces: 🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩
 * - En caso contrario retornará un error.

trick or treat
"""
import random

def countLettersOfTheName(arrayOfPeople:list) -> int:
    """count number of letters in the name"""
    #count letters in the name, each 2 in every name
    each2Letters = 0 
    for i in arrayOfPeople:
        each2 = int(len(i[0])/2) #divide by 2 and take the int part.
        each2Letters += each2
    #print(each2Letters)

    #count letters in the name, all together
    allLetters = 0 
    for i in arrayOfPeople:
        allLetters += len(i[0])
    #print(allLetters)

    return each2Letters, allLetters    

def countAge(arrayOfPeople:list) -> int:
    """"count of the age"""
    #count age (even numbers)
    evenNumbers = 0
    for i in arrayOfPeople:
        if i[1] % 2 == 0:
            evenNumbers += 1
    #print(evenNumbers)

    #count number of years (x3) until 10 years each
    groupOfThree = 0
    for i in arrayOfPeople:
        floorAge = i[1] // 3
        if floorAge > 3:
            groupOfThree += 3
        else:
            groupOfThree += floorAge
    #print(groupOfThree)
    return evenNumbers, groupOfThree

def countHeight(arrayOfPeople:list) -> int:
    """"count of height"""
    #count number of cms for each 100cms
    sumHeights = 0
    for i in arrayOfPeople:
        sumHeights += i[2]
    hundreds = int(sumHeights/100)
    
    #count cms for each 50cms max. 150cm each
    each50Height = 0
    for i in arrayOfPeople:
        floorHeight = i[2] // 50
        if floorHeight > 3:
            each50Height += 3
        else:
            each50Height += floorHeight
    #print(each50Height)
    return hundreds, each50Height


def halloweenGame(type: str, characteristics: list) -> list:
    """ function for the Halloween game """
    name = countLettersOfTheName(characteristics)
    age = countAge(characteristics)
    height = countHeight(characteristics)

    if type == "trick":
        trickList = []
        tricks = ["🎃", "👻", "💀", "🕷", "🕸", "🦇"]
        sumTricks = name[0] + age[0] + height[0]
        for i in range(sumTricks):
            trickList.append(random.choice(tricks))
        print(trickList)

    elif type == "treat":
        treatList = []
        treats = ["🍰", "🍬", "🍡", "🍭", "🍪", "🍫", "🧁", "🍩"]
        sumTreats = name[1] + age[1] + height[1]
        for i in range(sumTreats):
            treatList.append(random.choice(treats))
        print(treatList)
    else:
        raise Exception("Wrong combination! Please check")

    
halloweenGame("trick", [
    ["Lucia",9,125],
    ["Patricia",4,135],
    ["Carlos",3,80],
    ["Paco",24,190]
    ])

halloweenGame("treat", [
    ["Lucia",9,125],
    ["Patricia",4,135],
    ["Carlos",3,80],
    ["Paco",24,190]
    ])

