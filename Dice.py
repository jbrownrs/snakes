from random import randint

# Future improvement - pass in number sides of dice.
class Dice():

    def roll(self):
        sides = 6
        return randint(1, sides)

        
        
