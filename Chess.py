from Constants import *

import Piece
import Pawn 
import Knight 
import Rook 
import Bishop
import King 
import Queen

import operator
import copy

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
    #if row == column:
    #   return False
    return (row - 1, column - 1)

def swapPiece(pos1, pos2):
    pass

def initializeData():
    gameList = []
    for i in range(ROWS):
        gameList.append(copy.deepcopy(NONE_LIST))
    initializeBishops(gameList)
    initializeKings(gameList)
    initializeQueens(gameList)
    initializeKnights(gameList)
    initializeRooks(gameList)
    initializePawns(gameList)
    return gameList
    
def initializePawns(gameList):
    for i in [1, 6]:
        for j in range(8):
            if i == 1:
                gameList[i][j] = Pawn.Pawn(BLACK)
            else:
                gameList[i][j] = Pawn.Pawn(WHITE)


def initializeRooks(gameList):
    gameList[0][0] = Rook.Rook(BLACK)
    gameList[0][7] = Rook.Rook(BLACK)
    gameList[7][0] = Rook.Rook(WHITE)
    gameList[7][7] = Rook.Rook(WHITE)

def initializeBishops(gameList):
    gameList[0][2] = Bishop.Bishop(BLACK)
    gameList[0][5] = Bishop.Bishop(BLACK)
    gameList[7][2] = Bishop.Bishop(WHITE)
    gameList[7][5] = Bishop.Bishop(WHITE)

def initializeKnights(gameList):
    gameList[0][1] = Knight.Knight(BLACK)
    gameList[0][6] = Knight.Knight(BLACK)
    gameList[7][1] = Knight.Knight(WHITE)
    gameList[7][6] = Knight.Knight(WHITE)

def initializeQueens(gameList):
    gameList[0][4] = Queen.Queen(BLACK)
    gameList[7][4] = Queen.Queen(WHITE)

def initializeKings(gameList):
    gameList[0][3] = King.King(BLACK)
    gameList[7][3] = King.King(WHITE)


# def printBoard(piecesList):
#     """
#     piecesList is a list, that can be empty, consisting of triples
#     the first element is the piece, a character, e.g "R"
#     the second element is the row, an integer from 1 to 8
#     the third element is the column, an integer from 1 to 8
#     Returns nothing
#     """
#     print(SPACE + SPACE + SPACE.join(ALPHABET_ROW) + SPACE)
#     for i in range(ROWS):
#         currentRow = EMPTY_ROW[:]
#         for element in piecesList:
#             if element[1] == i:
#                 currentRow[element[2]] = element[0]
#         printRow = str(i + 1) + SPACE + SPACE.join(currentRow) + SPACE
#         print(printRow)
        
def printBoard(gameList):
    print(SPACE + SPACE + SPACE.join(ALPHABET_ROW) + SPACE)
    for i in range(ROWS):
        currentRow = gameList[i]
        stringRow = ''
        for element in currentRow:
            if element == None:
                element = UNDERSCORE
            stringRow += SPACE + str(element)
        printRow = str(i + 1) + stringRow + SPACE
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




def correctColorMoveHelper(pieceList, withinBoardList, pieceColor):
    finalList = []
    for position in withinBoardList:
        x = position[0]
        y = position[1]
        if pieceList[y][x] == None:
            finalList.append( (position) )
        elif pieceList[y][x].getColor() != pieceColor:
            finalList.append( (position) )
    return finalList


