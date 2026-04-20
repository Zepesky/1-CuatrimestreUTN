# 5. Imprimir los números múltiplos de 3 entre el 1 y el 10

for i in range(3, 11, 3):
    print(i)

for i in range(1, 11):
    if i % 3 == 0:
        print(i)