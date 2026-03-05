saldo = 1000
pin = "1234"
intentos = 3
acceso = False

for i in range(intentos):
    print("\n Bienvenido al cajero automatico \n")
    pin_u = input("Por favor ingrese su pin: ")
    if pin_u != pin:
        acceso == False
        print("El pin que ingresaste es incorrecto. vuelve a ingresarlo")

    else:
        acceso = True 
        print("\n tienes acceso al cajero\n")
    break

while acceso == True:
    print("\n1. Consultar el saldo actual")
    print("2. retirar dinero")
    print("3. depositar dinero")
    print("4. salir del cajero")

    opcion = input("Por favor ingrese la opcion que desea realizar: ")
    
    if opcion == "1":
        print(saldo)

    elif opcion == "2":
        cantidad = int(input("Por favor ingresa la cantidad: "))
        saldo -= cantidad
        print(f"su saldo actual es de {saldo}")

    elif opcion == "3":
        saldo + cantidad
        print(f"Depositaste con exito {saldo}")
        
    elif opcion == "4":
        acceso == False
        print("vuelve pronto")