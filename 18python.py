#18 LA CARRERA DE OBSTÁCULOS
"""
* Crea una función que evalúe si un/a atleta ha superado correctamente una carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo) o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera. Para ello tiene que realizar la opción correcta en cada tramo de la pista.
"""

def checkObstaclesRun(instructions: list, track: str) -> bool:
    """this function checks the instructions and track for a "obstacles race" """
    #check length
    lenghtInstructions = len(instructions)
    lenghtTrack = len(track)
    if lenghtInstructions != lenghtTrack:
        raise Exception("Check the instructions and track! Not the same lenght.")
    
    tiles = ""

    for i in range(0,lenghtInstructions):
        action = instructions[i]
        tile = track[i:i+1]
        if action == "run" and tile == "_":
            tiles += "_"
        elif action == "jump" and tile == "|":
            tiles += "|"
        elif  action == "jump" and tile == "_":
            tiles += "x"
            print(tiles)
            return False
        else:
            tiles += "/"
            print(tiles)
            return False

    #if "x" in tiles or "/" in tiles:
    #    return False

    print(tiles)
    return True


checkObstaclesRun(
    ["run","run","run","run","run","run","jump","run","run","jump","run","run","jump","run","jump","run","run","jump","run","run","jump","run","run"],
    "______|__|__|_|__|__|__"
)

checkObstaclesRun(
    ["run","run","run","run","run","run","jump","run","run","jump","run","run","jump","run","jump","run","run","jump","run","run","jump","run","run"],
    "__|___|__|__|_|__|__|__"
)

checkObstaclesRun(
    ["run","run","run","run","run","run","jump","run","run","jump","run","run","jump","run","jump","run","run","jump","run","run","jump","run","run"],
    "______|__|__|_|_____|__"
)

checkObstaclesRun(
    ["run","run","run","run","run","run","jump","run","run","jump","run","run","jump","run","run","jump","run","run"],
    "______|__|__|_|_____|__"
)




