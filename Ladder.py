from Feature import AbstractFeature

class Ladder(AbstractFeature):
    def __init__(self, touchPoint, offset):
        super().__init__(touchPoint)
        self.offset = offset
   
    def getNewPosition(self):
        position = self.touchPoint + self.offset
        return position
