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

match nombre:
    case "chuky":
        mensaje = "haz selecionado el chuky !preparate para no dormir¡ "
        men = "no tienes ningun descuento 😥"
    case "el conjuro":
        mensaje = "haz selecionado el conjuro !ya no la cuentes por que no vas¡"
        men = "no tienes ningun descuento 😥"
    case "iro man":
        mensaje = "haz selecionado iro man !preparate para la accion¡ "
        men = "no tienes ningun descuento 😥"
    case "dragon ball z":
        mensaje = "haz selecionado draggn  ball z !a elevar tu ki¡"
        men = "no tienes ningun descuento 😥" 
    case "el chapulin":
        monto_total *= 0.90
        mensaje = "haz selecionado el chapulin !no contaban con mi astucia¡"
        men = "excelente tienes un descuento del 10%"
    case _:
        pass

print("-"*30, "RESUMEN", "-"*30)
print(mensaje)
print(men)
print(f"El monto total a pagar es: ${monto_total:,}")
