import tkinter as tk

valor = 0 

def mais():
    global valor    
    valor +=1
    bt_menos.config(state="active")
    sv_valor.set(valor)    
    if valor >= 10:
        bt_mais.config(state="disabled")

def menos():
    global valor   
    valor -=1
    bt_mais.config(state="active")
    sv_valor.set(valor)
    if valor <= 0:
        bt_menos.config(state="disabled")

tela3 = tk.Tk()
sv_valor = tk.StringVar()
sv_valor.set(valor)
bt_menos = tk.Button(tela3, text="-", state="disabled", command=menos)
lb_valor = tk.Label(tela3, textvariable=sv_valor)
bt_mais =  tk.Button(tela3, text="+", command=mais)

bt_menos.grid(row=0, column=0, ipadx=10, ipady=10, padx=10)
lb_valor.grid(row=0, column=1, ipadx=10, ipady=10)
bt_mais.grid(row=0, column=2, ipadx=10, ipady=10, padx=10)

if __name__ == "__main__":
    tela3.mainloop()