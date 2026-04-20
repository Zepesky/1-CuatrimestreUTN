# 7. Pedirle al usuario su edad, determinar si es mayor (18 años o más), niño/a (menor de 10), pre-adolescente (edad entre 10 y 13 años inclusive) o adolescente (edad entre 13 y 17 años).

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Sos un adulto.")
elif edad < 10:
    print("Eres un niño.")
elif 10 <= edad <= 12:
    print("Eres pre adolecente.")
elif 13 <= edad <= 17:
    print("Eres un adolcente.")
else:
    print("Eres un adulto.")