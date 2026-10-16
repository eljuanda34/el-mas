class carro:
    def __init__(self, marca, modelo, color, cilindraje, año,):
        self.marca = marca
        self.modelo = modelo 
        self.color = color
        self.cilindraje = cilindraje
        self.año = año

    def acelerar(self):
        print(f"el carro {self.marca} {self.modelo} acelero!!")
    def frenar(self):
        print(f"el carro {self.marca} {self.modelo} freno!!")
    def girar_derecha(self):
        print(f"el carro {self.marca} {self.modelo} giro a la derecha!!")
    def girar_izquierda(self):
        print(f"el carro {self.marca} {self.modelo} giro a la izquierda!!")

marca = input("ingrese la marca: ")
modelo = input("ingrese el modelo: ")
color = input("ingrese el color: ")
cilindraje = input("ingrese el cilindraje: ")
año = input("ingrese el año: ")

mi_carro = carro(marca,modelo,color,cilindraje,año)

print(""" opciones 1. marca: 2. modelo: 3. color: 4. cilindraje: w. acelerar:  d. girar hacia la derecha:  a. girar hacia la izquierda: s. frenar: 5. año:  6. salir: """)

while True:
     print("-"*13, "BIENVENIDO", "-"*13)
     opcion = input("selecione unas de las opciones: ")
     match opcion:
         case "1" | "2" | "3" | "4" | "5" : 
            textos = ["su carro tiene la marca de", "tiene el modelo de", "tiene el color de", "tiene el el cilindraje de", "acelerar", "girar a la derecha", "girar a la izquierda"," " ,"tiene el año de"]
            valores =[mi_carro.marca, mi_carro.modelo ,mi_carro.color ,mi_carro.cilindraje ,mi_carro.año]
            idx = int(opcion) - 1
            print(textos[idx], valores[idx])

         case  "w" | "d" | "a" | "s" :
            acciones = { 
                "w": mi_carro.acelerar,
                "d": mi_carro.girar_derecha,
                "a": mi_carro.girar_izquierda,
                "s": mi_carro.frenar
            } 
            acciones[opcion]()

         case "6":
             print("-"*13, "saliendo es saliendo", "-"*13)
             break
         case _:
             print("opcion no encontrada")