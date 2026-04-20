# 10. Ingresar el sueldo, estado civil (casado o soltero) y cantidad de hijos de un empleado. Determinar si el empleado debe o no pagar el impuesto a las ganancias. El mismo no se pagará si el empleado es casado con hijos y sus ingresos son menores a $2200000.

sueldo = float(input("Ingrese su sueldo: "))
estado_civil = input("Ingrese su estado civil (casado/soltero): ").lower()
hijos = int(input("Ingrese cantidad de hijos: "))

if estado_civil == "casado" and hijos > 0 and sueldo < 2200000:
    print("No debe pagar impuesto a las ganancias")
else:
    print("Debe pagar impuesto a las ganancias")