import Piece
from Constants import *

class Knight(Piece.Piece):
    
    def __init__(self, color):
        super().__init__(color)
        
    def legalMove(self, piecesData, position1, position2):
        if abs(position1[0] - position2[0]) == 1 and abs(position1[1] - position2[1]) == 3:
            return True
        if abs(position1[1] - position2[1]) == 1 and abs(position1[0] - position2[0]) == 3:
            return True
        return False
        
        
    def __repr__(self):
        return "This is a " + self._color + ' Knight'
    
    def __str__(self):
        if self._color == BLACK:
            return 'n'
        return 'N'