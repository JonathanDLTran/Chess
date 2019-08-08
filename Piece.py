from Constants import *

class Piece:
    
    def getColor(self):
        return self._color
    
    def __init__(self, color):
        self._color = color

    def legalMove(self, piecesData, position1, position2):
        """
        Abstract Method
        """
        pass