# 🐍 **Atividade Prática – Sistema CRUD Simples em Python**

Nesta atividade, você irá desenvolver um **mini-sistema de cadastro e autenticação de usuários**, contendo **login**, **CRUD de usuários** e **controle de permissões**.
A interface pode ser feita com **Tkinter** ou **Flask**, e o **banco de dados será fornecido**.

---

## 🚀 **Objetivo Geral**

Criar um sistema totalmente funcional com:

* ✔️ Tela de login
* ✔️ Criação de conta
* ✔️ Listagem de usuários
* ✔️ Edição e exclusão
* ✔️ Regras de administrador
* ✔️ Senhas protegidas (hash)

---

# 📌 **Regras e Fluxos do Sistema**

---

## 🆕 **Fluxo: Novo Usuário**

**Login → Criar Conta**

Campos obrigatórios:

* 🧑 *login*
* 📧 *email*
* 🔒 *senha*
* 🎂 *data de nascimento*

Regras:

* ❗ **Nenhum campo pode ficar vazio**
* 🚫 **Não pode repetir login ou email**
* 🔐 **A senha deve ser armazenada com hash**
* 👑 **O primeiro usuário cadastrado deve ser marcado como ADM**
* ▶️ Após cadastro bem-sucedido, o usuário **já entra logado** e vai direto para a **Tela Principal**

---

## 🔐 **Fluxo: Usuário Existente**

**Tela de Login**

* O usuário informa **login** + **senha**
* ❗ **Não dar dica do erro em caso de falha**
  (nada de “senha incorreta”, apenas “Login inválido”)

Se o login for bem-sucedido → ir para a **Tela Principal**

---

# 🖥️ **Tela Principal**

Exibir uma **lista de usuários cadastrados**.

### 👑 Se o usuário atual for **ADM**:

* Pode **editar** qualquer usuário
* Pode **excluir** qualquer usuário

### 👤 Se **NÃO** for ADM:

* Pode editar **somente o próprio usuário**
* Pode excluir **somente o próprio usuário**

---

# ✏️ **Tela de Edição de Usuário**

Campos:

* 🧑 **Login:** mostrado, mas **não pode ser alterado**
* 📧 **Email:** pode alterar
* 🎂 **Data de nascimento:** pode alterar
* 🔑 **Senha:** comportamento especial ⤵️

### Caso o usuário editado seja **outro usuário**:

* Não mostrar campo de senha
* Mostrar um botão **“RESETAR SENHA”**

  * Ao clicar, a senha deve ser redefinida para algo genérico (ex.: `123`)

### Caso o usuário editado seja **o próprio usuário**:

* Deve ser possível **criar uma nova senha normalmente**

---

# 🗑️ **Exclusão de Usuário**

Não precisa criar uma tela separada — apenas exibir uma confirmação:

> **“Tem certeza disso? Posso excluir?”**

Comportamento:

* Se o usuário excluído for **o usuário logado**:

  * ❌ Deslogar
  * 🔄 Redirecionar para a tela inicial
* Caso contrário:

  * 🔄 Apenas recarregar a tela atual

---
Aqui está uma seção **“Recursos”** pronta para colar no seu README, com visual agradável, ícones e espaço para você inserir seus links:

---

## 📚 Recursos

Aqui estão alguns materiais de apoio importantes para o desenvolvimento da atividade:

### 🗄️ **Banco de Dados**

```sql
CREATE DATABASE SA_PY;

USE SA_PY;

CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(256) NOT NULL,
    email VARCHAR(250) NOT NULL UNIQUE,
    dt_nascimento DATE NOT NULL
);
```

---

### 🔐 **Exemplo: Como gerar hash de senha em Python**

Trecho simples utilizando `hashlib` (mas se quiser pode usar outro):

```python
import hashlib

def gerar_hash(senha: str) -> str:
    return hashlib.sha256(senha.encode()).hexdigest()

def verificar_senha(senha_digitada: str, hash_armazenado: str) -> bool:
    return gerar_hash(senha_digitada) == hash_armazenado

# Exemplo de uso:
senha_plana = "123"
senha_hashed = gerar_hash(senha_plana)
print("Hash:", senha_hashed)
```
---

# 🏁 **Entrega**

Sua entrega deve incluir o projeto funcional com UI (**Tkinter** ou **Flask**), seguindo fielmente todas as regras acima.

Boa prática e bom código! 💻✨

