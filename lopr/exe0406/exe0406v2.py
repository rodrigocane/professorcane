#Versão 2: agora reaproveitando código através do uso de funções (def)
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
    if opcao == 1:
        printar_saldo()
    elif opcao == 2:
        valorDeposito = float(input("Quanto tu qué colocá?\n"))
        depositar(valorDeposito)
    elif opcao == 3:
        saque = float(input("Quer sacar quanto?\n"))
        sacar(saque)
    elif opcao == 4:
        printar_extrato()
        printar_saldo()
    elif opcao == 5:
        if saldo > 0:
           sacar(saldo)        
        print("Conta encerrada. Volte sempre")
        break
    else:
        print("Tá perdido? Num sabe contar até 5??")
