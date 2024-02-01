#60 EL SOMBRERO SELECCIONADOR
"""
 * Crea un programa que simule el comportamiento del sombrero selccionador del universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que coloque al alumno en una de las 4 casas de Hogwarts:
 *   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador:
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
"""

def mostFrequent(List):
    counter = 0
    mostFrecuent = List[0]
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            mostFrecuent = i
 
    return mostFrecuent

def questions():
    """questions by the sorting hat"""
    input01 = input("""Which of the following options would you hate the most if people called it?
        (1) Ordinary
        (2) Ignorant
        (3) Coward
        (4) Egoist
        """)
    answerList={
      "1":"Gryffindor",
      "2":"Slytherin",
      "3":"Hufflepuff",
      "4":"Ravenclaw"
      }
    q1 = answerList.get(input01,"Invalid input")

    input02 = input("""After your death, what would you most like people to do when you hear your name?
        (1) She misses you, but smiles
        (2) Ask for more stories about your adventures
        (3) Think with admiration about your achievements
        (4) I don't care what people think of me after I die, it's what they think of me while I'm alive that counts
        """)
    q2 = answerList.get(input02,"Invalid input")
    
    input03 = input("""Given the option, you'd prefer to invent a potion that guarantees:
        (1) Glory
        (2) Wisdom
        (3) Love
        (4) Power
        """)
    q3 = answerList.get(input03,"Invalid input")    

    input04 = input("""How would you like to be known in history?
        (1) The wise
        (2) The Good One
        (3) The Great
        (4) The Bold
        """)
    q4 = answerList.get(input03,"Invalid input")        
    
    input05 = input("""Given the option, you'd prefer to invent a potion that guarantees:
        (1) Glory
        (2) Wisdom
        (3) Love
        (4) Power
        """)
    q5 = answerList.get(input05,"Invalid input")       
    
    print(q1,q2,q3,q4,q5)
    listHouses = []
    listHouses.append(q1)
    listHouses.append(q2)
    listHouses.append(q3)
    listHouses.append(q4)
    listHouses.append(q5)
    print(listHouses)
    houseToGo = mostFrequent(listHouses)
    print(f"You are going to study in: {houseToGo}")
    return houseToGo
 
questions()

