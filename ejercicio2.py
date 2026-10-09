productos = {"helado": 5000,"gaseosa":3500, "pan":4000}

def venta(prod,cant):
    if prod in productos:
        total = cant * productos[prod]
    return total

nombre = input("Ingrese nombre del cliente: ")
documento = input("Ingrese Documento del cliente: ")
Telefono = input("Ingrese Telefono del cliente: ")
cant_prod = int(input("Ingrese cantidad de productos: "))

lista_producto = []
total=0
canti_pro=0
for i in range(cant_prod):
    prod = input(f"Ingrese nombre del producto {i+1}: ")
    cant = int(input("Ingrese cantidad: "))
    total_pro = venta(prod,cant)
    total+=total_pro
    canti_pro+=cant
    lista_producto.append((prod,cant,total_pro))
print("-"*15,"Datos del Cliente","-"*15)
for prod,cant,total_pro in lista_producto:
     print("-"*15,"Detalles","-"*15)
     print(f"Producto: {prod}")
     print(f"Cantidad: {cant}")
     print(f"Subtotal: $ {total_pro:,}")
print("-"*15,"Datos de La compra","-"*15)
print(f"Total de Productos: {canti_pro}")
print(f"Total a Pagar: $ {total:,}")