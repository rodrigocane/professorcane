# 🌿 Programação Python nível 1 - Cada um no seu ◻
Usamos **funções**, **classes** e **módulos** para organizar e reutilizar código, evitando repetição e facilitando manutenção.
A **Programação Orientada a Objetos (POO)** vai além: permite modelar o mundo real em código, criando objetos com dados e comportamentos próprios.
Assim, o código fica mais legível, escalável e fácil de expandir sem bagunçar o que já funciona. (*GPT, Chat. 2025*)    


-   **Funções, classes, módulos**
	-   **Funções** -> Funções encapsulam trechos de código reutilizáveis. Podem receber parâmetros e podem retornar valores
	-   ```python
		def bom_dia(): #função sem parâmetros e sem retorno
			print("Bom dia")

		def printa_quadrado(a): #função que recebe um parâmetro "a"...
			print(a*a)          #... e printa "a" ao quadrado (ou seja, sem retorno)

		def quadrado(a): #função que recebe um parâmetro "a"...
			return a*a   #... e retorna "a" ao quadrado

		def bom_dia_nome(nome): #função que tem parâmetro mas não retorno
			if nome is None: #se o nome é "nulo" essa função não faz nada
				return #Aqui o return está sendo usado para interromper a função
			print(f"Bom dia {nome}")        
		```
	-   **Parâmetros e retornos**: nível 2 -> Tipagem e opcional
	-   ```python
		def print_soma(a:int, b:int): #Agora deixamos claro que o esperado é que "a" seja um int
			print(a+b)
			
		print_soma(5, 7)     # imprime 12
		print_soma("5", "7") # imprime "57", ou seja, o ":int" é uma DICA mas se vc desrespeitar, o Python tenta seguir a vida
		print_soma("5", 7)   # ❌ Erro! TypeError: can only concatenate str (not "int") to str

		def saudacao(nome: str, saudacao: str = "Olá"): #saudacao é um parâmetro opcional
			print(f"{saudacao}, {nome}!")
			
		saudacao("Rodrigo")          # Olá, Rodrigo!
		saudacao("Caio", "Salve")    # Salve, Caio!

		def quadrado(num: int) -> int: #Parâmetro e Retorno tipado
			return num * num

		# Parâmetros tipados, parâmetros opcionais, retorno tipado
		def calc_media(notas: list[float], arredondar: bool = False, decimais: int = 2) -> float:
			media = sum(notas) / len(notas)
			return round(media, decimais) if arredondar else media

		notas = [8.5, 9.2, 7.9]
		print(calc_media(notas))        # 8.533333333333333 => como se chamasse com (notas,False, 2)
		print(calc_media(notas, True))  # 8.53 => como se chamasse com (notas,True, 2)
		print(calc_media(notas, True,4))# 8.5333      
		```
	-   **Parâmetros e retornos**: nível 3 -> Retornando mais de um valor
	-   ```python
		#Pra dizer que o retorno é tupla de ints fazemos assim: tuple[int, int]
		def divisao_inteira(dividendo: int, divisor: int) -> tuple[int, int]:
			"""Retorna o quociente e o resto da divisão inteira."""
			quociente = dividendo // divisor #divisão inteira é com //
			resto = dividendo % divisor #resto da divisão
			return quociente, resto #Viu isso? dá pra retornar dois valores de uma vez!

		(d1, d2) = (10, 3) #E essa, tu sabia? Dá pra setar várias variáveis em uma linha
		(res_quociente, res_resto) = divisao_inteira(d1,d2) #Inclusive se os valores vierem de uma função
		print(f"{d1} / {d2} = {res_quociente} (com resto de {res_resto})") 
		# Vai printar 10 / 3 = 3 (com resto de 1)     
		```
	-   **Escopo de variáveis** -> Sombreamento de variáveis. Se vc declara uma variável que já foi declarada, o Python ignora a variável "de fora"
	-   ```python          
		def printar_contador():
			print(contador) #Acessa a variável contador que alguém já inventou em algum momento
			
		def inventar_contador():
			contador = 9
			print(contador) #Usa essa variável inventada aqui, sem ligar pro mundo exterior

        #printar_contador() # ❌ Erro! Aqui daria treta pq a função vai tentar usar uma variável que ainda não foi setada!
		contador = 6
		printar_contador() #6 (vai printar o valor de "contador" setado aqui em cima)
		inventar_contador()#9 (vai printar o valor de "contador" inventado na inventar_contador)
        printar_contador() #6 (printa 6 de novo. A função invertar_contador não alterou o valor de "contador")
		```
     - 🌍 **Escopo de variáveis** -> Variáveis criadas dentro de funções só existem ali dentro. Use **global** para modificar uma variável de fora da função (com cuidado!).
     -  ```python          
		def printar_contador():
			print(contador) #Aqui não precisa do "global" pq está só LENDO a variável "contador"
			
		def inventar_contador():
            global contador # GLOBAL -> Estamos avisando o Python que aqui dentro vamos ALTERAR  o valor dessa variável global
			contador = 9
			print(contador) #Usa essa variável global

        #printar_contador() # ❌ Erro! Aqui daria treta pq a função vai tentar usar uma variável que ainda não foi setada!
		contador = 6
		printar_contador() #6 (vai printar o valor de "contador" setado aqui em cima)
		inventar_contador()#9 (vai printar o valor de "contador" setado em inventar_contador)
        printar_contador() #9 (vai printar 9 pq o inventar_contador alterou o valor da variável)
		```
    -   **Classes** -> Uma **classe** é um “molde” para criar objetos com **atributos** (dados) e **métodos** (funções). As vezes chamamos atributos de propriedades ou props. Existe uma pequena diferencinha entre esses dois conceitos mas por enquanto ignora isso. 
    -   ```python
        from datetime import date, datetime
        #Classe Pessoa tem o construtor (com dois parâmetros), três atributos e um método (sem parâmetros)
        class Pessoa:
            def __init__(self, nomePessoa: str, data_nascimento: str):
                self.nome = nomePessoa #a variável recebida NÃO precisa ter o mesmo nome da propriedade que será alimentada
                self.cpf = None #Avisamos o Python que cada Pessoa tem um CPF, mas ainda não o setamos
                #Tb dá pra setar props baseado em "cálculos" ou funções. Recebemos uma string e transformamos em data
                self.data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()                 

            #Fiz um método para retornar a idade pois é um "campo calculado".
            #Baseado na data de nascimento (fixa) e na data atual (variável), a idade da Pessoa muda.
            def idade(self) -> int:
                hoje = date.today()
                dias = (hoje - self.data_nascimento).days
                return dias // 365  # divisão inteira pra desprezar aniversário ainda não feito
                
        magneto = Pessoa("Erik Lehnsherr", "30/01/1930") # Instanciando uma pessoa
        magneto.cpf = "214782" #Podemos alterar o valor do cpf assim
        #Acessar prop é "variavel.prop". Acessar método é "variavel.metodo(parâmetros)"
        #No caso o método idade() não tem parâmetros, mas precisa do () memo assim!
        print(f"{magneto.nome} tem {magneto.idade()} anos.")

        class FormatadorDuasCasas:
            def __init__(self):
                pass #Construtor vazio. Sem esse "pass" o Python surta
        
            def formatar(self, valor: float) -> float:
                return round(valor, 2) #Esse método não usa nada do objeto. Podia ser uma função né?

        fo1 = FormatadorDuasCasas()
        fo2 = FormatadorDuasCasas()
        phi = 233 / 144 #Phi (Φ) representa a "proporção áurea", que é uma constante matemática adorada por nerds
        print(f"{fo1.formatar(phi)} e {fo2.formatar(phi)}") #Printa "1.62 e 1.62" (o mesmo valor) pois não há diferença entre as duas instâncias

        class FormatadorCasas:
            def __init__(self, casas:int = 2):
                self.casas = casas #Começa com casas = 2 (a menos que o usuário queira começar com outro valor)
        
            def formatar(self, valor: float, casas: int = None) -> float:
                if casas is not None: #Ou seja, cada vez que vc pede pra formatar vc pode setar a prop "casas"
                    self.casas = casas
                return round(valor, self.casas)
        
        fo1 = FormatadorCasas()
        fo1.casas = 3 #Deixamos começar com 2 e depois setamos pra 3
        phi = 233 / 144
        #Vai imprimir 1.618 e 1.618056 e 1.618056 (ou seja, na segunda chamada vai alterar o valor da prop)
        print(f"{fo1.formatar(phi)} e {fo1.formatar(phi, 6)} e {fo1.formatar(phi)}")
        ```
	-   **Import** -> Podemos importar classes, funções e constantes de outros "módulos".
    -   ```python
        import datetime
        import tkinter as tk
        from math import pi, sqrt, floor

        print(datetime.date.today()) #Chamando no formato modulo.classe.método()
        tela = tk.Tk() #Aqui demos um apelido pro módulo então ficou apelidoDoModulo.método() [que no caso é um construtor]
        print(f"{pi} {sqrt(16)} {floor(3.99)}") #Importamos uma constante (pi) e duas funções do módulo math.
        #Aqui o Python já sabe que o sqrt é lá do math, não precisa chamar pelo nome completo        
        ```
	-   ```python
        #Só pra reforçar: esse import traz tudo pra dentro do teu código. 
        from semaforo import *
     	s1 = Semaforo(self) #Aqui dá pra usar o construtor Semaforo como se tivesse sido definido no arquivo atual
     	#Mas assim vai dar ruim se o teu arquivo atual tb tiver uma classe Semaforo

		#Com esse import está tudo disponível, mas só se falar o "nome completo" ou dar um apelido (e usá-lo)
        import semaforo
     	s1 = semaforo.Semaforo(self) #Chamando semaforo do módulo importado semaforo

     	import semaforo as smf
     	s1 = smf.Semaforo(self) #Chamando semaforo do módulo apelidado de smf

     	classe Semaforo:
     		def __init__(self):
     			pass
    	s_meu = Semaforo() #Chamando semaforo implementado aqui neste arquivo
     	```

