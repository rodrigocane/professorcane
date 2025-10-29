# 🌱 Programação Python nível 0 - Introdução

-   **Python basicão**
    -   Variáveis -> Python é fortemente tipado & dinamicamente tipado
    -   ```python
        x = 10          # durante a execução o Python descobriu que a variável x era um INT
        x = "10"        # mais pra frente a variável fez uma transição e virou STR.
                        # E tá tudo bem. E é sobre isso. A tipagem dinâmica tá aí pra isso!
        y = 0.0         # y é uma variável float        
        print(x + y)    # ❌ Erro! Não dá pra somar string com float (porque a tipagem é forte!).
        print(int(x)+y) # ✅ Sucesso! Convertendo "10" para o inteiro 10 o Python consegue fazer a soma
                        #    (pois ele tb não é tão malvado: converter de int pra float ele consegue)
        ```
    -   `print` -> Podemos combinar texto fixo e variáveis
    -   ```python
        print(x) #Imprime o valor contido na variável x
        print("Bom dia querido ", nome, ". Tudo bão?") # Concatenação de texto fixo e variável nome.
        print() #Imprime nada (só pra quebrar linha memo)
        print("\n\n\n") #"Imprime" 3 linhas vazias, pra dar uma espacin
        print(f"Hoje é {datetime.date.today()}.") # Aqui usamos a "fstring", que alterna entre fixo e variável
        ```
    -  `input` -> Pedindo informações ao usuário
    -   ```python
        idade = ("Quantos anos vc tem?") # Imprime a frase e joga o que for digitado pra variável idade
        if idade == 18: # Esse if NUNCA será verdadeiro pois se o usuário digitar 18, a variável terá "18"
        alunos_str = ("Digite o nome dos alunos (separados por espaço)")
        #Captura até digitar enter. Ex: se o usuário digitar "Ana Bea    Cris" tudo isso ficará na alunos_str
        alunos = alunos_str.split() #Agora quebramos a string em uma lista de strings. Cada espaço é uma "quebra"
        #Obs: o terceiro elemento da lista será "Cris". Os espaços a mais ali vão sumir no split        
        ```  
    -   Estruturas de dados mais comuns:
    -   ```python
        lista = [1, 2] # Sequência mutável e ordenada de valores, começando do índice 0
        lista.append("oi") # Veja que é heterogênea. Dá pra enfiar qualquer coisa na lista
        x = lista[2] # Agora x vale "oi", pois a posição [2] é o terceiro elemento.
        tupla = ("A", "B", "C") # Imutável. Nasceu de um jeito, morre do mesmo jeito!
        x = tupla[2] # Agora x vale "C"
        dicionario = {"nome": "Maria", "idade": 25} # Pares chave-valor. Cada chave te retorna um valor.
        dicionario["altura"] = 1.55 # Adicionando uma nova chave. O dicionário agora tem 3 chave-valor.
        dicionario["nome"] = "João" # Agora sobrescreveu o nome.
        print(dicionario["nome"]) # Vai imprimir "João"
        ```
    -   Funções de controle (if/elif/else/ternário)
    -   ```python
        if nota >= 7: #7 ou mais
          print("Passou!")
        elif 4 <= nota < 7: #Se nota está entre 4 e 6.99
          print("Exame mas ainda dá pra passar!")
        else: #Caso contrário
          print("💀 n00b")

        # Ternário - if/else em uma linha. Nível Sênior de qualidade!
        dia_semana = datetime.now().weekday() (Segunda = 0 Domingo = 6)        
        print("Fds" if dia_semana in (5, 6) else "Dia de semana")
        ```
    -   funções de repetição (for, foreach)
    -   ```python
        for i in range(3): #Vai de 0 a 2
          print("Loop ", i, end='. ') #Loop  0. Loop  1. Loop  2.
        for i in range(3,6): #Começa no 3 e vai até o 5. 
          print("Loop ", i, end='. ') #Loop  3. Loop  4. Loop  5.
        apelidos = ["Ana", "Bea", "Cris", 171]
        for apelido in apelidos: #Conhecido como foreach, preenche cada elemento da estrutura
            print("Olá, ", apelido)
        ```
    -   Import -> Recomenda-se colocar todos os imports nas primeiras linhas do arquivo
    -   ```python
        import math
        print(math.sqrt(16))  # usa o módulo math

        # dá pra importar lá no meio do rolê. Só fica feio que dói!
        from datetime import datetime #do módulo datetime importa a classe datetime
        print(datetime.now()) # agora dá pra usar a classe datetime de buenas

        import tkinter as tk #importou TKinter e "apelidou" de tk
        maintk = tk.Tk() #instanciando a classe Tk do módulo "tk"

        from flask import * #Import grosseirão. Importa tudo!
        session["agora"] = datetime.now() #Usamos a classe session do Flask
        ```
        - Se você for rodar um código e ver uma mensagem assim:
        -  `ModuleNotFoundError: No module named 'pandas'`
        -  É só intalar o módulo faltante: `pip install pandas`
 ------------------------------------------------------------------------
 # 📝 Exercícios
 Agora vem a parte prática. Tente fazer os programas abaixo sem delegar todo o trabalho pra Inteligência Artificial Generativa. Caso necessário, procure no Google o que precisa. Se vc for mtooo n00b mesmo, blz, pode pedir pra IA um TRECHO de código (ex: "Como gero um número aleatório entre 0 e 5 com Python?"). Mas use com moderação. Essa é sua última chance de aprender algo!
 Para cada "programa" você pode criar um arquivo separado (ex: exe1.py, exe2.py etc) ou tacar tudo no mesmo arquivo (ex: exercicios.py) e ir separando os "programas" em funções ou classes. Vc decide.
 
 1. Monte um programa que pergunte o nome e depois a idade do usuário. Se o usuário for maior de 18 anos, imprima "Já sabe dirigir?". Caso contrário imprima "Vc é uma criança ainda. Aproveite!"
 2. Monte um programa que imprima uma série de frutas que você gosta e o preço por quilo aproximado de cada uma delas (não precisa consultar o valor real no site do Giassi. Coloca qualquer coisa ae)
 3. Monte um programa que pergunte ao usuário "Par ou ímpar". Depois peça um número de 0 a 5. Sorteie um número de 0 a 5 (usando o módulo `random`) e então diga se o usuário ganhou ou perdeu no par ou ímpar. Mas fique atento: tem usuário desatento que vai digitar "impar" quando vc pedir "Par ou Ímpar". Tem usuário engraçadinho que vai digitar "Pocahontas". No número mema coisa: vai ter gente digitando 11, vai ter gente digitando "dois". Prepare seu código pra esses engraçadinhos e/ou desatentos!
 4. Monte um programa que pergunte ao usuário "Quantas notas?". Então faça um loop para armazenar cada nota. Por fim, calcule a média das notas e imprima:      
    - "C é o bichão memo hein doido?" para alunos nota 10.
    
    - "Parabéns" pra 9.9 até 8.
    
    - "Pelo menos passou" pra 7.9 até 7.
    
    - "Na traaaaaaave" pro aluno 6.9
    
    - "n00b" pra quem tiver média de 6.8 a 4.
    
    - "💀 já era mano!" pros demais
