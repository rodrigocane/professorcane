#Versão 1: funcional, mas com várias oportunidades de melhoria!
saldo = 0.0
extrato = []

while True:
    opcao = (input("Qual a ação?\n1:Ver o saldo\n2:Depositar\n3:Saque\n4:Extrato\n5:Encerrar conta\n"))
    if not opcao.isnumeric():
        print("tá de zuera, né amigão? Tenta denovo ae")
        continue
    
    opcao = int(opcao)
    if opcao == 1:
        print(f"Saldo atual: R${saldo:.2f}")
    elif opcao == 2:
        valorDeposito = float(input("Quanto tu qué colocá?"))
        saldo += valorDeposito
        extrato.append(f"Depósito: 📈R${valorDeposito:.2f}")

        print(f"Saldo atual: R${saldo:.2f}")
    elif opcao == 3:
        print("Saque")
        saque = float(input("Quer sacar quanto?"))
        if saque > saldo:
            print("Tu nem tem tanta grana, seu fulero!")
            continue
        
        saldo -= saque
        extrato.append(f"Saque: 📉R${saque:.2f}")
        print(f"Saldo atual: R${saldo:.2f}")
    elif opcao == 4:
        for movimentacao in extrato: #for Each
            print(movimentacao)

        print(f"Saldo atual: R${saldo:.2f}")
    elif opcao == 5:
        if saldo > 0:
            saque = saldo
            saldo -= saque
            extrato.append(f"Saque: 📉R${saque:.2f}")
            print(f"Saldo atual: R${saldo:.2f}")
        
        print("Conta encerrada. Volte sempre")
        break
    
    else:
        print("Tá perdido? Num sabe contar até 5??")
