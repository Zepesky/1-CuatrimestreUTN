def crear_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any):
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz.append(fila)

def mostrar_matriz():
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != None:
                print(f"{matriz[i][j]}", end="\t")
            else:
                print(f"**", end="\t")
        print("")
        
def multiplicar_matriz_por_ezcalar(matriz, escalar):
    matriz_resultado = crear_matriz(len(matriz), len(matriz[0]),0)

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz_resultado[i][j] = matriz[i][j] * escalar

    return matriz_resultado
    
matriz = [[1,2,5],
          [2,6,3],
          [4,7,3]
]

escalar = 5

matriz_resultado = multiplicar_matriz_por_ezcalar(matriz, escalar)
mostrar_matriz(matriz)