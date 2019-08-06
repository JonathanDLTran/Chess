import Piece
from Constants import *

class Rook(Piece.Piece):
    
    def moved(self):
        self._hasMoved = True
    
    
    def __init__(self, color):
        super().__init__(color)
        self._hasMoved = False
        
    def legalMove(self, position1, position2):
        rowDifference = position1[0] - position2[0]
        columnDifference = position1[1] - position2[1]
        if rowDifference != 0 and columnDifference != 0:
            return False
        if rowDifference == 0:
            column = position1[1]
            rowStart = position1[0]
            rowEnd = position2[0]
            rows = range(rowStart + 1, rowEnd)
            if self.rowIsOccupied(piecesData, rows, column):
                return False
        if columnDifference == 0:
            row = position1[0]
            columnStart = position1[1]
            columnEnd = position2[1]
            columns = range(columnStart + 1, columnEnd)
            if self.columnIsOccupied(piecesData, row, columns):
                return False
        if self._color == BLACK:
            if position2[1] > position1[1]:
                return False
            return True
        if position2[1] <  position1[1]:
            return False
        return True
            
            
        
        # if not on the same column, or row, return False
        # if there is a piece between position1 and position2, return False
        # if black:
            # if column2 is greated than column1, return false
            # else true
        # else white:
            # if column2 is lesser than column1, return False
            # ELSE TRUE
            
    def columnIsOccupied(self, piecesData, row, column):
        """
        Returns true if position row, column in piecesData is occupied
        False otherwise
        """
        for element in column:
            if piecesData[row][element] != None:
                return True
        return False
            
    def rowIsOccupied(self, piecesData, row, column):
        """
        Returns true if position row, column in piecesData is occupied
        False otherwise
        """
        for element in row:
            if piecesData[element][column] != None:
                return True
        return False
    
    def __str__(self):
        return 'R'
    
    def __repr__(self):
        return 'R'