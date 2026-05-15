from math import sqrt

class DeliveryAddress:
    def __init__(self, x, y, addressName):
        self.__addressName = addressName
        self.__x = x
        self.__y = y
    
    def getName(self):
        return self.__addressName
    
    def getX(self):
        return self.__x

    def getY(self):
        return self.__y
    
    def getDistance(self):
        return sqrt(self.__x^2 + self.__y^2)