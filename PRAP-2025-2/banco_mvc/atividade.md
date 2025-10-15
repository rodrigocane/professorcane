# 🏦 Projeto: Sistema Bancário (MVC + DAL)

## 📋 Descrição geral

Este projeto tem como objetivo implementar um **sistema de gerenciamento de contas bancárias**, utilizando **Python** e o padrão **MVC** com uma camada **DAL (Data Access Layer)** para persistência de dados.

O sistema deve permitir:

- ✅ **Cadastrar** novas contas bancárias  
- ✏️ **Editar** contas existentes  
- ❌ **Excluir** contas  
- 💸 **Transferir valores** entre contas  
- 📜 **Listar todas as operações** realizadas  
- 🧾 **Listar todas as contas** — esta deve ser considerada a **tela principal** do sistema

A aplicação foi pensada para rodar em **modo texto (console)**, mas com estrutura organizada para poder evoluir futuramente (ex: trocar a interface, mudar o banco, etc).

---

## ⚙️ O que já está pronto

- A estrutura de **padrão MVC com DAL** já está bem encaminhada  
- O **banco de dados é criado automaticamente**, não sendo necessário nenhum script externo  
- As classes `Conta`, `ContaDAL` e parte do fluxo de cadastro já estão modeladas  
- O projeto já possui **divisão clara entre camadas** (`model`, `view`, `controller`, `dal`)  

---

## 🧩 O que falta implementar

A base do sistema já está criada, mas ainda há funções a serem **completadas e refinadas**.  
Entre as tarefas a concluir:

- Finalizar **todas as operações CRUD** (`cadastrar`, `editar`, `excluir`)  
- Implementar a **transferência de valores** entre contas  
- Criar **listagem de operações** com informações de origem, destino, valor e data  
- Tornar a listagem de contas a **tela principal** da aplicação. Ou seja, o o `exibir_menu` deveria antes listar todas as contas e seus respectivos saldos.
- Garantir que as regras de negócio sejam respeitadas em todas as ações (ex: não permitir saldo negativo em transferências, IDs válidos, etc.)

---

## 👥 Regras de trabalho

- O projeto pode ser desenvolvido **em equipe de até 4 pessoas**  
- Cada integrante deve manter **uma cópia pessoal** do código, seja no:
  - GitHub (fork ou repositório próprio)
  - AVA da instituição
  - E-mail pessoal (zipado, se preferir)
- O **código-fonte pode ser reorganizado ou evoluído** à vontade:
  - Podem ser criadas **novas funções, classes ou módulos**
  - Podem ser **adicionadas novas colunas ou tabelas** no banco, conforme necessidade
- O importante é que as **regras de negócio originais** (cadastro, edição, exclusão, transferência e listagens) continuem sendo respeitadas

---

## 🚀 Conceitos exercitados

Este projeto serve como **revisão prática** dos principais conceitos vistos ao longo do curso:

### 🧠 Programação em Python
- Estruturas de controle e funções
- Classes, objetos, atributos e métodos
- Encapsulamento e passagem de objetos como parâmetro
- Tipagem dinâmica e anotações de tipo (`conta: Conta`)
- Leitura e escrita no terminal
- Manipulação de exceções (`try`, `except`)

### 🧩 Padrões e Arquitetura
- Padrão **MVC (Model–View–Controller)**
- Camada de acesso a dados (**DAL**)
- Separação de responsabilidades entre as camadas
- Persistência de dados com **SQLite (ou similar)**

### 💾 Banco de Dados
- Criação automática de tabelas
- Operações **CRUD**
- Relacionamentos simples (ex: entre conta e operação)

### 🧠 Extras importantes
- Organização de projeto em múltiplos arquivos
- Reutilização de código
- Leitura e manutenção de código de terceiros
- Colaboração com Git e GitHub

---

## 🎯 Objetivo final

Ao concluir esta atividade, você terá:
- Um **sistema funcional completo**, com fluxo de dados do usuário até o banco  
- Um **exemplo real de aplicação Python estruturada**  
- Uma **revisão prática** de praticamente todos os conceitos essenciais de programação que vimos até aqui  

---

💡 **Dica:**  
Antes de sair programando, leia o código já existente com atenção.  
Entender a lógica que já está pronta vai te ajudar a manter a coerência do sistema e evitar retrabalho.

