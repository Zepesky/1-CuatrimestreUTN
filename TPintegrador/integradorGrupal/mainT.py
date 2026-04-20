from colorama import *

init(autoreset=True)
bandera = True
pacientes = 0
masculinos = 0
femeninos = 0
#variables maximas
max_temperatura = 0
temp_max_edad = 0
temp_max_nombre = ""
temp_max_genero = ""
temp_max_ingreso = ""

max_presion = 0
pres_max_edad = 0
pres_max_nombre = ""
pres_max_genero = ""
pres_max_ingreso = ""


#variables minimas
min_temperatura = 0
temp_min_edad = 0
temp_min_nombre = ""
temp_min_genero = ""
temp_min_ingreso = ""

A_pos = 0
A_neg = 0
B_pos = 0
B_neg = 0
AB_pos = 0
AB_neg = 0
O_pos = 0
O_neg = 0


print(Fore.RED + """
====================================
    ✙---------MEDICPY---------✙ 
====================================
""")
#Entradas...
while bandera:
    
    print(f"""
    ====================================
    |          -OPERACIONES-           |
    |**********************************|
    |-1.Archivo de pacientes           |
    |-2.Estadisticas                   |
    |-3.Deportes                       |
    ====================================
    |-Cant pacientes: {pacientes}      |
    ====================================
    """)
    operacion = int(input("Que operacion desea realizar: "))

    if operacion == 1:
        #archivo de paciente:
        while True:
            
            pacientes += 1
            
            #Datos doctor
            doctor = input(Fore.MAGENTA + "|> Doctor a cargo: " + Style.RESET_ALL)

            #paciente
            ingreso = input(Fore.GREEN + "|> Hora de ingreso 24HS: "+ Style.RESET_ALL)
            nombre_paciente = input(Fore.GREEN + "|> Nombre del paciente: "+ Style.RESET_ALL)
            apellido_paciente = input(Fore.GREEN + "|> Apellido: "+ Style.RESET_ALL)
            edad_paciente = int(input(Fore.GREEN + "|> Edad: "+ Style.RESET_ALL))

            genero = input(Fore.GREEN + "|> Género: (Femenino/Masculino/Otro): "+ Style.RESET_ALL)

            sangre = input(Fore.GREEN + "|> Tipo de Sangre: [A,B,AB,0][+ -]: "+ Style.RESET_ALL)
            kilos = int(float(input(Fore.GREEN + "|> Ingrese su peso: "+ Style.RESET_ALL)))

            temperatura = float(input(Fore.YELLOW +"|> Temperatura del paciente: "+ Style.RESET_ALL))
            frecuencia_cardiaca = float(input(Fore.YELLOW +"|> Frecuencia cardíaca: "+ Style.RESET_ALL))
            presion = float(input(Fore.YELLOW +"|> Presión arterial: "+ Style.RESET_ALL))
            dolor = int(input(Fore.YELLOW +"|> Escala de dolor (0-10): "+ Style.RESET_ALL))
            #Categoricas
            tos = str(input(Fore.YELLOW +"|> ¿Presenta tos? (sí/no): "+ Style.RESET_ALL))
            respiracion = int(input(Fore.YELLOW +"""|> Respiración:  1.Normal
            |               2.Agitada
            |               3.Irregular
            |               4.Dolor: """+ Style.RESET_ALL))
            vomitos = str(input(Fore.YELLOW +"|> Vómitos: (sí/no): "+ Style.RESET_ALL))
            medicamentos = str(input(Fore.YELLOW +"|> Toma medicación? (sí/no): "+ Style.RESET_ALL))
            ejercicio = str(input(Fore.YELLOW + "|> ¿Hace ejercicio? (sí/no): "+ Style.RESET_ALL))
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
            #--------------------
            #contadores
            if genero == "masculino" or genero == "m":
                masculinos += 1
            if genero == "femenino" or genero == "f":
                femeninos += 1
            #--------------------
            #Maximos
            if temperatura > max_temperatura:
                max_temperatura = temperatura
                temp_max_nombre = nombre_paciente + apellido_paciente
                temp_max_genero = genero
                temp_max_edad = edad_paciente
                temp_max_ingreso = ingreso

            if presion > max_presion:
                max_presion = presion
                pres_max_nombre = nombre_paciente + apellido_paciente
                pres_max_genero = genero
                pres_max_edad = edad_paciente
                pres_max_ingreso = ingreso
            #--------------------
            #Minimos
            if temperatura > min_temperatura:
                min_temperatura = temperatura
                temp_min_nombre = nombre_paciente + apellido_paciente
                temp_min_genero = genero
                temp_min_edad = edad_paciente
                temp_min_ingreso = ingreso
            #--------------------
            if sangre == "A+" or sangre == "a+":
                A_pos += 1
            if sangre == "A-" or sangre == "a-":
                A_neg += 1
            if sangre == "B+" or sangre == "b+":
                B_pos += 1
            if sangre == "B-" or sangre == "b-":
                B_neg += 1
            if sangre == "AB+" or sangre == "ab+":
                AB_pos += 1
            if sangre == "AB-" or sangre == "ab-":
                AB_neg += 1
            if sangre == "O+" or sangre == "o+":
                O_pos += 1
            if sangre == "O-" or sangre == "o-":
                O_neg += 1
            #--------------------
            #REGLAS

            print(Back.CYAN +"""
            ====================================
            ✙---------Recomendaciones---------✙ 
            ====================================
            """+ Style.RESET_ALL)

            if estado_critico and dolor_alto:
                print(Back.LIGHTRED_EX +"⚠ > Atención urgente."+ Style.RESET_ALL)

            if posible_infeccion and resp_agitada:
                print(Fore.GREEN +"⚠ > Posible afección respiratoria."+ Style.RESET_ALL)

            if dolor <= 3 and not fiebre and presion < 140:
                print(Fore.YELLOW +"△ > Condiciones leves control ambulatorio."+ Style.RESET_ALL)

            if 36 <= temperatura <= 37.5:
                print(Fore.YELLOW +"✔ > Temperatura normal"+ Style.RESET_ALL)

            if edad_paciente > 65 and fiebre and presion_alta:
                print(Back.RED +"⚠ > Posible problema "+ Style.RESET_ALL)

            if vomitos in ["s", "si", "sí"] and dolor <= 5:
                print(Fore.YELLOW +"△ > Posible problema digestivo" + Style.RESET_ALL)

            if resp_dolorosa and taquicardia:
                print(Fore.YELLOW +"⚠ > Evaluar oxigenación"+ Style.RESET_ALL)

            if posible_infeccion and dolor_alto:
                print(Fore.YELLOW +"⚠ > Posible afeccion respiratoria"+ Style.RESET_ALL)

            if riesgo_cardiovascular:
                print(Fore.YELLOW +"⚠ > Control cardiovascular"+ Style.RESET_ALL)

            if dolor_extremo and (fiebre or taquicardia):
                print(Back.RED + "⚠ > Dolor crítico acompañado de signos vitales alterados.\nSe recomienda atención médica urgente."+ Style.RESET_ALL)

            if estado_critico and riesgo_edad:
                print(Back.RED + "⚠ > Fiebre alta con taquicardia en paciente mayor.\n Se recomienda evaluación médica urgente."+ Style.RESET_ALL)

            if edad_paciente <= 12 and fiebre:
                print(Fore.YELLOW + "⚠ > Paciente pediátrico con fiebre"+ Style.RESET_ALL)

            if ejercicio in ["s","si","sí"]:
                cuantas_veces = int(input(Fore.YELLOW +"|> ¿Cuantas veces a la semana haces ejercicio? 1/5: "+ Style.RESET_ALL))
                clima_agua = input(Fore.YELLOW +"|> ¿En que clima se encuentra,cuando entrena? frio/templado/calor: "+ Style.RESET_ALL)
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
                        print(Fore.GREEN + "✔ > Podrias incrementar a tres veces por semana para lograr una buena forma fisica"+ Style.RESET_ALL)
                    elif cuantas_veces <=4:
                        print(Fore.GREEN + "✔ > Estas en buena forma física"+ Style.RESET_ALL)
                    else:
                        print(Fore.LIGHTGREEN_EX +"✔ > Tu nivel de actividad fisica es muy bueno" + Style.RESET_ALL)

            if ejercicio in ["n","no","nó"]:
                agua_act_fisica = 0
                clima_agua = 0
                print(Fore.YELLOW +" ✘ > Deberia practicar 3 veces por semana en lo posible"+ Style.RESET_ALL)

            if edad_paciente < 18:
                agua_por_edad = 200
            elif edad_paciente < 59:
                agua_por_edad = 100
            else:
                agua_por_edad = 300

            agua_total_mililitros = agua_por_peso + agua_por_edad + clima_agua + agua_act_fisica

            agua_paciente = (agua_total_mililitros/1000)



            print(f"""
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

            continuar = input("Desea realizar otro archivo? (s/n): ")

            if continuar != "s":
                print("Saliendo...")
                break

    elif operacion == 2:
        
        print("""
        ====================================
        |          -OPERACIONES-           |
        |**********************************|
        |           [Graficos]             |
        |-[1.Cantidad de generos]          |
        |-[2.Tipos de sangre]              |
        |**********************************|
        |-3.Estadisticas Generales         |
        ====================================
        """)
        estadisticas = int(input("Que grafico quiere ver [1,2,3]: "))
        
        if estadisticas == 1 and pacientes == 0:
            print("No hay datos para graficar...")
            estadisticas = int(input("Que grafico quiere ver [1,2,3]: "))

        if estadisticas == 1:
            #Generos
            total = masculinos + femeninos
            
            if total == 0:
                print("No hay datos para graficar...")
            
            else:
                porcentaje_m = (masculinos / total) * 100
                porcentaje_f = (femeninos / total) * 100 
                
                largo_barra = 30
                
                #masculinos
                llenos_m = int((porcentaje_m / 100) * largo_barra)
                vacios_m = largo_barra - llenos_m
                barra_m = "█" * llenos_m + "░" * vacios_m
                
                #femeninos
                llenos_f = int((porcentaje_f / 100) * largo_barra)
                vacios_f = largo_barra - llenos_f
                barra_f = "█" * llenos_f + "░" * vacios_f
                
                print("""
                    ====================================
                    |            -Generos-             |
                    ====================================
                """)

                print(f"Maculinos: {masculinos} {porcentaje_m}%")
                print(Fore.BLUE + f"M|{barra_m}|\n" + Style.RESET_ALL)

                print(f"Femeninos: {femeninos} {porcentaje_f}%")
                print(Fore.MAGENTA + f"F|{barra_f}|" + Style.RESET_ALL)
                
                volver = input("volver? (s/n): ")
                if volver != "s":
                    print("Saliendo...")
                    bandera = False


        elif estadisticas == 2:
                #Sangres
                total = A_pos + A_neg + B_pos + B_neg + AB_pos + AB_neg + O_pos + O_neg

                if total == 0:
                    print("No hay datos para graficar...")
                    
                print("""
                    ====================================
                    |            -Sangres-             |
                    ====================================
                """)
                if A_pos > 0:
                    porcentaje_A_pos = (A_pos / total) * 100
                    largo_barra = 30
                    lleno = int((porcentaje_A_pos / 100) * largo_barra)
                    vacio = largo_barra - lleno
                    barra = "█" * lleno + "░" * vacio
                    print(f"|A+|{porcentaje_A_pos:.1f}%| |{barra}|")

                if A_neg > 0:
                    porcentaje_A_neg = (A_neg / total) * 100
                    largo_barra = 30
                    lleno = int((porcentaje_A_neg / 100) * largo_barra)
                    vacio = largo_barra - lleno
                    barra = "█" * lleno + "░" * vacio
                    print(f"|A-|{porcentaje_A_neg:.1f}%| |{barra}|")
                    
                if B_pos > 0:
                    porcentaje_B_pos = (B_pos / total) * 100
                    largo_barra = 30
                    lleno = int((porcentaje_B_pos / 100) * largo_barra)
                    vacio = largo_barra - lleno
                    barra = "█" * lleno + "░" * vacio
                    print(f"|B+|{porcentaje_B_pos:.1f}%| |{barra}|")
                    
                if B_neg > 0:
                    porcentaje_B_neg = (B_neg / total) * 100
                    largo_barra = 30
                    lleno = int((porcentaje_B_neg / 100) * largo_barra)
                    vacio = largo_barra - lleno
                    barra = "█" * lleno + "░" * vacio
                    print(f"|B-|{porcentaje_B_neg:.1f}%| |{barra}|")

                if AB_pos > 0:
                    porcentaje_AB_pos = (AB_pos / total) * 100
                    largo_barra = 30
                    lleno = int((porcentaje_AB_pos / 100) * largo_barra)
                    vacio = largo_barra - lleno
                    barra = "█" * lleno + "░" * vacio
                    print(f"|AB+|{porcentaje_AB_pos:.1f}%| |{barra}|")

                if AB_neg > 0:
                    porcentaje_AB_neg = (AB_neg / total) * 100
                    largo_barra = 30
                    lleno = int((porcentaje_AB_neg / 100) * largo_barra)
                    vacio = largo_barra - lleno
                    barra = "█" * lleno + "░" * vacio
                    print(f"|AB-|{porcentaje_AB_neg:.1f}%| |{barra}|")
                    
                if O_pos > 0:
                    porcentaje_O_pos = (O_pos / total) * 100
                    largo_barra = 30
                    lleno = int((porcentaje_O_pos / 100) * largo_barra)
                    vacio = largo_barra - lleno
                    barra = "█" * lleno + "░" * vacio
                    print(f"|O+|{porcentaje_O_pos:.1f}%| |{barra}|")

                if O_neg > 0:
                    porcentaje_O_neg = (O_neg / total) * 100
                    largo_barra = 30
                    lleno = int((porcentaje_O_neg / 100) * largo_barra)
                    vacio = largo_barra - lleno
                    barra = "█" * lleno + "░" * vacio
                    print(f"|O-|{porcentaje_O_neg:.1f}%| |{barra}|")
                    
                    volver = input("volver? (s/n): ")
                    if volver != "s":
                        print("Saliendo...")
                        bandera = False

        elif estadisticas == 3:
            print("""
                    ====================================
                    |          -ESTADISTICAS-          |
                    |**********************************|
                    |-1.Casos Criticos                 |
                    |-2.Casos Leves                    |
            """)
            casos = int(input("Que estadisticas presisas ver"))
            
            if casos == 1:
                print("""
                        ====================================
                        |              -Casos-             |
                        |**********************************|
                        |1.Mayor temperatura               |
                        |2.Mayor presion                   |
                """)
                caso_critico = input("Que caso critico desea ver: ")
                if caso_critico == "1":
                    print(f"""
                        ======================================
                        |ingreso: [{temp_max_ingreso}        |
                        |************************************|
                        |Nombre [{temp_max_ingreso}]         |
                        |Edad [{temp_max_edad}]              |
                        |Genero [{temp_max_genero}]          |
                        |Temperatura [{max_temperatura}]     |
                        ======================================
                    """)
                    volver = input("volver? (s/n): ")
                    if volver != "s":
                        print("Saliendo...")
                        bandera = False
                    
                elif caso_critico == "2":
                    print(f"""
                        ======================================
                        |ingreso: [{pres_max_ingreso}        |
                        |************************************|
                        |Nombre [{pres_max_ingreso}]         |
                        |Edad [{pres_max_edad}]              |
                        |Genero [{pres_max_genero}]          |
                        |Temperatura [{max_presion}]         |
                        ======================================
                    """)
                    volver = input("volver? (s/n): ")
                    if volver != "s":
                        print("Saliendo...")
                        bandera = False
                        
                    elif caso_critico == "2":
                        pass
                        
                    
            elif casos == 2:
                print("""
                        ====================================
                        |              -Casos-             |
                        |**********************************|
                        |1.Menor temperatura               |
                        |2.
                """)
                caso_leve = input("Que caso critico desea ver: ")
                if caso_leve == "1":
                    print(f"""
                        ======================================
                        |ingreso: [{temp_min_ingreso}        |
                        |************************************|
                        |Nombre [{temp_min_ingreso}]         |
                        |Edad [{temp_min_edad}]              |
                        |Genero [{temp_min_genero}]          |
                        |Temperatura [{min_temperatura}]     |
                        ======================================
                    """)
                    volver = input("volver? (s/n): ")
                    if volver != "s":
                        print("Saliendo...")
                        bandera = False
                        
        else:
            print("Ingrese valor valido!")
            operacion = int(input("Que operacion desea realizar: "))
        
    continuar_menu = input("Desea realizar alguna otra operacion? (s/n): ")
    if continuar_menu != "s":
        print("Saliendo...")
        bandera = False