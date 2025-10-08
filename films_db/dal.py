# Módulo: dal.py (ou pode ser models.py, dependendo da sua preferência)

from dbcon import criar_conexao # Importa a função de conexão com o DB
from models import Filme
import mysql.connector

class FilmeDAL:
    def __init__(self):
        pass # Não precisa de nada aqui, apenas para instanciar a classe

    def _obter_filme_do_registro(self, registro):
        """Método auxiliar para converter um registro (tupla/lista) do MySQL em um objeto Filme."""
        if not registro:
            return None
        return Filme(
            id=registro[0],
            titulo_original=registro[1],
            titulo_portugues=registro[2],
            ano_lancamento=registro[3],
            link=registro[4],
            opiniao=registro[5]
        )

    # --- MÉTODOS CRUD ---

    # C - CREATE
    def adicionar(self, filme):
        """Insere um novo filme no banco de dados."""
        conn = criar_conexao()
        cursor = conn.cursor()
        
        sql = """
            INSERT INTO filme (titulo_original, titulo_portugues, ano_lancamento, link, opiniao)
            VALUES (%s, %s, %s, %s, %s)
        """
        valores = (
            filme.titulo_original,
            filme.titulo_portugues,
            filme.ano_lancamento,
            filme.link,
            filme.opiniao
        )
        
        cursor.execute(sql, valores)
        conn.commit()
        filme.id = cursor.lastrowid # Atribui o ID gerado automaticamente
        cursor.close()
        conn.close()
        return filme

    # R - READ (Busca por ID)
    def buscar_por_id(self, filme_id):
        """Busca um filme pelo ID."""
        conn = criar_conexao()
        cursor = conn.cursor()
        
        sql = "SELECT id, titulo_original, titulo_portugues, ano_lancamento, link, opiniao FROM filme WHERE id = %s"
        cursor.execute(sql, (filme_id,))
        
        registro = cursor.fetchone()
        cursor.close()
        conn.close()
        
        return self._obter_filme_do_registro(registro)

    # R - READ (Listar Todos)
    def listar_todos(self):
        """Lista todos os filmes no banco de dados."""
        conn = criar_conexao()
        cursor = conn.cursor()
        
        sql = "SELECT id, titulo_original, titulo_portugues, ano_lancamento, link, opiniao FROM filme"
        cursor.execute(sql)
        
        registros = cursor.fetchall()
        cursor.close()
        conn.close()
        
        # Converte todos os registros em objetos Filme
        return [self._obter_filme_do_registro(reg) for reg in registros]

    # U - UPDATE
    def atualizar(self, filme):
        """Atualiza um filme existente (baseado no ID)."""
        conn = criar_conexao()
        cursor = conn.cursor()

        # Note que o ENUM 'opiniao' é atualizado diretamente pela string
        sql = """
            UPDATE filme SET 
                titulo_original = %s, 
                titulo_portugues = %s, 
                ano_lancamento = %s, 
                link = %s, 
                opiniao = %s
            WHERE id = %s
        """
        valores = (
            filme.titulo_original,
            filme.titulo_portugues,
            filme.ano_lancamento,
            filme.link,
            filme.opiniao,
            filme.id
        )
        
        cursor.execute(sql, valores)
        conn.commit()
        linhas_afetadas = cursor.rowcount
        cursor.close()
        conn.close()
        return linhas_afetadas > 0

    # D - DELETE
    def deletar(self, filme_id):
        """Deleta um filme pelo ID."""
        conn = criar_conexao()
        cursor = conn.cursor()
        
        sql = "DELETE FROM filme WHERE id = %s"
        cursor.execute(sql, (filme_id,))
        
        conn.commit()
        linhas_afetadas = cursor.rowcount
        cursor.close()
        conn.close()
        return linhas_afetadas > 0