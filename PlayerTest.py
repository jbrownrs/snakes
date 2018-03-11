import unittest, Player

class TestPlayer(unittest.TestCase):

    def test_getName(self):
        P = Player.Player('PlayerA')
        self.assertEqual(P.getName(),'PlayerA')

    def test_getPosition(self):
        P = Player.Player('PlayerA')
        self.assertEqual(P.getPosition(),1)

    def test_setPosition(self):
        P = Player.Player('PlayerA')
        P.setPosition(2)
        self.assertEqual(P.getPosition(),2)
    
if __name__ == '__main__':
    unittest.main() 
