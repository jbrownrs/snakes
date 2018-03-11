import Board, Player, Dice

class Game():

    def __init__(self):
        self.Board = Board.Board()
        self.Dice = Dice.Dice()
        self.Players = []

    def addPlayers(self):
        numPlayers = int(input('How many players?'))
        for i in range(0, numPlayers):
            tempname = input('Enter player name:')
            self.Players.append(Player.Player(tempname))

    def play(self):
        winner = False
        while winner == False:
            for player in self.Players:
                winner = self.__makeMove(player)
                if winner:
                    break

    def __makeMove(self, player):
        #get current position
        oldPosition = player.getPosition()
        print('It is your turn ' + player.getName())
        print('Press any key to roll')
        roll = self.Dice.roll()
        print('You rolled a {}'.format(roll))
        print('You were at position {}'.format(oldPosition))
        initialPosition = roll + oldPosition
        if self.hasWon(initialPosition):
            return True
        newPosition = self.Board.getFinalPosition(initialPosition)
        print('You are now at position {}'.format(newPosition))
        player.setPosition(newPosition)
        return self.hasWon(newPosition)

    def hasWon(self, position):
        if self.Board.getSize() <= position:
            print('You have won!')
            return True
        else:
            return False

# TODO - Game reset() method
