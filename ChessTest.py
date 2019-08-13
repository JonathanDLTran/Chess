from Chess import *
from Constants import *

def testParser():
    print("testing Parser")
    currentPlayer = "Edward"
    opposingPlayer = "SheldonMike"
    parser(currentPlayer, opposingPlayer)
    print("Pass parser")

def testKnightMove():
    print("Testing knight moves")
    # Standard case
    color = WHITE
    gameList = initializeData()
    printBoard(gameList)
    pos = (3, 3) # column 3, row 3
    assert set(whereCanKnightMove(pos, gameList, color)) == set([(2, 1), (1, 2), (1, 4), (2, 5), (4, 5), (5, 4), (5, 2), (4, 1)])
    
    color = BLACK
    pos = (3, 3) # column 3, row 3
    assert set(whereCanKnightMove(pos, gameList, color)) == set([(1, 2), (1, 4), (2, 5), (4, 5), (5, 4), (5, 2)])
    
    color = WHITE
    pos = (0, 7)
    assert set(whereCanKnightMove(pos, gameList, color)) == set([(1, 5)])
    
    color = BLACK
    pos = (0, 7)
    assert set(whereCanKnightMove(pos, gameList, color)) == set([(1, 5),  (2, 6)])
    
    color = WHITE
    pos = (5, 1)
    assert set(whereCanKnightMove(pos, gameList, color)) == set([(3, 0), (3, 2), (4, 3), (6, 3), (7, 2), (7, 0)])
    
    color = BLACK
    pos = (5, 1)
    assert set(whereCanKnightMove(pos, gameList, color)) == set([(3, 2), (4, 3), (6, 3), (7, 2)])
    print("Pass knight moves")
    
