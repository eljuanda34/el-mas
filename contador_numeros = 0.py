contador_numeros = 0
suma = 0
positivo = 0
negativo = 0
ceros = 0
pares = 0
impares = 0

cantidad_numeros = int(input(" ¿cuantos numeros desea ingresar? " ))


for i in range(cantidad_numeros):
    contador_numeros +=1
    print("\n ¿cual es su", contador_numeros, "numero? ")

    numero = int(input( "ingrese el numero: "))
    
    if numero>0:
        positivo += 1
    elif numero<0:
        negativo += 1
    else:
        ceros +=1

    if numero % 2 == 0:
            pares +=1
    else:
            impares +=1

    suma += numero
    prom = suma / cantidad_numeros

print("\n==============================")
print("RESUMEN FINAL")
print("total de numeros positivos", positivo)
print("total de numeros negativos", negativo)
print("total de numeros iguales a 0 son", ceros)
print("total de numeros pares", pares)
print("total de numeros impares", impares)
print("el promedio es ", prom)