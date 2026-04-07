#4.Mostrar la suma de los números pares desde el 1 hasta el 10.

suma = 0
i = 1

while i < 10:
    
    if i % 2 == 0:
        suma += i
    i += 1

print(f"{suma}")