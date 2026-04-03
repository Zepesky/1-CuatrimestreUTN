#lugar de pruebas de codigo ;)
from colorama import *

def transfusion(sangre):
    
    print(Back.RED +f"""
    ====================
        3.Trasfucion
    ====================
        """+ Style.RESET_ALL)

    op = int(input("Que desea hacer?:"))
    
    if op == 3:
        comparador = input("Tipo de sangre de 2do paciente: ").upper().strip()
    
        if op == 3:
            if sangre == "A+" and comparador in ["A+","A-","O+","O-"]:
                return("Transfucion exitosa.")
            elif sangre == "B+" and comparador in ["B+","B-","O+","O-"]:
                return("Transfucion exitosa.")
            elif sangre == "AB+" and comparador in ["A+","A-","O+","O-","AB-"]:
                return("Transfucion exitosa.")
            elif sangre == "A-" and comparador in ["A-","O-"]:
                return("Transfucion exitosa.")
            elif sangre == "B-" and comparador in ["B-","O-"]:
                return("Transfucion exitosa.")       
            elif sangre == "AB-" and comparador in ["A-","B-","AB-","O-"]:
                return("Transfucion exitosa.")
            elif sangre == "O+" and comparador in ["O+","O-"]:
                return("Transfucion exitosa.")
            elif sangre == "O-" and comparador in ["O-"]:
                return("Transfucion exitosa.") 
            else:
                return("Tipos sangre no compatibles.")
    
