from conta_bancaria import ContaBancaria


class Usuario(ContaBancaria):
    def __init__(self, nome, cpf):
        super().__init__()
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}"


if __name__ == "__main__":
    # Testando o código
    usuario1 = Usuario("João da Silva", "123.456.789-00")
    usuario2 = Usuario("Maria Souza", "987.654.321-00")

    usuario1.deposito(1000)
    usuario1.saque(500)
    usuario1.extrato()

    usuario2.deposito(1500)
    usuario2.saque(200)
    usuario2.saque(300)
    usuario2.extrato()
