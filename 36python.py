#36 BATALLA POKÉMON
"""
 * Crea un programa que calcule el daño de un ataque durante una batalla Pokémon.
 * - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
 * - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
 * - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico (buscar su efectividad)
 * - El programa recibe los siguientes parámetros:
 *  - Tipo del Pokémon atacante.
 *  - Tipo del Pokémon defensor.
 *  - Ataque: Entre 1 y 100.
 *  - Defensa: Entre 1 y 100.
"""

dictEfectivity = {
    "WaterWater": 0.5,
    "WaterFire": 2,
    "WaterPlant": 0.5,
    "WaterElectric": 1,
    "FireWater": 0.5,
    "FireFire": 0.5,
    "FirePlant": 2,
    "FireElectric": 1,
    "PlantWater": 2,
    "PlantFire": 0.5,
    "PlantPlant": 0.5,
    "PlantElectric": 1,
    "ElectricWater": 2,
    "ElectricFire": 1,
    "ElectricPlant": 0.5,
    "ElectricElectric": 0.5
}

def pokemonCombat(typePokemonAttack:str, attack:int, typePokemonDefense:str, defense:int)-> int:
    """function to determinate the damage of the combat"""
    efectivity = dictEfectivity[typePokemonAttack+typePokemonDefense]
    damage = 50 *(attack/defense)* efectivity
    print("{:10.2f}".format(damage))
     

pokemonCombat("Water",100, "Plant",50)
pokemonCombat("Water",80, "Plant",33)
pokemonCombat("Electric",80, "Water",33)




