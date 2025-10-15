from dbcon import criar_conexao
from models import *

class DAL:
    def __init__(self, DB_NAME):
        self.DB_NAME = DB_NAME

    def _row_para_conta(self, row):
        return Conta(
            numero=row['numero'],
            digito=row['digito'],
            titular=row['titular'],
            saldo_inicial=row['saldo_atual'],
            id=row['id']
        )

    # C
    def cadastrar_conta(self, conta:Conta):               
        sql = "INSERT INTO conta (numero, digito, titular, saldo_atual) VALUES VALUES (%s, %s, %s, %s)"
        valores = (conta.numero, conta.digito, conta.titular, conta.saldo_atual)
        conn = criar_conexao(self.DB_NAME) 
        cursor = conn.cursor()
        cursor.execute(sql, valores)
        conn.commit()
        conta.id = cursor.lastrowid # Atribui o ID gerado automaticamente
        cursor.close()
        conn.close()
        return conta

    def efetua_operacao(self, operacao:Operacao):
        sql = ""
        valores = (operacao)
        conn = criar_conexao(self.DB_NAME)
        cursor = conn.cursor()
        # seu código 
        cursor.close()
        conn.close()
        return operacao
    
    # R
    def buscar_conta(self, id=None, numero=None, digito=None):
        """Método para buscar conta pelo id ou por numero e digito"""        
        conn = criar_conexao(self.DB_NAME)
        cursor = conn.cursor(dictionary=True)
        if id is not None:
            sql = "SELECT id, numero, digito, titular, saldo_atual FROM conta WHERE id = %(id)s"
            cursor.execute(sql, {'id': id})
        else:
            sql = """
                SELECT id, numero, digito, titular, saldo_atual
                FROM conta
                WHERE numero = %(numero)s AND digito = %(digito)s
            """
            cursor.execute(sql, {'numero': numero, 'digito': digito})
                
        row = cursor.fetchone()
        if not row:
            return None
        conta = self._row_para_conta(row)
        cursor.close()
        conn.close()
        return conta
    
    def buscar_contas(self):       
        sql = "SELECT id, numero, digito, titular, saldo_atual FROM conta"
        conn = criar_conexao(self.DB_NAME)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        rows = cursor.fetchall()
        contas = [self._row_para_conta(row) for row in rows]
        cursor.close()
        conn.close()
        return contas
    
    def buscar_operacoes(self):
        sql = "SELECT id, data_hora, o.titular, d.titular, valor FROM operacao t JOIN conta o ON o.id = t.id_conta_origem JOIN conta d ON d.id = t.id_conta_destino ORDER BY t.id"
        conn = criar_conexao(self.DB_NAME)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        rows = cursor.fetchall()
        operacoes = [rows] #aqui seria melhor fazer algum tipo de conversão
        cursor.close()
        conn.close()
        return operacoes
    
    # U
    def atualizar(self, conta:Conta):
        sql = """
                UPDATE conta
                SET numero = %(numero)s,
                    digito = %(digito)s,
                    titular = %(titular)s,
                    saldo_atual = %(saldo)s
                WHERE id = %(id)s
            """
        parametros = {
            'numero': conta.numero,
            'digito': conta.digito,
            'titular': conta.titular,
            'saldo': conta.saldo_atual,
            'id': conta.id
        }
        conn = criar_conexao(self.DB_NAME)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, parametros)
        conn.commit()
        sucesso = cursor.rowcount == 1 #Retorna True se uma linha tiver sido atualizada
        cursor.close()
        conn.close()
        return sucesso
    

    # D
    def excluir_conta(self, conta:Conta):
        sql = "DELETE FROM conta WHERE id = %s"        
        conn = criar_conexao(self.DB_NAME)
        cursor = conn.cursor()
        cursor.execute(sql, (conta.id))
        conn.commit()
        sucesso = cursor.rowcount == 1 #Retorna True se uma linha tiver sido excluída
        cursor.close()
        conn.close()
        return sucesso