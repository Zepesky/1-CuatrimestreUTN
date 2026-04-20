# 6. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números


suma = 0
contador = 0

for i in range(10):
    x = int(input("Ingrese 10 numeros: ")) 
    
    if x == 0:
        break

    suma += x
    contador += 1
    
if contador > 0:
    promedio = suma / contador
else:
    promedio = 0

print(f"suma = {suma}, promedio = {promedio}")