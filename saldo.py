saldo = 500000
opcion = 0

while opcion !=4:
    print("1 consultar saldo ")
    print("2 retirar dinero ")
    print("3 depositar dinero ")
    print("4 finalizar ")

    opcion = int(input("seleccione una opcion del (1-4): "))

    if opcion ==1:
        print(f"su saldo es: ${saldo}")
    elif opcion ==2:
        retiro =float(input("cuanto dinero deseas retirar? "))
        if retiro <=0:
            print("debe retirar en numeros positivos")
        elif retiro > saldo:
            print("vya pa que se lo culeen no tiene plata")
        else:
            saldo-=retiro
            print(f"eres la gaver. su nuevo saldo es: ${saldo}")
    elif opcion ==3:
        deposito = float(input("cuanto dinero deseas depositar? "))
        if deposito <=0:
            print("tiene que poner plata no quitar cabron")
        else:
            saldo+=deposito
            print(f"excelente ahora tienes: ${saldo} ")
    elif opcion ==4:
        print("gracias por tu tiempo")
    else:
        print("error vuelva a intentarlo")