# 8. Ingresar 10 números. Solo sumar los que estén fuera del rango 50-100.

suma = 0 
for i in range(10):
    numero = int(input("Asigne un numero: "))
    if numero < 50 or numero > 100:
        continue
    suma += numero

print(suma)