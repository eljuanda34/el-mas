def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero."
    return a / b

def menu_operaciones():
    while True:
        print("\n--- MENÚ DE OPERACIONES ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "5":
            print("¡Hasta luego! Gracias por usar la calculadora.")
            break
            
        elif opcion in ["1", "2", "3", "4"]:
    
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if opcion == "1":
                resultado = sumar(num1, num2)
                print(f"Resultado de la suma: {resultado}")
            elif opcion == "2":
                resultado = restar(num1, num2)
                print(f"Resultado de la resta: {resultado}")
            elif opcion == "3":
                resultado = multiplicar(num1, num2)
                print(f"Resultado de la multiplicación: {resultado}")
            elif opcion == "4":
                resultado = dividir(num1, num2)
                print(f"Resultado de la división: {resultado}")
                
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
menu_operaciones()