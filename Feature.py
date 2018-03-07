from abc import ABCMeta, abstractmethod
 
class AbstractFeature(object, metaclass=ABCMeta):
 
    def __init__(self, touchPoint):
        self.touchPoint = touchPoint
        super().__init__()
    
    @abstractmethod
    def getNewPosition(self):
        pass
