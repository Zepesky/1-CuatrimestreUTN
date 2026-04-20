# 4. Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo, si se ingresa el numero 5:

tabla = int(input("ingres que tabla: "))

for i in range(0, 11, 1):
    resustado = tabla * i
    print(f"{tabla} x {i} = {resustado}")