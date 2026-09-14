sal = int(input( "cual es tu sueldo: "))

pension = sal * 0.125
salud = sal * 0.04
caja = sal * 0.04
aux=249000


horas_ex = int(input("cuantas horas extras trabajaste: "))

horas_extras = horas_ex * 10422

salario = sal-pension-salud-caja+aux+horas_extras

print("su salario total es: ",salario)