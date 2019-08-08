import Piece
from Constants import *

class Bishop(Piece.Piece):
    
    def __init__(self, color):
        super().__init__(color)
        
    def legalMove(self, position1, position2):
        pass
    
    def __str__(self):
        if self._color == BLACK:
            return 'b'
        return 'B'
    
    def __repr__(self):
        return "This is a " + self._color + " Bishop"