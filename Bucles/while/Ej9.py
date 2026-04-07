#9.Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.
i = 0 
suma = 0
promedio = 1 

while i < 5:
    numero = int(input("Ingrese un valor: "))    
    suma += numero
    i += 1
    
    

promedio *= suma / i 

print(f"""
.La suma de sus numeros es {suma}
.El promedio de sus numeros es {promedio}
    """)