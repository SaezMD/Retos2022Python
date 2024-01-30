#55 EL PARTIDO DE TENIS
"""
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien gane cada punto del juego.

 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
"""

dictScore = ["Love", 15, 30, 40, "Deuce", "Advantage P1", "Advantage P2"]

def tennisGameControl(gameSecuence: str)-> str:
    """function to control the scores in a tennis game"""
    p1 = 0
    p2 = 0
    finishFlag = 0
    resultScore = []

    for i in gameSecuence:
        if i != "P1" and i != "P2":
            raise Exception("Wrong entry. Please check it.")
        else: 
            if i == "P1":
                p1 += 1
            elif i == "P2":
                p2 += 1
            
            if p1 == p2 and p1>2:
                resultScore.append("Deuce")

            elif p1 > 3 and p1 > p2+1:
                resultScore.append("Game P1")

            elif p2 > 3 and p2 > p1+1:
                resultScore.append("Game P2")

            elif p1 > 3 and p1 > p2:
                resultScore.append("Advantage P1")
            elif p2 > 3 and p2 > p1:
                resultScore.append("Advantage P2")      

            else:    
                resultScore.append(str(dictScore[p1]) + " - " + str(dictScore[p2])) 
        
        #print(p1, p2)
    if "Game" in resultScore[-2]:
        raise Exception("Wrong entry. Please check it.")
    else:
        for i in resultScore:
            print(i)


tennisGameControl(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"])

tennisGameControl(["P1", "P2", "P2", "P2", "P1", "P2",])

tennisGameControl(["P1", "P2", "P2", "P2", "P2"])


tennisGameControl(["P1", "P1", "P1", "P2", "P2", "P2", "P2", "P1", "P2", "P2"])

