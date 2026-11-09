import tkinter as tk 

ventana = tk.Tk()
ventana.title("bienvenido")
ventana.geometry("720x720") 
ventana.grid_anchor("center")


texto = tk.Label(text="login", font=("new roman",15), fg="black")
texto.grid(row=0, column=4, padx=3, pady=10)

texto = tk.Label(pady=15, text="ingrese el usuario", font=("new roman",11), fg="black")
texto.grid(row=1, column=1, padx=3, pady=10)

caja_texto1=tk.Entry(width= 25, font=("new roman",16))
caja_texto1.grid(row=1, column=4, padx=7, pady=12)

texto = tk.Label(pady=15, text="password", font=("new roman",11), fg="black")
texto.grid(row=4, column=1, padx=7, pady=12)

caja_texto2=tk.Entry(width= 25, font=("new roman",16), borderwidth=5)
caja_texto2.grid(row=4, column=4, padx=7, pady=12)

boton = tk.Butto(text= "ingresar",font=("new roman",13), fg="white", bg="blue")
boton.grid(row=5, column=4, pady=5, padx=5)

ventana.mainloop()