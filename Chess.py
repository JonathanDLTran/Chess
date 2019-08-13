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
    
    def getPlayerName(self):
        if self.whichPlayerMove:
            return self.p1
        return self.p2
    
    def getOpposingPlayerName(self):
        if self.whichPlayerMove:
            return self.p2
        return self.p1
    
    def whichPlayer(self):
        return self.whichPlayerMove
    
    def changePlayer(self):
        self.whichPlayerMove = not self.whichPlayerMove
        
    def whichPlayerMoves(self):
        print("Player " + str(self.getPlayerName()) + " to move on this round.")
    
    def increaseRound(self):
        self.round += 1
    
    def printRound(self):
        print("This is round # " + str(self.round))
        
    def addMoves(self, movesList):
        self.gameBoardData.append(movesList)
        
    def giveColor(self):
        if self.whichPlayerMove:
            return WHITE
        return BLACK
    
    def oppositeColor(self):
        if self.whichPlayerMove:
            return BLACK
        return WHITE
    
    def printStartingRules(self):
        print('\n')
        print("This is a standard game of chess.")
        print("White moves first, and white starts at the top of the board, while black starts at the bottom.")
        print("Good Luck!")
        print('\n')
        
    """
    attributes:
    self.p1 is white
    self.p2 is Black
    whichPlayerMove: True if white's turn, which is player1, false if black, player2
    round : [int] which increases from 0
    positionsPossible : [list] of all the positions possible in each round
    gameBoardData : [List of [List]] with information about piece, location and color, a sort of memory
    """
    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.round = START
        self.whichPlayerMove = True
        self.positionsPossible = []
        self.gameBoardData = []
        self.enpassantList = []
        
        
    def initializeGameSettings(self):
        self.gameBoardData = initializeData()
        #customList1 = [('k', BLACK, 4, 0), ('k', WHITE, 6, 7), ('r', BLACK, 7, 3), ('p', WHITE, 6, 6), ('r', WHITE, 5, 7), ('p', WHITE, 5, 6), ('q', BLACK, 7, 7)]
        #customList2 = [('k', WHITE, 2, 0), ('q', BLACK, 3, 3), ('b', BLACK, 4, 3), ('k', BLACK, 4, 5)]
        #self.gameBoardData = printCustomBoard(customList2)
        self.printStartingRules()
    
    def playGame(self):
        while(True):
            self.increaseRound()
            self.printRound()
            self.whichPlayerMoves()
            currentColor = self.giveColor()
            oppositeColor = self.oppositeColor()
            currentPlayer = self.getPlayerName()
            opposingPlayer = self.getOpposingPlayerName()
            currentPiecesAlive = whichPieceAlive(currentColor, self.gameBoardData)
            oppositePiecesAlive = whichPieceAlive(oppositeColor, self.gameBoardData)
            enemyPieces = enemyAttackList(oppositeColor, oppositePiecesAlive, self.gameBoardData, self.enpassantList)
            currentPieces = whereAttack(currentColor, currentPiecesAlive, self.gameBoardData, self.enpassantList, enemyPieces)
            isKingAttacked = isKingUnderCheck(self.gameBoardData, currentColor, enemyPieces)
            

            print("Game board before move. ")
            printBoard(self.gameBoardData)

            
            if isKingAttacked:
                print(str(currentColor) + " King is under attack; You are under check.")
                legalMovesList = determineCheckmate(currentColor, oppositeColor, self.gameBoardData, currentPieces)
                if legalMovesList == []:
                    print(str(currentPlayer) + " is in checkmate.")
                    print("Game over.")
                    print("Quitting game.")
                    return
                
                playerMove = parserUnit(currentPlayer, opposingPlayer, currentPieces, self.gameBoardData, enemyPieces, currentColor, legalMovesList)
                result = self.playerMakesLegalMove(playerMove, currentColor)
                if result == False:
                    return 
                
            else:
                print("You are not under check.")
                legalMovesList = determineLegalMoves(currentColor, oppositeColor, self.gameBoardData, currentPieces)
                if legalMovesList == []:
                    print("The game is a stalemate and will end in a draw.")
                    print("Game over.")
                    print("Quitting game.")
                    return
                
                playerMove = parserUnit(currentPlayer, opposingPlayer, currentPieces, self.gameBoardData, enemyPieces, currentColor, legalMovesList)
                result = self.playerMakesLegalMove(playerMove, currentColor)
                if result == False:
                    return 
                
            print("Game board after move. ")
            printBoard(self.gameBoardData)
            self.positionsPossible.append(currentPieces)
            self.changePlayer()
            
    def playerMakesLegalMove(self, playerMove, currentColor):
        if playerMove == False:
                print("Quitting game")
                return False
        if playerMove[0] == 'castle':
            rook = playerMove[1][0]
            rookX = rook[0]
            rookY = rook[1]
            king = playerMove[1][1]
            kingX = king[0]
            kingY = king[1]
            lastPart = playerMove[2]
            if lastPart == LEFT_CASTLE:
                movePieces(king, (kingX - 2, kingY), self.gameBoardData)
                movePieces(rook, (rookX + 3, rookY), self.gameBoardData)
                kingMove((kingX - 2, kingY), self.gameBoardData)
                rookMove((rookX + 3, rookY), self.gameBoardData)
            else:
                movePieces(king, (kingX + 2, kingY), self.gameBoardData)
                movePieces(rook, (rookX - 2, rookY), self.gameBoardData)
                kingMove((kingX + 2, kingY), self.gameBoardData)
                rookMove((rookX - 2, rookY), self.gameBoardData)
            self.enpassantList = []
        else:
            pieceDict = {'p' : pawnMove,
                         'r' : rookMove,
                         'k' : kingMove}
            start = playerMove[0]
            piece = self.gameBoardData[start[1]][start[0]]
            end = playerMove[1]
            if str(piece).lower() == 'p':
                enpassantCapture(start, end, self.gameBoardData)
            movePieces(start, end, self.gameBoardData)
            if str(piece).lower() in pieceDict:
                pieceDict[str(piece).lower()](end, self.gameBoardData)
            self.enpassantList = []
            if str(piece).lower() == 'p':
                if abs(start[1] - end[1]) == 2:
                    self.enpassantList.append(end)
                promotionOfPawn(end, currentColor, self.gameBoardData)

