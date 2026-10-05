def valor_inventario(cantidad, precio):
    return cantidad * precio
productos = []
gran_total_inventario = 0
numero_productos =(int(input("cuantos productos desea ingresar: ")))

for i in range(numero_productos):
    print(f"\nproducto {i+1}:")

    nombre = input("ingrese el nombre del producto: ")
    cantidad = int(input("ingrese la cantidad del producto: "))
    precio = float(input("ingrese el precio del producto: "))
    if cantidad < 5:
        print("tiene el stock bajo")
    
    subtotal = valor_inventario(cantidad, precio)
    gran_total_inventario += subtotal
    
    producto_diccionario = {
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad,
    "valor-total": subtotal
    }
    productos.append(producto_diccionario)
    
    print(f"el valor total del producto {nombre} es: {subtotal}")

print(f"el gran total del inventario es: {gran_total_inventario}")
print("\nproductos registrados:")
for producto in productos:
    print("-"*20)
    for clave, valor in producto.items():
        print(f"{clave}: {valor}")