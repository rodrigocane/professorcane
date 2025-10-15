from datetime import datetime

class Conta:
    def __init__(self, numero, digito, titular, saldo_inicial: float = 0.0, id: int = None):
        self.numero = numero
        self.digito = digito
        self.titular = titular
        self.saldo_atual = saldo_inicial
        self.id = id

    def pode_ser_excluida(self):
        return self.saldo_atual == 0

class Operacao:
    def __init__(self, contaOrigem:Conta, contaDestino:Conta, valor:float, id: int = None, datahora: datetime = None):
        self.contaOrigem = contaOrigem
        self.contaDestino = contaDestino
        self.valor = valor
        self.id = id
        self.dataHora = datahora if datahora is not None else datetime.now()
    
    def valida(self):
        return self.contaOrigem.saldo_atual >= self.valor