def crear_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any):
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz.append(fila)
        
    return matriz
    
def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print("")
        
        
matriz = crear_matriz(3,4,0)

mostrar_matriz(matriz)