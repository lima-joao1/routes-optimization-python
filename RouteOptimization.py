class RouteOptimization:

    def __init__(self, route):
        self.__route = route
        self.__optimizedRoute = []
        self.__currentLocation = 0


    def optimize(self):
        for i in range(len(self.__route.getOrders())):
            self.getNextDeliveryPoint()
        
        return self.__optimizedRoute

    def getNextDeliveryPoint(self):
        nextOrder = self.__route.getOrders()[0]
        orderDistanceFromLocation = self.__route.getOrders()[0].getCustomer().getDeliveryAddress().getDistance() - self.__currentLocation        

        for order in self.__route.getOrders():
            if (order.getCustomer().getDeliveryAddress().getDistance() - self.__currentLocation < orderDistanceFromLocation):
                nextOrder = order
                orderDistanceFromLocation = abs(order.getCustomer().getDeliveryAddress().getDistance() - self.__currentLocation)
                
        self.__currentLocation = nextOrder.getCustomer().getDeliveryAddress().getDistance()
        self.__optimizedRoute.append(nextOrder)
        self.__route.getOrders().remove(nextOrder)