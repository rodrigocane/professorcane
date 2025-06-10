#Versão 3: agora com reaproveitamento de código (def) e com otimização de performance e legibilidade (match/case)
saldo = 0.0
extrato = []

def printar_saldo():
    print(f"Saldo atual: R${saldo:.2f}")

def depositar(valor):
    global saldo
    saldo += valor
    extrato.append(f"Depósito: 📈R${valor:.2f}")
    printar_saldo()

def sacar(valor):    
    global saldo
    if valor > saldo:
        print("Tu nem tem tanta grana, seu fulero!\n")
        return
    saldo -= valor
    extrato.append(f"Saque: 📉R${valor:.2f}")
    printar_saldo()

def printar_extrato():
    for movimentacao in extrato: 
        print(movimentacao)

while True:
    opcao = (input("Qual a ação?\n1:Ver o saldo\n2:Depositar\n3:Saque\n4:Extrato\n5:Encerrar conta\n"))
    if not opcao.isnumeric():
        print("tá de zuera, né amigão? Tenta denovo ae")
        continue
    
    opcao = int(opcao)
    match opcao:
        case 1:
            printar_saldo()
        case 2:
            valorDeposito = float(input("Quanto tu qué colocá?\n"))
            depositar(valorDeposito)
        case 3:
            saque = float(input("Quer sacar quanto?\n"))
            sacar(saque)
        case 4:
            printar_extrato()
            printar_saldo()
        case 5:
            if saldo > 0:
                sacar(saldo)        
            print("Conta encerrada. Volte sempre")
            break
        case _:
            print("Tá perdido? Num sabe contar até 5??")
