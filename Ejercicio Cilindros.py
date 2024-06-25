Datos = []
Direccion = []
Sector = []
Cilindros5 = []
Cilindros15 = []
Cilindros45 = []

Menu = True
while Menu:
    print("1-Registrar Pedido")
    print("2-Listar todos los pedidos")
    print("3-Imprimir hoja de ruta")
    print("4-Salir del programa")
    op = input("Seleccione una opcion: ")
    break
if op == "1":
    print("Registro Pedido")
    cliente = input("Ingrese su nombre de usuario: ")
    Datos.append(cliente)
    casa = input("Ingrese la direccion del pedido: ")
    Direccion.append(casa)
    comuna = input("Ingrese la comuna en la que recide: ")
    Sector.append(comuna)
    print("COMPRA DE LOS CILINDROS")
    C5 = input("Ingrese la cantidad de cilindros de 5 que quiere: ")
    Cilindros5.append(C5)
    C15 = input("Ingrese la cantidad de cilindros de 15 que quiere: ")
    Cilindros15.append(C15)
    C45 = input("Ingrese la cantidad de cilindros de 45 que quiere: ")
    Cilindros45.append(C45)
    print("Los Cilindros que usted ha comprado son: ",Cilindros5)
    print("Los Cilindros que usted ha comprado son: ",Cilindros15)
    print("Los Cilindros que usted ha comprado son: ",Cilindros45)