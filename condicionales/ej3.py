#3. A partir del ingreso de una edad, determinar si la persona es mayor de edad o no. Si es mayor de 18 se mostrará el mensaje “UD ES MAYOR DE EDAD” caso contrario “UD ES MENOR DE EDAD”.

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("UD ES MAYOR DE EDAD.")
else:
    print("UD ES MENOR DE EDAD.")