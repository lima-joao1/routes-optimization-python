class Vehicle:
    def __init__(self, vehiclePlate, driverName, capacity):
        self.__vehiclePlate = vehiclePlate
        self.__driverName = driverName
        self.__capacity = capacity

    def getDriverName(self):
        return self.__driverName
    
    def getVehiclePlate(self):
        return self.__vehiclePlate
    
    def getCapacity(self):
        return self.__capacity