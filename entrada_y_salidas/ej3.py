from colorama import Fore, init
init(autoreset=True, convert=True)

#3. Realizar un programa que pida el ingreso del nombre y la edad de una persona por input. Mostrar la información con el siguiente formato: “Su nombre es: ____ y tiene: ___ años”. Utilizar colorama para mostrar el valor de las variables.

nombre = str(input("Cual es su nombre?: "))

edad = input("Cual es su edad?: ")

print(f"Su nombre es {Fore.MAGENTA}{nombre} y tiene {Fore.LIGHTRED_EX}{edad} años")

