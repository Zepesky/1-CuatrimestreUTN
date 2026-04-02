from colorama import *
init(autoreset=True)

def separador():
    print(Back.WHITE + "=" * 32 + Style.RESET_ALL)


#Entradas...

print(Fore.RED + """
===============================
   ✙ SISTEMA MÉDICO BÁSICO ✙ 
===============================
""")
#Datos doctor
separador()
while True:
    try:
        doctor = str(input(Fore.MAGENTA + "|-Doctor a cargo: " + Style.RESET_ALL))
        separador()
        #paciente
        nombre_pac = str(input(Fore.GREEN + "|-Nombre del paciente: "+ Style.RESET_ALL))
        apellido_pac = str(input(Fore.GREEN + "|-Apellido: "+ Style.RESET_ALL))

        #validacion de caracteres str rompe codigo

        edad_pac = int(input(Fore.GREEN + "|-Edad: "+ Style.RESET_ALL))        
        genero = str(input(Fore.GREEN + "|-Género: (Femenino/Masculino/Otro): "))
        separador()

        #Datos numericos
        temperatura = float(input(Fore.YELLOW +"|Temperatura del paciente: "+ Style.RESET_ALL))
        frec_cardiaca = float(input(Fore.YELLOW +"|Frecuencia cardíaca: "+ Style.RESET_ALL))
        presion = float(input(Fore.YELLOW +"|Presión arterial: "+ Style.RESET_ALL))
        dolor = int(input(Fore.YELLOW +"|Escala de dolor (0-10): "+ Style.RESET_ALL))

        #Categoricas
        tos = str(input(Fore.YELLOW +"|-¿Presenta tos? (sí/no): "+ Style.RESET_ALL)).lower()
        respiracion = str(input(Fore.YELLOW +"|-Respiración: Normal, Agitada, Irregular, Dolor: "+ Style.RESET_ALL)).lower()
        vomitos = str(input(Fore.YELLOW +"|-Vómitos: (sí/no): "+ Style.RESET_ALL)).lower()
        medicamentos = str(input(Fore.YELLOW +"|-Toma medicación?: (sí/no):"+ Style.RESET_ALL)).lower()
        break
    except ValueError:
        print(Back.RED +"⚠︎ -Error Dato no válido!")
separador()
#reglas
def recomendaciones():
    lista = []
    
    #var modificadas
    fiebre = temperatura >= 38
    taquicardia = frec_cardiaca > 100
    presion_alta = presion > 140

    if fiebre and taquicardia and dolor > 7:
        lista.append("Atención urgente.")
    if (tos in ["s", "si", "sí"]  and fiebre) or (respiracion == "agitada"):
        lista.append("Posible afección respiratoria.")
    if dolor <= 3:
        lista.append("Condiciones leves control ambulatorio.")
    if 36 <= temperatura <= 37.5:
        lista.append("Temperatura normal")
    if edad_pac > 65 and fiebre and presion_alta:
        lista.append("Paciente de riesgo")
    if (vomitos == "s") and dolor <= 5:
        lista.append("Posible problema digestivo")
    if (respiracion == "dolor") and taquicardia:
        lista.append("Evaluar oxigenación")
    if fiebre and tos == "s" and dolor > 5:
        lista.append("Reposo y seguimiento")
    if presion_alta and edad_pac > 50:
        lista.append("Control cardiovascular")
    if dolor >= 9:
        lista.append("Dolor crítico, internación preventiva")
    if temperatura >= 39:
        lista.append("Fiebre alta")
    if edad_pac <= 12 and fiebre:
        lista.append("Paciente pediátrico con fiebre")
    if not lista:
        lista.append("Sin indicadores de riesgo importantes")
        
    return lista
    
resultado = recomendaciones()

    
print(f"""
====================================
Doctor a cargo: {doctor}
------------------------------------
        Datos del paciente
Paciente: {nombre_pac} {apellido_pac}
Edad: {edad_pac}
Genero: {genero}
------------------------------------
Medicacion previa: {medicamentos}
------------------------------------
""")
print("=" * 32)

for x in resultado:
    if "urgente" in x.lower() or "crítico" in x.lower():
        print(Fore.RED + "⚠ " + x)
    elif "riesgo" in x.lower():
        print(Fore.YELLOW + "⚠ " + x)
    else:
        print(Fore.GREEN + "- " + x)
        
print("=" * 32)