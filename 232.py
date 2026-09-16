n1 = float(input("ingrese primera nota "))
n2 = float(input("ingrese segunda nota "))
n3 = float(input("ingrese tercera nota "))

prom = (n1 + n2 + n3) / 3

if prom <= 2.9:
    r ="reprobado"

elif prom >= 3.0 and prom <= 3.9:
    r ="aceptable"

elif prom >= 4.0 and prom <=4.5:
    r = "bueno"

else:
    r = "excelente"

print(" el promedio es: ", prom)
print("el estudiante esta: ", r)