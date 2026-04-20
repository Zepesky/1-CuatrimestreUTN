

cant_empleados = 0
cant_empleados__masc = 0
empleado_maximo = 0

cont_tec = 0
cont_tec_ = 0
cont_rv = 0

bandera = True

total = 0

while cant_empleados <= 2:
    nombre_empleado = str(input("Ingrese su nombre: "))
    edad_empleado = int(input("Ingrese su edad: "))
    genero_empleado = str(input("Ingrese su genero femenino/masculino: "))
    tec = str(input("Tecnologia elegida [IA, RV/RA, IOT]: "))
    
    total += 1
    
    if tec == "ia":
        cont_ia 
    
    if genero_empleado == "masculino":
        cont_masculino += 1
    
    if genero_empleado == "masculino" and 25 <= edad_empleado <= 50 and (tec == "ia" or tec == "iot") :
        cont_tec += 1
        
    if tec != "ia" and genero_empleado != "femenino" and 33 <= edad_empleado <= 40:
        cont_tec_ += 1

    if genero_empleado == "masculino" and edad_empleado > empleado_maximo:
        empleado_maximo = edad_empleado
        empleado_maximo_nombre = nombre_empleado
        tec_maximo = tec
    
    if bandera or edad_empleado < empleado_minimo:
        empleado_minimo = edad_empleado
        nombre_empleado_minimo = nombre_empleado
        bandera = False
    
    cant_empleados += 1

if total > 0:
    porsentaje_novoto = (cont_tec_ * 100) / total 
else:
    porsentaje = 0
    
print(f"""
_________________________________
|===============================|
|Masculinos 25 y 50 : {cont_tec}|
|*******************************|
|        Empleado mayor         |
|nombre:{empleado_maximo_nombre}|
|                               |
|edad: {empleado_maximo}        |
|*******************************|
|===============================|
""")


