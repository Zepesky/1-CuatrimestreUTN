def crear_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial: any):
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz.append(fila)

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != None:
                print(f"{matriz[i][j]}", end="\t")
            else:
                print(f"**", end="\t")
        print("")
        
def suma_matriz(matriz_a, matriz_b):
    #verificar q el rango sea igual
    matriz_resultado = crear_matriz(len(matriz_a), len(matriz_b[0]),0)

    for i in range(len(matriz_a)):
        for j in range(len(matriz_a[i])):
            matriz_resultado[i][j] = matriz_a[i][j] + matriz_a[i][j]
    return matriz_resultado
    
matriz_a = [[1,2,5],
            [2,6,3],
            [4,7,3]
]         
matriz_b = [ [1,2,5],
            [4,5,3],
            [4,2,3]
]

suma_matriz(matriz_a, matriz_b)
mostrar_matriz(matriz_resultado)