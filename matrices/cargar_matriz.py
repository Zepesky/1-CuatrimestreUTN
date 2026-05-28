def cargar_matiz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            numero = int(input("ingrese un numero: "))
            
            matriz[i][j] = numero
            