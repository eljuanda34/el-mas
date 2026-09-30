list1 = []
list2 = []
resul = []
print("ingrese los numeros en las siguientes listas")

for x in range(5):
    num1 = int(input("digite los numeros: "))
    list1.append(num1)

for x in range(5):
    num2 = int(input("digite los numeros: "))
    list2.append(num2)
    resul.append(list1[x]+list2[x])
print(list1)
print(list2)
print("el resultado es", resul)