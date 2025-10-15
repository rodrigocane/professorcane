from models import Conta


class Tela:
    def __init__(self, controller):
        self.controller = controller

    def exibir_listagem_contas(self):
        print("Contas atuais")
        contas = self.controller.listar_contas()
        for conta in contas:
            print(f"({conta.id}) R${conta.saldo_atual} {conta.numero}-{conta.digito} de {conta.titular}")
        print()

    def exibir_menu(self):        
        print("Escolha uma operação:")
        print("C - Cadastrar Conta")
        print("U - Atualizar Conta")
        print("D - Excluir Conta")
        print("O - Realizar Operação")
        print("R - Listar Operações")
        opcao = input("Opção: ")
        match opcao:
            case "C":
                self.controller.cadastrar_conta()
            case "U":
                id = input("Qual id da conta a ser alterada?")
                self.controller.alterar_conta(id)
            case "D":
                id = input("Qual id da conta a ser excluida?")
                self.controller.alterar_conta(id)
            case "O":
                self.controller.iniciar_operacao(self)
            case "R":
                self.controller.historico_transacoes(self)
            case _:
                print("Que opção é essa, querido? Tenta denovo ae")
                self.exibir_menu()
    
    def mostra_tela_cadastro(self, conta:Conta=None) -> Conta:        
        if conta is None:
            conta = Conta(None, None, None, None)
            cadastrando = True
        else:
            cadastrando = False

        print("Cadastrando nova conta" if cadastrando else f"Atualizando conta {conta.id}. Deixe em branco para manter o valor atual")
        numero = input("Numero: " if cadastrando else f"Numero ({conta.numero})")
        numero = conta.numero if not numero.isnumeric() else numero
        digito = input("Digito: " if cadastrando else f"Digito ({conta.digito})")
        digito = conta.digito if not digito.isnumeric() or int(digito) > 9 else digito
        titular = input("Titular: " if cadastrando else f"Titular ({conta.titular})")
        titular = conta.titular if titular.strip() else titular
        saldo = 0 #vc faz essa cansei rs
        return conta
    
    def exibir_tela_operacao(self):
        print("Fazendo uma operação daora")
        print("Aí tem que perguntar os dados pro usuário")
        print("Depois perguntar pro controller se dá pra fazer a operação")
        print("Se deu boa, avisa o usuário e vida que segue!")

    def exibir_listagem_operacoes(self, operacoes):
        print("Operações")
        for operacao in operacoes:
            print(operacao) #tem que melhorar isso

    def _exibir_msg(self, icone, msg):
        print(f"{icone} - {msg}")

    def exibir_erro_fatal(self, msg):
        icone = "💀"
        print(f"{icone}{icone}{icone}")
        self._exibir_msg(icone, msg)
        print(f"{icone}{icone}{icone}")

    def exibir_msg_ok(self, msg):
        self._exibir_msg("✅", msg)

    def exibir_msg_fracasso(self, msg):
        self._exibir_msg("🚫", msg)