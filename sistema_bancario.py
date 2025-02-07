menu = """ 

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """ # As """ são usadas para formatar strings, ao usá-las no início e fim de strings, tudo que está dentro delas manterá sua formatação, isso inlcui linhas e espaços.

saldo = 0
limite = 500
extrato = "" # Aspas duplas usadas para definir que a variável vai receber uma string que ainda não foi criada.
numero_saques = 0
LIMITE_SAQUES = 3 

while True: # O "True" é usado para definir a condição em que o "while" deve rodar.

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("informe o valor do depósito: "))

        if valor > 0:
            saldo += valor # O parâmetro "+=" e uma forma de agregação, nesse caso seria como se escrevêssimos "saldo = saldo + valor".
            extrato += f"Depósito: R$ {valor:.2f}\n" # Formatação de string, as estrutura dentro das {} se lê da seguinte maneira, "valor:", onde valor é a variável que traz um float, seguido de ".2f", onde o número 2 após
                                                     #o ponto indica o número de casas decimais que serão exibidos.   
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor> limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não possui saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saldo excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedidos.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas monvimentações." if not extrato else extrato)
        print(f"\nSaldo R$ {saldo:.2f}")
        print("=========================================")

    elif  opcao == "q":
        break # Usado para para o laço de repetução "while"

    else:
        print("Operação inválida! Por favor selecione novamente a operação desejada.")



























