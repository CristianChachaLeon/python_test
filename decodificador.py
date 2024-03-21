def decodificador(numero):
    array_leds=[0,0,0,0]
    for x in range(3,-1,-1):  
        impar = numero % 2
        array_leds[x]= impar
        numero = int(numero/2)
    
    return array_leds



print("Decodificador")

#numero = int(input("Ingrese un numero: "))

for x in range(0,10):
    numero= x
    print("numero de entrada: ",end="")
    print(numero)
    array_leds=decodificador(numero)
    print(array_leds)
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



