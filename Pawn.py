import Piece
import Constants

class Pawn(Piece.Piece):
    
    def leaveBaseline(self):
        self._hasLeftBaseline = True
        
    def reachOpposite(self):
        self._reachOppositeSide = True
    
    def __init__(self, color):
        super().__init__(color)
        self._hasLeftBaseline = False
        self._reachOppositeSide = False
        
    def legalMove(self, position1, position2, piecesData):
        """
        position1 and position2 are valid indexed positions (e.g row 2 is 1 and column 1 is 0)
        returns True if the pawn can move from position1 to position2, otherwise False
        """

        if position1[1] != position2[1]:
            return False
        column = position1[1]
        rows = range(position1[0] + 1, position2[0])
        if self.isOccupied(piecesData, rows, column):
            return False
        if self._color == BLACK:
            if position1[0] < position2[0]:
                return False
            return self.distanceHelper(position1, position2)
        else:
            if position1[0] > position2[0]:
                return False
            return self.distanceHelper(position1, position2)
            

    def distanceHelper(self, position1, position2):
        """
        Position1 and position2 are valid positions
        returns True iif the pawn can move there, false otherwise
        """
        distance = abs(position1[0] - position2[0])
        if self._hasLeftBaseline:
            if distance < 1 or distance > 1:
                return False
            return True
        else:
            if distance < 1 or distance > 2:
                return False
            return True
        
    def isOccupied(self, piecesData, rows, column):
        """
        gameList is a pieces Data
        rows is a list of integers between 0 and 7
        column is an integer between 0 and 7
        return True if occupied, false if not
        """
        for row in rows:
            if piecesData[row][column] != None:
                return True
        return False
                
        
    def __repr__(self):
        return 'P'
    
    def __str__(self):
        return 'P'
    
        