def testRookMove():
    print("test rook moves")
    color = WHITE
    gameList = initializeData()
    printBoard(gameList)
    pos = (3, 4)
    assert set(whereCanRookMove(pos, gameList, color)) == set([(0, 4), (1, 4), (2, 4), (4, 4), (5, 4), (6, 4), (7, 4), (3, 1), (3, 2), (3, 3), (3, 5)])
    
    color = BLACK
    pos = (3, 4)
    assert set(whereCanRookMove(pos, gameList, color)) == set([(0, 4), (1, 4), (2, 4), (4, 4), (5, 4), (6, 4), (7, 4), (3, 2), (3, 3), (3, 5), (3, 6)])  
    
    color = WHITE
    pos = (0, 0)
    assert set(whereCanRookMove(pos, gameList, color)) == set([(0, 1), (1, 0)])
    
    color = BLACK
    pos = (0, 0)
    assert set(whereCanRookMove(pos, gameList, color)) == set([])
    
    color = WHITE 
    pos = (0, 5)
    assert set(whereCanRookMove(pos, gameList, color)) == set([(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (0, 1), (0, 2), (0, 3), (0, 4)])
    
    color = BLACK
    pos = (0, 5)
    assert set(whereCanRookMove(pos, gameList, color)) == set([(1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (0, 2), (0, 3), (0, 4), (0, 6)])
    
    #####TODO: ADD TESTS WHERE GAME LIST CHNANGES
    
    print("pass rook moves")
    
def testBishopMove():
    print("Test bishop moves")
    color = WHITE
    gameList = initializeData()
    pos = (3, 3)
    assert set(whereCanBishopMove(pos, gameList, color)) == set([(1, 1), (1, 5), (2, 4), (2, 2), (4, 2), (4, 4), (5, 5), (5, 1)])
    
    color = BLACK
    pos = (3, 3)
    assert set(whereCanBishopMove(pos, gameList, color)) == set([(0, 6), (1, 5), (2, 4), (2, 2), (4, 2), (4, 4), (5, 5), (6, 6)])
    
    color = WHITE
    pos = (0, 7)
    assert set(whereCanBishopMove(pos, gameList, color)) == set([])
    
    color = BLACK
    pos = (0, 7)
    assert set(whereCanBishopMove(pos, gameList, color)) == set([(1, 6)])
   
    color = WHITE
    pos = (6, 1)
    assert set(whereCanBishopMove(pos, gameList, color)) == set([(7, 2), (7, 0), (5, 0), (5, 2), (4, 3), (3, 4), (2, 5)])
    
    color = BLACK
    pos = (6, 1)
    assert set(whereCanBishopMove(pos, gameList, color)) == set([(7, 2), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6)])

    print("Pass Bishop moves")
    
def testKingMove():
    print("Test king")
    color = WHITE
    gameList = initializeData()
    pos = (5, 3)
    assert set(whereCanKingMove(pos, gameList, color)) == set([(4, 2), (5, 2), (6, 2), (4, 3), (6, 3), (4, 4), (5, 4), (6, 4)])
    
    color = BLACK
    pos = (5, 3)
    assert set(whereCanKingMove(pos, gameList, color)) == set([(4, 2), (5, 2), (6, 2), (4, 3), (6, 3), (4, 4), (5, 4), (6, 4)])

    color = WHITE
    pos = (0, 7)
    assert set(whereCanKingMove(pos, gameList, color)) == set([])

    color = BLACK
    pos = (0, 7)
    assert set(whereCanKingMove(pos, gameList, color)) == set([(0, 6), (1, 7), (1, 6)])
    
    print("pass King")
    
def testQueenMove():
    print("test queen")
    color = WHITE
    gameList = initializeData()
    pos = (3, 4)
    assert set(whereCanQueenMove(pos, gameList, color)) == set([(0, 1), (1, 2), (2, 3), (3, 3), (3, 2), (3, 1), (4, 3), (5, 2), (6, 1), (0, 4), (1, 4), (2, 4), (4, 4), (5, 4), (6, 4), (7, 4), (2, 5), (3, 5), (4, 5)])
    
    color = BLACK
    gameList = initializeData()
    pos = (3, 4)
    assert set(whereCanQueenMove(pos, gameList, color)) == set([(1, 2), (2, 3), (3, 3), (3, 2), (4, 3), (5, 2), (0, 4), (1, 4), (2, 4), (4, 4), (5, 4), (6, 4), (7, 4), (2, 5), (3, 5), (4, 5), (1, 6), (3, 6), (5, 6)])
    
    print("pass queen")
    
def testPawnMove():
    print("Test pawn")
    color = WHITE
    gameList = initializeData()
    pos = (4, 6)
    leftBaseline = False
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(4, 5), (4, 4)])
    
    color = WHITE
    gameList = initializeData()
    pos = (4, 6)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(4, 5)])
    
    color = BLACK
    gameList = initializeData()
    pos = (4, 6)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(3, 7), (5, 7), "D"])
    
    color = BLACK
    gameList = initializeData()
    pos = (0, 6)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(1, 7), "D"])
    
    
    color = BLACK
    gameList = initializeData()
    pos = (7, 6)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(6, 7), "D"])
    
    color = BLACK
    gameList = initializeData()
    pos = (7, 7)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([])
    
    color = BLACK
    gameList = initializeData()
    pos = (4, 4)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(4, 5)])
    
    color = WHITE
    gameList = initializeData()
    pos = (2, 4)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(2, 3)])
    
    color = WHITE
    gameList = initializeData()
    pos = (0, 2)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(1, 1)])
    
    color = WHITE
    gameList = initializeData()
    pos = (5, 2)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(4, 1), (6, 1)])
    
    
    color = WHITE
    gameList = initializeData()
    pos = (7, 2)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(6, 1)])
    
    color = WHITE
    gameList = initializeData()
    pos = (0, 2)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(1, 1)])
    
    
    color = WHITE
    gameList = initializeData()
    pos = (0, 0)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([])
    
    color = WHITE
    gameList = initializeData()
    pos = (3, 1)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(2, 0), (4, 0), "D"])
    
    color = WHITE
    gameList = initializeData()
    pos = (0, 1)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(1, 0), "D"])
    
    color = WHITE
    gameList = initializeData()
    pos = (4, 1)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(3, 0), (5, 0), "D"])
    
    
    color = WHITE
    gameList = initializeData()
    pos = (7, 1)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(6, 0), "D"])
    
    color = BLACK
    gameList = initializeData()
    pos = (3, 1)
    leftBaseline = False
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(3, 2), (3, 3)])
    
    color = BLACK
    gameList = initializeData()
    pos = (3, 1)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(3, 2)])
    
    color = BLACK
    gameList = initializeData()
    pos = (3, 2)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(3, 3)])
    
    
    color = BLACK
    gameList = initializeData()
    pos = (7, 1)
    leftBaseline = False
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(7, 2), (7, 3)])
    
    
    color = BLACK
    gameList = initializeData()
    pos = (7, 1)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(7, 2)])
    
    color = BLACK
    gameList = initializeData()
    pos = (0, 1)
    leftBaseline = False
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(0, 2), (0, 3)])
    
    
    color = BLACK
    gameList = initializeData()
    pos = (0, 1)
    leftBaseline = True
    enpassantPos = []
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(0, 2)])
    
    
    #test en passant
    color = BLACK
    gameList = initializeData()
    pos = (1, 4)
    leftBaseline = True
    enpassantPos = [(0, 4)]
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(0, 5), (1, 5)])
    
    color = BLACK
    gameList = initializeData()
    pos = (1, 4)
    leftBaseline = True
    enpassantPos = [(2, 4)]
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(2, 5), (1, 5)])
    
    color = BLACK
    gameList = initializeData()
    pos = (2, 4)
    leftBaseline = True
    enpassantPos = [(0, 4)]
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(2, 5)])
    
    color = BLACK
    gameList = initializeData()
    pos = (2, 4)
    leftBaseline = True
    enpassantPos = [(4, 4)]
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(2, 5)])
    
    color = BLACK
    gameList = initializeData()
    pos = (1, 3)
    leftBaseline = True
    enpassantPos = [(0, 4)]
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(1, 4)])
    
    color = WHITE
    gameList = initializeData()
    pos = (1, 3)
    leftBaseline = True
    enpassantPos = [(0, 3)]
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(1, 2), (0, 2)])
    
    
    print("pass pawn")
    
