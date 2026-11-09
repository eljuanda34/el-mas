import tkinter as tk 

ventana = tk.Tk()
ventana.title("calculo de promedio")
ventana.geometry("620x620") 
ventana.grid_anchor("center")


def calcular_promedio():
    suma = (float(caja_texto1.get()) + float(caja_texto2.get()) + float(caja_texto3.get()))
    promedio = suma / 3
    if promedio >= 4.0:
        texto_promedio.config(text=f"El promedio es: {promedio:.1f} - Aprobado")
    else:
        texto_promedio.config(text=f"El promedio es: {promedio:.1f} - Reprobado")

texto = tk.Label(text="calcular promedio", font=("new roman",15), fg="black")
texto.grid(row=0, column=1, padx=2, pady=10)

texto = tk.Label(pady=15, text="ingrese la primera nota", font=("new roman",11), fg="black")
texto.grid(row=1, column=1, padx=3, pady=10)

caja_texto1 = tk.Entry(width=20, font=("new roman",16))
caja_texto1.grid(row=1, column=2, padx=7, pady=12)

texto = tk.Label(pady=15, text="ingrese la segunda nota", font=("new roman",11), fg="black")
texto.grid(row=3, column=1, padx=4, pady=10)

caja_texto2 = tk.Entry(width=20, font=("new roman",16))
caja_texto2.grid(row=3, column=2, padx=7, pady=12)

texto = tk.Label(pady=15, text="ingrese la tercera nota", font=("new roman",11), fg="black")
texto.grid(row=5, column=1, padx=5, pady=10)

caja_texto3 = tk.Entry(width=20, font=("new roman",16))
caja_texto3.grid(row=5, column=2, padx=7, pady=12)

boton = tk.Button(text="calcular promedio", font=("new roman",13), fg="white", bg="blue", command=calcular_promedio)
boton.grid(row=7, column=1, pady=10, padx=5)

texto_promedio = tk.Label(text="el promedio es:", font=("new roman",12), fg="black")
texto_promedio.grid(row=7, column=2, padx=3, pady=10)

ventana.mainloop()