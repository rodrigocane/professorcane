import tkinter as tk
from semaforo import *
import time

class Tktela2():
    def __init__(self, root=None):
        self.ciclo_longo = 8000
        self.ciclo_curto = 2000
        self.ciclo_atual_longo = False
        self.inicio = time.time()
        self.root_tk2 = tk.Toplevel(root)
        self.root = root
        self.root_tk2.title("Semáforo Lindo")

        # Cria dois semáforos lado a lado só pra mostrar
        self.s1 = Semaforo(self.root_tk2)
        self.s1.grid(row=0, column=0, padx=20, pady=20)

        self.s2 = Semaforo(self.root_tk2)
        self.s2.grid(row=0, column=1, padx=20, pady=20)

        # Teste: acender luz vermelha do primeiro
        self.s1.acender(SemaforoCor.VERDE)
        self.s2.acender(SemaforoCor.VERMELHO)
        self.root.after(self.ciclo_longo, self.proximo_ciclo)
    
    def proximo_ciclo(self):
        if self.ciclo_atual_longo:
            self.s1.avancar_cor()
            self.s2.avancar_cor()
            self.ciclo_atual_longo = False
            self.root.after(self.ciclo_longo, self.proximo_ciclo)
        else:
            if self.s1.cor == SemaforoCor.VERDE:
                self.s1.avancar_cor()
            else:
                self.s2.avancar_cor()
            self.ciclo_atual_longo = True
            self.root.after(self.ciclo_curto, self.proximo_ciclo)
        agora = time.time()
        # Fiz esse print só pra acompanhar pelo prompt se está sendo respeitado o tempo de cada ciclo
        # print(f"[{agora - self.inicio:05.2f}s] -> S1: {self.s1.cor.name}, S2: {self.s2.cor.name}")
        
    
