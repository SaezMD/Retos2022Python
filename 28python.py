#28 VECTORES ORTOGONALES
"""
 * Crea un programa que determine si dos vectores son ortogonales.
 * - Los dos array deben tener la misma longitud.
 * - Cada vector se podría representar como un array. Ejemplo: [1, -2]
"""

def checkVectors(vector1: list, vector2: list) -> bool:
    """function to determinate id 2 vectors are orthogonal"""
    #check if the vectors have the same lenght
    if len(vector1) != len(vector2):
        raise Exception("Vector have not the same lenght.") 
    
    #check if the vectos are orthogonal:
    result = vector1[0]*vector2[0] + vector1[1]*vector2[1] 
    if result == 0:
        print("The vectors are orthogonal.")
        return True
    print("The vectors are NOT orthogonal!")
    return False

checkVectors([3, 2], [-2, 3])

checkVectors([3, 5], [-2, 3])