producto ={
    "nombre":"genoprazol",
    "precio": 7000,
    "cantidad":5,
    "categotia":"IBP"
}
print (producto)
producto["nombre"]
print (producto ["nombre"])

producto["precio"]
print (producto["precio"])

producto ["precio"] = 9345
print (producto)

producto["marca"] = "genoma_lab"

del producto ["cantidad"]
print (producto)
for x in producto:
    print(x)
for x in producto.values():
    print(x)
    
for x in producto.items():
    print(x)