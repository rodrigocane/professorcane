import tkinter as tk
from semaforo import *
import time

ciclo_longo = 8000
ciclo_curto = 2000

ciclo_atual_longo = False
def proximo_ciclo():
    global ciclo_atual_longo
    if ciclo_atual_longo:
        s1.avancar_cor()
        s2.avancar_cor()
        ciclo_atual_longo = False
        root_tk2.after(ciclo_longo, proximo_ciclo)
    else:
        if s1.cor == SemaforoCor.VERDE:
            s1.avancar_cor()
        else:
            s2.avancar_cor()
        ciclo_atual_longo = True
        root_tk2.after(ciclo_curto, proximo_ciclo)
    agora = time.time()
    print(f"[{agora - inicio:05.2f}s] -> S1: {s1.cor.name}, S2: {s2.cor.name}")
    
root_tk2 = tk.Tk()
root_tk2.title("Semáforo Lindo")

# Cria dois semáforos lado a lado só pra mostrar
s1 = Semaforo(root_tk2)
s1.grid(row=0, column=0, padx=20, pady=20)

s2 = Semaforo(root_tk2)
s2.grid(row=0, column=1, padx=20, pady=20)

# Teste: acender luz vermelha do primeiro
s1.acender(SemaforoCor.VERDE)
s2.acender(SemaforoCor.VERMELHO)

if __name__ == "__main__":
    inicio = time.time()
    root_tk2.after(ciclo_longo, proximo_ciclo)
    root_tk2.mainloop()
