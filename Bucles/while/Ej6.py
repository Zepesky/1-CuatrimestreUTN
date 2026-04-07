#6.Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.

suma = 0
i = 0

while True:
    x = input("Ingrese un valor o (n) si no desea ingresar mas: ")
    
    if x != "n":
        break
    x = float(x)
    suma += x
    i += 1
    
    if i > 0:
        promedio = suma / i
        print(f"""
            Su suma es {suma}
            Su promedio es {i}
            """)
    else:
        print("No se ingresaron datos")