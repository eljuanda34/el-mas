
estudiantes = []

num_de_estudiantes = int(input("cuantos estudiantes desea registrar: "))

for i in range(num_de_estudiantes):

    nombre = input("ingrese el nombre del estudiantes: ")
    estudiantes.append(nombre)

print("\nestudiantes registrados:")
print(estudiantes)
print("total de estudiantes:", len(estudiantes))


for x in estudiantes:
    print(x)
