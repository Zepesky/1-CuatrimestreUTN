#5.Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.

i = 0 

suma = 0 

while i < 5:
    x = int(input("Ingrese valor a x: "))
    suma += x
    i += 1

prom = suma / 5

print(suma)
print(prom)
