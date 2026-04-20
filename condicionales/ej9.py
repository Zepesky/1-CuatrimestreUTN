# 9. Los argentinos nativos y por opción desde los dieciséis (16) años y los argentinos naturalizados desde los dieciocho (18) años están habilitados a votar. A partir del ingreso de la edad del usuario y el estado (si es naturalizado o nativo), se deberá informar si es o no posible que la persona concurra a votar en base a la información suministrada.

edad = int(input("Ingrese su edad: "))
tipo = input("Ingrese si es nativo o naturalizado: ")

if tipo == "nativo":
    if edad >= 16:
        print("Podés votar.")
    else:
        print("No podés votar.")

elif tipo == "naturalizado":
    if edad >= 18:
        print("Podés votar.")
    else:
        print("No podés votar.")

else:
    print("Tipo inválido.")