def testCustomBoard():
    print("testing custom Board")
    customList = [('p', BLACK, 0, 0)]
    printCustomBoard(customList)
    
    customList = [('p', BLACK, 7, 7)]
    printCustomBoard(customList)
    
    customList = [('p', BLACK, 3, 5)]
    printCustomBoard(customList)
    
    customList = [('p', WHITE, 0, 0)]
    printCustomBoard(customList)
    
    customList = [('p', WHITE, 7, 7)]
    printCustomBoard(customList)
    
    customList = [('p', WHITE, 3, 5)]
    printCustomBoard(customList)
    
    customList = [('p', WHITE, 3, 5), ('k', WHITE, 2, 1), ('r', BLACK, 0, 0), ('n', BLACK, 3, 4), ('b', WHITE, 7, 1), ('q', BLACK, 4, 4)]
    newBoard = printCustomBoard(customList)
    
    deletePos = (3, 5)
    deletePiece(deletePos, newBoard)
    printBoard(newBoard)
    deletePos = (2, 1)
    deletePiece(deletePos, newBoard)
    printBoard(newBoard)
    deletePos = (0, 0)
    deletePiece(deletePos, newBoard)
    printBoard(newBoard)
    deletePos = (3, 4)
    deletePiece(deletePos, newBoard)
    printBoard(newBoard)
    deletePos = (7, 1)
    deletePiece(deletePos, newBoard)
    printBoard(newBoard)
    deletePos = (4, 4)
    deletePiece(deletePos, newBoard)
    printBoard(newBoard)
    
    customList = [('p', WHITE, 3, 5), ('p', BLACK, 3, 6), ('p', BLACK, 0, 6), ('p', BLACK, 7, 2), ('k', WHITE, 2, 1), ('r', BLACK, 0, 0), ('n', BLACK, 3, 4), ('b', WHITE, 7, 1), ('q', BLACK, 4, 4)]
    newBoard = printCustomBoard(customList)
    swapPieces((3, 5), (0, 6), newBoard)
    printBoard(newBoard)
    
    customList = [('p', WHITE, 3, 5), ('p', WHITE, 0, 6), ('p', BLACK, 7, 2), ('k', WHITE, 2, 1), ('r', BLACK, 0, 0), ('n', BLACK, 3, 4), ('b', WHITE, 7, 1), ('q', BLACK, 4, 4)]
    newBoard = printCustomBoard(customList)
    swapPieces((3, 5), (0, 6), newBoard)
    printBoard(newBoard)
    
    customList = [('p', WHITE, 3, 5), ('p', BLACK, 0, 6), ('p', BLACK, 7, 2), ('k', WHITE, 2, 1), ('r', BLACK, 0, 0), ('n', BLACK, 3, 4), ('b', WHITE, 7, 1), ('q', BLACK, 4, 4)]
    newBoard = printCustomBoard(customList)
    swapPieces((2, 1), (4, 4), newBoard)
    printBoard(newBoard)
    
    customList = [('p', WHITE, 3, 5), ('p', BLACK, 0, 6), ('p', BLACK, 7, 2), ('k', WHITE, 2, 1), ('r', WHITE, 1, 1), ('r', BLACK, 0, 0), ('n', BLACK, 3, 4), ('b', WHITE, 7, 1), ('q', BLACK, 4, 4)]
    newBoard = printCustomBoard(customList)
    swapPieces((0, 0), (1, 1), newBoard)
    printBoard(newBoard)
    
    customList = [('p', WHITE, 3, 5), ('p', BLACK, 0, 6), ('p', BLACK, 7, 2), ('k', WHITE, 2, 1), ('r', WHITE, 1, 1), ('r', BLACK, 0, 0), ('n', BLACK, 3, 4), ('b', WHITE, 7, 1), ('q', BLACK, 4, 4)]
    newBoard = printCustomBoard(customList)
    movePieces((4, 4), (5, 5), newBoard)
    printBoard(newBoard)

    movePieces((5, 5), (3, 5), newBoard)
    printBoard(newBoard)
    
    movePieces((3, 5), (0, 6), newBoard)
    printBoard(newBoard)
    
    movePieces((0, 6), (7, 2), newBoard)
    printBoard(newBoard)
    
    movePieces((7, 2), (2, 1), newBoard)
    printBoard(newBoard)
    
    movePieces((2, 1), (1, 1), newBoard)
    printBoard(newBoard)
    
    movePieces((1, 1), (0, 0), newBoard)
    printBoard(newBoard)
    
    movePieces((0, 0), (3, 4), newBoard)
    printBoard(newBoard)
    
    movePieces((3, 4), (7, 1), newBoard)
    printBoard(newBoard)
    
    movePieces((7, 1), (4, 4), newBoard)
    printBoard(newBoard)
    
    deletePiece((4, 4), newBoard)
    printBoard(newBoard)
    
    print("pass custom board")
    
