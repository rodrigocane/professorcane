class ContaCorrente:
    def __init__(self, cartao, titular, conta, saldo:int):
        self.__cartao = cartao
        self.__titular = titular
        self.__conta = conta
        self.__saldo = saldo
    
    @property
    def saldo(self):
        return self.__saldo
        
    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, novoNome):        
        self.__titular = novoNome

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo}")

    def depositar(self, valor:int):
        self.__saldo += valor
        self.exibir_saldo()
    
    def sacar(self, valor:int):
        if self.saldo < valor:
            return False
        self.__saldo -= valor
        self.exibir_saldo()
        return True    

contas = {
    "123": ContaCorrente("123", "Rodrigo Rodrigues", "0171-9", 5000),
    "456": ContaCorrente("456", "Sandy Júnior", "1234-5", 2500),
    "789": ContaCorrente("789", "Hideo Kojima", "6789-0", 1500),
    "321": ContaCorrente("321", "José de Camargo", "5432-1", 8000),
    "654": ContaCorrente("654", "Jefferson Beijos", "9876-4", 10000000000)
}


tentativas = 0
while tentativas < 3:
    cartao_inserido = input("Insira seu cartão: ")
    if not cartao_inserido.isnumeric() or cartao_inserido not in contas:
        print("Cartão inválido")
        tentativas += 1
        continue
    conta = contas[cartao_inserido]

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
