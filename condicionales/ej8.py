# 8. A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:

# ● Menos de 160 cm: Base

# ● Entre 160 cm y 179 cm: Escolta

# ● Entre 180 cm y 199 cm: Alero

# ● 200 cm o más: Ala-Pívot o Pívot

altura = int(input("Ingrese la altura del jugador: "))

if altura < 160:
    print("Sera Base")
elif 160 <= altura <= 179:
    print("Sera Escolta")
elif 180 <= altura <= 199:
    print("Seras Alero")
elif altura >= 200:
    print("Sera Pivot")
else:
    print("Sera espectador")

