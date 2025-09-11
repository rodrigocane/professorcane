import tkinter as tk

turno = 0
def turno_calc():
    global turno
    match(turno):
        case 0:
            bt_yel.config(text="   ")
            bt_red.config(text="***")
            bt_gre2.config(text="***")
            bt_red2.config(text="   ")
            turno = 1
            tela.after(8000, turno_calc)
        case 1:
            bt_yel2.config(text="***")
            bt_gre2.config(text="  ")
            turno = 2
            tela.after(2000, turno_calc)      
        case 2:
            bt_gre.config(text="***")
            bt_red.config(text="   ")
            bt_yel2.config(text="   ")
            bt_red2.config(text="***")
            turno = 3
            tela.after(8000, turno_calc)         
        case _:
            bt_gre.config(text="   ")
            bt_red.config(text="   ")
            bt_yel.config(text="***")
            turno = 0
            tela.after(2000, turno_calc)

tela = tk.Tk()
bt_gre = tk.Button(tela, bg='green', text='   ')
bt_yel = tk.Button(tela, bg='gold', text='   ')
bt_red = tk.Button(tela, bg='red', text='   ')

bt_gre.grid(row=2,column=0, padx=10)
bt_yel.grid(row=1,column=0)
bt_red.grid(row=0,column=0)

bt_gre2 = tk.Button(tela, bg='green', text='   ')
bt_yel2 = tk.Button(tela, bg='gold', text='   ')
bt_red2 = tk.Button(tela, bg='red', text='   ')

bt_gre2.grid(row=2,column=1, padx=10)
bt_yel2.grid(row=1,column=1)
bt_red2.grid(row=0,column=1)

turno_calc()
tela.mainloop()
