#4. A partir del ingreso de la altura de un basquetbolista determinar si es pivot o no. Para serlo el mismo deberá medir más de 1.80 metros.

altura = float(input("Cual es su altura?: "))

if altura > 1.80:
    print("Seras pivot.")
else:
    print("No seras  pivot.")