def makeAMove(playerMove, pieceList):
    pieceDict = {'p' : pawnMove,
                 'r' : rookMove,
                 'k' : kingMove}
    start = playerMove[0]
    piece = pieceList[start[1]][start[0]]
    end = playerMove[1]
    if str(piece).lower() == 'p':
        enpassantCapture(start, end, pieceList)
    movePieces(start, end, pieceList)
    if str(piece).lower() in pieceDict:
        pieceDict[str(piece).lower()](end, pieceList)
    
def determineCheckmate(currentColor, oppositeColor, currentPieceList, currentMovesDict):
    
    leaveCheckList = []
    for key in currentMovesDict:
        start = key
        for value in currentMovesDict[key]:
            if type(value) != str:
                end = value
                copiedPieceList = copy.deepcopy(currentPieceList)
                makeAMove( (start, end), copiedPieceList)
                if (checkIfMoveIsLegal(copiedPieceList, currentColor, oppositeColor)):
                    leaveCheckList.append( end )
   
    return leaveCheckList

def checkIfMoveIsLegal(pieceList, currentColor, oppositeColor, enpassantList = []):
    oppositePiecesAlive = whichPieceAlive(oppositeColor, pieceList)
    enemyPieces = enemyAttackList(oppositeColor, oppositePiecesAlive, pieceList, enpassantList)
    return not isKingUnderCheck(pieceList, currentColor, enemyPieces)
    

def determineLegalMoves(currentColor, oppositeColor, currentPieceList, currentMovesDict):
    return determineCheckmate(currentColor, oppositeColor, currentPieceList, currentMovesDict)
        