------------------------------------------------------------------------
 # 📝 Exercícios
 Agora vem a parte prática. Tente fazer os programas abaixo sem delegar todo o trabalho pra Inteligência Artificial Generativa. Caso necessário, procure no Google o que precisa. Se vc for mtooo n00b mesmo, blz, pode pedir pra IA um TRECHO de código (ex: "Como gero um número aleatório entre 0 e 5 com Python?"). Mas use com moderação. Essa é sua última chance de aprender algo!
 Para cada "programa" você pode criar um arquivo separado (ex: exe1.py, exe2.py etc) ou tacar tudo no mesmo arquivo (ex: exercicios.py) e ir separando os "programas" em funções ou classes. Vc decide.
 
 1. **Revisão da revisão (passada):** Importe todos as funções do exercício da aula passada. Então faça um código simples que pergunta qual função o usuário quer executar e executa-a. Ex: 1 - Função Idade. 2 - Preço das frutas etc. Se ainda não tiver terminado a lista anterior, que tal terminá-la agora? :}
 2. **Dobro:** Crie uma função chamada dobro(valor) que receba um número e retorne o dobro dele. Depois, peça um número ao usuário com input() e use print() para mostrar o resultado.
 3. **Históricozinho:** Crie uma classe Empilhadeira com três métodos: empilhar(valor), desempilhar() e printar(). "Empilhar" adiciona "valor" a uma lista. "Desempilhar" deleta o último valor adicionado. "Printar" printa a lista de valores na tela (note que só esse printa coisas). Em seguida monte um método que peça via input ao usuário a operação no formato: "OP valor". Ex: "E 57" empilha o valor 57. "D" desempilha. "P" printa.
