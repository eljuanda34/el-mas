positivo = 0
negativo = 0
suma = 0
for i in range(1,10):
    numero = int(input(f"digite el numero {i}: " ))
    if numero <=0:
        c = "el numero es negativo"
        negativo += 1
    else:
        c = "el numero es positivo"
        positivo += 1
    suma += numero
    prom = suma / 10

print("numeros positivos:", positivo)
print("numeros negativos:", negativo)
print( " la suma es :", suma)
print("el promedio es:", prom)