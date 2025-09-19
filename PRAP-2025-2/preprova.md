# 📝 Lista de Revisão Pré-Prova --- Programação Python

Antes da prova objetiva, é importante revisar os principais conteúdos trabalhados em aula. O material "teórico" com alguns exemplinhos você encontra <a href="https://rodrigocane.github.io/PRAP-2025-2/preprova1.html" target="_blank">aqui</a>.

Essa lista de exercícios foi pensada para **refrescar a memória** sobre
os tópicos que podem cair na prova:

-   **Python em geral**
    -   funções
    -   `print`
    -   listas, tuplas, dicionários
    -   `pip install`
-   **POO (Programação Orientada a Objetos)**
    -   classe
    -   métodos
    -   construtor
    -   propriedades
-   **Pandas**
    -   DataFrame
    -   criação de colunas
    -   filtros
    -   funções de agrupamento
-   **Tkinter**
    -   `grid()` x `Frame`
    -   `tk.Tk()` x `tk.Toplevel()`
    -   Entry, Button, Label
    -   Propriedades dos widgets

------------------------------------------------------------------------

## ✅ Exercício 1 --- Revisão Python básico

Crie um programa que:

1. Define uma função `media(lista)` que recebe uma lista de números e
retorna a média.

2. Peça ao usuário para digitar 3 números (usando `input()`),
armazene-os em uma **lista** e calcule a média usando a função.

3. Mostre o resultado com `print()`.

💡 *Dica: use `map(int, input().split())` para ler vários números de uma
vez.*
------------------------------------------------------------------------

## ✅ Exercício 2 --- POO

Implemente uma classe `Produto` com:

- **Atributos**: `nome` e `preco`

- **Construtor** (`__init__`) para inicializar os atributos

- Um **método** `desconto(porcentagem)` que aplica um desconto ao preço

No programa principal:

1. Crie um objeto `Produto("Caneta", 5.0)`

2. Aplique um desconto de 10% e mostre o novo preço

------------------------------------------------------------------------

## ✅ Exercício 3 --- Pandas

Com o Pandas, faça um mini relatório de vendas:

1.  Crie um DataFrame com 2 colunas: `"produto"` e `"quantidade"`.

2.  Adicione uma coluna `"preco_unit"` com valores (à sua escolha).

3.  Crie outra coluna `"total"` = quantidade × preço_unit.

4.  Use `groupby` para mostrar a soma de vendas por produto.

------------------------------------------------------------------------

## ✅ Exercício 4 --- Tkinter

Monte uma interface simples com Tkinter que tenha:

- Uma **Entry** para digitar um nome

- Um **Button** "Mostrar"

- Um **Label** que exibe `"Olá, <nome>"` quando o botão é clicado

💡 *Reforce o uso de `grid()` e mostre a diferença se usar `pack()`.*

------------------------------------------------------------------------

🎯 **Objetivo**: Esses 4 exercícios revisam os pontos principais que
podem cair na prova --- do Python básico até POO, Pandas e Tkinter.
