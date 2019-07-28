ROWS = 8
COLUMNS = 8
EMPTY_ROW = (COLUMNS) * ["_"]


def printBoard(piecesList):
    """
    piecesList is a list, that can be empty, consisting of triples
    the first element is the piece, a character, e.g "R"
    the second element is the row, an integer from 1 to 8
    the third element is the column, an integer from 1 to 8
    Returns nothing
    """
    for i in range(ROWS):
        currentRow = EMPTY_ROW[:]
        for element in piecesList:
            if element[1] == i:
                currentRow[element[2]] = element[0]
        printRow = "." + ".".join(currentRow) + "."
        print(printRow)
        
        
def createPawnsList():
    """
    """
    pawnsList = []
    for i in [1, 6]:
        for j in range(8):
            subTuple = tuple(['P', i, j])
            pawnsList.append(subTuple)
    return pawnsList


piecesList = [('P', 1, 0), ('P', 1, 1), ('P', 1, 2), ('P', 1, 3), ('P', 1, 4), ('P', 1, 5), ('P', 1, 6), ('P', 1, 7),
    ('P', 6, 0), ('P', 6, 1), ('P', 6, 2), ('P', 6, 3), ('P', 6, 4), ('P', 6, 5), ('P', 6, 6), ('P', 6, 7)]
piecesList = createPawnsList()
printBoard(piecesList)