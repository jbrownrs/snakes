
import unittest
import Feature, Square, Ladder, Snake

class TestFeatures(unittest.TestCase):

    def test_SquarePosition(self):
        sq = Square.Square(42)
        expectedPosition = 42
        self.assertEqual(sq.getNewPosition(), expectedPosition)


    def test_SnakePosition(self):
        snake = Snake.Snake(42,2)
        expectedPosition = 40
        self.assertEqual(snake.getNewPosition(), expectedPosition)

    def test_LadderPosition(self):
        lad = Ladder.Ladder(42,2)
        expectedPosition = 44
        self.assertEqual(lad.getNewPosition(), expectedPosition)
        
        
if __name__ == '__main__':
    unittest.main()
