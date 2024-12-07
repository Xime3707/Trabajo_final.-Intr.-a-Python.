from tkinter import messagebox, Label, Tk, StringVar, CENTER, ttk, Entry, Button

#Ventana
ventana=Tk()
ventana.configure(background="blue")
ventana.title("Conversor de Celsius a Kelvin")
ventana.geometry("350x250")
ventana.resizable(False, False)

def conversor():
    celsius=temperatura.get().strip()
    try:
        celsius=float(celsius)
        kelvin=celsius+273.15
        if kelvin<0:
            messagebox.showerror("Error", "La temperatura en Kelvin no puede ser negativa")
        else:
            resultado.set(f"{int(kelvin)} k")
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido/usar punto en lugar de coma")

resultado=StringVar(ventana)
temperatura=StringVar(ventana)

Label(ventana, text="Conversor Celsius a Kelvin", font=("Arial", 14)).grid(row=0, column=0, columnspan=10, pady=10, padx=55)
Label(ventana, text="Ingrese temperatura en Celsius: ").grid(row=1, column=0, padx=80, pady=10)
temperatura=Entry(ventana, justify="center")
temperatura.grid(row= 2, columnspan=1, padx=1, pady=1)

Button(ventana, text="Convertir", command=conversor).grid(row=3, column=0, padx=80, pady=10)

Label(ventana, text="Resultado en Kelvin:").grid(row=4, column=0, padx=80, pady=10)
Label(ventana, textvariable=resultado).grid(row=5, column=0, padx=80, pady=10)

ventana.mainloop()