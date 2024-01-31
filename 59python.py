#59 PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK
"""
 * Crea un programa que calcule quien gana más partidas al piedra, papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel), "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.

"""

def rockPaperScissorsLizardSpock(gameList: list)-> str:
    """function to get the winner in the game"""
    player1 = 0
    tie = 0
    
    for i in gameList:
        if i[0] == "scissors" and i[1] == "paper":
            player1 += 1
        if i[0] == "paper" and i[1] == "rock":
            player1 += 1
        if i[0] == "rock" and i[1] == "lizzard":
            player1 += 1
        if i[0] == "lizzard" and i[1] == "spock":
            player1 += 1
        if i[0] == "spock" and i[1] == "scissors":
            player1 += 1
        if i[0] == "scissors" and i[1] == "lizzard":
            player1 += 1
        if i[0] == "lizzard" and i[1] == "papel":
            player1 += 1
        if i[0] == "papel" and i[1] == "spock":
            player1 += 1
        if i[0] == "spock" and i[1] == "rock":
            player1 += 1
        if i[0] == "rock" and i[1] == "scissors":
            player1 += 1

        if i[0] == i[1]:
            tie += 1
        
    player2 = len(gameList) - player1 - tie
    #print(player1, player2)

    if player1 > player2:
        return print(f"Winner is Player 1")
    elif player1 == player2:
        return print(f"Tie")
    else:
        return print(f"Winner is Player 2")
    

rockPaperScissorsLizardSpock([("rock", "scissors"), ("rock", "scissors"), ("scissors", "rock"), ("spock", "rock"), ("lizzard", "rock"), ("scissors", "scissors")])