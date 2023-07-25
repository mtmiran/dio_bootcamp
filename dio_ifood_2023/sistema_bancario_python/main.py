from conta_bancaria import ContaBancaria
from usuario import Usuario

menu = """
    [ D ] Depositar
    [ S ] Sacar
    [ E ] Extrato
    [ Q ] Sair
    """


# criando a conta
usuario = Usuario("João da Silva", "123.456.789-00")


# inicio
while True:
    opcao = input(menu).upper()

    if opcao == "D":
        valor = float(input("Valor do depósito: R$"))
        usuario.deposito(valor)

    elif opcao == "S":
        valor = float(input("Valor do saque: R$"))
        usuario.saque(valor)

    elif opcao == "E":
        usuario.extrato()

    elif opcao == "Q":
        break

    else:
        print("Operação inválida. Selecione a operação desejada novamente.")
