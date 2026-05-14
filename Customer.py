from DeliveryAddress import DeliveryAddress

class Customer:
    def __init__(self, customerName, DeliveryAddress):
        self.__customerName = customerName
        self.__deliveryAddress = DeliveryAddress

    def getName(self):
        return self.__customerName
    
    def setName(self, name):
        self.__customerName = name

    def getDeliveryAddress(self):
        return self.__deliveryAddress

    def setDeliveryAddress(self, DeliveryAddress):
        self.__deliveryAddress = DeliveryAddress