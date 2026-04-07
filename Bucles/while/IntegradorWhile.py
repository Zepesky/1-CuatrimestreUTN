# Integrador While
# Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
# La suma acumulada de los números negativos.
# La suma acumulada de los números positivos.
# La cantidad de números negativos ingresados.
# El promedio de los números positivos.
# El número positivo más grande.
# El porcentaje de números negativos ingresados, respecto del total de ingresos.

suma_positivos = 0
suma_negativos = 0

cant_positivos = 0
cant_negativos = 0

maximo_positivo = None
i = 0

while True:
    x = input("Ingrese un número (o 'n' para salir): ")
    
    if x.lower() == "n":
        break
    
    x = float(x)
    i += 1
    
    if x > 0: 
        suma_positivos += x
        cant_positivos += 1
        #maximo de positivos
        if maximo_positivo is None or x > maximo_positivo:
            maximo_positivo = x

    elif x < 0:
        suma_negativos += x
        cant_negativos += 1

# Promedio positivos
if cant_positivos > 0:
    promedio = suma_positivos / cant_positivos
else:
    promedio = 0

if i > 0:
    porcentaje_neg = (cant_negativos / i) * 100
else:
    porcentaje_neg = 0
    
print(f"""
===================
1.Suma positivos: {suma_positivos}
2.Suma negativos: {suma_negativos}
3.Cant Negativos: {cant_negativos}
4.Promedio positivo: {promedio}
5.Maximo positivo: {maximo_positivo}
6.Porsentaje negativos: {porcentaje_neg}%
""")