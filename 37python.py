#37 LOS ANILLOS DE PODER
"""
 * ¡La Tierra Media está en guerra! En ella lucharán razas leales a Sauron contra otras bondadosas que no quieren que el mal reine sobre sus tierras.
 * Cada raza tiene asociado un "valor" entre 1 y 5:
 * - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3), Númenóreanos (4), Elfos (5)
 * - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2), Huargos (3), Trolls (5)
 * Crea un programa que calcule el resultado de la batalla entre los 2 tipos de ejércitos:
 * - El resultado puede ser que gane el bien, el mal, o exista un empate. Dependiendo de la suma del valor del ejército y el número de integrantes.
 * - Cada ejército puede estar compuesto por un número de integrantes variable de cada raza.
 * - Tienes total libertad para modelar los datos del ejercicio.
 * Ej: 1 Peloso pierde contra 1 Orco
 *     2 Pelosos empatan contra 1 Orco
 *     3 Pelosos ganan a 1 Orco
"""

goodArmy = {
    "Pelosos": 1,
    "Sureños buenos": 2,
    "Enanos": 3, 
    "Númenóreanos": 4,
    "Elfos": 5
}

evilArmy = {
    "Sureños malos": 2,
    "Orcos": 2,
    "Goblins": 2,
    "Huargos": 3,
    "Trolls": 5
}

def combatESDLA(goodSoldiers: dict, evilSoldiers: dict) -> str:
    """funciton to calculate power of both armies"""
    goodPower = 0
    evilPower = 0
    for k,v in goodSoldiers.items():
        #print(k,v)
        #print(goodArmy[k])
        soldiersPower = v*goodArmy[k]
        goodPower += soldiersPower

    for k,v in evilSoldiers.items():
        soldiersPower = v*evilArmy[k]
        evilPower += soldiersPower

    #print(goodPower, evilPower)

    if goodPower > evilPower:
        return print("Good Army wins!")
    elif goodPower == evilPower:
        return print("Tie!")
    else:
        return print("Evil Army wins!")


goodArmy01 = {
    "Pelosos": 100,
    "Sureños buenos": 200,
    "Enanos": 300, 
    "Númenóreanos": 400,
    "Elfos": 500
}
evilArmy01 = {
    "Sureños malos": 20,
    "Orcos": 20,
    "Goblins": 20,
    "Huargos": 30,
    "Trolls": 50
}
combatESDLA(goodArmy01,evilArmy01)

goodArmy02 = {
    "Pelosos": 2,
    "Sureños buenos": 1,
    "Enanos": 1, 
    "Númenóreanos": 1,
    "Elfos": 1
}
evilArmy02 = {
    "Sureños malos": 2,
    "Orcos": 1,
    "Goblins": 1,
    "Huargos": 1,
    "Trolls": 1
}
combatESDLA(goodArmy02,evilArmy02)

goodArmy03 = {
    "Sureños buenos": 1,
    "Enanos": 1, 
    "Elfos": 1
}
evilArmy03 = {
    "Sureños malos": 4,
    "Orcos": 1,
    "Goblins": 2,
    "Huargos": 2,
    "Trolls": 1
}
combatESDLA(goodArmy03,evilArmy03)