def promotionOfPawn(position, color, pieceList):
    if color == BLACK and position[1] == 7:
        pawnPromotion(position, color, pieceList)
    elif color == WHITE and position[1] == 0:
        pawnPromotion(position, color, pieceList)

def enpassantCapture(oldPawnPos, newPawnPos, pieceList):
    """
    Use before the pawn actually moves
    """
    oldX = oldPawnPos[0]
    oldY = oldPawnPos[1]
    newX = newPawnPos[0]
    newY = newPawnPos[1]
    if newY - oldY > 0:
        if abs(oldX - newX) == 1 and pieceList[newY][newX] == None:
            pos = (newX, newY - 1)
            deletePiece(pos, pieceList)
    elif newY - oldY < 0:
        if abs(oldX - newX) == 1 and pieceList[newY][newX] == None:
            pos = (newX, newY + 1)
            deletePiece(pos, pieceList)
        
def rookMove(newRookPos, pieceList):
    x = newRookPos[0]
    y = newRookPos[1]
    rook = pieceList[y][x]
    rook.moved()
    
def kingMove(newKingPos, pieceList):
    x = newKingPos[0]
    y = newKingPos[1]
    king = pieceList[y][x]
    king.moved()
    
def pawnMove(newPawnPos, pieceList):
    x = newPawnPos[0]
    y = newPawnPos[1]
    pawn = pieceList[y][x]
    pawn.leaveBaseline()


def kingPosition(pieceList, color):
    for y in range(len(pieceList)):
        for x in range(len(pieceList[y])):
            if type(pieceList[y][x]) == King.King and pieceList[y][x].getColor() == color:
                return (x, y)
            
def isKingUnderCheck(pieceList, color, enemyAttackList):
    kingPos = kingPosition(pieceList, color)
    return kingPos in enemyAttackList
        
    
def parserUnit(currentPlayer, opposingPlayer, currentPieces, pieceList, enemyAttackList, color, legalMovesList):
    while(True):
        playerMove = parser(currentPlayer, opposingPlayer)
        if playerMove == False:
            return False
        elif type(playerMove) == tuple and playerMove[0] == 'castle':
            rookPos = playerMove[1][0]
            kingPos = playerMove[1][1]
            res = castleParserHelper(rookPos, kingPos, pieceList, enemyAttackList, color)
            if res != False:
                return list(playerMove) + res
            else:
                print("Your castling move failed. Please enter a new valid move.")
        elif playerMove != True:
            piece = playerMove[0]
            moveTo = playerMove[1]
            if piece in currentPieces and moveTo in currentPieces[piece] and moveTo in legalMovesList:
                return playerMove
            elif piece in currentPieces and moveTo in currentPieces[piece] and moveTo not in legalMovesList:
                print("That move will place your king in check. ")
            print("That move you made was not valid.")
            print("Please enter a valid move again.")
        else:
            print("Draw was declined. Please enter your move again")

def parser(currentPlayer, opposingPlayer):
    toContinue = True
    while(toContinue):
        startCoordinate = input("Please input the start coordinate as a row column pair, with space between row and column: ")
        single = parserSingleWordHelper(startCoordinate, currentPlayer, opposingPlayer)
        if single == False:
            return False
        elif single == True:
            return True
        elif type(single) == tuple:
            return single
        endCoordinate = input("Please input the end coordinate as a row column pair, with space between row and column: ")
        single = parserSingleWordHelper(endCoordinate, currentPlayer, opposingPlayer)
        if single == False:
            return False
        elif single == True:
            return True
        elif type(single) == tuple:
            return single
        lc1 = legalCoordinate(startCoordinate)
        lc2 = legalCoordinate(endCoordinate)
        if lc1 == False or lc2 == False:
            print("One of your coordinates was not formated properly.")
            print("Please type your coordinate like 'a, 6' ")
            print("Asking for coordinates again")
        elif (lc1 == lc2):
            print("The start coordinate cannot be the same as the end coordinate. ")
            print("Asking for coordinates again")
        else:
            return [lc1, lc2]
        
