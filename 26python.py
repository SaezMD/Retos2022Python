#26 PIEDRA, PAPEL, TIJERA
"""
Crea un programa que calcule quien gana más partidas al piedra, papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
"""

dictResults ={
    '("R","R")': 0,
    '("R","S")': 1,
    '("R","P")': 2,
    '("S","R")': 2,
    '("S","S")': 0,
    '("S","P")': 1,
    '("P","R")': 1,
    '("P","S")': 2,
    '("P","P")': 0,
}

def rockPaperScissorsWinner(game: list) -> str:
    """function to analyse a list of games for the RPS couples"""
    listOfGames = game.split(", ")

    player1 = 0
    player2 = 0
    tier = 0
    for i in range(len(listOfGames)):
        #print(listOfGames[i])
        if listOfGames[i] in dictResults.keys():
            result = dictResults.get(listOfGames[i])
            if result == 1:
                player1 += 1
            elif result == 2:
                player2 += 1
            elif result == 0:
                tier += 1
        else:
            raise Exception("Error, check the list of games.")

    if player1 > player2:
        return print("Player 1")
    elif player2 > player1:
        return print("Player 2")
    else:
        return print("Tie")

rockPaperScissorsWinner('("R","S"), ("R","S"), ("R","R"), ("P","R"), ("S","R"), ("P","S")')





