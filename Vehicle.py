class Vehicle:
    def __init__(self, vehicleName, driverName, capacity):
        self.__vehicleName = vehicleName
        self.__driverName = driverName
        self.__capacity = capacity

    def getDriverName(self):
        return self.__driverName
    
    def getVehicleName(self):
        return self.__vehicleName
    
    def getCapacity(self):
        return self.__capacity