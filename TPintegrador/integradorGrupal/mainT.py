from colorama import *

init(autoreset=True)

def separador():
    print(Back.WHITE + "=" * 36 + Style.RESET_ALL)
        

print(Fore.RED + """
====================================
    ✙---------MEDICPY---------✙ 
====================================
""")

#Entradas...


#Datos doctor
doctor = input(Fore.MAGENTA + "|-Doctor a cargo: " + Style.RESET_ALL).strip()

#paciente
nombre_paciente = input(Fore.GREEN + "|-Nombre del paciente: "+ Style.RESET_ALL).strip()
apellido_paciente = input(Fore.GREEN + "|-Apellido: "+ Style.RESET_ALL).strip()
edad_paciente = int(input(Fore.GREEN + "|-Edad: "+ Style.RESET_ALL))
    
genero = input(Fore.GREEN + "|-Género: (Femenino/Masculino/Otro): "+ Style.RESET_ALL).strip().lower()
sangre = input(Fore.GREEN + "|-Tipo de Sangre: [A,B,AB,0][+ -]: "+ Style.RESET_ALL).upper().strip()
kilos = int(float(input(Fore.GREEN + "|-Ingrese su peso: "+ Style.RESET_ALL)))

temperatura = float(input(Fore.YELLOW +"|Temperatura del paciente: "+ Style.RESET_ALL))
frecuencia_cardiaca = float(input(Fore.YELLOW +"|Frecuencia cardíaca: "+ Style.RESET_ALL))
presion = float(input(Fore.YELLOW +"|Presión arterial: "+ Style.RESET_ALL))
dolor = int(input(Fore.YELLOW +"|Escala de dolor (0-10): "+ Style.RESET_ALL))
#Categoricas
tos = str(input(Fore.YELLOW +"|-¿Presenta tos? (sí/no): "+ Style.RESET_ALL)).lower()
respiracion = int(input(Fore.YELLOW +"""|-Respiración:  1.Normal
|               2.Agitada
|               3.Irregular
|               4.Dolor: """+ Style.RESET_ALL))
vomitos = str(input(Fore.YELLOW +"|-Vómitos: (sí/no): "+ Style.RESET_ALL)).lower()
medicamentos = str(input(Fore.YELLOW +"|-Toma medicación? (sí/no): "+ Style.RESET_ALL)).lower()
ejercicio = str(input(Fore.YELLOW + "|-¿Hace ejercicio? (sí/no): "+ Style.RESET_ALL)).lower()


#calculos

fiebre = temperatura >= 38
taquicardia = frecuencia_cardiaca > 100
presion_alta = presion > 140

riesgo_edad = edad_paciente > 60
dolor_alto = dolor >= 7
dolor_extremo = dolor >= 9

resp_agitada = respiracion == 2
resp_dolorosa = respiracion == 4

posible_infeccion = fiebre and tos in ["s","si","sí"]
estado_critico = fiebre and taquicardia
riesgo_cardiovascular = presion_alta and edad_paciente > 50
agua_por_peso = kilos * 30
agua_act_fisica = 0
clima_agua = 0

#-------------------
if respiracion == 1:
    respiracion_str = "Normal"
elif respiracion == 2:
    respiracion_str = "Agitada"
elif respiracion == 3:
    respiracion_str = "Irregular"
elif respiracion == 4:
    respiracion_str = "Con dolor"
else:
    respiracion_str = "Desconocida"

#REGLAS

print(Back.CYAN +"""
====================================
✙---------Recomendaciones---------✙ 
====================================
"""+ Style.RESET_ALL)

if estado_critico and dolor_alto:
    print(Back.LIGHTRED_EX +"⚠ -Atención urgente."+ Style.RESET_ALL)

if posible_infeccion and resp_agitada:
    print(Fore.GREEN +"⚠ -Posible afección respiratoria."+ Style.RESET_ALL)

if dolor <= 3 and not fiebre and presion < 140:
    print(Fore.YELLOW +"△ -Condiciones leves control ambulatorio."+ Style.RESET_ALL)

if 36 <= temperatura <= 37.5:
    print(Fore.YELLOW +"✔ -Temperatura normal"+ Style.RESET_ALL)

if edad_paciente > 65 and fiebre and presion_alta:
    print(Back.RED +"⚠ -Posible problema "+ Style.RESET_ALL)

