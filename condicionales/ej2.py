#2. A partir del ingreso de una edad, determinar si la persona es mayor de edad. Si es mayor o igual que 18 se mostrará el mensaje “UD ES MAYOR DE EDAD”.

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("UD ES MAYOR DE EDAD.")
else:
    print("Usted es menos de edad.")