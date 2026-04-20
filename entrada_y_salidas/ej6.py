#6. Realizar un programa que permita el ingreso de dos números. Calcular la suma, resta, multiplicación y división de los mismos. Mostrar los resultados por pantalla. Utilizar una variable para mostrar el resultado (concatenar).

print("""
================
1. Suma
2. Resta
3. Multipicacion
4. Division
================
""")

x = float(input("Asigne valor a X: "))

y = float(input("Asigne valor a Y: "))

op = int(input("Que operacion desea realizar?: "))

resultado = ""

if op == 1:
    resultado = "La suma es: " + str(x + y)

if op == 2:
    resultado = "La resta es: " + str(x - y)

if op == 3:
    resultado = "La multiplicación es: " + str(x * y)

if op == 4:
    if y != 0:
        resultado = "La división es: " + str(x / y)
    else:
        resultado = "Error: no se puede dividir por cero"

print(resultado)
