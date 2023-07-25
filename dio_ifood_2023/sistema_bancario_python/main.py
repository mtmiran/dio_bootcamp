from conta_bancaria import ContaBancaria

menu = """
    [ D ] Depositar
    [ S ] Sacar
    [ E ] Extrato
    [ Q ] Sair
    """


# criando a conta
conta = ContaBancaria()

# inicio
while True:
    opcao = input(menu).upper()

    if opcao == "D":
        valor = float(input("Valor do depósito: R$"))
        conta.deposito(valor)

    elif opcao == "S":
        valor = float(input("Valor do saque: R$"))
        conta.saque(valor)

    elif opcao == "E":
        conta.extrato()

    elif opcao == "Q":
        break

    else:
        print("Operação inválida. Selecione a operação desejada novamente.")
