# 🌿 Programação Python nível 1 - Cada um no seu ◻

-   **Funções, classes, módulos**
    -   Funções -> Funções encapsulam trechos de código reutilizáveis. Podem receber parâmetros e podem retornar valores
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
    - Parâmetros e retornos: nível 2
    - ```python
        def print_soma(a:int, b:int): #Agora deixamos claro que o esperado é que "a" seja um int
           print(a+b)
        soma(5, 7)     # imprime 12
        soma("5", "7") # imprime "57", ou seja, o ":int" é uma DICA mas se vc desrespeitar, o Python tenta seguir a vida
        soma("5", 7)   # ❌ Erro! TypeError: can only concatenate str (not "int") to str

        def saudacao(nome: str, saudacao: str = "Olá"): #saudacao é um parâmetro opcional
            print(f"{saudacao}, {nome}!")

        saudacao("Rodrigo")          # Olá, Rodrigo!
        saudacao("Caio", "Salve")    # Salve, Caio!
      ```
        

  👷👷👷👷
  👷 WIP 👷
  👷👷👷👷
