c = float(input("ingresa el valor de la compra: "))

if c <= 99999:
    d = c
    r ="no obtiene descuento"

elif c >= 100000 and c <= 199999:
    d = c*0.95
    r ="obtiene descuento del 5%"

else:
    d = c*0.90
    r ="obtiene el descuento del 10%"

print(" el valor de la cuenta es: ", d)
print(" el cliente: ", r)