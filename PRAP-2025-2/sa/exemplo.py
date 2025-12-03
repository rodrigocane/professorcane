import tkinter as tk
from dbcon import criar_conexao #Vejam que estou importando o criar_conexao de um tal de dbcon.py
import hashlib

def gerar_hash(senha: str) -> str:
    return hashlib.sha256(senha.encode()).hexdigest()

def insere_admin():
    '''
    Código de exemplo que cadastra um usuário administrador com senha 123.
    Usem este exemplo para ver como conectar ao banco (chamando o dbcon.criar_conexao), como criar cursor, como passar o SQL
    '''
    conn = criar_conexao() 
    cursor = conn.cursor()
    sql = "INSERT INTO usuario (login, senha, email, dt_nascimento) VALUES (%s, %s, %s, %s)"
    senha_hashed = gerar_hash("123")
    cursor.execute(sql, ("adm", senha_hashed, "administr@dor.com","2000-01-01"))
    conn.commit()
    cursor.close()
    conn.close()

insere_admin()
