def registar_ventas():

    ventas = []
    num_ventas = int(input("cuantas ventas desea registrar: "))

    for i in range(num_ventas):
        print(f"\nventa {i + 1}:")
        nombre = input("Ingrese el nombre del producto: ")
        valor = float(input("Ingrese el valor del producto: "))
        ventas.append({"nombre": nombre, "valor": valor})
    return ventas
def analizar_ventas(listas_ventas):

    if not listas_ventas:
        print("No hay ventas registradas.")
        return
    
    total_vendido = sum(x["valor"] for x in listas_ventas)
    promedio = total_vendido / len(listas_ventas)
    venta_mas_alta = max(listas_ventas, key=lambda x: x["valor"])

    if total_vendido > 500000:
        print("meta alcanzada")
    else:
        print("meta no alcanzada")
    
    print("\n"+ "-" * 30)
    print(f"numero de ventas registradas:{len(listas_ventas)}")
    print(f"total vendido:{total_vendido}:")
    print(f"promedio vendido:{promedio}" )
    print(f"venta de mayor valor:{venta_mas_alta["nombre"]}({venta_mas_alta["valor"]})")
    
mis_ventas = registar_ventas()
analizar_ventas(mis_ventas)