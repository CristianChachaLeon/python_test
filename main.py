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

print("Programa 1: Fibonacci")
rango_fibonacci = input("numero para la serie de fibonacci: ")
print("rango de valores")
serie_fibonaci(int(rango_fibonacci))




