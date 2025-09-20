from enum import Enum
import tkinter as tk

class SemaforoCor(Enum):
    '''Enum que representa as cores de um semáforo, trazendo os valores (ativo,inativo)'''
    VERMELHO = ("#FF0000", "#4D0000")    
    AMARELO = ("#FFFF00", "#4D4D00")
    VERDE = ("#00FF00", "#004D00")

class Semaforo(tk.Frame):
    def __init__(self,  master=None, cor: SemaforoCor=SemaforoCor.VERMELHO, **kwargs):
        super().__init__(master, **kwargs)
        self._cor = cor
        self.config(bg="black", padx=10, pady=10, bd=3, relief="ridge")
        self.canvas = tk.Canvas(self, width=60, height=180, bg="black", highlightthickness=0)
        self.canvas.pack()
        self.luzes = {}

        yzero = 10
        yum = 50
        for cor in SemaforoCor:
            self.luzes[cor] = self.canvas.create_oval(10, yzero, 50, yum, fill=cor.value[1])
            yzero += 55
            yum += 55

    def acender(self, nova_cor:SemaforoCor):
        """Muda a cor de uma luz específica e apaga as outras"""
        self._cor = nova_cor
        for c, item in self.luzes.items():
            (pos, outline, width) = (0, "white", 3) if nova_cor == c else (1,"", 0)
            self.canvas.itemconfig(item, fill=c.value[pos], outline=outline, width=width)            

    @property
    def cor(self) -> SemaforoCor:
        return self._cor
    
    def proxima_cor(self):
        """Calcula qual a próxima cor na sequencia"""
        match(self._cor):
            case SemaforoCor.VERDE:
                return SemaforoCor.AMARELO
            case SemaforoCor.VERMELHO:
                return SemaforoCor.VERDE
            case _:
                return SemaforoCor.VERMELHO
            
    def avancar_cor(self):
        """Muda a cor para a próxima na sequencia"""
        self.acender(self.proxima_cor())

