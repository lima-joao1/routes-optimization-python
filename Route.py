class Route:
    def __init__(self, orders, vehicle):
        self.__orders = orders
        self.__vehicle = vehicle

    def getOrders(self):
        return self.__orders
    
    def getVehicle(self):
        return self.__vehicle
    
    def getRouteWeight(self):
        routeWeight = 0
        for order in self.__orders:
            routeWeight += order.getOrderWeight()
        return routeWeight

    def __str__(self):
        return f"Veículo: {self.getVehicle().getVehiclePlate()} \nMotorista: {self.getVehicle().getDriverName()} \nCapacidade: {self.getVehicle().getCapacity()} kg"