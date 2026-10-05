def calcular_total(cantidad):
    """Recibe una lista de la cantidad y devuelve su total."""
    gran_total_inventario = 0
    return cantidad * precio

def producto_mas_vendido(total_vent):
    """Determinar la cantidad del producto según su subtotal."""
    
    for ventas_db in ventas_db:
        nombre = ventas_db["nombre del producto"]
        cantidad = ventas_db["cantidad"]
        if nombre in cantidad:
            cantidad[nombre] += cantidad
        else:
            cantidade[nombre] = cantidad
        
    producto_mayor = None
    cantidad_mayor = 0
    for nombre, cantidad in cantidades.items():
        if cantidades > cantidad_mayor:
            cantidad_mayor = cantidad
            producto_mayor = nombre
    print(f"producto mas vedido: {producto_mayor}" )
    print(f"cantidad vendida: {cantidad_mayor}")
     
def registrar_venta(lista_ventas):

    """Solicita datos, procesa rendimiento y guarda las ventas."""
    print("\n--- Registrar Nueva venta ---")
    nombre = input("Nombre del producto: ").strip()
    precio = float(input("precio del producto: "))
    cantidad = int(input("cantidad del producto: "))
    
    subtotal = registrar_venta(lista_ventas)
    gran_total_inventario += subtotal
    
    ventas = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "total_vent": subtotal
    }
    
    lista_ventas.append(ventas)
    print(f"¡ {nombre} registrado con éxito !")

def mostrar_ventas(lista_ventas):
    """Muestra la lista completa de ventas registradas."""
    print("\n--- Lista de ventas ---")
    if not lista_ventas:
        print("No hay ventas registradas en el sistema.")
        return

    for est in lista_ventas:
        print(f"nombre: {est['nombre']} | precio: {est['precio']} | cantidad: {est['cantidad']} | total_venta: {est['total_vent']} | : ({est['subtotal']})")

def buscar_producto(lista_ventas):
    """REQUISITO 6: Busca un producto por su nombre exacto."""
    print("\n--- Buscar producto ---")
    if not lista_ventas:
        print("El sistema está vacío.")
        return
        
    nombre_buscar = input("Ingresa el nombre del producto a buscar: ").strip()
    
    for est in lista_ventas:

        if est["nombre"].lower() == nombre_buscar.lower():
            print("\n¡Estudiante producto en contrado!")
            print(f"Nombre: {est['nombre']}")
            print(f"precio: {est['precio']}")
            print(f"cantidad: {est['cantidad']}")
            print(f"total_venta: {est['total-vent']:.2f}")
            print(f"subtotal: {est['subtotal']}")
            return
            
    print(f"No se encontró ningún producto con el nombre '{nombre_buscar}'.")

def iniciar_sistema():
    ventas_db = []

    while True:

        print("\n=== SISTEMA DE ADMISTRACION DE VENTAS ===")
        print("1. Registrar venta")
        print("2. Mostrar todas las ventas")
        print("3. Buscar producto")
        print("4. Mostrar total vendido")
        print("5. producto mas vendido")
        print("6. salir ")
        
        opcion = input("Selecciona una opción (1-6): ").strip()
        
        if opcion == "1":
            registrar_venta(ventas_db)
        elif opcion == "2":
            mostrar_todas_las_ventas(ventas_db)
        elif opcion == "3":
            buscar_producto(ventas_db)
        elif opcion == "4":
            mostrar_total_vendido(ventas_db)
        elif opcion == "5":
            producto_mas_vendido(ventas_db)
        elif opcion == "6":
            print("Saliendo del sistema. ¡Que tengas un excelente día!")
            break
        else:
            print("Opción no válida. Por favor, introduce un número del 1 al 6.")

iniciar_sistema()