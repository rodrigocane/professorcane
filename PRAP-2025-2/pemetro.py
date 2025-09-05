import tkinter as tk

def calcular():
    try:
        value = float(pes.get())
        valor_metros.set(round((int(0.3048 * value * 10000.0 + 0.5)/10000.0),2))
    except ValueError:
        pass

tela = tk.Tk()
tela.title("Conversor Pé pra Metro")
tela.geometry('400x200')

frame_principal = tk.Frame(tela, pady=10)
frame_principal.pack()

pes = tk.Entry(frame_principal, width=7)
pes.grid(row=0, column=1)
pes_label = tk.Label(frame_principal, text=" pés")
pes_label.grid(row=0, column=2)

eq_label = tk.Label(frame_principal, text="equivale a ")
eq_label.grid(row=1, column=0)

valor_metros = tk.StringVar()
label_valor = tk.Label(frame_principal, textvariable=valor_metros)
label_valor.grid(row=1,column=1)

label_metros = tk.Label(frame_principal, text=" metros")
label_metros.grid(row=1, column=2)

button_calc = tk.Button(frame_principal, text="Calcular", command=calcular)
button_calc.grid(row=2, column=2)


tela.mainloop()
