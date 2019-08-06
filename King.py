import Piece
from Constants import *

class King(Piece.Piece):
    
    def moved(self):
        self._hasMoved = True
    
    def __init__(self, color):
        super().__init__(color)
        self._hasMoved = False
        
    def __str__(self):
        return 'K'
    
    def __repr__(self):
        return "K"