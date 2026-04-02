#10. Realizar un programa que a partir del ingreso del importe de una compra, aplique un 25% de descuento. Mostrar por pantalla cuánto es el total a pagar y cuánto fue el descuento obtenido.

print("""
__________________
    apusmarket
==================
    Productos 
==================
1. Monster: $2,900
2. Cafe: $2,000
3. Pizza: $ 12,000
==================
""")

total = 0

while True:
    x = int(input("Ingrese el importe del producto: "))
    
    total += x
    
    y = str(input("Desea comprar algo mas? (s/n): ")).lower()

    if y != "s":
        break

print(f"Total a pagar: ${total}")