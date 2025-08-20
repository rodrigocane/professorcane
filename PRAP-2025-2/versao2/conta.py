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
