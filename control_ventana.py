cantidad_luz=100
motor =False
while(1):
    
    comando=input("Comando usuario:")
    print(comando)

    instruccion = comando.split('=')[0]
    argumento = int(comando.split('=')[1])

    match  instruccion:
        case  "cantidad_luz":
            print("guardar cantidad luz")
            cantidad_luz=argumento
        case "completamente_abierta":
            ventan_abierta=True
        case "completamente_cerrada":
            ventan_abierta=False
            


    #control motor
    if ventan_abierta==False and cantidad_luz<50 :
        print("abrir toda la ventana")
        print("activar motor derecha")
        motor=True
        dirreccion = "derecha"

    if motor==True and ventan_abierta==True:
        print("motor stop")
        motor = False