def parserSingleWordHelper(section, currentPlayer, opposingPlayer):
    if section.lower().strip() == 'quit':
        return False
    if section.lower().strip() == 'draw':
        drawResult = proposeDraw(currentPlayer, opposingPlayer)
        return drawResult
    if section.lower().strip() == 'resign':
        resign(currentPlayer, opposingPlayer)
        return False
    if section.lower().strip() == 'castle':
        castlePair = castle()
        return ('castle', castlePair)
    return None
    
def resign(currentPlayer, opposingPlayer):
    print(str(currentPlayer) + " is resigning this game.")
    print(str(opposingPlayer) + " has won.")
    print("Good game. Exiting program ...")
    
def proposeDraw(currentPlayer, opposingPlayer):
    toContinue = True
    while(toContinue):
        print(str(currentPlayer) + " is proposing a draw game.")
        print(str(opposingPlayer) +  " do you accept this draw game?")
        print("Please enter 'yes' or 'no' ")
        result = input("Please enter whether you accept the draw game: ").strip().lower()
        if result in DRAW_LIST:
            print(str(opposingPlayer) + " has responded with " + str(result))
            if result == 'yes':
                print("The game is a draw. Exiting program...")
            else:
                print(str(opposingPlayer)  + " has rejected your draw offer. The game will continue.")
            return result != 'yes'
        
        
def castle():
    while(True):
        print("You wish to castle. ")
        print("Please enter the first coordinate of the rook and the second coordinate of the king for which you would like to castle.")
        print("Enter each coordinate with a space between x and y coordinates, such as 'a 5' ")
        coordinate1 = input("Please input the rook's coordinate: ")
        coordinate2 = input("Please input the king's coordinate: ")
        lc1 = legalCoordinate(coordinate1)
        lc2 = legalCoordinate(coordinate2)
        if lc1 == False or lc2 == False:
            print("One of your coordinates was not formated properly.")
            print("Please type your coordinate like 'a, 6' ")
            print("Asking for coordinates again")
        elif (lc1 == lc2):
            print("The start coordinate cannot be the same as the end coordinate. ")
            print("Asking for coordinates again")
        else:
            return (lc1, lc2)

                
def legalCoordinate(coordinate):
    coordinate = coordinate.strip()
    if coordinate.find(" ") == -1:
        return False
    space = coordinate.index(' ')
    column = coordinate[:space]
    row = coordinate[space + 1:]
    row = row.strip(); column = column.strip()
    if len(row) != 1 or len(column) != 1:
        return False
    if ( not row.isnumeric() ) or ( not column.isalpha() ):
        return False
    row = int(row)
    if (row < 1) or (row > 8) or (column.upper() not in ALPHABET_ROW):
        return False
    newColumn = ord(column.upper()) - LETTER_OFFSET
    return (newColumn, row - 1)

def pawnPromotionParser():
    toContinue = True
    while(toContinue):
        print("You have reached the maximum rank that a pawn can reach.")
        print("You must promote the pawn to a queen, rook, bishop or knight of your color.")
        print("Which do you choose?")
        print("Input your choice below as 'queen', 'rook', 'bishop', or 'knight'.")
        response = input("Input your choice for piece here: ")
        response = response.lower().strip()
        if response in PROMOTION_LIST:
            print("Deleting the pawn and replacing it with your new piece")
            return response
        else:
            print("Your input was not a valid choice.")
            print("Please try again. ")
    
def pawnPromotion(position, color, pieceList):
    reply = pawnPromotionParser()
    pieceDict = {'queen' : Queen.Queen, 'rook' : Rook.Rook,
                 'bishop' : Bishop.Bishop, 'knight' : Knight.Knight}
    xPos = position[0]
    yPos = position[1]
    pieceList[yPos][xPos] = pieceDict[reply](color)
    
def whichPieceAlive(color, pieceList):
    returnList = []
    for y in range(len(pieceList)):
        for x in range(len(pieceList[y])):
            if pieceList[y][x] != None:
                if pieceList[y][x].getColor() == color:
                    returnList.append( (x, y) )
    return returnList

