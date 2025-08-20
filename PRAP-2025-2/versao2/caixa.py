from datetime import datetime
from conta import ContaCorrente

class CaixaEletronico:
    def __init__(self, contas:list[ContaCorrente]):
        self.contas = contas
        self.saldo = 0
        self.data_inicio = datetime.today()

    def iniciar(self):
        tentativas = 0
        while tentativas < 3:
            cartao_inserido = input("Insira seu cartão: ")
            if not cartao_inserido.isnumeric() or cartao_inserido not in self.contas:
                print("Cartão inválido")
                tentativas += 1
                continue
            conta = self.contas[cartao_inserido]

            tentativas = 0
            while True:
                print("Operações disponíveis:")
                print("1 - Saldo\n2 - Depósito\n3 - Saque\n4 - Sair")
                operacao = int(input())
                match(operacao):
                    case 1:
                        conta.exibir_saldo()
                    case 2: #depósito         
                        depositar = int(input("Quanto você quer depositar? "))
                        if depositar <= 0:
                            print("Valor negativo não né, fera?")
                            continue
                        conta.depositar(depositar)
                        print("Depósito deu boa")
                    case 3: #Saque
                        saque = int(input("Quer sacar quanto hoje? "))
                        if saque <= 0:
                            print("Valor negativo não né, fera?")
                            continue
                        if not conta.sacar(saque):
                            print("Tinxerga mermão. Tu não tem tanta grana não.")
                            continue
                        print("Saque realizado com sucesso")
                    case 4:
                        print(f"Até mais, {conta.titular}.")
                        break
                    case _:
                        print("Tá perdido amigo? É 1, 2, 3 ou 4.")

        print("Limite de tentativas excedido. Esse caixa se auto destruirá em 4s")
