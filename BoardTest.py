import unittest, Board

# This test is specific to the hardcoded 3x3 grid
# in the Board init (for now...)
class TestBoard(unittest.TestCase):

    def test_getFinalPositionForSquares(self):
        B = Board.Board()
        posn = 1 # Square on posn 1
        self.assertEqual(B.getFinalPosition(posn), posn)
        
    def test_getFinalPositionForSnakes(self):
        B = Board.Board()
        # Snake on posn 6 slithers down to 2
        self.assertEqual(B.getFinalPosition(6), 2)

    def test_getFinalPositionForLadder(self):
        B = Board.Board()
        # Ladder on posn 3 climbs up to 7
        self.assertEqual(B.getFinalPosition(3), 7)

    def test_getSize(self):
        B = Board.Board()
        self.assertEqual(B.getSize(), 9)

if __name__ == '__main__':
    unittest.main()
        
