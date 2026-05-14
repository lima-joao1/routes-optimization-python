from Customer import Customer
from DeliveryAddress import DeliveryAddress
from CustomerArchive import CustomerArchive
from VehicleArchive import VehicleArchive
from Vehicle import Vehicle
from OrderArchive import OrderArchive
from Order import Order

def orderRegister():
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
        

customerArchive = CustomerArchive()
vehicleArchive = VehicleArchive()
orderArchive = OrderArchive()


while True:
    print("****** Program ******")

    print()
    printOptions()
    command = int(input("Função desejada [1-3]: "))

    if (command == 0):
        break

    commandManager(command)