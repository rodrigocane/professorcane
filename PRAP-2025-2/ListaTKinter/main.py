import tkinter as tk
from tk2 import *

def rodar(tela):
    match(tela):
        case 1:
            pass #rodar1()
        case 2:
            rodar2(maintk)
        case 3:
            pass #rodar3()
        case 4:
            pass #rodar4()
        case _:
            pass #rodar5()

maintk = tk.Tk()
for i in range(1,5):
   tk.Button(maintk, text=f"Tela {i}", command=lambda: rodar(i)).pack()

maintk.mainloop()
