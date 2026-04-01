#4. Realizar un programa que pida el ingreso de la descripción de un producto y su precio. Mostrar los datos con el siguiente formato y con un solo print

producto = str(input("Que producto desea agregar?: "))

precio = int(input("precio del producto: "))

print(f"""
=====================
Producto: {producto}
- - - - - - - - - - -

precio: {precio}

=====================
""")