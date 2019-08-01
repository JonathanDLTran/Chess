import Constants

class Chess:
    
    
    def parser(self):
        toContinue = True
        while(toContinue):
            startCoordinate = input("Please input the start coordinate as a row column pair, with space between row and column: ")
            endCoordinate = input("Please input the end coordinate as a row column pair, with space between row and column: ")
            if 'quit' in [startCoordinate.lower().strip(), endCoordinate.lower().strip()]:
                return
            if (not self.legalCoordinate(startCoordinate)) or (not self.legalCoordinate(endCoordinate)):
                print("One of your coordinates was not formated properly.")
                print("Please type your coordinate like '1, 6' ")
                print("Asking for coordinates again")
            else:
                start = self.legalCoordinate(startCoordinate)
                end = self.legalCoordinate(endCoordinate)
                return [start, end]
                
    def legalCoordinate(self, coordinate):
        if "" not in coordinate:
            return False
        space = coordinate.index("")
        row = coordinate[:space]
        column = coordinate[space + 1:]
        row = row.strip(); column = column.strip()
        if len(row) != 1 or len(column) != 1:
            return False
        if ( not row.isnumeric() ) or ( not column.isnumeric() ):
            return False
        row = int(row); column = int(column)
        if (row < 1) or (row > 8) or (column < 1) or (column > 8):
            return False
        return (row, column)
    
    
def parser():
    toContinue = True
    while(toContinue):
        startCoordinate = input("Please input the start coordinate as a row column pair, with space between row and column: ")
        if startCoordinate.lower().strip() == 'quit':
            return
        endCoordinate = input("Please input the end coordinate as a row column pair, with space between row and column: ")
        if endCoordinate.lower().strip() == 'quit':
            return
        if (not legalCoordinate(startCoordinate)) or (not legalCoordinate(endCoordinate)):
            print("One of your coordinates was not formated properly.")
            print("Please type your coordinate like '1, 6' ")
            print("Asking for coordinates again")
        else:
            start = legalCoordinate(startCoordinate)
            end = legalCoordinate(endCoordinate)
            return [start, end]
                
def legalCoordinate(coordinate):
    if SPACE not in coordinate:
        print('1')
        return False
    print(coordinate)
    coordinate = coordinate.strip()
    space = coordinate.index(SPACE)
    print("space", space)
    row = coordinate[:space]
    column = coordinate[space + 1:]
    row = row.strip(); column = column.strip()
    print("row", row)
    print("column", column)
    if len(row) != 1 or len(column) != 1:
        print('2')
        return False
    if ( not row.isnumeric() ) or ( not column.isnumeric() ):
        print('3')
        return False
    row = int(row); column = int(column)
    if (row < 1) or (row > 8) or (column < 1) or (column > 8):
        print('4')
        return False
    if row == column:
        return False
    return (row - 1, column - 1)


def initializeData():
    gameList = []
    for i in range(ROWS):
        gameList.append(NONE_LIST)
    initializeBishops(gameList)
    initializeKings(gameList)
    initializeQueens(gameList)
    initializeKnights(gameList)
    initializeRooks(gameList)
    initializePawns(gameList)
    self.piecesData = gameList
    
    
def initializePawns(gameList):
    for i in [1, 6]:
        for j in range(8):
            if i == 1:
                gameList[i][j] = Pawn(BLACK)
            else:
                gameList[i][j] = Pawn(WHITE)


def initializeRooks(gameList):
    gameList[0][0] = Rook(BLACK)
    gameList[0][7] = Rook(BLACK)
    gameList[7][0] = Rook(WHITE)
    gameList[7][7] = Rook(WHITE)

def initializeBishops(gameList):
    gameList[0][2] = Bishop(BLACK)
    gameList[0][5] = Bishop(BLACK)
    gameList[7][2] = Bishop(WHITE)
    gameList[7][5] = Bishop(WHITE)

def initializeKnights(gameList):
    gameList[0][1] = Knight(BLACK)
    gameList[0][6] = Knight(BLACK)
    gameList[7][1] = Knight(WHITE)
    gameList[7][6] = Knight(WHITE)

def initializeQueens(gameList):
    gameList[0][4] = Queen(BLACK)
    gameList[7][4] = Queen(WHITE)

def initializeKings():
    gameList[0][3] = King(BLACK)
    gameList[7][3] = King(WHITE)


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

print(parser())

piecesList = [('P', 1, 0), ('P', 1, 1), ('P', 1, 2), ('P', 1, 3), ('P', 1, 4), ('P', 1, 5), ('P', 1, 6), ('P', 1, 7),
    ('P', 6, 0), ('P', 6, 1), ('P', 6, 2), ('P', 6, 3), ('P', 6, 4), ('P', 6, 5), ('P', 6, 6), ('P', 6, 7)]
piecesList = createPawnsList()
printBoard(piecesList)