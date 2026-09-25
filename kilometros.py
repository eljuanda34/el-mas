opcion = 0
moto = 1500
automovil = 2500
camioneta = 3500


while opcion !=4:
    print("tipo de vehiculo")
    print("1. moto")
    print("2. automovil")
    print("3. camioneta")
    print("4. finalizar")

    opcion = (int(input("seleccione una opcion del (1-4): ")))
    if opcion == 1:
        distancia = float(input("¿cuantos kilometros deseas recorrer?: "))
        resultado = distancia*moto
        
        if distancia <= 0:
            print("debe realizar los kilometros mayores a cero")
        elif distancia >50:
            descuento = resultado *0.10
            total = resultado-descuento
            print("debe pagar:",descuento)

    elif opcion == 2:
        distancia = float(input("¿cuantos kilometros deseas recorrer?: "))
        resultado = distancia*automovil
        if distancia < 0:
            print("debe realizar los kilometros mayores a cero")
        elif distancia >50:
            descuento = resultado*0.10
            total = resultado-descuento
            print("debe pagar:",descuento)

    elif opcion == 3:
        distancia = float(input("¿cuantos kilometros deseas recorrer?: "))
        resultado = distancia*camioneta
        if distancia < 0:
            print("debe realizar los kilometros mayores a cero")
        elif distancia >50:
            descuento = resultado*0.10
            total = resultado-descuento
            print("debe pagar:",descuento)

    elif opcion ==4:
        print("gracias por tu tiempo")
    else:
        print("error vuelva a intentarlo")
        