def enemyAttackList(color, listOfAlivePieces, pieceList, oppositeColorEnpassantList):
    pieceDict = {'n' : whereCanKnightMove,
                 'b' : whereCanBishopMove,
                 'r' : whereCanRookMove,
                 'k' : whereCanKingMove,
                 'q' : whereCanQueenMove}
    attackList = []
    for pos in listOfAlivePieces:
        piece = str(pieceList[pos[1]][pos[0]]).lower()
        if piece != 'p':
            attacks = pieceDict[piece](pos, pieceList, color)
            attackList += attacks
        else:
            pawn = pieceList[pos[1]][pos[0]]
            leftBaseline = pawn.hasLeftBaseline()
            attacks = whereCanPawnMove(pos, pieceList, color, leftBaseline, oppositeColorEnpassantList)
            attackList += attacks
    return attackList

def whereAttack(color, listOfAlivePieces, pieceList, oppositeColorEnpassantList, enemyAttackList):
    pieceDict = {'n' : whereCanKnightMove,
                 'b' : whereCanBishopMove,
                 'r' : whereCanRookMove,
                 'k' : whereCanKingMove,
                 'q' : whereCanQueenMove}
    attackDict = {}
    for pos in listOfAlivePieces:
        piece = str(pieceList[pos[1]][pos[0]]).lower()
        if piece != 'p':
            attacks = pieceDict[piece](pos, pieceList, color)
            attackDict[pos] = attacks
        else:
            pawn = pieceList[pos[1]][pos[0]]
            leftBaseline = pawn.hasLeftBaseline()
            attacks = whereCanPawnMove(pos, pieceList, color, leftBaseline, oppositeColorEnpassantList)
            attackDict[pos] = attacks
    castleList = canCastleOccur(pieceList, enemyAttackList, color)
    attackDict[CASTLE] = castleList
    return attackDict

        
        
        

def initializeEmptyData():
    gameList = []
    for i in range(ROWS):
        gameList.append(copy.deepcopy(NONE_LIST))
    return gameList

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
    print('\n')


def printCustomBoard(customList):
    """
    where custom list is a list of four tuples, the first element is piece type a single char in lowercase alphabet, e.g. 'p', second
    is color, e.g. WHITE, third is x pos, an int between 0 and 7 and fourth is y pos, an int between 0 and 7
    returns the initialized board according to how you want it
    """
    pieceDict = {'p' : Pawn.Pawn, 'b' : Bishop.Bishop,
                 'r' : Rook.Rook, 'n' : Knight.Knight,
                 'q' : Queen.Queen, 'k' : King.King}
    emptyData = initializeEmptyData()
    for piece in customList:
        pieceType = piece[0]
        color = piece[1]
        x = piece[2]
        y = piece[3]
        emptyData[y][x] = pieceDict[pieceType](color)
    printBoard(emptyData)
    return emptyData


def movePieces(pos1, pos2, pieceList):
    x1 = pos1[0]
    y1 = pos1[1]
    x2 = pos2[0]
    y2 = pos2[1]
    p1 = pieceList[y1][x1]
    p2 = pieceList[y2][x2]
    if p2 == None:
        return swapPieces(pos1, pos2, pieceList)
    pieceList[y2][x2] = p1
    pieceList[y1][x1] =  None
    
    
def swapPieces(pos1, pos2, pieceList):
    x1 = pos1[0]
    y1 = pos1[1]
    x2 = pos2[0]
    y2 = pos2[1]
    p1 = pieceList[y1][x1]
    p2 = pieceList[y2][x2]
    pieceList[y1][x1] = p2
    pieceList[y2][x2] = p1
    
def deletePiece(pos, pieceList):
    x = pos[0]
    y = pos[1]
    pieceList[y][x] = None

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

