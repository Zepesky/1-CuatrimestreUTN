# 13. Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.

numero = int(input("Ingrese un número: "))
contador = 0

for i in range(2, numero + 1):
    bandera = True


    for j in range(2, i):
        if i % j == 0:
            bandera = False


    if bandera:
        print(i)
        contador += 1
        
        
print(f"{contador}")