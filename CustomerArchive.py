class CustomerArchive:
    def __init__(self):
        self.__customers = []
    
    def add(self, customer):
        self.__customers.append(customer)

    def showCustomers(self):
        i = 1

        for customer in self.__customers:
            print(f"{i} - {customer.getName()}")
            i += 1
    
    def getCustomers(self):
        return self.__customers
    
    def getCustomer(self, index):
        return self.__customers[index-1]
    
    def deleteCustomer(self, customer):
        self.__customers.remove(customer)