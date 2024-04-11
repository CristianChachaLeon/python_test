
def suma(numero1,numero2):
    resultado = numero1+numero2
    return resultado

def restar(numero1,numero2):
    resultado = numero1-numero2
    return resultado

def serie_fibonaci(rango):
    n_b = 1
    n_a = 0
    for x in range(1,rango+1):
        resultado = n_a + n_b 
        print(resultado,end=" ")  
        if x % 10 == 0:
            print()
        n_a = n_b
        n_b = resultado
    print()

print("Calculadora")
ejecutar = True
while(ejecutar):
    opciones = input("opcion 1:sumar\nopcion 2: restar\nopcion 5:fibonacci\nopcion 0:salir\n")

    opciones = int(opciones)
    if opciones == 0:
        ejecutar=False

    elif opciones == 5: 
        numero1 = input("Introducir cantidad de numeros para la serie: ")   
        numero1 = int(numero1)
    else:
        numero1 = input("Introducir primer numero: ")   
        numero2 = input("Introducir segundo numero: ")
        numero1 = int(numero1)
        numero2 = int(numero2)


    if opciones == 1:
        resultado = suma(numero1,numero2) 
    elif opciones == 2:
        resultado = restar(numero1,numero2) 
    elif opciones == 5:
        serie_fibonaci(numero1)
                                         
    if(opciones != 5  and opciones!=0):   
        print("resultado ",resultado)






