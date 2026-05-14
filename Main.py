from Customer import Customer
from DeliveryAddress import DeliveryAddress
from CustomerArchive import CustomerArchive
from VehicleArchive import VehicleArchive
from Vehicle import Vehicle


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

def printOptions():

    print("""1. Cadastrar clientes
2. Cadastrar veículos
3. Alterar cadastro de cliente
4. Cadastrar pedidos
0. Sair""")

    print()

def changeRegister():
    if (not customerArchive.getCustomers()):
        print("Nenhum cliente cadastrado.")
        return
    
    customerArchive.showCustomers()
    customerToChange = int(input(f"Digite o número do cliente que deseja alterar: "))
    customer = customerArchive.getCustomer(customerToChange)

    print(f"Alterando o cadastro do cliente {customer.getName()}, de endereço {customer.getDeliveryAddress().getName()}, x, y: ({customer.getDeliveryAddress().getX()}, {customer.getDeliveryAddress().getY()})")
    print()

    print("""1. Alterar nome
2. Alterar endereço
3. Deletar cliente""")
    
    choice = int(input("Escolha a opção desejada [1-3]: "))
    
    if (choice == 1):
        newName = input("Digite o novo nome: ")
        customer.setName(newName)
        print(f"Nome do cliente alterado para {customer.getName()}")
    
    elif (choice == 2):
        newAddressName = input("Digite o nome do novo endereço: ")
        newAddressX = int(input("Digite a coordenada X do novo endereço: "))
        newAddressY = int(input("Digite a coordenada Y do novo endereço: "))
        newAddress = DeliveryAddress(newAddressName, newAddressX, newAddressY)

        customer.setDeliveryAddress(newAddress)
        print(f"Endereço mudado para {customer.getDeliveryAddress().getName()}, de coordenadas ({customer.getDeliveryAddress().getX()}, {customer.getDeliveryAddress().getY()}).")

    elif (choice == 3):
        customerArchive.deleteCustomer(customer)
        print("Cliente deletado.")
    
def commandManager(command):
    if (command == 1):
        customerRegister()
    
    if (command == 2):
        changeRegister()

    if (command == 3):
        vehicleRegister()
        

customerArchive = CustomerArchive()
vehicleArchive = VehicleArchive()

print("****** Program ******")

while True:
    print()
    printOptions()
    command = int(input("Função desejada [1-3]: "))

    if (command == 0):
        break

    commandManager(command)