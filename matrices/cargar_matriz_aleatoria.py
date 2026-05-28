def crear_matriz(cantidad_filas: int, cantidad_columnas: int, valor_inicial):
    matriz = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas
        matriz.append(fila)
    return matriz


def mostrar_matriz(matriz):  # ✅ agregar el parámetro
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] is not None:
                print(f"{matriz[i][j]}", end="\t")
            else:
                print("**", end="\t")
        print("")


def cargar_matriz_aleatoria(matriz, cant_filas, cant_columnas):
    seguir = "si"
    while seguir == "si":

        numero = int(input("Ingrese un número (distinto de 0): "))
        while numero == 0:
            print("El número no puede ser 0.")
            numero = int(input("Ingrese un número (distinto de 0): "))

        fila = int(input(f"Ingrese una fila (1 a {cant_filas}): "))
        while fila < 1 or fila > cant_filas:
            print(f"Fila inválida. Debe estar entre 1 y {cant_filas}.")
            fila = int(input(f"Ingrese una fila (1 a {cant_filas}): "))

        columna = int(input(f"Ingrese una columna (1 a {cant_columnas}): "))
        while columna < 1 or columna > cant_columnas:
            print(f"Columna inválida. Debe estar entre 1 y {cant_columnas}.")
            columna = int(input(f"Ingrese una columna (1 a {cant_columnas}): "))

        matriz[fila - 1][columna - 1] = numero

        seguir = input("¿Cargar otro? (si/no): ").strip().lower()
        while seguir not in ("si", "no"):
            print("Respuesta inválida.")
            seguir = input("¿Cargar otro? (si/no): ").strip().lower()


matriz = crear_matriz(3, 4, None)
cargar_matriz_aleatoria(matriz, len(matriz), len(matriz[0]))
mostrar_matriz(matriz)