def castleParserHelper(rookPos, kingPos, pieceList, enemyAttackList, color):
    kingX = kingPos[0]
    kingY = kingPos[1]
    rookX = rookPos[0]
    rookY = rookPos[1]
    if type(pieceList[kingY][kingX]) != King.King:
        print("Your king position was not a king. Try again")
        return False
    if type(pieceList[rookY][rookX]) != Rook.Rook:
        print("Your rook position was not a rook. Try again")
        return False
    if rookX < kingX:
        return leftCastleParserHelper(rookPos, kingPos, pieceList, enemyAttackList, color)
    elif rookX > kingX:
        return rightCastleParserHelper(rookPos, kingPos, pieceList, enemyAttackList, color)
    print("King and Rook cannot castle when they are on the same column.")
    return False
    
def rightCastleParserHelper(rookPos, kingPos, pieceList, enemyAttackList, color):
    kingX = kingPos[0]
    kingY = kingPos[1]
    newKing = None
    if color == BLACK and kingX == 4 and kingY == 0:
        newKing = kingPos
    if color == WHITE and kingX == 4 and kingY == 7:
        newKing = kingPos
    if newKing == None:
        print("Your king is not in the right place to castle. ")
        return False
    
    newRook = None
    xPos = rookPos[0]
    yPos = rookPos[1]
    if color == BLACK and xPos == 7 and yPos == 0:
        newRook = rookPos
    if color == WHITE and xPos == 7 and yPos == 7:
        newRook = rookPos
    if newRook == None:
        print("Your rook is not in the right place to castle. ")
        return False
    kingX = newKing[0]
    kingY = newKing[1]
    rookX = newRook[0]
    rookY = newRook[1]
    kingPiece = pieceList[kingY][kingX]
    rookPiece = pieceList[rookY][rookX]
    if kingPiece.hasKingMoved() or rookPiece.hasRookMoved():
        print("You cannot castle because either your king or rook has moved previously. ")
        return False
    # rook is right of king and is at h1 or h8
    if color == BLACK:
        if pieceList[0][5] != None or pieceList[0][6] != None:
        # if there are any pieces on f1, g1:
            print("There are pieces between your rook and king, so you cannot castle.")
            return False
        if ((4, 0) in enemyAttackList) or ((5, 0) in enemyAttackList) or ((6, 0) in enemyAttackList):
        # if any of e1 or f1, or g1 are under attack
            print("You cannot castle because your king cannot be under check, nor can it move through a region that is under attack.")
            return False
        return [RIGHT_CASTLE]
    else:
        # if there are any pieces on f8, g8 :
        if pieceList[7][5] != None or pieceList[7][6] != None:
            print("There are pieces between your rook and king, so you cannot castle.")
            return False
        if ((4, 7) in enemyAttackList) or ((5, 7) in enemyAttackList) or ((6, 7) in enemyAttackList):
        # if any of  e8 or f8, or g8 are under attack
            print("You cannot castle because your king cannot be under check, nor can it move through a region that is under attack.")
            return False
        return [RIGHT_CASTLE]

