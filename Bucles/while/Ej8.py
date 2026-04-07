#8.Ingresar 10 números enteros. Determinar el máximo y el mínimo.
i = 0
maximo = 0
minimo = 0

while i < 5:
    number = int(input("Ingrese un numero: "))

    #####Inicializacion de max y min#####
    if number > maximo or i == 0: # esta va a ser la primera iteracion
        maximo = number
    
    if number < minimo or  i == 0:
        minimo = number
    #     maximo = number
    #     minimo = number
    # else:
    #     if number > maximo:
    #         maximo = number
    
    #     if number < minimo:
    #         minimo = number
    
    
    i += 1
    
print(f"Max: {maximo}")
print(f"Min: {minimo}")

# ctrl + ] para comentar todo 