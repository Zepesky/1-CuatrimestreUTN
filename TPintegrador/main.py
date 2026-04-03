from GodPlanes import tranfucion
from colorama import *


init(autoreset=True)

def separador():
    print(Back.WHITE + "=" * 36 + Style.RESET_ALL)
        

print(Fore.RED + """
====================================
    ✙---------MEDICPY---------✙ 
====================================
""")

#validacion de caracteres 
#Entradas...
while True:
    try:
        separador()
        #Datos doctor
        doctor = input(Fore.MAGENTA + "|-Doctor a cargo: " + Style.RESET_ALL).strip()
        separador()
        #paciente
        nombre_pac = input(Fore.GREEN + "|-Nombre del paciente: "+ Style.RESET_ALL).strip()
        apellido_pac = input(Fore.GREEN + "|-Apellido: "+ Style.RESET_ALL).strip()
        edad_pac = int(input(Fore.GREEN + "|-Edad: "+ Style.RESET_ALL))
        genero = input(Fore.GREEN + "|-Género: (Femenino/Masculino/Otro): "+ Style.RESET_ALL).strip().lower()
        sangre = input(Fore.GREEN + "|-Tipo de Sangre: [A,B,AB,0][+ -]: "+ Style.RESET_ALL).upper().strip()
        
        
        #✰NewSkill✰
        #.isalpha() es False cuando (" ", "nombre1", "nombre!")
        #.replace ("lo que busco", "lo nuevo")
        if not (doctor.replace(" ", "")).isalpha():
            print(Back.RED +"⚠︎ -Error Solo letras!")
            continue
        
        if not (nombre_pac.replace(" ", "")).isalpha():
            print(Back.RED +"⚠︎ -Error Nombre no valido!")
            continue
        
        if not (apellido_pac.replace(" ", "")).isalpha():
            print(Back.RED +"⚠︎ -Error Apellido no valido!")
            continue
        
        if genero not in ["femenino","masculino","otro"]:
            print(Back.RED +"⚠︎ -Error Genero no válido!")
            continue
        
        if sangre in ["A","B","AB","O"]:
            signo = input("Ingrese + o - : ").strip()
            sangre += signo
            continue
        
        if edad_pac <= 0 or edad_pac >= 120:
            print(Back.RED +"⚠︎ -Error edad no válida!")
            continue
        
        separador()
        break

    except ValueError:
        print(Back.RED +"⚠︎ -Error la Edad debe ser un numero!")
        
#-ayuda esto de validar ya me quemo!

while True:
    try:
        #Datos numericos
        temperatura = float(input(Fore.YELLOW +"|Temperatura del paciente: "+ Style.RESET_ALL))
        frec_cardiaca = float(input(Fore.YELLOW +"|Frecuencia cardíaca: "+ Style.RESET_ALL))
        presion = float(input(Fore.YELLOW +"|Presión arterial: "+ Style.RESET_ALL))
        dolor = int(input(Fore.YELLOW +"|Escala de dolor (0-10): "+ Style.RESET_ALL))

        #Categoricas
        tos = str(input(Fore.YELLOW +"|-¿Presenta tos? (sí/no): "+ Style.RESET_ALL)).lower()
        respiracion = int(input(Fore.YELLOW +"""|-Respiración:  1.Normal
|               2.Agitada
|               3.Irregular
|               4.Dolor: """+ Style.RESET_ALL))
        vomitos = str(input(Fore.YELLOW +"|-Vómitos: (sí/no): "+ Style.RESET_ALL)).lower()
        medicamentos = str(input(Fore.YELLOW +"|-Toma medicación?: (sí/no):"+ Style.RESET_ALL)).lower()
        
        if tos not in ["s", "si", "sí", "no"]:
            print(Back.RED +"⚠︎ -Error Solo letras!")
            continue
                
        if vomitos not in ["s", "si", "sí", "no"]:
            print(Back.RED +"⚠︎ -Error Solo letras!")
            continue 
                
        if medicamentos not in ["s", "si", "sí", "no"]:
            print(Back.RED +"⚠︎ -Error Solo letras!")
            continue
        if not 0 <= dolor <= 10:
            print(Back.RED + "⚠︎ -Error escala de dolor debe ser 0-10!")
            continue            
                    
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
    if (tos in ["s", "si", "sí"]  and fiebre) or (respiracion == "2"):
        lista.append("Posible afección respiratoria.")
    if dolor <= 3:
        lista.append("Condiciones leves control ambulatorio.")
    if 36 <= temperatura <= 37.5:
        lista.append("Temperatura normal")
    if edad_pac > 65 and fiebre and presion_alta:
        lista.append("Paciente de riesgo")
    if vomitos in ["s", "si", "sí"] and dolor <= 5:
        lista.append("Posible problema digestivo")
    if (respiracion == "4") and taquicardia:
        lista.append("Evaluar oxigenación")
    if fiebre and tos in ["s", "si", "sí"] and dolor > 5:
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
Sangre: {sangre}
------------------------------------
Medicación previa: {Fore.LIGHTYELLOW_EX}{medicamentos}{Style.RESET_ALL}
Respiración: {Fore.LIGHTCYAN_EX}{respiracion}{Style.RESET_ALL}
Presión: {Fore.LIGHTCYAN_EX}{presion}{Style.RESET_ALL}
Temperatura: {Fore.LIGHTCYAN_EX}{temperatura}{Style.RESET_ALL}
Dolor: {Fore.LIGHTCYAN_EX}{dolor}{Style.RESET_ALL}
FrCardiaca: {Fore.LIGHTCYAN_EX}{frec_cardiaca}{Style.RESET_ALL}
------------------------------------
""")
separador()
for x in resultado:
    if "urgente" in x.lower() or "crítico" in x.lower():
        print(Fore.RED + "⚠ " + x)
    elif "riesgo" in x.lower():
        print(Fore.YELLOW + "⚠ " + x)
    else:
        print(Fore.GREEN + "- " + x)
separador()

#✰NewSkill✰ 
#from (archivo.py) import (parametro) esto importa
#   un archivo que este en la misma carpeta
print(tranfucion(sangre))