def whereCanPawnMove(pos, pieceList, color, leftBaseline, enpassantPos):
    xPos = pos[0]
    yPos = pos[1]
    forwardList = []
    if color == BLACK:
        newY = yPos + 1
        if newY < ROWS and pieceList[newY][xPos] == None:
            forwardList.append( (xPos, newY) )
            furtherY = newY + 1
            if not leftBaseline and furtherY >= 0 and pieceList[furtherY][xPos] == None:
                forwardList.append( (xPos, furtherY) )
    else:
        newY = yPos - 1
        if newY >= 0 and pieceList[newY][xPos] == None:
            forwardList.append( (xPos, newY) )
            furtherY = newY - 1
            if not leftBaseline and furtherY < ROWS and pieceList[furtherY][xPos] == None:
                forwardList.append( (xPos, furtherY) )
    finalList = forwardList + pawnCaptureHelper(pos, pieceList, color) + enpassantHelper(pos, color, enpassantPos)
    return finalList + pawnPromotionHelper(finalList, color)
    
def enpassantHelper(pos, color, enpassantPos):
    if enpassantPos == None:
        return []
    enpassantList = []
    xPos = pos[0]
    eXPos = enpassantPos[0]
    yPos = pos[1]
    eYPos = enpassantPos[1]
    if color == BLACK:
        if abs(xPos - eXPos) == 1 and yPos - eYPos == 0:
            enpassantList.append( (eXPos, eYPos + 1) )
    else:
        if abs(xPos - eXPos) == 1 and yPos - eYPos == 0:
            enpassantList.append( (eXPos, eYPos - 1) )
    return enpassantList

def pawnCaptureHelper(pos, pieceList, color):
    xPos = pos[0]
    yPos = pos[1]
    captureList = []
    newX1 = xPos - 1; newX2 = xPos + 1
    if color == BLACK:
        newY = yPos + 1
        if newY < ROWS and newX1 >= 0 and pieceList[newY][newX1] != None:
            captureList.append( (newX1, newY) )
        if newY < ROWS and newX2 < ROWS and pieceList[newY][newX2] != None:
            captureList.append( (newX2, newY) )
    else:
        newY = yPos - 1
        if newY >= 0 and newX1 >= 0 and pieceList[newY][newX1] != None:
            captureList.append( (newX1, newY) )
        if newY >= 0 and newX2 < ROWS and pieceList[newY][newX2] != None:
            captureList.append( (newX2, newY) )
    return captureList

def pawnPromotionHelper(finalList, color):
    promotionList = []
    for pos in finalList:
        if color == BLACK:
            if pos[1] == 7:
                promotionList.append("D")
                return promotionList
        else:
            if pos[1] == 0:
                promotionList.append("D")
                return promotionList
    return promotionList

                

def whereCanBishopMove(pos, pieceList, color):
    xPos = pos[0]
    yPos = pos[1]
    NEList = []; NWList = []; SEList = []; SWList = []
    toContinue = True
    res1 = bishopMoveHelper('<', xPos, xPos + 1, '<', yPos, yPos + 1, pieceList, NEList)
    res2 = bishopMoveHelper('<', xPos, xPos + 1, '>', yPos, yPos - 1, pieceList, NWList)
    res3 = bishopMoveHelper('>', xPos, xPos - 1, '<', yPos, yPos + 1, pieceList, SEList)
    res4 = bishopMoveHelper('>', xPos, xPos - 1, '>', yPos, yPos - 1, pieceList, SWList)
    uneditedList = res1 + res2 + res3 + res4
    finalList = correctColorMoveHelper(pieceList, uneditedList, color)
    return finalList
    

def bishopMoveHelper(xOps, xPos, xCounter, yOps, yPos, yCounter, pieceList, posCanMoveList):
    compOps = { '>' : operator.gt,
                '<' : operator.lt}
    toContinue = True
    if xOps =='<':
        xBound = ROWS
    else:
        xBound = -1
    if yOps == "<":
        yBound = ROWS
    else:
        yBound = -1
    while(compOps[xOps](xCounter, xBound) and compOps[yOps](yCounter, yBound) and toContinue):
        
        if pieceList[yCounter][xCounter] == None:
            posCanMoveList.append( (xCounter, yCounter) )
        else:
            posCanMoveList.append( (xCounter, yCounter) )
            toContinue = False
        
        if xOps == '<':
            xCounter += 1
        else:
            xCounter -= 1
        if yOps == '<':
            yCounter += 1
        else:
            yCounter -= 1
    return posCanMoveList

