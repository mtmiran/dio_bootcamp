class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido. O valor deve ser positivo.")

    def saque(self, valor):
        if 0 < valor <= 500 and len(self.saques) < 3 and self.saldo >= valor:
            self.saldo -= valor
            self.saques.append(valor)
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        elif len(self.saques) >= 3:
            print("Limite diário de saques atingido (3 saques por dia).")
        elif valor <= 0 or valor > 500:
            print(
                """Valor de saque inválido.
                  O valor deve estar entre R$ 0,01 e R$ 500,00."""
            )
        else:
            print("Saldo insuficiente para realizar o saque.")

    def extrato(self):
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")


if __name__ == "__main__":
    # Testando o código
    conta = ContaBancaria()

    conta.deposito(1000)
    conta.deposito(500.45)
    conta.saque(200)
    conta.saque(700)
    conta.saque(300)
    conta.saque(400)

    conta.extrato()
