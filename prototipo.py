
estudiantes = []
nombre_y_promedios = []

num_de_estudiantes = int(input("cuantos estudiantes desea registrar: "))

for i in range(num_de_estudiantes):
    print(f"\nestudiante {i+1}:")

    nombre = input("ingrese el nombre del estudiante: ")
    notas_estudiantes = []
    for j in range(1,4):
        nota = float(input(f"ingrese la nota {j} del estudiante: "))
        notas_estudiantes.append(nota)
    estudiantes.append({"nombre": nombre, "notas": notas_estudiantes})

print("\nestudiantes registrados:")
print(estudiantes)
print("total de estudiantes:", len(estudiantes))

for x in estudiantes:
    print("-"*20)
    prom = sum(x["notas"]) / len(x["notas"])
    x["promedio"] = prom
    x["estado"] = "aprobado" if prom >= 3 else "reprobado"

    nombre_y_promedios.append((x["nombre"], prom))
    for clave, vALOR in x.items():
        print(f"{clave}: {vALOR}")
print("-"*20)
print("\nlista de nombres y promedios guardados:", nombre_y_promedios)