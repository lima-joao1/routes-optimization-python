class VehicleArchive:
    def __init__(self):
        self.__vehicles = []
    
    def add(self, vehicle):
        self.__vehicles.append(vehicle)
    
    def getVehicles(self):
        return self.__vehicles
    
    def getVehicle(self, index):
        return self.__vehicles[index - 1]