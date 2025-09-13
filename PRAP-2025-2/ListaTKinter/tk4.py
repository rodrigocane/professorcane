import tkinter as tk

def formatar_numero(num):
    if isinstance(num, float) and num.is_integer():
        return str(int(num))  # Mostra sem vírgula
    return f"{num:.4f}"

def calcular(operacao):
    global num_result
    try:
        match(operacao):
            case "+":
                result = float(num_esq.get()) + float(num_dir.get())
            case "-":
                result = float(num_esq.get()) - float(num_dir.get())
            case "/":
                result = float(num_esq.get()) / float(num_dir.get())
            case "*":
                result = float(num_esq.get()) * float(num_dir.get())
            
        num_result.set(formatar_numero(result))
    except ValueError:
        num_result.set("Deu ruim")

tela4 = tk.Tk()
tela4.title("Calc fulera")

num_esq = tk.StringVar()
num_dir = tk.StringVar()
num_result = tk.StringVar()

tamanho = 2
txt_esq = tk.Entry(tela4, textvariable=num_esq, width=7, justify="right", font=("Arial", 15))
txt_dir = tk.Entry(tela4, textvariable=num_dir, width=7, justify="right", font=("Arial", 15))

btn_mais = tk.Button(tela4, text="➕", font=("Arial", 15), command=lambda: calcular("+"))
btn_meno = tk.Button(tela4, text="➖", font=("Arial", 15), command=lambda: calcular("-"))
btn_divi = tk.Button(tela4, text="➗", font=("Arial", 15), command=lambda: calcular("/"))
btn_mult = tk.Button(tela4, text="✖️", font=("Arial", 15), command=lambda: calcular("*"))

lb_result = tk.Label(tela4, textvariable=num_result, width=20, font=("Arial", 15, "bold"))

txt_esq.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
txt_dir.grid(row=0, column=2, columnspan=2, padx=5, pady=5)
btn_mais.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
btn_meno.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
btn_divi.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
btn_mult.grid(row=1, column=3, padx=5, pady=5, sticky="ew")
lb_result.grid(row=2, column=0, columnspan=4, pady=10)

if __name__ == "__main__":
    tela4.mainloop()
