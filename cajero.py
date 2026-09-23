s = float(input("saldo disponible: "))
m = float(input("monto a retirar: "))
t = input("tipo de cuanta ahorros o corriente: ")
ss = input(" tienes tarjeta activa? ")

if ss != "si":
    w = "tarjeta bloqueada o inactiva"
elif m<=0:
    w = "monto invalido"
elif m > s:
    w = "saldo insuficiente"
elif t == "ahorros" and m > 1000000:
    w = "excede el maximo permitido a retirar de 1000000"
elif t == "corriente" and m > 2000000:
    w = "excede el maximo permitido a retirar de 2000000"
else:
    restante = s - m
 
if m > 500000:
        w = f"Retiro grande: verifique la operación. Saldo restante: {restante}"
else:
        w = f"Retiro normal. Saldo restante: {restante}"
print(m)