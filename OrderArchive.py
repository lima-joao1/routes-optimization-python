class OrderArchive:
    def __init__(self):
        self.__orders = []

    def add(self, order):
        self.__orders.append(order)
    
    def getOrders(self):
        return self.__orders

    def showOrders(self):
        if (not self.__orders):
            print("Nenhum pedido em aberto.")
            return
        
        i = 1
        print("Pedidos em aberto: ")
        for order in self.__orders:
            print(f"{i} - {order.getOrderID()}, {order.getOrderWeight()} kg, cliente: {order.getCustomer().getName()}")
            i += 1 
        
    def getOrder(self, index):
        return self.__orders[index - 1]
    
    def removeOrder(self, order):
        self.__orders.remove(order)