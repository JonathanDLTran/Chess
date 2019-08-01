import Constants

class Piece:
    
    def __init__(self, color):
        self._color = color

    def legalMove(self, position1, position2):
        """
        Abstract Method
        """
        pass