if vomitos in ["s", "si", "sí"] and dolor <= 5:
    print(Fore.YELLOW +"△ -Posible problema digestivo" + Style.RESET_ALL)

if resp_dolorosa and taquicardia:
    print(Fore.YELLOW +"⚠ -Evaluar oxigenación"+ Style.RESET_ALL)

if posible_infeccion and dolor_alto:
    print(Fore.YELLOW +"⚠ -Posible afeccion respiratoria"+ Style.RESET_ALL)

if riesgo_cardiovascular:
    print(Fore.YELLOW +"⚠ -Control cardiovascular"+ Style.RESET_ALL)

if dolor_extremo and (fiebre or taquicardia):
    print(Back.RED + "⚠ -Dolor crítico acompañado de signos vitales alterados.\nSe recomienda atención médica urgente."+ Style.RESET_ALL)

if estado_critico and riesgo_edad:
    print(Back.RED + "⚠ -Fiebre alta con taquicardia en paciente mayor.\n Se recomienda evaluación médica urgente."+ Style.RESET_ALL)

if edad_paciente <= 12 and fiebre:
    print(Fore.YELLOW + "⚠ -Paciente pediátrico con fiebre"+ Style.RESET_ALL)

if ejercicio in ["s","si","sí"]:
    cuantas_veces = int(input(Fore.YELLOW +"|-¿Cuantas veces a la semana haces ejercicio? 1/5: "+ Style.RESET_ALL))
    clima_agua = input(Fore.YELLOW +"|-¿En que clima se encuentra,cuando entrena? frio/templado/calor: "+ Style.RESET_ALL)
    if clima_agua == "frio":
        clima_agua = 0
    elif clima_agua == "templado":
        clima_agua = 250
    else:
        clima_agua = 1000

    if cuantas_veces < 3:
        agua_act_fisica = 400
    else:
        agua_act_fisica = 800
    if not 1 <= cuantas_veces <= 7:
        print("Valor inválido")
    else:    
        if  cuantas_veces <= 2:
            print(Fore.GREEN + "✔ -Podrias incrementar a tres veces por semana para lograr una buena forma fisica"+ Style.RESET_ALL)
        elif cuantas_veces <=4:
            print(Fore.GREEN + "✔ -Estas en buena forma física"+ Style.RESET_ALL)
        else:
            print(Fore.LIGHTGREEN_EX +"✔ -Tu nivel de actividad fisica es muy bueno" + Style.RESET_ALL)

if ejercicio in ["n","no","nó"]:
    agua_act_fisica = 0
    clima_agua = 0
    print(Fore.YELLOW +" ✘ -Deberia practicar 3 veces por semana en lo posible"+ Style.RESET_ALL)

if edad_paciente < 18:
    agua_por_edad = 200
elif edad_paciente < 59:
    agua_por_edad = 100
else:
    agua_por_edad = 300

agua_total_mililitros = agua_por_peso + agua_por_edad + clima_agua + agua_act_fisica

agua_paciente = (agua_total_mililitros/1000)


    
print(Back.WHITE + f"""
====================================
Doctor a cargo: {doctor}
------------------------------------
        Datos del paciente
Paciente: {nombre_paciente} {apellido_paciente}
Edad: {edad_paciente}
Genero: {genero}
Sangre: {sangre}
------------------------------------
Medicación previa: {Fore.LIGHTYELLOW_EX}{medicamentos}{Style.RESET_ALL}
Respiración: {Fore.LIGHTCYAN_EX}{respiracion_str}{Style.RESET_ALL}
Presión: {Fore.LIGHTCYAN_EX}{presion}{Style.RESET_ALL}
Temperatura: {Fore.LIGHTCYAN_EX}{temperatura}{Style.RESET_ALL}
Dolor: {Fore.LIGHTCYAN_EX}{dolor}{Style.RESET_ALL}
FrCardiaca: {Fore.LIGHTCYAN_EX}{frecuencia_cardiaca}{Style.RESET_ALL}
Ejercicio: {Fore.LIGHTCYAN_EX}{ejercicio}{Style.RESET_ALL}
Agua que debe tomar el paciente: {Fore.LIGHTCYAN_EX} {agua_paciente:.2f}{Style.RESET_ALL}
------------------------------------
====================================
""")