def leftCastleParserHelper(rookPos, kingPos, pieceList, enemyAttackList, color):
    kingX = kingPos[0]
    kingY = kingPos[1]
    newKing = None
    if color == BLACK and kingX == 4 and kingY == 0:
        newKing = kingPos
    if color == WHITE and kingX == 4 and kingY == 7:
        newKing = kingPos
    if newKing == None:
        print("Your king is not in the right place to castle. ")
        return False
    newRook = None
    
    xPos = rookPos[0]
    yPos = rookPos[1]
    if color == BLACK and xPos == 0 and yPos == 0:
        newRook = rookPos
    if color == WHITE and xPos == 0 and yPos == 7:
        newRook = rookPos
    if newRook == None:
        print("Your rook is not in the right place to castle. ")
        return False
    # rook is left of king, and is at a1 or a8
    kingX = newKing[0]
    kingY = newKing[1]
    rookX = newRook[0]
    rookY = newRook[1]
    kingPiece = pieceList[kingY][kingX]
    rookPiece = pieceList[rookY][rookX]
    if kingPiece.hasKingMoved() or rookPiece.hasRookMoved():
        print("You cannot castle because either your king or rook has moved previously. ")
        return False
    if color == BLACK:
        # if king or rook has moved:
        # if there are any pieces on b1, c1 or d1:
        if pieceList[0][1] != None or pieceList[0][2] != None or pieceList[0][3] != None:
            print("There are pieces between your rook and king, so you cannot castle.")
            return False
        # if any of c1 or d1, or e1 are under attack
        if ((2, 0) in enemyAttackList) or ((3, 0) in enemyAttackList) or ((4, 0) in enemyAttackList):
            print("You cannot castle because your king cannot be under check, nor can it move through a region that is under attack.")
            return False
        return [LEFT_CASTLE]
    else:
        if pieceList[7][1] != None or pieceList[7][2] != None or pieceList[7][3] != None:
        # if there are any pieces on b8, c8 or d8:
            print("There are pieces between your rook and king, so you cannot castle.")
            return False
        if ((2, 7) in enemyAttackList) or ((3, 7) in enemyAttackList) or ((4, 7) in enemyAttackList):
        # if any of  c8 or d8, or e8 are under attack
            print("You cannot castle because your king cannot be under check, nor can it move through a region that is under attack.")
            return False
        return [LEFT_CASTLE]
    
    

def canCastleOccur(pieceList, enemyAttackList, color):
    king = None
    rookList = []
    for y in range(len(pieceList)):
        for x in range(len(pieceList[y])):
            piece = pieceList[y][x]
            if type(piece) == King.King and piece.getColor() == color:
                king = (x, y)
            elif type(piece) == Rook.Rook and piece.getColor() == color:
                rookList.append( (x, y) )
    c1 = leftCastleHelper(king, rookList, pieceList, enemyAttackList, color)
    c2 = rightCastleHelper(king, rookList, pieceList, enemyAttackList, color)
    return c1 + c2

def leftCastleHelper(king, rookList, pieceList, enemyAttackList, color):
    castleList = []
    if king == None or rookList == []:
        return castleList
    kingX = king[0]
    kingY = king[1]
    newKing = None
    if color == BLACK and kingX == 4 and kingY == 0:
        newKing = king
    if color == WHITE and kingX == 4 and kingY == 7:
        newKing = king
    if newKing == None:
        return castleList
    newRook = None
    for rook in rookList:
        xPos = rook[0]
        yPos = rook[1]
        if color == BLACK and xPos == 0 and yPos == 0:
            newRook = rook
        if color == WHITE and xPos == 0 and yPos == 7:
            newRook = rook
    if newRook == None:
        return castleList
    # rook is left of king, and is at a1 or a8
    kingX = newKing[0]
    kingY = newKing[1]
    rookX = newRook[0]
    rookY = newRook[1]
    kingPiece = pieceList[kingY][kingX]
    rookPiece = pieceList[rookY][rookX]
    if kingPiece.hasKingMoved() or rookPiece.hasRookMoved():
        return castleList
    if color == BLACK:
        # if king or rook has moved:
        # if there are any pieces on b1, c1 or d1:
        if pieceList[0][1] != None or pieceList[0][2] != None or pieceList[0][3] != None:
            return castleList
        # if any of c1 or d1, or e1 are under attack
        if ((2, 0) in enemyAttackList) or ((3, 0) in enemyAttackList) or ((4, 0) in enemyAttackList):
            return castleList
        return [LEFT_CASTLE]
    else:
        if pieceList[7][1] != None or pieceList[7][2] != None or pieceList[7][3] != None:
        # if there are any pieces on b8, c8 or d8:
            return castleList
        if ((2, 7) in enemyAttackList) or ((3, 7) in enemyAttackList) or ((4, 7) in enemyAttackList):
        # if any of  c8 or d8, or e8 are under attack
            return castleList
        return [LEFT_CASTLE]
        
        

