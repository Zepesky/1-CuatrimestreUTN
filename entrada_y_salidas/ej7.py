#7. Realizar un programa que pida dos números enteros. Calcular y mostrar el resto de la división entre ambos números. Ej.: "El resto de dividir 7 por 2 es: 1" .

x = int(input("Asigne un valor entero a x: "))
y = int(input("Asigne un valor entero a y: "))

resto = (x % y)

print(f"El resto de tu operacion es {x}%{y}: {resto}")