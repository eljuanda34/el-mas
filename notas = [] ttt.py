notas = []
print("-"*30, "DATOS PRINCIPALES", "-"*30)
nombre = input("Ingrese el nombre del estudiante: ")
asignatura = input("Ingrese la asignatura: ")
cantidad = int(input("Ingrese la cantidad de notas que desea ingresar: "))
promedio = 0
for i in range(cantidad):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)
promedio = sum(notas) / len(notas)
match promedio:
    case x if x >= 4.5:
        mesaje = ("pro 😎")
    case x if x >= 4:
        mesaje = ("superior😯")
    case _:
        mesaje = ("conoces a yaper 💀")
print("-"*30, "RESULTADOS", "-"*30)
print("El estudiante es: ",nombre)
print("La asignatura es: ",asignatura)
print("El promedio es: ",f"{promedio:.2f}")
print("El estudiante es: ",mesaje)
print ("Las notas ingresadas son: ",notas)