def rightCastleHelper(king, rookList, pieceList, enemyAttackList, color):
    castleList = []
    if king == None or rookList == []:
        return castleList
    
    kingX = king[0]
    kingY = king[1]
    newKing = None
    if color == BLACK and kingX == 4 and kingY == 0:
        newKing = king
    if color == WHITE and kingX == 4 and kingY == 7:
        newKing = king
    if newKing == None:
        return castleList
    newRook = None
    for rook in rookList:
        xPos = rook[0]
        yPos = rook[1]
        if color == BLACK and xPos == 7 and yPos == 0:
            newRook = rook
        if color == WHITE and xPos == 7 and yPos == 7:
            newRook = rook
    if newRook == None:
        return castleList
    kingX = newKing[0]
    kingY = newKing[1]
    rookX = newRook[0]
    rookY = newRook[1]
    kingPiece = pieceList[kingY][kingX]
    rookPiece = pieceList[rookY][rookX]
    if kingPiece.hasKingMoved() or rookPiece.hasRookMoved():
            return castleList
    # rook is right of king and is at h1 or h8
    if color == BLACK:
        if pieceList[0][5] != None or pieceList[0][6] != None:
        # if there are any pieces on f1, g1:
            return castleList
        if ((4, 0) in enemyAttackList) or ((5, 0) in enemyAttackList) or ((6, 0) in enemyAttackList):
        # if any of e1 or f1, or g1 are under attack
            return castleList
        return [RIGHT_CASTLE]
    else:
        # if there are any pieces on f8, g8 :
        if pieceList[7][5] != None or pieceList[7][6] != None:
            return castleList
        if ((4, 7) in enemyAttackList) or ((5, 7) in enemyAttackList) or ((6, 7) in enemyAttackList):
        # if any of  e8 or f8, or g8 are under attack
            return castleList
        return [RIGHT_CASTLE]

def whereCanPawnMove(pos, pieceList, color, leftBaseline, enpassantPos):
    xPos = pos[0]
    yPos = pos[1]
    forwardList = []
    if color == BLACK:
        newY = yPos + 1
        if newY < ROWS and pieceList[newY][xPos] == None:
            forwardList.append( (xPos, newY) )
            furtherY = newY + 1
            if not leftBaseline and furtherY >= 0 and furtherY <= 7 and pieceList[furtherY][xPos] == None:
                forwardList.append( (xPos, furtherY) )
    else:
        newY = yPos - 1
        if newY >= 0 and pieceList[newY][xPos] == None:
            forwardList.append( (xPos, newY) )
            furtherY = newY - 1
            if not leftBaseline and furtherY >= 0 and furtherY < ROWS and pieceList[furtherY][xPos] == None:
                forwardList.append( (xPos, furtherY) )
    finalList = forwardList + pawnCaptureHelper(pos, pieceList, color) + enpassantHelper(pos, pieceList, color, enpassantPos)
    return finalList + pawnPromotionHelper(finalList, color)
    
def enpassantHelper(pos, pieceList, color, enpassantPos):
    if enpassantPos == []:
        return []
    enpassantList = []
    xPos = pos[0]
    yPos = pos[1]
    for pos in enpassantPos:
        eXPos = pos[0]
        eYPos = pos[1]
        if color == BLACK:
            if abs(xPos - eXPos) == 1 and yPos - eYPos == 0:
                if (pieceList[eYPos + 1][eXPos] == None):
                    enpassantList.append( (eXPos, eYPos + 1) )
        else:
            if abs(xPos - eXPos) == 1 and yPos - eYPos == 0:
                if (pieceList[eYPos - 1][eXPos] == None):
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

def askName():
    playerName = input("Please enter your name: ")
    return playerName

if __name__ == '__main__':
    print("Chess v1.01")
    print("Player1 is WHITE")
    print("Player 1, please enter your name. ")
    player1 = askName()
    print("Player2 is BLACK")
    print("Player 2, please enter your name. ")
    player2 = askName()
    game = Chess(player1, player2)
    game.initializeGameSettings()
    game.playGame()


