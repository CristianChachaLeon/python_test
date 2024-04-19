saldo_Cristian = 100
saldo_Andres = 200


def check_name_password(nombre,password):

    check = False
    if (nombre == "cristian" and password == "1234"):
        check = True
    elif (nombre == "andres" and password == "456"):
        check = True
    return check

def getSaldo(nombre):
    if (nombre == "cristian") :  #Cuenta de Cristian
        saldo = saldo_Cristian
    elif(nombre == "andres"):
        saldo = saldo_Andres
    return saldo

def setSaldo(nombre,cantidad):
    global saldo_Cristian
    global saldo_Andres
    if (nombre == "cristian"):
        saldo_Cristian =cantidad
    elif(nombre == "andres"):
        saldo_Andres = cantidad


while(1):
    print("Cajero automatico")
    nombre = input("Ingrese nombre: ")
    password = input("Ingrese password: ")

    if (check_name_password(nombre,password)):
        print("Bienvendio "+nombre)
        ejectar = True
        while(ejectar):
            opcion = int(input("1.Ver Saldo\n2.Retirar Dinero\n3.Ingresar Dinero\n0.Salir\n"))
            saldo = getSaldo(nombre)
            match opcion:
                case 1:
                    print("Saldo: ",saldo)
                case 2:
                    cantidad=int(input("Cantidad de dinero a retirar:"))
                    if ( saldo - cantidad >= 0) :
                        setSaldo(nombre, saldo-cantidad)
                        print("Saldo actual: ",getSaldo(nombre))
                    else:
                        print("Saldo insuficiente, saldo actual:",getSaldo(nombre))
                case 3:
                    cantidad=int(input("Cantidad de dinero a ingresar:"))
                    setSaldo(nombre, saldo+cantidad)
                    print("Saldo actual: ",getSaldo(nombre))
                case 0:
                    ejectar = False

    else:
        print("Error de contraseña o usuario")   
