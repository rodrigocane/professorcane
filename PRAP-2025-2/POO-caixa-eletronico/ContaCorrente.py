class ContaCorrente:
    def __init__(self, cartao, titular, numero, saldo_inicial):
        self.__cartao = cartao
        self.__titular = titular
        self.__numero = numero
        self.__saldo = saldo_inicial

    @property
    def cartao(self):
        return self.__cartao

    @property
    def titular(self):
        return self.__titular

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    def mostrar_saldo(self):
        print(f"Saldo conta {self.__numero}: R${self.__saldo}")

    def depositar(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            print("O valor deve ser um número inteiro maior que zero.")
            return False
        self.__saldo += valor
        print("Depósito realizado com sucesso.")
        self.mostrar_saldo()
        return True

    def sacar(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            print("O valor deve ser um número inteiro maior que zero.")
            return False
        if valor > self.__saldo:
            print("Saldo insuficiente na conta.")
            return False
        self.__saldo -= valor
        print("Saque realizado com sucesso.")
        self.mostrar_saldo()
        return True
