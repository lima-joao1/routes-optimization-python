class VehicleArchive:
    def __init__(self):
        self.__vehicles = []
    
    def add(self, vehicle):
        self.__vehicles.append(vehicle)
    
    def getVehicles(self):
        return self.__vehicles