from Customer import Customer
from DeliveryAddress import DeliveryAddress
from CustomerArchive import CustomerArchive
from VehicleArchive import VehicleArchive
from Vehicle import Vehicle
from OrderArchive import OrderArchive
from Order import Order
from Route import Route
from RouteOptimization import RouteOptimization

def orderRegister():
    if not customerArchive.getCustomers():
        print("Nenhum cliente registrado. É necessário registrar antes de cadastrar um pedido.")
        return
    
    orderID = input("Digite o código do pedido: ")
    orderWeight = int(input("Digite a massa do pedido (kg): "))
    
    customerArchive.showCustomers()

    customerIndex = int(input("Digite o índice do cliente que fez o pedido: "))
    customer = customerArchive.getCustomer(customerIndex)

    order = Order(orderID, orderWeight, customer)
    orderArchive.add(order)

def vehicleRegister():
    vehiclePlate = input("Digite a placa do veículo: ")
    driverName = input("Digite o nome do motorista: ")
    vehicleCapacity = int(input("Digite a capacidade de carga do veículo (kg): "))

    vehicle = Vehicle(vehiclePlate, driverName, vehicleCapacity)
    vehicleArchive.add(vehicle)


def customerRegister():
    customerName = input("Digite o nome do cliente: ").capitalize()
    customerAddress = input("Digite o endereço do cliente: ").split(" ")
    properAddress = " ".join(word.capitalize() for word in customerAddress)
    addressX = int(input("Coordenada X do ponto de entrega: "))
    addressY = int(input("Coordenada Y do ponto de entrega: "))

    deliveryAddress = DeliveryAddress(addressX, addressY, properAddress)
    customer = Customer(customerName, deliveryAddress)
    customerArchive.add(customer)

    print()
    print(f"Cliente {customer.getName()}, endereço {customer.getDeliveryAddress().getName()} cadastrado!")

def printOptions():

    print("""1. Cadastrar clientes
2. Alterar cadastro de cliente
3. Cadastrar veículos
4. Cadastrar pedidos
5. Mostrar pedidos em aberto
6. Iniciar
0. Sair""")

    print()

def changeRegister():
    if (not customerArchive.getCustomers()):
        print("Nenhum cliente cadastrado.")
        return
    
    customerArchive.showCustomers()
    customerToChange = int(input(f"Digite o número do cliente que deseja alterar (0 p/ voltar): "))
    
    if (customerToChange == 0):
        return 
    
    customer = customerArchive.getCustomer(customerToChange)

    print(f"Alterando o cadastro do cliente {customer.getName()}, {customer.getDeliveryAddress().getName()}, x, y: ({customer.getDeliveryAddress().getX()}, {customer.getDeliveryAddress().getY()})")
    print()

    print("""1. Alterar nome
2. Alterar endereço
3. Deletar cliente""")
    
    choice = int(input("Escolha a opção desejada [1-3]: "))
    
    if (choice == 1):
        newName = input("Digite o novo nome (0 p/ voltar): ")
        
        if (newName == "0"):
            return

        customer.setName(newName)
        print(f"Nome do cliente alterado para {customer.getName()}")
    
    elif (choice == 2):
        newAddressName = input("Digite o nome do novo endereço (0 p/ voltar): ")
        
        if (newAddressName == "0"):
            return
        
        newAddressX = int(input("Digite a coordenada X do novo endereço: "))
        newAddressY = int(input("Digite a coordenada Y do novo endereço: "))
        newAddress = DeliveryAddress(newAddressName, newAddressX, newAddressY)

        customer.setDeliveryAddress(newAddress)
        print(f"Endereço mudado para {customer.getDeliveryAddress().getName()}, de coordenadas ({customer.getDeliveryAddress().getX()}, {customer.getDeliveryAddress().getY()}).")

    elif (choice == 3):
        confirmation = input(f"Tem certeza que deseja deletar o cliente {customer.getName()} (Y/N)?")
        
        if (confirmation == "N"):
            return

        customerArchive.deleteCustomer(customer)
        print("Cliente deletado.")