def testCastleMove():
    print("test castle")
    color = WHITE
    gameList = initializeData()
    customList = [('k', WHITE, 4, 7), ('r', WHITE, 0, 7), ('r', WHITE, 7, 7)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = []
    assert canCastleOccur(newBoard, enemyAttackList, color) == [LEFT_CASTLE, RIGHT_CASTLE]
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 7), ('r', BLACK, 0, 7), ('r', BLACK, 7, 7)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = []
    assert canCastleOccur(newBoard, enemyAttackList, color) == []
    
    color = WHITE
    gameList = initializeData()
    customList = [('k', WHITE, 4, 0), ('r', WHITE, 0, 0), ('r', WHITE, 7, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = []
    assert canCastleOccur(newBoard, enemyAttackList, color) == []
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = []
    assert canCastleOccur(newBoard, enemyAttackList, color) == [LEFT_CASTLE, RIGHT_CASTLE]
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0), ('p', BLACK, 5, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = []
    assert canCastleOccur(newBoard, enemyAttackList, color) == [LEFT_CASTLE]
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0), ('b', BLACK, 2, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = []
    assert canCastleOccur(newBoard, enemyAttackList, color) == [RIGHT_CASTLE]
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0), ('p', WHITE, 1, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = []
    assert canCastleOccur(newBoard, enemyAttackList, color) == [RIGHT_CASTLE]
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0), ('p', WHITE, 6, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = []
    assert canCastleOccur(newBoard, enemyAttackList, color) == [LEFT_CASTLE]
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0), ('q', BLACK, 2, 0), ('p', BLACK, 3, 0), ('b', BLACK, 5, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = []
    assert canCastleOccur(newBoard, enemyAttackList, color) == []
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0), ('p', WHITE, 2, 0), ('p', WHITE, 5, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = []
    assert canCastleOccur(newBoard, enemyAttackList, color) == []
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = []
    assert canCastleOccur(newBoard, enemyAttackList, color) == []
    
    color = BLACK
    gameList = initializeData()
    customList = [('r', BLACK, 0, 0), ('r', BLACK, 7, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = []
    assert canCastleOccur(newBoard, enemyAttackList, color) == []
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = []
    assert canCastleOccur(newBoard, enemyAttackList, color) == [LEFT_CASTLE]
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 7, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = []
    assert canCastleOccur(newBoard, enemyAttackList, color) == [RIGHT_CASTLE]
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 5, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = []
    assert canCastleOccur(newBoard, enemyAttackList, color) == []
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 1, 0), ('r', BLACK, 7, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = []
    assert canCastleOccur(newBoard, enemyAttackList, color) == [RIGHT_CASTLE]
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 6, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = []
    assert canCastleOccur(newBoard, enemyAttackList, color) == [LEFT_CASTLE]
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(2, 0)]
    assert canCastleOccur(newBoard, enemyAttackList, color) == [RIGHT_CASTLE]
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(3, 0)]
    assert canCastleOccur(newBoard, enemyAttackList, color) == [RIGHT_CASTLE]
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(4, 0)]
    assert canCastleOccur(newBoard, enemyAttackList, color) == []
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(5, 0)]
    assert canCastleOccur(newBoard, enemyAttackList, color) == [LEFT_CASTLE]
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(6, 0)]
    assert canCastleOccur(newBoard, enemyAttackList, color) == [LEFT_CASTLE]
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(0, 0)]
    assert canCastleOccur(newBoard, enemyAttackList, color) == [LEFT_CASTLE, RIGHT_CASTLE]
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(7, 0)]
    assert canCastleOccur(newBoard, enemyAttackList, color) == [LEFT_CASTLE, RIGHT_CASTLE]
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(0, 0), (7, 0)]
    assert canCastleOccur(newBoard, enemyAttackList, color) == [LEFT_CASTLE, RIGHT_CASTLE]
    
        
    color = WHITE
    gameList = initializeData()
    customList = [('k', WHITE, 4, 7), ('r', WHITE, 0, 7), ('r', WHITE, 7, 7)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(2, 7)]
    assert canCastleOccur(newBoard, enemyAttackList, color) == [RIGHT_CASTLE]
    
    color = WHITE
    gameList = initializeData()
    customList = [('k', WHITE, 4, 7), ('r', WHITE, 0, 7), ('r', WHITE, 7, 7)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(3, 7)]
    assert canCastleOccur(newBoard, enemyAttackList, color) == [RIGHT_CASTLE]
    
    color = WHITE
    gameList = initializeData()
    customList = [('k', WHITE, 4, 7), ('r', WHITE, 0, 7), ('r', WHITE, 7, 7)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(4, 7)]
    assert canCastleOccur(newBoard, enemyAttackList, color) == []
    
    color = WHITE
    gameList = initializeData()
    customList = [('k', WHITE, 4, 7), ('r', WHITE, 0, 7), ('r', WHITE, 7, 7)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(5, 7)]
    assert canCastleOccur(newBoard, enemyAttackList, color) == [LEFT_CASTLE]
    
    color = WHITE
    gameList = initializeData()
    customList = [('k', WHITE, 4, 7), ('r', WHITE, 0, 7), ('r', WHITE, 7, 7)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(6, 7)]
    assert canCastleOccur(newBoard, enemyAttackList, color) == [LEFT_CASTLE]
    
    color = WHITE
    gameList = initializeData()
    customList = [('k', WHITE, 4, 7), ('r', WHITE, 0, 7), ('r', WHITE, 7, 7)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(0, 7)]
    assert canCastleOccur(newBoard, enemyAttackList, color) == [LEFT_CASTLE, RIGHT_CASTLE]
    
    color = WHITE
    gameList = initializeData()
    customList = [('k', WHITE, 4, 7), ('r', WHITE, 0, 7), ('r', WHITE, 7, 7)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(7, 7)]
    assert canCastleOccur(newBoard, enemyAttackList, color) == [LEFT_CASTLE, RIGHT_CASTLE]
    
    color = WHITE
    gameList = initializeData()
    customList = [('k', WHITE, 4, 7), ('r', WHITE, 0, 7), ('r', WHITE, 7, 7)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(0, 7), (7, 7)]
    assert canCastleOccur(newBoard, enemyAttackList, color) == [LEFT_CASTLE, RIGHT_CASTLE]
    
    color = WHITE
    gameList = initializeData()
    customList = [('k', WHITE, 4, 7), ('r', WHITE, 0, 7), ('r', WHITE, 7, 7)]
    newBoard = printCustomBoard(customList)
    king = newBoard[7][4]
    king.moved()
    enemyAttackList = [(0, 7), (7, 7)]
    assert canCastleOccur(newBoard, enemyAttackList, color) == []
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(0, 7), (7, 7)]
    king = newBoard[0][4]
    king.moved()
    assert canCastleOccur(newBoard, enemyAttackList, color) == []
    
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(0, 7), (7, 7)]
    rook = newBoard[0][0]
    rook.moved()
    assert canCastleOccur(newBoard, enemyAttackList, color) == [RIGHT_CASTLE]
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(0, 7), (7, 7)]
    rook = newBoard[0][7]
    rook.moved()
    assert canCastleOccur(newBoard, enemyAttackList, color) == [LEFT_CASTLE]
    
    color = BLACK
    gameList = initializeData()
    customList = [('k', BLACK, 4, 0), ('r', BLACK, 0, 0), ('r', BLACK, 7, 0)]
    newBoard = printCustomBoard(customList)
    enemyAttackList = [(0, 7), (7, 7)]
    rook1 = newBoard[0][0]
    rook1.moved()
    rook2 = newBoard[0][7]
    rook2.moved()
    assert canCastleOccur(newBoard, enemyAttackList, color) == []
    
    
    print("Pass castle")
    
def testPawnPromotion():
    print("test pawn promotion")
    position = (5, 0)
    color = WHITE
    customList = [('p', WHITE, 5, 0)]
    newBoard = printCustomBoard(customList)
    pawnPromotion(position, color, newBoard)
    printBoard(newBoard)
    
    position = (3, 7)
    color = BLACK
    customList = [('p', WHITE, 3, 7)]
    newBoard = printCustomBoard(customList)
    pawnPromotion(position, color, newBoard)
    printBoard(newBoard)
    print("pass pawn promotion")

#testParser()
testKnightMove()
testRookMove()
testBishopMove()
testKingMove()
testQueenMove()
testPawnMove()
testCustomBoard()
testCastleMove()
#testPawnPromotion()