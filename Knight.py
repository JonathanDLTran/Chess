import Piece
import Constants

class Knight(Piece.Piece):
    
    def __init__(self, color):
        super().__init__(color)
        
    def legalMove(self, position1, position2):
        if abs(position1[0] - position2[0]) == 1 and abs(position1[1] - position2[1]) == 3:
            return True
        if abs(position1[1] - position2[1]) == 1 and abs(position1[0] - position2[0]) == 3:
            return True
        return False
        
        
    def __repr__(self):
        return 'K'
    
    def __str__(self):
        return 'K'