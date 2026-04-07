#7.Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.
suma = 0
producto = 0 
negativos = False


while True:
    x = input("Asigne un valor o de lo contratrio salga con (n): ")
    
    if x == "n".lower():
        break
    
    if x > 0:
        suma += x
    elif x < 0:
        producto *= x
        negativos = True
        
print(f"La suma de sus numeros Positivos es {suma}")

if negativos:
    print(F"Su producto es {producto}")
else:
    print("No tiene negativos")