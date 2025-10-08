import mysql.connector
from mysql.connector import errorcode
import os

SQL_FILE_PATH = "film_db_init.sql" 
DB_NAME = "films_db"
DB_HOST = "localhost"
DB_PORT = 3306 
DB_USER = "root"
DB_PASSWORD = ""

def criar_conexao_servidor():    
    return mysql.connector.connect(
                host=DB_HOST,
                port=DB_PORT,
                user=DB_USER,
                password=DB_PASSWORD
            )

def criar_conexao():
    """Cria e retorna uma conexão com o banco de dados 'films_db'."""
    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    
    
def inicializar_banco_dados():
    # --- PASSO 1: Garantir a não existência do DB ---
    try:
        conn_servidor = criar_conexao_servidor()
        cursor_servidor = conn_servidor.cursor()
        
        # Cria o banco de dados se não existir
        cursor_servidor.execute(f"DROP DATABASE IF EXISTS {DB_NAME}")        
        cursor_servidor.execute(f"CREATE DATABASE {DB_NAME}")        
        cursor_servidor.close()
        conn_servidor.close()

    except mysql.connector.Error as err:
        print(f"Erro ao criar/verificar o banco de dados: {err}")
        return # Encerra se não conseguir nem criar o DB
    except Exception as e:
        # Captura qualquer erro de aplicação (IO, DB, lógica, etc.)
        print(f"Ocorreu um erro inesperado: {e}")
    
    # --- PASSO 2: Conectar ao DB e executar o script SQL ---
    try:
        conn_db = criar_conexao()
        cursor_db = conn_db.cursor()

        # 2.1. Ler o conteúdo do arquivo SQL
        with open(SQL_FILE_PATH, 'r', encoding='utf-8') as f:
            sql_script = f.read()

            
        sqls = sql_script.split(";")
        for sql in sqls:
            cursor_db.execute(sql)
        
        conn_db.commit()
        print(f"Script de inicialização '{SQL_FILE_PATH}' executado com sucesso.")

        cursor_db.close()
        conn_db.close()

    except FileNotFoundError:
        print(f"ERRO: Arquivo SQL não encontrado em {SQL_FILE_PATH}")
    except mysql.connector.Error as err:
        print(f"Erro ao executar o script SQL: {err}")
    except Exception as e:
        # Captura qualquer erro de aplicação (IO, DB, lógica, etc.)
        print(f"Ocorreu um erro inesperadoeee: {e}")    