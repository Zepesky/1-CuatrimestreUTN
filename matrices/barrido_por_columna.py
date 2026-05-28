

def mostrar_matriz_por_columna(matriz):
    for i in range(len(matriz[0])):
        for j in range(len(matriz[i])):
                print(f"{matriz[i][j]}", end="\t")

        
def sumar_matriz(matriz):
    acumulador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
                print(matriz[i][j])
                acumulador += matriz [i][j]
    return acumulador

matriz = [  [1,3,6,5],
            [3,9,8,2],
            [2,5,6,4]
]

mostrar_matriz_por_columna(matriz)

sumar_matriz(matriz)
