from Chess import *
from Constants import *

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
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(4, 5), (4, 4)])
    
    color = WHITE
    gameList = initializeData()
    pos = (4, 6)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(4, 5)])
    
    color = BLACK
    gameList = initializeData()
    pos = (4, 6)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(3, 7), (5, 7), "D"])
    
    color = BLACK
    gameList = initializeData()
    pos = (0, 6)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(1, 7), "D"])
    
    
    color = BLACK
    gameList = initializeData()
    pos = (7, 6)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(6, 7), "D"])
    
    color = BLACK
    gameList = initializeData()
    pos = (7, 7)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([])
    
    color = BLACK
    gameList = initializeData()
    pos = (4, 4)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(4, 5)])
    
    color = WHITE
    gameList = initializeData()
    pos = (2, 4)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(2, 3)])
    
    color = WHITE
    gameList = initializeData()
    pos = (0, 2)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(1, 1)])
    
    color = WHITE
    gameList = initializeData()
    pos = (5, 2)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(4, 1), (6, 1)])
    
    
    color = WHITE
    gameList = initializeData()
    pos = (7, 2)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(6, 1)])
    
    color = WHITE
    gameList = initializeData()
    pos = (0, 2)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(1, 1)])
    
    
    color = WHITE
    gameList = initializeData()
    pos = (0, 0)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([])
    
    color = WHITE
    gameList = initializeData()
    pos = (3, 1)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(2, 0), (4, 0), "D"])
    
    color = WHITE
    gameList = initializeData()
    pos = (0, 1)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(1, 0), "D"])
    
    color = WHITE
    gameList = initializeData()
    pos = (4, 1)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(3, 0), (5, 0), "D"])
    
    
    color = WHITE
    gameList = initializeData()
    pos = (7, 1)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(6, 0), "D"])
    
    color = BLACK
    gameList = initializeData()
    pos = (3, 1)
    leftBaseline = False
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(3, 2), (3, 3)])
    
    color = BLACK
    gameList = initializeData()
    pos = (3, 1)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(3, 2)])
    
    color = BLACK
    gameList = initializeData()
    pos = (3, 2)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(3, 3)])
    
    
    color = BLACK
    gameList = initializeData()
    pos = (7, 1)
    leftBaseline = False
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(7, 2), (7, 3)])
    
    
    color = BLACK
    gameList = initializeData()
    pos = (7, 1)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(7, 2)])
    
    color = BLACK
    gameList = initializeData()
    pos = (0, 1)
    leftBaseline = False
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(0, 2), (0, 3)])
    
    
    color = BLACK
    gameList = initializeData()
    pos = (0, 1)
    leftBaseline = True
    enpassantPos = None
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(0, 2)])
    
    
    #test en passant
    color = BLACK
    gameList = initializeData()
    pos = (1, 4)
    leftBaseline = True
    enpassantPos = (0, 4)
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(0, 5), (1, 5)])
    
    color = BLACK
    gameList = initializeData()
    pos = (1, 4)
    leftBaseline = True
    enpassantPos = (2, 4)
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(2, 5), (1, 5)])
    
    color = BLACK
    gameList = initializeData()
    pos = (2, 4)
    leftBaseline = True
    enpassantPos = (0, 4)
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(2, 5)])
    
    color = BLACK
    gameList = initializeData()
    pos = (2, 4)
    leftBaseline = True
    enpassantPos = (4, 4)
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(2, 5)])
    
    color = BLACK
    gameList = initializeData()
    pos = (1, 3)
    leftBaseline = True
    enpassantPos = (0, 4)
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(1, 4)])
    
    color = WHITE
    gameList = initializeData()
    pos = (1, 3)
    leftBaseline = True
    enpassantPos = (0, 3)
    assert set(whereCanPawnMove(pos, gameList, color, leftBaseline, enpassantPos)) == set([(1, 2), (0, 2)])
    
    
    print("pass pawn")
    
testKnightMove()
testRookMove()
testBishopMove()
testKingMove()
testQueenMove()
testPawnMove()