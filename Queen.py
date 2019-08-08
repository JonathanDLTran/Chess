import Piece
from Constants import *

class Queen(Piece.Piece):
    
    def __init__(self, color):
        super().__init__(color)
        
        
    def __str__(self):
        if self._color == BLACK:
            return 'q'
        return 'Q'
    
    def __repr__(self):
        return "This is a " +  self._color + ' Queen'
        