def ordersWeight(ordersToRoute):
    weight = 0
    for order in ordersToRoute:
        weight += order.getOrderWeight()

    return weight


def ordersToRoute(vehicle):
    if (not orderArchive.getOrders()):
        print("Nenhum pedido em aberto.")
        return 
    ordersToRoute = []
    vehicleCapacity = vehicle.getCapacity()

    while True:
        orderArchive.showOrders()
        orderIndex = int(input("\nSelecione o índice do pedido a ser adicionado à rota (0 p/ continuar): "))

        if (orderIndex == 0):
            break

        order = orderArchive.getOrder(orderIndex)

        if (order.getOrderWeight() <= vehicleCapacity):
            ordersToRoute.append(order)
            vehicleCapacity -= order.getOrderWeight()
            orderArchive.removeOrder(order)

        else:
            print(f"Capacidade do caminhão excedida. Não é possível adicionar o pedido de código: {order.getOrderID()} ")
    
    print("\n==================================")
    print("RELATÓRIO FINAL DA ROTA DE ENTREGA:")
    print(f"\nCapacidade máxima do veículo (kg): {vehicle.getCapacity()}")
    print(f"Tamanho da carga (kg): {ordersWeight(ordersToRoute)}\n")
    
    
    return ordersToRoute

def vehicleToRoute():
    if (not vehicleArchive.getVehicles()):
        print("Nenhum veículo cadastrado. É necessário ter ao menos um veículo cadastrado para iniciar uma rota.")
        return 
    
    print("Veículos disponíveis: ")
    i = 1
    for vehicle in vehicleArchive.getVehicles():
        print(f"{i} - {vehicle}")
        i += 1

    vehicleIndex = int(input(f"Selecione o índice do veículo: [1-{len(vehicleArchive.getVehicles())}]: "))
    vehicle = vehicleArchive.getVehicle(vehicleIndex)
    print("\n========================")
    print(f"\nVeículo selecionado: \n\n{vehicle}\n")
    return vehicle

def routeCreation():
    print("Iniciando rota...")
    
    vehicle = vehicleToRoute()   
    orders = ordersToRoute(vehicle)

    return Route(orders, vehicle)

def distanceBetween(ax, ay, bx, by):
    from math import sqrt
    return sqrt((bx - ax)**2 + (by - ay)**2)

def routeOptimizer():
    finalRoute = routeCreation()
    optimization = RouteOptimization(finalRoute)

    optimizedRoute = optimization.optimize()
    optimizedRouteInfo(optimizedRoute, finalRoute)

    
def optimizedRouteInfo(route, finalRoute):
    totalTraveled = 0

    print(finalRoute)

    for order in route:
        totalTraveled += order.getCustomer().getDeliveryAddress().getDistance()
    
    print("\nRota: ")
    print("| Depósito -> ", end="")

    for i in range(len(route)):
        print(f"{route[i]} -> ", end="")
    print("Depósito |")
    
    totalTraveled += route[len(route) - 1].getCustomer().getDeliveryAddress().getDistance()
    print(f"\nDistância percorrida: {totalTraveled:.2f} km\n")

    orderArchive.showOrders()

    
def commandManager(command):
    if (command == 1):
        customerRegister()
    
    elif (command == 2):
        changeRegister()

    elif (command == 3):
        vehicleRegister()

    elif (command == 4):
        orderRegister()

    elif (command == 5):
        orderArchive.showOrders()

    elif (command == 6):
        routeOptimizer()
        

customerArchive = CustomerArchive()
vehicleArchive = VehicleArchive()
orderArchive = OrderArchive()


while True:
    print("\n****** Program ******")

    print()
    printOptions()
    command = int(input("Função desejada [1-6]: "))

    if (command == 0):
        break

    commandManager(command)
    