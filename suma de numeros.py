c = int(input("digite el numero? "))
suma = 0
for x in range(1,c+1):
     print (x) 
     suma = suma + x
print("la suma es:", suma)

suma = 0
for i in range(1,6):
     numero = float(input(f"digite el numero {i}: "))
     suma += numero
     prom = suma / 5

print("el promedio es:", prom)

edad = 0
resultado = ""
for i in range(1,6):
     edad = int(input(f"digite la edad de la persona {i}: "))
     if edad >= 18:
          r = "es mayor de edad"
     else:
          r = "es menor de edad"
     resultado += f"la persona {i} {r}\n"
print("\n=== reporte de edades ===")
print(resultado)