#41 TRIÁNGULO DE PASCAL
"""
 * Crea una función que sea capaz de dibujar el "Triángulo de Pascal" indicándole únicamente el tamaño del lado.
 *
 * - Aquí puedes ver rápidamente cómo se calcula el triángulo:
 *   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif

     1
    1 1
   1 2 1
  1 3 3 1 
 1 4 6 4 1
1 5 10 10 5 1
"""

def pascalTriangle(size: int)-> str:
    """function to create the triangle of Pascal when you have the length of the base"""
    list = []
    for n in range(size):
        list.append([]) #create a list of lists
        list[n].append(1) #create n list full of 1's
        #print(list)   
        for m in range(1, n):
            list[n].append(list[n-1][m-1] + list[n -1] [m])
        if size != 0: # if size is greater than 0
            list[n].append(1) #add 1 to the line
    print(list)
    #print the lists in different lines
    for n in range(size):        
        print(" " * (size-n),end="") #print spaces before the line
        for m in range(0, n+1):
            print("{0:4}".format(list[n][m]),end="") #print the lines with total characteres spaces to keep room until 1.000
        print()


pascalTriangle(12)
