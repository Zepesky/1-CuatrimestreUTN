matrix = [
    [5,6,9,1], #0
    [4,3,1,9], #1
    [1,0,7,2]  #2
]


def mostrar_matriz():
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != None:
                print(f"{matrix[i][j]}", end="\t")
            else:
                print(f"**", end="\t")
        print("")
        
        
        
# sumar matices
def sumar_matriz(matriz):
    acumulador = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
                print(matrix[i][j])
                acumulador += matrix [i][j]
    return acumulador