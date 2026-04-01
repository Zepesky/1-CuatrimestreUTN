#9. Realizar un programa que a partir del ingreso de un sueldo y de un porcentaje de aumento, calcule y muestre el sueldo con el aumento porcentual ingresado por el usuario.

sueldo = float(input("Ingrese su sueldo: "))

aumento = float(input("Ingrese el porsentaje de aumento (%): "))

incremento = sueldo * aumento / 100

total = sueldo + incremento

print(f"""
===================
Sueldo: ${sueldo}
-------------------
Aumento: {aumento}%
-------------------
Presentismo: ${incremento}
-------------------
Total: ${total}
===================
""")