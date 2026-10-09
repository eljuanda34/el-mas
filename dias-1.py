print("-"*30, "BIENVENIDO A NUESTRA PAGINA PARA VER PELICULAS", "-"*30)
tarifas = {"lunes": 5000, "martes": 5000, "miércoles": 6000, "jueves": 6000, "viernes": 7000, "sábado": 8000, "domingo": 8000}
print("tarifas de peliculas por dia de la semana")
for dia, tarifa in tarifas.items():
    print(f"{dia.capitalize()}: ${tarifa:,}")
print("-"*30, "-", "-"*30)
dia = input("Ingrese el dia de la semana: ").lower()

peliculas =["chuky", "el conjuro", "iro man", "dragon ball z", "el chapulin"]
print("peliculas disponibles")
for codigo, pelicula in enumerate(peliculas, start=1):
    print(f"{codigo}: {pelicula}")
print("-"*30, "-", "-"*30)
nombre = input("Ingrese el nombre de la pelicula: ").lower()
cantidad = int(input("Ingrese la cantidad de entradas: "))
monto_total = cantidad * tarifas[dia]

print(f"El monto total a pagar es: ${monto_total:,}")