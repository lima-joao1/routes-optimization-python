class Route:
    def __init__(self, orders, vehicle):
        self.__orders = orders
        self.__vehicle = vehicle

    def getOrders(self):
        return self.__orders
    
    def getVehicle(self):
        return self.__vehicle
    
    def __str__(self):
        return f"Veículo: {self.getVehicle().getVehiclePlate()} \n Motorista: {self.getVehicle().getDriverName()} \n Capacidade: {self.getVehicle().getCapacity()} kg"