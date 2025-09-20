import tkinter as tk


class BotaoAfundado(tk.Button):
    def __init__(self, master=None, **kwargs):
        # Se existir um command passado, guarda para poder chamar depois
        self._command = kwargs.pop("command", None)
        super().__init__(master, command=self._on_click, **kwargs)
        print('BotaoAfundado')
        self.config(command=self._on_click)

    def _on_click(self):
        print('click mouse')
        self.config(state="disabled")
        if self._command:
            self._command()

valor = 0 

def rodar3(root=None):
    tela3 = tk.Toplevel(root)
    sv_valor = tk.StringVar()
    sv_valor.set(valor)
    bt_menos = BotaoAfundado(tela3, text="-", state="disabled")
    bt_menos.config(command=lambda:menos(bt_mais, sv_valor, bt_menos))
    lb_valor = tk.Label(tela3, textvariable=sv_valor)
    bt_mais =  BotaoAfundado(tela3, text="+")
    bt_mais.config(command=lambda:mais(bt_mais, sv_valor, bt_menos))

    bt_menos.grid(row=0, column=0, ipadx=10, ipady=10, padx=10)
    lb_valor.grid(row=0, column=1, ipadx=10, ipady=10)
    bt_mais.grid(row=0, column=2, ipadx=10, ipady=10, padx=10)

def mais(bt_mais:tk.Button, sv_valor:tk.StringVar, bt_menos:tk.Button):
    global valor
    valor +=1
    bt_menos.config(state="active")
    sv_valor.set(valor)    
    if valor >= 10:
        bt_mais.config(state="disabled")

def menos(bt_mais, sv_valor, bt_menos):
    global valor
    valor -=1
    bt_mais.config(state="active")
    sv_valor.set(valor)
    if valor <= 0:
        bt_menos.config(state="disabled")

