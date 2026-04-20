# 11. Mostrar un número aleatorio entre el 1 y el 10 inclusive.

import random

numero = random.randint(1, 10)

if numero >= 1 and numero <= 10:
    print("Número generado:", numero)
else:
    print("Error")