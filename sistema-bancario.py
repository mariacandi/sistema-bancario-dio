menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
deposito = 0
saque = 0
extrato = ""
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = float(input("Digite o valor: "))
        if deposito > 0:
              print("Saldo atual: R$ ", round((saldo + deposito), 3))
              saldo += deposito
              extrato += f"Depósito: R$ {deposito} \n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        print("Saque")
        if numero_saques < LIMITE_SAQUES:
            saque =  float(input("Digite o valor: "))
            if saque > saldo:
                print("Não é possível realizar essa operação. Saldo insuficiente.")
                print(f"Saldo atual: R$ {saldo}")
            
            elif saque < 0:
                print("Operação falhou! O valor informado é inválido.")

            elif saque <= limite:
                numero_saques += 1
                saldo -= saque
                extrato += f"Saque: R$ {saque} \n"
                print("Saldo atual: R$ ", round(saldo, 3))
            else:
                print(f"Não é possível realizar essa operação. O valor do saque excede o limite.")
        else:
                print("Não é possível realizar essa operação. Número de saques diários excedido.")
    
    elif opcao == "e":
        print("Extrato")
        if deposito == 0 and saque == 0:
            print("Nenhuma movimentação foi realizada.")
        else:
            print(extrato)
        
        print(f"Saldo total: R$ ", round(saldo, 3))

    elif opcao == "q":
        print("Obrigado por utilizar o nosso banco!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")