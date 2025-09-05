import tkinter as tk

tela = tk.Tk()
tela.title("Tela Alo mundo")
tela.resizable(width=True, height=True) #assegurando que dá pra redimensionar
tela.geometry('400x200')

frame_topo = tk.Frame(tela)
frame_topo.pack(side='top')
lbl_tela = tk.Label(frame_topo, text="CADASTRO",font=("Arial", 30, "bold"))
lbl_tela.pack()

frame_nome = tk.Frame(tela)
frame_nome.pack()
lbl_nome = tk.Label(frame_nome, text="Nome:",font=("Arial", 20))
lbl_nome.grid(row=0, column=0)
in_nome = tk.Entry(frame_nome, font=("Arial", 20))
in_nome.grid(row=0, column=1)

lbl_cpf = tk.Label(tela, text="CPF:", font=("Arial", 20, "bold"))
in_cpf = tk.Entry(tela)
btn_cad = tk.Button(tela, text="OK", font=("Arial", 20, "bold"))

tela.mainloop()
