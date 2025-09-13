import tkinter as tk

def selecionar():
    cor = escolha.get()
    lb_cor.config(fg=cor, text=cor)

tela5 = tk.Tk()
tela5.title("Seletor")

fonte = ("Arial",15,"bold")
opcoes = ["gold", "indianred", "cyan", "grey20", "coral", "darkgreen", "tomato", "palegreen"]
escolha = tk.StringVar(value=opcoes[0])
ls = tk.OptionMenu(tela5, escolha, *opcoes)
ls.config(font=("Arial",15))
ls['menu'].config(font=("Arial",15))

bt_ok = tk.Button(tela5, text="Selecionar", font=fonte, command=selecionar)
lb_cor = tk.Label(tela5, font=fonte)


ls.pack(padx=10,pady=10, fill="both")
bt_ok.pack(padx=10,pady=10)
lb_cor.pack(padx=10,pady=10, fill="both")

if __name__ == "__main__":
    tela5.mainloop()

