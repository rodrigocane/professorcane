titular = "Rodrigo Rodrigues"
cartao = 123
conta = "0171-9"
saldo = 5000

cartao_inserido = input("Insira seu cartão: ")
if int(cartao_inserido) != cartao:
    print("Cartão inválido")
    exit()

while True:
    print("Operações disponíveis:")
    print("1 - Saldo\n2 - Depósito\n3 - Saque\n4 - Sair")
    operacao = int(input())

    if operacao == 1:
        print(f"Saldo atual: R${saldo}")
    elif operacao == 2: #depósito         
        depositar = int(input("Quanto você quer depositar? "))
        if depositar <= 0:
            print("Valor negativo não né, fera?")
            continue
        saldo += depositar
        print("Depósito deu boa")
        print(f"Saldo atual: R${saldo}")
    elif operacao == 3: #Saque
        saque = int(input("Quer sacar quanto hoje? "))
        if saque <= 0:
            print("Valor negativo não né, fera?")
            continue
        if saque > saldo:
            print("Saldo insuficiente")
            continue
        saldo -= saque
        print("Saque realizado com sucesso")
        print(f"Saldo atual: R${saldo}")
    elif operacao == 4:
        print(f"Até mais, {titular}.")
        exit()
    else:
        print("Só temos as opções 1, 2, 3 ou 4.")
