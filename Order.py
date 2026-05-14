class Order:
    def __init__(self, orderID, orderWeight, customer):
        self.__orderID = orderID
        self.__orderWeight = orderWeight
        self.__customer = customer

    def getOrderID(self):
        return self.__orderID
    
    def getOrderWeight(self):
        return self.__orderWeight
    
    def getCustomer(self):
        return self.__customer