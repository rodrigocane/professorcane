import tkinter as tk
from datetime import datetime

def rodar1(root=None):
    tk1_tk = tk.Toplevel(root)
    tk1_tk.title("Exercicio 1")
    fr_superior = tk.Frame(tk1_tk)
    lb_nome = tk.Label(fr_superior, text="Digite seu nome: ")
    txt_nome = tk.Entry(fr_superior)
    bt_go = tk.Button(fr_superior, text="Ok", command=lambda: cumprimento(txt_nome,lb_nome))

    lb_nome.grid(row=0, column=0, ipadx=5, ipady=5)
    txt_nome.grid(row=0, column=1, ipadx=5, ipady=5)
    bt_go.grid(row=0, column=2, ipadx=5, padx=5, ipady=5)
    fr_superior.pack(pady=5, padx=10)

    fr_inferior = tk.Frame(tk1_tk)
    lb_saudacao = tk.Label(fr_inferior, font=("Arial", 20, "bold"), fg="#AAAAFF")
    lb_saudacao.pack(fill="both")
    fr_inferior.pack(padx=10, pady=5)

def cumprimento(txt_nome, lb_saudacao):
    nome = txt_nome.get().strip()
    hora = datetime.now().hour
    saudacao = ""
    if 1 <= hora <= 12:
        saudacao = "Bom dia"
    elif 13 <= hora <= 18:
        saudacao = "Boa tarde"
    else:
        saudacao = "Boa noite"

    lb_saudacao.config(text=f"{saudacao}, {nome}.")