#66 ADIVINA LA PALABRA
"""
* Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
 * - El juego comienza proponiendo una palabra aleatoria incompleta
 *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
 * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que la palabra a adivinar)
 *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta uno al número de intentos
 *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno al número de intentos
 *   - Si el contador de intentos llega a 0, el jugador pierde
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
"""
import random

wordsRandom = ["casapapis", "computer", "balls", "charger", "kindles", "candles", "mouse", "hallucinogenic", "amphetamine", "medicine"]


#choose random word from the list
completeWord = wordsRandom[random.randrange(0,len(wordsRandom))]
print(completeWord)

#show >60% of the words
hideLetters = len(completeWord)
hideWord = list(completeWord)

while hideLetters > int(len(completeWord)*0.6):
    #print(completeWord[random.randrange(0,len(completeWord))])
    randNow = random.randrange(0,len(completeWord))
    if hideWord[randNow] != "_":
        hideWord[randNow] = "_"
        hideLetters -= 1

print(hideWord)

def gameHideLetters():
    tries = 10
    while tries > 0:

        userGuess = input("Enter some letter to guess or the complete word: ")

        #check if entry is a letter or word
        if len(userGuess) > 1:
            #Word:
            if userGuess == completeWord:
                return print(f"Found it! Correct word is: {completeWord}")
            else:
                print("Wrong word.")
                tries -= 1
                print(f"There are: {tries} remaining tries.")
        else: 
            #letter:
            if userGuess in completeWord:
                for i in range(len(completeWord)):
                    if userGuess == completeWord[i]:
                        hideWord[i] = userGuess
                if "_" in hideWord:
                    print(hideWord)
                else:
                    return print(f"Found it! Correct word is: {completeWord}") 
            else: 
                tries -= 1
                print(f"There are: {tries} remaining tries.")


gameHideLetters()


