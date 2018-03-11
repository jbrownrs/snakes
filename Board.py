from Feature import AbstractFeature
from Snake import Snake
from Ladder import Ladder
from Square import Square

class Board():

    def __init__(self):
        # to use a factory or something in future?
        self.board = {}
        self.board[1] = Square(1)
        self.board[2] = Square(2)
        self.board[3] = Ladder(3,4)
        self.board[4] = Square(4)
        self.board[5] = Square(5)
        self.board[6] = Snake(6,4)
        self.board[7] = Square(7)
        self.board[8] = Square(8)
        self.board[9] = Square(9) 

    def getFinalPosition(self, position):
        F = self.board.get(position)
        return F.getNewPosition()

    def getSize(self):
        return len(self.board)
