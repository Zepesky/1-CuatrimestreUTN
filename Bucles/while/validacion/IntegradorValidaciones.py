# Integrador validaciones.

# Una empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar la carga y validación de datos.
# Los datos requeridos son:
# · Apellido
# · Edad, entre 18 y 90 años inclusive.
# · Estado civil: “Soltero”,” Casado”, “Divorciado” o “Viudo”.
# · Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.
# Una vez ingresados y validados los datos, mostrarlos por pantalla.
# Integrador while y validaciones.
# A partir de los datos del integrador de validaciones, ingresar datos de personas hasta que el usuario lo desee y calcular:
# a. Cantidad de personas cuya edad esta entre 25 y 40.
# b. Porcentaje de personas de cada estado civil.
# c. Promedio de edades de los casados.
# d. Datos de la persona más joven.
# e. Datos de la persona viuda con mayor edad.

#variables
contador_sol = 0
contador_cas = 0
contasdor_div = 0
contador_viu = 0
contador_edad = 0 
seguir = "si"
edades_cas = 0 

bandera_primer_per = True

while seguir == "si":
    #ingreso de datos
    
    #primarios
    apellito = str(input("ingrese el apellido"))  
    edad = int(input("Ingrese la edad: "))
    
    while edad < 18 or edad > 90:
        edad = int(input("Error Ingrese edad valida."))
    
    estado_civ = str(input("Ingrese estado civil [Soltero], [Casado], [Divorciado], [viudo]."))
    
    while estado_civ != "Soltero" and estado_civ != "Casado" and estado_civ != "Divorciado" and estado_civ != "Viudo":
        estado_civ = input("ERROR, ingresar estado civil: ")
    
    legajo = int(input("Ingrese numero de legajo:"))
    while legajo < 1000 and legajo > 9999:
        legajo = int(input("ERROR, reingrese ingrese el legajo: "))
    
    #stats
    # a. Cantidad de personas cuya edad esta entre 25 y 40.
    if edad >= 25 and edad <= 40:
        contador_edad += 1
    
    #b. Porcentaje de personas de cada estado civil.
    match estado_civ:
        case "Casado":
            contador_cas += 1
            edades_cas += 1
        case "Soltero":
            contador_sol += 1
        case "Divorciado":
            contador_div += 1
        case "Viudo":
            contador_viu += 1
            # e. Datos de la persona viuda con mayor edad.
            if contador_viu == 1 or edad > maxima_edad:
                maxima_edad = edad
                maximo_apellido = apellito
                maximo_legajo = legajo
            

    # d. Datos de la persona más joven.
    if bandera_primer_per == True or edad < minima_edad:
        minima_edad = edad
        minimo_apellido = apellito
        minimo_estad_civ = estado_civ
        minimo_legajo = legajo
        
        bandera_primer_per = False
    
    seguir = input("Ingresar otra persona? (si/no): ")
    
    while seguir != "si" and seguir != "no":
        seguir = input("ERROR, ingresar (si/no): ")
        

contador_personas = contador_cas + contador_sol + contador_viu + contador_div 

porcentaje_cas = (contador_cas * 100) / contador_personas
porcentaje_sol = (contador_sol * 100) / contador_personas
porcentaje_div = (contador_div * 100) / contador_personas
porcentaje_viu = (contador_viu * 100) / contador_personas




#SALIDAS
print(contador_edad)

if contador_viu > 0:
    print(maximo_apellido)
    
if edades_cas > 0:
    promedio_edad_cas = edades_cas / contador_cas
    print(promedio_edad_cas)
else:
    print("No se pudo calcular el promedio")
