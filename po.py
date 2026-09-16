p = float(input("ingrese su peso en kg : "))
a = float(input("ingrese su altura en m : "))

imc = p/(a*a)

if imc <= 18.5:
    m ="le falta yuca"

elif imc >= 18.5 and imc <= 24.9:
    m ="usted parte bocato"

elif imc >= 25 and imc <= 29.9:
 m ="usted se paso de leche"

else:
   m ="se denomina planeta "

print("su imc es : ", imc , m ) 