import mysql.connector

DB_HOST = "localhost"
DB_PORT = 3406
DB_USER = "root"
DB_PASSWORD = ""

def criar_conexao(DB_NAME):
    """Cria e retorna uma conexão com o banco de dados DB_NAME."""
    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def bd_init(DB_NAME) -> bool:
    try:
        conn = mysql.connector.connect(
            host=DB_HOST, 
            port=DB_PORT, 
            user=DB_USER, 
            password=DB_PASSWORD
        )    
        cursor = conn.cursor()
        cursor.execute(f"SHOW DATABASES LIKE '{DB_NAME}'")
        result = cursor.fetchone()

        if result is not None:
            return True #se já tem a base vou confiar que tá ok!

        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE {DB_NAME}")  
        cursor.close()
        conn.close()
        
        try:
            conn_db = criar_conexao()
            cursor_db = conn_db.cursor()
            
            with open(f"{DB_NAME}.sql", 'r', encoding='utf-8') as f:
                sql_script = f.read()
                
            sqls = sql_script.split(";")
            for sql in sqls:
                cursor_db.execute(sql)
            
            conn_db.commit()
            cursor_db.close()
            conn_db.close()
            return True 
        except FileNotFoundError:
            print(f"ERRO: Arquivo SQL não encontrado em {DB_NAME}.sql")            
        except mysql.connector.Error as err:
            print(f"Erro ao executar o script SQL: {err}")
        except Exception as e:            
            print(f"Ocorreu um erro inesperadoeee: {e}")        
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    return False #Se chegou aqui é pq deu ruim o baguio :(

