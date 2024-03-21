import math 

def decodificador(numero):
    array_leds=[] 
    rango_sup=int(math.log2(numero))

    for x in range(0,rango_sup+1):  
        impar = numero % 2
        array_leds.append(impar)
        numero = int(numero/2)
    
    return array_leds



print("Decodificador")

#numero = int(input("Ingrese un numero: "))
rango_max=50
for x in range(1,rango_max): 
    numero= x
    print("numero de entrada: ",end="")
    print(numero)
    array_leds=decodificador(numero)
    print("Numero de espacios para imprimir")
    formato=int(math.log2(rango_max))
    print(formato)
    print(array_leds[::-1])

    #array ['a','b','c','d']ç
    #array[0.4  0.4 0.1 ]

    #lista ( 1 , 'a' , 3.4 , 5.6)
# for x in range(3,0,-1): # 
#     impar = numero % 2
#     array_leds[x]= impar
#     numero = int(numero/2)



# if numero == 0:    
#     array_leds[0]=0
#     array_leds[1]=0
#     array_leds[2]=0
#     array_leds[3]=0
# elif numero == 1:
#     array_leds[0]=0
#     array_leds[1]=0
#     array_leds[2]=0
#     array_leds[3]=1
# elif numero == 2:
#     array_leds[0]=0
#     array_leds[1]=0
#     array_leds[2]=1
#     array_leds[3]=0



