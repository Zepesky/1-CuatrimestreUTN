# 10. Realizar un programa que permita mostrar una pirámide de números. Por ejemplo: si se ingresa el numero 5, la salida del programa será la siguiente:

x = int(input("Ingrese un numero:"))

for i in range(1, x + 1):
    fila = " " * (x - i)
    
    for j in range(1 ,i , 1):
        fila += str(j)
    
    for j in range(i - 1, 0, -1):
        fila += str(j)
    
    print(fila)