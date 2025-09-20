import tkinter as tk
from tk1 import *
from tk2 import *
from tk3 import *
from tk4 import *
from tk5 import *

def rodar(tela):
    match(tela):
        case 1:
            rodar1(maintk)
        case 2:
            Tktela2(maintk)
        case 3:            
            rodar3(maintk)
        case 4:
            rodar4(maintk)
        case _:
            rodar5(maintk)

maintk = tk.Tk()
for i in range(1,6):
    tk.Button(maintk, text=f"Tela {i}", command=lambda x=i: rodar(x)).pack(pady=5)

maintk.mainloop()
