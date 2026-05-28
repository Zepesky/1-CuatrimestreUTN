def crear_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial):
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz.append(fila)
    return matriz


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] is not None:
                print(f"{matriz[i][j]}", end="\t")
            else:
                print("**", end="\t")
        print("")


def producto_matriz(matriz_a, matriz_b):
    filas_a = len(matriz_a)
    columnas_a = len(matriz_a[0])
    columnas_b = len(matriz_b[0])

    matriz_resultado = crear_matriz(filas_a, columnas_b, 0)

    for i in range(filas_a):
        for j in range(columnas_b):
            for k in range(columnas_a):
                matriz_resultado[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return matriz_resultado


matriz_a = [[1, 2, 5],
            [2, 4, 3],
            [4, 7, 3]]

matriz_b = [[1, 2, 5],
            [4, 5, 3],
            [4, 2, 3]]

matriz_resultado = producto_matriz(matriz_a, matriz_b)
mostrar_matriz(matriz_resultado)