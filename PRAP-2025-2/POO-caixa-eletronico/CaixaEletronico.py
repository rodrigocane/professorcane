from ContaCorrente import ContaCorrente

class CaixaEletronico:
    def __init__(self, saldo_inicial):
        self.__saldo_caixa = saldo_inicial
        self.__contas = {
            "123": ContaCorrente("123", "Rodrigo Rodrigues", "0171-9", 5000),
            "456": ContaCorrente("456", "Sandy Júnior", "1234-5", 2500),
            "789": ContaCorrente("789", "Hideo Kojima", "6789-0", 1500),
            "321": ContaCorrente("321", "José de Camargo", "5432-1", 8000),
            "654": ContaCorrente("654", "Jefferson Beijos", "9876-4", 10000000000)
        }

    def saque(self, conta):
        valor = input("Digite o valor do depósito: ")
        if not valor.isnumeric():
            print("Valor inválido.")
            return
        valor = int(valor)
        if conta.depositar(valor):
            self.__saldo_caixa += valor

    def deposito(self, conta):
        valor = input("Digite o valor do saque: ")
        if not valor.isnumeric():
            print("Valor inválido.")
            return

        valor = int(valor)
        # Primeiro checa saldo da conta
        if valor > conta.saldo:
            print("Saldo insuficiente na conta.")
            return

        # Depois checa saldo do caixa
        if valor > self.__saldo_caixa:
            print("Este caixa não possui dinheiro suficiente. Tente um valor menor ou procure outro caixa.")
            return

        if conta.sacar(valor):
            self.__saldo_caixa -= valor

    def iniciar(self):
        while True:
            cartao = input("Insira seu cartão (3 dígitos): ")
            
            if cartao not in self.__contas:
                print("Cartão inválido!\n")
                continue

            conta = self.__contas[cartao]
            print(f"\nTitular: {conta.titular}")
            print(f"Conta: {conta.numero}")

            while True:
                print("\nEscolha uma opção:")
                print("1 - Saldo\n2 - Depósito")
                print("3 - Saque\n4 - Sair")

                opcao = input("Opção: ")
                match opcao:
                    case "1":
                        conta.mostrar_saldo()                    
                    case "2":
                        self.saque(conta)                            
                    case "3":
                        self.deposito(conta)                                
                    case "4":
                        print(f"Até logo, {conta.titular}\n")
                        break
                    case _:
                        print("Opção inválida.")
