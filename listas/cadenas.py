cadena = "Hello world"
nueva_cadena = ""

for i in range(len(cadena)):
    if cadena[i] == "l":
        nueva_cadena += "*"

        
print(nueva_cadena)