def whereCanQueenMove(pos, pieceList, color):
    uneditedList = whereCanBishopMove(pos, pieceList, color) + whereCanRookMove(pos, pieceList, color)
    finalList = correctColorMoveHelper(pieceList, uneditedList, color)
    return finalList
  

def whereCanKingMove(pos, pieceList, color):
    xPos = pos[0]
    yPos = pos[1]
    uneditedList = [(xPos + 1, yPos - 1), (xPos + 0, yPos - 1),
                    (xPos - 1, yPos - 1), (xPos - 1, yPos + 0),
                    (xPos + 1, yPos + 0), (xPos + 1, yPos + 1),
                    (xPos + 0, yPos + 1), (xPos - 1, yPos + 1)]
    withinBoardList = []
    for position in uneditedList:
        if (position[0] >= 0) and (position[0] <= 7) and (position[1] >= 0) and (position[1] <= 7 ):
            withinBoardList.append(position)
    return correctColorMoveHelper(pieceList, withinBoardList, color)
    

def whereCanKnightMove(pos, pieceList, color):
    """
    pos is a two tuple: the first element is the column, the second element is the row,
    both elements are integers between 0 and 7.
    returns a list of two tuples in which the knight can move to legitamately
    for which every element in the tuple is an integer between 0 and 7, COLUMN FIRST, ROW SECOND
    """
    xPos = pos[0]
    yPos = pos[1]
    uneditedList = [(xPos + 1, yPos + 2), (xPos + 1, yPos - 2),
                    (xPos - 1, yPos + 2), (xPos - 1, yPos - 2),
                    (xPos + 2, yPos + 1), (xPos + 2, yPos - 1),
                    (xPos - 2, yPos + 1), (xPos - 2, yPos - 1)]
    withinBoardList = []
    for position in uneditedList:
        if (position[0] >= 0) and (position[0] <= 7) and (position[1] >= 0) and (position[1] <= 7 ):
            withinBoardList.append(position)
    finalList = []
    return correctColorMoveHelper(pieceList, withinBoardList, color)


def whereCanRookMove(pos, piecesList, color):
    """
    pos is a tuple with first element as column, second element as row
    """
    xPos = pos[0]
    yPos = pos[1]
    xList1 = []; xList2 = []; yList1 = []; yList2 = []
    res1 = moveRookHelper('<', xPos, xPos + 1, yPos, None, piecesList, xList1)
    res2 = moveRookHelper('>', xPos, xPos - 1, yPos, None, piecesList, xList2)
    res3 = moveRookHelper('<', xPos, None, yPos, yPos + 1, piecesList, yList1)
    res4 = moveRookHelper('>', xPos, None, yPos, yPos - 1, piecesList, yList2)
    return correctColorMoveHelper(piecesList, res1 + res2 + res3 + res4, color)

    
def moveRookHelper(comparisonOp, xPos, xCounter, yPos, yCounter, piecesList, posCanMoveList):
    compOps = { '>' : operator.gt,
                '<' : operator.lt}
    toContinue = True
    if comparisonOp == '<':
        bound = ROWS 
    else:
        bound = -1
    if xCounter == None:
        counter = yCounter
    else:
        counter = xCounter
    while( compOps[comparisonOp](counter, bound) and toContinue):
        if xCounter == None:
            newX = xPos; newY = counter
        else:
            newX = counter; newY = yPos
        if piecesList[newY][newX] == None: # because piecesList is ordered by row, first not by column first
            posCanMoveList.append( (newX, newY) )
        else:
            posCanMoveList.append( (newX, newY) )
            toContinue = False
        if comparisonOp == '<':
            counter += 1
        else:
            counter -= 1
    return posCanMoveList
    



