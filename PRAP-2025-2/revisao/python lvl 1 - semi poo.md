# 🌿 Programação Python nível 1 - Cada um no seu ◻
Usamos **funções**, **classes** e **módulos** para organizar e reutilizar código, evitando repetição e facilitando manutenção.
A **Programação Orientada a Objetos (POO)** vai além: permite modelar o mundo real em código, criando objetos com dados e comportamentos próprios.
Assim, o código fica mais legível, escalável e fácil de expandir sem bagunçar o que já funciona. (*GPT, Chat. 2025*)    


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
    - Parâmetros e retornos: nível 2 -> Tipagem e opcional
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
   - Parâmetros e retornos: nível 3
   - ```python
        def divisao_inteira(dividendo: int, quociente: int) -> (int, int)
     ```
   - ??? 

  👷👷👷👷
  👷 WIP 👷
  👷👷👷👷
