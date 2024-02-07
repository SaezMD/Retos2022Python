#34 CICLO SEXAGENARIO CHINO
"""
 * Crea un función, que dado un año, indique el elemento y animal correspondiente en el ciclo sexagenario del zodíaco chino.
 * - Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
 * - El ciclo sexagenario se corresponde con la combinación de los elementos madera, fuego, tierra, metal, agua 
    y los animales rata, buey, tigre, conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo(en este orden).
 * - Cada elemento se repite dos años seguidos.
 * - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
"""

listElements = [
    "madera",
    "madera",
    "fuego",
    "fuego",
    "tierra",
    "tierra",
    "metal",
    "metal",
    "agua",
    "agua"
]

listElementsENG = [
    "wood",
    "wood",
    "fire",
    "fire",
    "earth",
    "earth",
    "metal",
    "metal",
    "water",
    "water"
]

listAnimals = [
    "rata", 
    "buey", 
    "tigre", 
    "conejo", 
    "dragón", 
    "serpiente", 
    "caballo", 
    "oveja", 
    "mono", 
    "gallo", 
    "perro", 
    "cerdo"
]

listAnimalsENG = [
    "rat", 
    "ox", 
    "tiger", 
    "rabbit", 
    "dragon", 
    "snake", 
    "horse", 
    "sheep", 
    "monkey", 
    "rooster", 
    "dog", 
    "pig"
]

def chineseCycle(year: int)-> str:
    """function to get the sexagenary cycle of thhe Chinese 60-year calendar cycle is based on the combinations of a 
    cycle of ten heavenly stems and twelve earthly branches. Each year is named by a pair of one stem and one branch. """
    refYear = year-1924 
    elementYear = refYear % 10
    animalYear = refYear % 12
    print(year,listAnimals[animalYear],listElements[elementYear],listAnimalsENG[animalYear],listElementsENG[elementYear])

chineseCycle(1924)
chineseCycle(1950)
chineseCycle(1951)
chineseCycle(1952)
chineseCycle(1983)
chineseCycle(2024)
chineseCycle(2025)