import unittest, Player

class TestPlayer(unittest.TestCase):

    def test_getName(self):
        P = Player.Player('Gareth')
        self.assertEqual(P.getName(),'Gareth')

    def test_getPosition(self):
        P = Player.Player('Gareth')
        self.assertEqual(P.getPosition(),1)

    def test_setPosition(self):
        P = Player.Player('Gareth')
        P.setPosition(2)
        self.assertEqual(P.getPosition(),2)
    
if __name__ == '__main__':
    unittest.main() 
