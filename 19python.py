#19 TRES EN RAYA
"""
 * Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
 * - O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.
"""

def threeInLine(matrix: list) -> str:
    """function to check 3 in line matrix"""
#Check ratio and Check characteres
    xNumbers = 0
    oNumbers = 0
    empty = 0
    others = []
    for row in matrix:
        for i in range(0, len(row)):
            if row[i] == "X":
                xNumbers += 1
            elif row[i]  == "O":
                oNumbers += 1
            elif row[i]  == "":
                empty += 1
            else:
                others.append(row[i])
    #print(xNumbers, oNumbers, empty, others)
    
    if others:
        raise Exception(f'Wrong characteres. Please check the matrix! {others}. The matrix only can contain: "X", "O" & "".')

    if xNumbers != oNumbers and xNumbers != oNumbers+1 and xNumbers != oNumbers-1:
        raise Exception(f"Wrong ratio levels. Please check the matrix. X= {xNumbers}, O= {oNumbers}, Empty= {empty}")
    
#Check columns
    xLines = 0 
    oLines = 0     
    colums = [[] for i in range(3)]

    for i in range(0, 3):
        for row in matrix:
            colums[i].append(row[i])   
    
    for row in colums:
        if row[0] == row[1] and row[1] == row[2]:
            if row[0] == "X":
                xLines += 1
            elif row[0] == "O":
                oLines += 1

    #print("columns",xLines, oLines)

#Check rows
    for row in matrix:
        if row[0] == row[1] and row[1] == row[2]:
            if row[0] == "X":
                xLines += 1
            elif row[0] == "O":
                oLines += 1
    
    #print("rows",xLines, oLines)

#Check diagonal
    diago01 = []
    diago02 = []
    #Create diagonal 1
    for i in range(0, 3):
        diago01.append(matrix[i][i])
    #Create diagonal 2
    diago02.append(matrix[0][-1])
    diago02.append(matrix[1][1])
    diago02.append(matrix[-1][0])

    #Check if diagonal are all X or all O or not equal
    for diago in (diago01, diago02):
        if diago[0] == diago[1] and diago[1] == diago[2]:
            if diago[0] == "X":
                xLines += 1
            elif diago[0] == "O":
                oLines += 1

    #print("diago",xLines, oLines)
    # Check winner
    if xLines > oLines:
        print("winner X")
    elif xLines < oLines:
        print("winner O")
    else:
        print("Empate")

matrix00 = [["X","X","X"],
            ["X","X","X"],
            ["X","X","X"]]

matrix01 = [["O","X","X"],
            ["X","O","X"],
            ["X","X","O"]]

matrix02 = [["O","X","O"],
            ["X","O","X"],
            ["X","X","O"]]

matrix03 = [["O","",""],
            ["","O","X"],
            ["X","X","O"]]

matrix04 = [["O","O","O"],
            ["X","X","X"],
            ["X","X","O"]]

matrix05 = [["X","O","O"],
            ["X","O","X"],
            ["X","O","O"]]

matrix06 = [["X","O","O"],
            ["X","X","X"],
            ["X","O","O"]]

matrix07 = [["X","O","X"],
            ["O","O","X"],
            ["X","O","O"]]

threeInLine(matrix02)
threeInLine(matrix03)
threeInLine(matrix04)
threeInLine(matrix05)
threeInLine(matrix06)
threeInLine(matrix07)

#threeInLine(matrix00)
#threeInLine(matrix01)
