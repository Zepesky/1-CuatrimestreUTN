#8. Realizar un programa que a partir del ingreso de un sueldo (valor flotante) muestre dicho valor con un incremento del 15%.

sueldo = float(input("Ingrese su sueldo: "))

incremento = sueldo * 0.15 

total = sueldo + incremento

print(f"""
===================
Sueldo: ${sueldo}
-------------------
Presentismo: ${incremento}
-------------------
Total: ${total}
===================
""")