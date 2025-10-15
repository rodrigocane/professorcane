from dbcon import *
from dal import DAL
from tela import *

DB_NAME = "da_bank"

class Controller:
    def __init__(self):
        self.view = Tela(self)
            
    def iniciar(self):
        if not bd_init(DB_NAME):
            self.view.exibir_erro_fatal("Não foi possível criar/acessar o BD")
            return
        self.dal = DAL(DB_NAME)
        self.view.exibir_menu()

    def listar_contas(self):
        return self.dal.buscar_contas()

    def cadastrar_conta(self):
        nova_conta = self.view.mostra_tela_cadastro()
        if self.dal.cadastrar_conta(nova_conta):
            self.view.exibir_msg_ok(f"Conta {nova_conta.id} do titular {nova_conta.titular} cadastrada com sucesso.")
        else:
            self.view.exibir_msg_fracasso(f"Não deu pra cadastrar a conta do titular {nova_conta}. Malz aí")
        
        self.view.exibir_menu()
    
    def alterar_conta(self, id):
        conta = self.view.mostra_tela_cadastro(self.dal.buscar_conta(id))
        if self.dal.atualizar(conta):
             self.view.exibir_msg_ok(f"Conta {conta.id} do titular {conta.titular} alterada com sucesso.")
        else:
            self.view.exibir_msg_fracasso(f"Não deu pra atualizar a conta do titular {conta}. Malz aí")
        
        self.view.exibir_menu()

    def excluir_conta(self, id):
        conta = self.dal.buscar_conta(id)
        if conta.pode_ser_excluida() and self.dal.excluir_conta(conta):
             self.view.exibir_msg_ok(f"Conta {conta.id} do titular {conta.titular} excluída com sucesso.")
        else:
            self.view.exibir_msg_fracasso(f"Não deu pra excluir a conta do titular {conta}. Tem que tá zerada hein?")
        
        self.view.exibir_menu()

    def historico_transacoes(self):
        self.view.exibir_listagem_operacoes(self.dal.buscar_operacoes())

    def iniciar_operacao(self):
        self.view.exibir_tela_operacao()


if __name__ == '__main__':
    app = Controller()
    app.iniciar()    