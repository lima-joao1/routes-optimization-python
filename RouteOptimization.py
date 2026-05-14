from math import sqrt

class RouteOptimization:
    def __init__(self, route):
        self.__route = route

    def optimize(self):
        currentCapacity = self.__route.getVehicle().getCapacity()

        previousPosition = 0
        for order in self.__route.getOrders():
            shortestDistanceToTravel = 0
            x = order.getCustomer().getDeliveryAddress().getX()
            y = order.getCustomer().getDeliveryAddress().getY()
            distance = sqrt(x^2 + y^2) - previousPosition


            if (distance < shortestDistanceToTravel):
                shortestDistanceToTravel = distance
                previousPosition  
