#12.ingresar un numero. determinar su es primo o no primo
primo = True

numero = int(input("ingrese un numero: "))
for i in range (2, numero):
    if numero % i == 0:
        primo = False
        break
    
if primo and numero > 1:
    print("Es primo")
else:
    print("no es primo")